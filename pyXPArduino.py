"""
pyXPArduino.py
--------------
Application entry point and main window controller.

This module bootstraps the PyQt5 application, initialises all subsystems
(logging, X-Plane UDP server, XML config, Arduino threads, edit forms), and
provides the :class:`pyXPArduino` main-window class that ties everything
together.

Architecture overview
~~~~~~~~~~~~~~~~~~~~~
.. code-block:: text

    pyXPArduino (QMainWindow)
      ├─ arduinoConfig          — XML config CRUD
      ├─ Arduino (×N threads)   — per-board serial + routing
      ├─ pyXPUDPServer thread   — X-Plane UDP comms
      └─ Edit forms (×7)        — per-component-type GUI panels

Build / distribute
~~~~~~~~~~~~~~~~~~
To build a standalone executable::

    pyinstaller pyXPArduino.spec --clean

Usage::

    python3 pyXPArduino.py
"""

# To distribute, run: pyinstaller pyXPArduino.spec --clean
import json
import logging
import logging.config
import os, getpass, sys
import glob

if getattr(sys, 'frozen', False):
    # we are running in a bundle
    working_dir = sys._MEIPASS
else:
    working_dir = os.getcwd()

print("Working dir:"+str(working_dir))

with open(os.path.join(working_dir,"config/logging_conf.json"), "r") as fd:
    logging.config.dictConfig(json.load(fd))

from PyQt5 import QtCore, QtGui, QtWidgets # Import the PyQt5 modules we'll need
from PyQt5.QtWidgets import QApplication, QMainWindow,QTreeWidgetItem, QMenu
import sys # We need sys so that we can pass argv to QApplication
import gui.pyXPQTableLogger as pyXPQTableLogger

import xml.etree.ElementTree as ET

import gui.mainwindow as mainwindow# This file holds our MainWindow and all design related things
import gui.deleteConfirmationDialog as deleteConfirmationDialog
import gui.pyXPunsavedChangesConfirmationDialog as unsavedChangesConfirmationDialog
import gui.pyXPaddArduinoDialog as pyXPaddArduinoDialog
import gui.pyXPpickXPCommandDialog as pyXPpickXPCommandDialog
import gui.pyXPUDPConfigDialog as pyXPUDPConfigDialog

import gui.pyXPswitchEditForm as pyXPswitchEditForm
import gui.pyXPpotentiometerEditForm as pyXPpotentiometerEditForm
import gui.pyXPpwmEditForm as pyXPpwmEditForm
import gui.pyXPdigOutputEditForm as pyXPdigOutputEditForm
import gui.pyXPservoEditForm as pyXPservoEditForm
import gui.pyXProtencoderEditForm as pyXProtencoderEditForm
import gui.pyXPinstrumentEditForm as pyXPinstrumentEditForm

import lib.arduinoXMLconfig
import lib.XPrefData as XPrefData
import pyxpudpserver as XPUDP
import lib.arduinoSerial as ardSerial
import lib.Arduino as Arduino

#: str: Application version string displayed in the window title.
VERSION = "v1.3"

mainConfigFile = os.path.join(working_dir,'config/config.xml')
UDPconfigFile = os.path.join(working_dir,'config/UDPSettings.xml')
instrumentsFolder = os.path.join(working_dir,'instruments')


class pyXPArduino(QMainWindow, mainwindow.Ui_MainWindow):
    """Main application window for pyXPArduino.

    Inherits from both :class:`PyQt5.QtWidgets.QMainWindow` and the
    auto-generated ``mainwindow.Ui_MainWindow`` layout class.

    Responsibilities:

    * Initialise and own all subsystems (UDP server, XML config, Arduino
      threads, edit forms, dialogs).
    * Manage the Arduino tree widget, keeping it in sync with the XML config.
    * Route tree-selection events to the correct component edit form.
    * Handle file operations (open / create / save Arduino config files).
    * Propagate unsaved-change state to the Save toolbar action.

    The typical lifecycle is::

        form = pyXPArduino()
        form.show()
        form.initialise()   # loads config, starts threads
        app.exec_()
        # on close → closeEvent() stops all threads

    Attributes:
        arduinoList (list[Arduino]): Running Arduino thread objects, one per
            configured board.
        ardXMLconfig (arduinoConfig): Shared XML configuration manager.
        ardConfigFile (str): Path to the currently loaded Arduino config XML.
        updatingCompPanel (bool): Guard flag — suppresses edit callbacks
            while the component panel is being programmatically populated.
        _refreshingArduinoTree (bool): Guard flag — suppresses attribute-change
            callbacks while the tree widget is being rebuilt.
        _refreshingInstrumentTree (bool): Guard flag for the instrument tree.
    """

    def __init__(self):
        """Set up the main window UI, status bar, and 500 ms refresh timer.

        Called once at application startup.  Does **not** load configuration
        or start threads — call :meth:`initialise` after :meth:`show` for
        that.
        """
        super(self.__class__, self).__init__()
        self.setupUi(self)  # This is defined in design.py file automatically
                            # It sets up layout and widgets that are defined

        self.QTableLogger = pyXPQTableLogger.pyXPQTableLogger()
        self.QTableLogger.setupQtWidget(self.centralwidget)
        self.verticalLayout_2.addWidget(self.QTableLogger.widget)
        logging.getLogger().addHandler(self.QTableLogger)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.updateMessages)
        self.timer.start(500)
        self.setWindowTitle("pyXPArduino "+VERSION)

        # build status bar
        self.statusBar = QtWidgets.QStatusBar()
        self.statusBar.setStyleSheet("QStatusBar { border-top:1px; border-style: solid;border-color: grey; }")

        self.setStatusBar(self.statusBar)

        self.statusBarArdXMLfileName = QtWidgets.QLabel()
        self.statusBar.addWidget(self.statusBarArdXMLfileName,1)

        self.statusBarUDPServerStatus = QtWidgets.QLabel()
        self.statusBarUDPServerStatus.setStyleSheet("QLabel { border-left:2px; border-style: solid;border-color: grey; }")
        self.statusBar.addWidget(self.statusBarUDPServerStatus,1)

    def initialise(self):
        """Load configuration, start all subsystems, and populate the UI.

        Performs the full application startup sequence:

        1. Loads ``config/config.xml`` to find the Arduino config file path.
        2. Loads the X-Plane dataref and command reference files.
        3. Starts the ``pyXPUDPServer`` thread.
        4. Parses the Arduino XML configuration file.
        5. Creates and starts one :class:`~lib.Arduino.Arduino` thread per
           configured board.
        6. Instantiates all component edit forms and adds them to the layout.
        7. Builds the Arduino and instrument trees.
        8. Hides all edit forms until a tree item is selected.

        Should be called once, after :meth:`show`, so the window is visible
        while initialisation runs.
        """
        logging.debug("Running as user: "+getpass.getuser())
        self.loadConfig()
        XPrefData.loadXPReferenceFiles()

        XPUDP.pyXPUDPServer.initialiseUDPXMLConfig(UDPconfigFile)

        XPUDP.pyXPUDPServer.start()

        self.updatingCompPanel = True
        self._refreshingArduinoTree = False
        self._refreshingInstrumentTree = False

        self.ardXMLconfig = lib.arduinoXMLconfig.arduinoConfig()
        self.ardXMLconfig.registerFileLoadedStatusCallback(self.handleArdFileLoadedStatusChanged)
        self.ardXMLconfig.loadConfigFile(self.ardConfigFile)
        self.ardXMLconfig.registerArduinoAttributeChangedCallback(self.handleArduinoAttributeChange)

        self.arduinoList = []

        self.refreshArduinoList()

        self.deleteConfirmDialog = deleteConfirmationDialog.DeleteConfirmationDialog()
        self.unsavedChangesConfirmationDialog = unsavedChangesConfirmationDialog.unsavedChangesConfirmationDialog()

        self.addArduinoDialog = pyXPaddArduinoDialog.pyXPAddArduinoDialog()
        self.pickXPCommandDialog = pyXPpickXPCommandDialog.pyXPpickXPCommandDialog()
        self.pickXPCommandDialog.refreshCommandList()
        self.editXPUDPConfigDialog = pyXPUDPConfigDialog.pyXPUDPConfigDialog(UDPconfigFile)
        #switch edit form
        self.ardSwitchEditForm = pyXPswitchEditForm.pyXPswitchEditForm(self.editPaneWidget, self.ardXMLconfig, self.actionSave)
        self.horizontalLayoutEditPane.addWidget(self.ardSwitchEditForm)
        self.ardSwitchEditForm.nameUpdated.connect(self.updateComponentName)

        #rot encoder edit form
        self.ardRotencoderEditForm = pyXProtencoderEditForm.pyXProtencoderEditForm(self.editPaneWidget, self.ardXMLconfig, self.actionSave)
        self.horizontalLayoutEditPane.addWidget(self.ardRotencoderEditForm)
        self.ardRotencoderEditForm.nameUpdated.connect(self.updateComponentName)

        #potentiometer edit form
        self.ardPotentiometerEditForm = pyXPpotentiometerEditForm.pyXPpotentiometerEditForm(self.editPaneWidget, self.ardXMLconfig, self.actionSave)
        self.horizontalLayoutEditPane.addWidget(self.ardPotentiometerEditForm)
        self.ardPotentiometerEditForm.nameUpdated.connect(self.updateComponentName)

        #PWM edit form
        self.ardPWMEditForm = pyXPpwmEditForm.pyXPpwmEditForm(self.editPaneWidget, self.ardXMLconfig, self.actionSave)
        self.horizontalLayoutEditPane.addWidget(self.ardPWMEditForm)
        self.ardPWMEditForm.nameUpdated.connect(self.updateComponentName)

        #Digital output edit form
        self.ardDigOutputEditForm = pyXPdigOutputEditForm.pyXPdigOutputEditForm(self.editPaneWidget, self.ardXMLconfig, self.actionSave)
        self.horizontalLayoutEditPane.addWidget(self.ardDigOutputEditForm)
        self.ardDigOutputEditForm.nameUpdated.connect(self.updateComponentName)

        #Servo edit form
        self.ardServoEditForm = pyXPservoEditForm.pyXPservoEditForm(self.editPaneWidget, self.ardXMLconfig, self.actionSave)
        self.horizontalLayoutEditPane.addWidget(self.ardServoEditForm)
        self.ardServoEditForm.nameUpdated.connect(self.updateComponentName)

        #Instrument edit form
        self.instrumentEditForm = pyXPinstrumentEditForm.pyXPinstrumentEditForm(self.instrumentEditPane, os.path.join(working_dir, 'config/configGraphics.ini'), self.actionSave)
        self.horizontalLayout_instrumentEditPane.addWidget(self.instrumentEditForm)

        self.ardBaudComboBox.addItems(lib.arduinoXMLconfig.ARD_BAUD)

        self.refreshArduinoTree()
        self.ardSwitchEditForm.hide()
        self.arduinoEditForm.hide()
        self.ardPotentiometerEditForm.hide()
        self.ardPWMEditForm.hide()
        self.ardDigOutputEditForm.hide()
        self.ardServoEditForm.hide()
        self.ardRotencoderEditForm.hide()
        self.instrumentEditForm.hide()
        self.refreshInstrumentTree()
        self.tabWidget.setCurrentIndex(0)

        self.actionSave.setEnabled(False)
        self.updatingCompPanel = False

    def loadConfig(self):
        """Read the main ``config/config.xml`` file to retrieve the Arduino config path.

        Parses the main application config file and extracts the
        ``<ardConfigFilePath>`` element value, storing it in
        :attr:`ardConfigFile` and displaying it in the status bar.
        """
        self.xmlcfgtree = ET.parse(mainConfigFile)
        self.xmlcfgroot = self.xmlcfgtree.getroot()

        ardTags = self.xmlcfgroot.findall(".//ardConfigFilePath")
        if len(ardTags) > 0: # arduino config file tag
            self.ardConfigFile = ardTags[0].text
            logging.info("arduino config file located at: "+str(self.ardConfigFile))
            self.statusBarArdXMLfileName.setText("Ard config file: "+str(self.ardConfigFile))

    def handleArdFileLoadedStatusChanged(self, status):
        """Enable or disable the Arduino tree and Add-Arduino action based on file status.

        Connected to the :meth:`~lib.arduinoXMLconfig.arduinoConfig.registerFileLoadedStatusCallback`
        on the XML config manager.  Disables the tree and toolbar action when
        no valid config file is loaded so the user cannot add hardware without
        a configuration target.

        Args:
            status (bool): ``True`` if a config file is successfully loaded;
                ``False`` otherwise.
        """
        if status == True:
            self.actionAdd_Arduino.setEnabled(True)
            self.arduinoTreeWidget.setEnabled(True)
        else:
            self.actionAdd_Arduino.setEnabled(False)
            self.arduinoTreeWidget.setEnabled(False)

    def openArduinoConfigFile(self):
        """Open a file-picker dialog and load a new Arduino configuration XML file.

        If there are unsaved changes the user is prompted to discard them
        before proceeding.  On a successful file selection, updates
        ``config/config.xml`` with the new path, reloads the Arduino XML
        config, and rebuilds the tree.
        """
        proceed = True
        if self.actionSave.isEnabled() == True: #check first if we have unsaved changes and prompt for confirmation
            proceed = False
            returnCode = self.unsavedChangesConfirmationDialog.exec()
            if returnCode == 1:
                proceed = True

        if proceed == True:
            logging.info('Open Arduino config file')
            filename = QtWidgets.QFileDialog.getOpenFileName(self, "Open Arduino config file", '//', "XML files (*.xml)")
            logging.info("File name: "+ str(filename))

            if filename[0] != '': # if a file has been selected
                ardTags = self.xmlcfgroot.findall(".//ardConfigFilePath")
                if len(ardTags) > 0: # arduino config file tag
                    ardTags[0].text = filename[0] # update it and write to config file on disk
                    self.ardConfigFile = ardTags[0].text
                    self.xmlcfgtree.write(mainConfigFile)

                self.statusBarArdXMLfileName.setText("Ard config file: "+str(self.ardConfigFile))
                self.ardXMLconfig.loadConfigFile(self.ardConfigFile)
                self.refreshArduinoList()
                self.refreshArduinoTree()

    def createArduinoConfigFile(self):
        """Open a save-file dialog and create a new empty Arduino configuration XML file.

        If there are unsaved changes the user is prompted to discard them
        before proceeding.  Creates an empty ``<arduinoConfig>`` XML file at
        the chosen path, updates ``config/config.xml``, and reloads the tree.
        """
        proceed = True
        if self.actionSave.isEnabled() == True: #check first if we have unsaved changes and prompt for confirmation
            proceed = False
            returnCode = self.unsavedChangesConfirmationDialog.exec()
            if returnCode == 1:
                proceed = True

        if proceed == True:

            logging.info('Create Arduino config file')
            filename = QtWidgets.QFileDialog.getSaveFileName(self, "Create new Arduino config file", '//', "XML files (*.xml)")
            logging.info("File name: "+ str(filename))

            if filename[0] != '': # if a file has been selected
                ardTags = self.xmlcfgroot.findall(".//ardConfigFilePath")
                if len(ardTags) > 0: # arduino config file tag
                    ardTags[0].text = filename[0] # update it and write to config file on disk
                    self.ardConfigFile = ardTags[0].text
                    self.xmlcfgtree.write(mainConfigFile)

                self.statusBarArdXMLfileName.setText("Ard config file: "+str(self.ardConfigFile))
                self.ardXMLconfig.createConfigFile(filename[0])
                self.ardXMLconfig.loadConfigFile(self.ardConfigFile)
                self.refreshArduinoList()
                self.refreshArduinoTree()

    def refreshArduinoList(self):
        """Stop all running Arduino threads and restart them from the current config.

        Calls :meth:`~lib.Arduino.Arduino.quit` on every existing thread,
        clears :attr:`arduinoList`, then creates and starts a new
        :class:`~lib.Arduino.Arduino` instance for each board defined in the
        XML configuration.  Sends the initial pin-configuration to each board
        after starting.
        """
        for arduino in self.arduinoList: # first stop all arduinos
            arduino.quit()

        self.arduinoList = [] # reset the list

        for arduino in self.ardXMLconfig.getArduinoList(): #re populate the list
            self.arduinoList.append(Arduino.Arduino(arduino['serial_nr'],
                                                    XPUDP.pyXPUDPServer,
                                                    self.ardXMLconfig
                                                    ))
        for arduino in self.arduinoList: # start all arduinos
            arduino.start()
            arduino.updateComponentList('*', '', arduino.ardSerialNumber, 'pin')

    def closeEvent(self, event):
        """Handle the window close event — stop threads and confirm unsaved changes.

        If there are unsaved changes the user is prompted.  If the user
        confirms (or there are no unsaved changes), the UDP server and all
        Arduino threads are stopped before the window closes.  If the user
        cancels, the close event is ignored.

        Args:
            event (QCloseEvent): The Qt close event.  Call
                ``event.ignore()`` to cancel the close.
        """
        proceed = True
        if self.actionSave.isEnabled() == True:
            proceed = False
            returnCode = self.unsavedChangesConfirmationDialog.exec()
            if returnCode == 1:
                proceed = True

        if proceed == True:
            XPUDP.pyXPUDPServer.quit()
            for arduino in self.arduinoList:
                arduino.quit()
        else:
            event.ignore()

    def ardSwitchChanged(self, pin, value):
        """Placeholder callback for direct switch-change notifications.

        Currently unused — switch state changes are handled via the XML config
        callback chain.  Reserved for future direct-event handling.

        Args:
            pin (int): The pin number that changed.
            value (int): The new pin value (0 or 1).
        """
        logging.debug("ard switch changed callback, pin", pin)

    def updateMessages(self):
        """Refresh the UDP server status label in the status bar.

        Called every 500 ms by the QTimer set up in :meth:`__init__`.
        Reads the ``statusMsg`` string from ``pyXPUDPServer`` and updates
        the right-hand status bar label.
        """
        self.statusBarUDPServerStatus.setText(XPUDP.pyXPUDPServer.statusMsg)

    def refreshInstrumentTree(self):
        """Scan the instruments folder and rebuild the instrument tree widget.

        Reads all ``*.xml`` files from the ``instruments/`` directory and
        populates the instruments tree with one top-level item per file.
        Column 0 holds the filename; column 1 holds the full path (used when
        an item is selected).
        """
        self._refreshingInstrumentTree = True
        instrumentList = glob.glob(instrumentsFolder+'/*.xml')
        logging.info('Instruments list')
        logging.info(instrumentList)

        boldFont = QtGui.QFont()
        boldFont.setBold(True)
        self.instrumentsTreeWidget.clear()

        for instrument in instrumentList:
            head, tail = os.path.split(instrument)
            instrumentTreeElem = QTreeWidgetItem([ tail, instrument ])
            instrumentTreeElem.setFont(0, boldFont)

            self.instrumentsTreeWidget.addTopLevelItem(instrumentTreeElem)
            instrumentTreeElem.setExpanded(False)

        self.instrumentsTreeWidget.resizeColumnToContents(0)
        self._refreshingInstrumentTree = False

    def instrumentTreeSelectionChanged(self):
        """Handle selection changes in the instruments tree widget.

        Reads the full instrument XML path from column 1 of the selected item
        and calls ``show()`` on the instrument edit form with that path.
        """
        if len(self.instrumentsTreeWidget.selectedItems()) > 0:
            instrumentPath = self.instrumentsTreeWidget.selectedItems()[0].text(1)
            self.instrumentEditForm.show(instrumentPath)

    def instrumentRun(self):
        """Launch the instrument graphics renderer for the currently selected instrument.

        Delegates to the instrument edit form's ``run()`` method.
        """
        self.instrumentEditForm.run()

    def refreshArduinoTree(self):
        """Rebuild the Arduino tree widget from the current XML configuration.

        Clears the tree and repopulates it by iterating the parsed XML tree.
        Builds a three-level hierarchy:

        * Level 0: Arduino board (with connected/disconnected icon).
        * Level 1: ``inputs`` / ``outputs`` containers.
        * Level 2: Component-type containers (e.g. ``switches``, ``pwms``).
        * Level 3: Individual component items (name + ID).

        Column 0 holds the display name, column 1 holds the serial number or
        component ID, and column 2 holds the XML element tag (used by
        :meth:`ardTreeSelectionChanged` to identify item type).
        """
        self._refreshingArduinoTree = True
        logging.debug ("refreshArduinoTree")

        boldFont = QtGui.QFont()
        boldFont.setBold(True)
        self.arduinoTreeWidget.clear()
        if self.ardXMLconfig.configFileLoaded == True:
            for arduino in self.ardXMLconfig.root: # cycle through arduinos
                ardTreeElem = QTreeWidgetItem([ arduino.attrib['name'], arduino.attrib['serial_nr'], arduino.tag ])
                ardTreeElem.setFont(0, boldFont)

                if arduino.attrib['connected'] == 'Connected':
                    icon = QtGui.QIcon()
                    icon.addPixmap(QtGui.QPixmap(":/newPrefix/ardIcon2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                    ardTreeElem.setIcon(0, icon)
                else:
                    icon = QtGui.QIcon()
                    icon.addPixmap(QtGui.QPixmap(":/newPrefix/ardIconDisconnected.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                    ardTreeElem.setIcon(0, icon)

                self.arduinoTreeWidget.addTopLevelItem(ardTreeElem)
                ardTreeElem.setExpanded(True)

                for inoutputs in arduino: # cycle through input outputs
                    inoutputsTreeElem = QTreeWidgetItem([ inoutputs.attrib['description'], '', inoutputs.tag ])
                    if inoutputs.tag == "inputs":
                        icon = QtGui.QIcon()
                        icon.addPixmap(QtGui.QPixmap(":/newPrefix/inputIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                        inoutputsTreeElem.setIcon(0, icon)
                    if inoutputs.tag == "outputs":
                        icon = QtGui.QIcon()
                        icon.addPixmap(QtGui.QPixmap(":/newPrefix/outputIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                        inoutputsTreeElem.setIcon(0, icon)

                    ardTreeElem.addChild(inoutputsTreeElem)
                    inoutputsTreeElem.setExpanded(True)

                    for inputOutputTypes in inoutputs:  # iterate through input and output types
                        inputOutputTypesTreeElem = QTreeWidgetItem([ inputOutputTypes.attrib['description'], '', inputOutputTypes.tag ])
                        inoutputsTreeElem.addChild(inputOutputTypesTreeElem)
                        inputOutputTypesTreeElem.setExpanded(True)


                        for inputOutput in inputOutputTypes:  # iterate through input and output types
                            inputOutputTreeElem = QTreeWidgetItem([ inputOutput.attrib['name'], inputOutput.attrib['id'], inputOutput.tag ])
                            inputOutputTypesTreeElem.addChild(inputOutputTreeElem)

        self.arduinoTreeWidget.resizeColumnToContents(0)
        self._refreshingArduinoTree = False

    def updateComponentName(self, compID, compName):
        """Update the display name of a component in the tree widget.

        Called via the ``nameUpdated`` signal emitted by component edit forms
        when the user renames a component.  Finds the tree item by ID (column
        1) and sets column 0 to the new name.

        Args:
            compID (str): Unique component ID stored in column 1 of the tree.
            compName (str): New display name to show in column 0.
        """
        items = self.arduinoTreeWidget.findItems (compID, QtCore.Qt.MatchExactly|QtCore.Qt.MatchRecursive,1)
        if len(items)>0:
            items[0].setText(0, compName)

    def handleArduinoAttributeChange(self, ardSerialNr, attribute):
        """React to Arduino attribute changes by refreshing the Arduino edit form.

        Registered as a callback on the XML config manager.  Ignores events
        fired during tree rebuilds (guarded by :attr:`_refreshingArduinoTree`).

        Args:
            ardSerialNr (str): Serial number of the Arduino whose attribute
                changed.
            attribute (str): Name of the changed attribute.
        """
        logging.debug('ard attribute changed')
        if self._refreshingArduinoTree == False:
            self.__updateArduinoEditFormData(ardSerialNr)

    def __updateArduinoEditFormData(self, ardID):
        """Refresh the Arduino edit form fields with current data from the XML config.

        Only updates the form if the Arduino identified by ``ardID`` is
        currently selected in the tree.  Updates all fields including
        connection/status indicators with colour-coded labels and icon updates
        in the tree.

        Args:
            ardID (str): Serial number of the Arduino to display.
        """
        if len(self.arduinoTreeWidget.selectedItems()) > 0 and self.arduinoTreeWidget.selectedItems()[0].text(1) == ardID : # only update if that ard is selected in the tree
            ardData = self.ardXMLconfig.getArduinoData(ardID)
            logging.debug("ard data:"+str(ardData))
            self.ardSerialNrLineEdit.setText(ardData['serial_nr'])
            self.ardBaudComboBox.setCurrentText(ardData['baud'])
            self.ardPortLineEdit.setText(ardData['port'])
            self.ardNameLineEdit.setText(ardData['name'])
            self.ardDescriptionLineEdit.setText(ardData['description'])
            self.ardManufacturerLineEdit.setText(ardData['manufacturer'])
            self.ardSerialConnStatusLabel.setText(ardData['connected'])
            if ardData['connected'] == 'Connected':
                self.ardSerialConnStatusLabel.setStyleSheet("QLabel { background-color : green; color : white; }")
                items = self.arduinoTreeWidget.findItems (ardID, QtCore.Qt.MatchExactly|QtCore.Qt.MatchRecursive,1)
                if len(items)>0:
                    icon = QtGui.QIcon()
                    icon.addPixmap(QtGui.QPixmap(":/newPrefix/ardIcon2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                    items[0].setIcon(0, icon)
            else:
                self.ardSerialConnStatusLabel.setStyleSheet("QLabel { font-weight: bold; background-color : red; color : white; }")
                items = self.arduinoTreeWidget.findItems (ardID, QtCore.Qt.MatchExactly|QtCore.Qt.MatchRecursive,1)
                if len(items)>0:
                    icon = QtGui.QIcon()
                    icon.addPixmap(QtGui.QPixmap(":/newPrefix/ardIconDisconnected.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                    items[0].setIcon(0, icon)

            if ardData['ard_status'] == 'Running':
                self.ardStatusLabel.setStyleSheet("QLabel { background-color : green; color : white; }")
                items = self.arduinoTreeWidget.findItems (ardID, QtCore.Qt.MatchExactly|QtCore.Qt.MatchRecursive,1)
                if len(items)>0:
                    icon = QtGui.QIcon()
                    icon.addPixmap(QtGui.QPixmap(":/newPrefix/ardIcon2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                    items[0].setIcon(0, icon)
            else:
                self.ardStatusLabel.setStyleSheet("QLabel { font-weight: bold; background-color : red; color : white; }")
                items = self.arduinoTreeWidget.findItems (ardID, QtCore.Qt.MatchExactly|QtCore.Qt.MatchRecursive,1)
                if len(items)>0:
                    icon = QtGui.QIcon()
                    icon.addPixmap(QtGui.QPixmap(":/newPrefix/ardIconDisconnected.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                    items[0].setIcon(0, icon)

            self.ardFirmwareVersionLabel.setText(ardData['firmware_version'])
            self.ardStatusLabel.setText(ardData['ard_status'])

    def ardTreeSelectionChanged(self):
        """Show the appropriate component edit form when a tree item is selected.

        Hides all edit forms, reads the XML tag stored in column 2 of the
        selected tree item, and shows the matching edit form (or Arduino edit
        form if an Arduino node is selected).

        The ``updatingCompPanel`` guard is set during this method to suppress
        spurious ``editingFinished`` callbacks triggered by programmatic field
        population.
        """
        self.updatingCompPanel = True
        logging.debug("Ard tree selection changed")
        self.ardSwitchEditForm.hide()
        self.arduinoEditForm.hide()
        self.ardPotentiometerEditForm.hide()
        self.ardPWMEditForm.hide()
        self.ardDigOutputEditForm.hide()
        self.ardServoEditForm.hide()
        self.ardRotencoderEditForm.hide()

        if len(self.arduinoTreeWidget.selectedItems()) > 0:
            tag         = self.arduinoTreeWidget.selectedItems()[0].text(2)
            compID = self.arduinoTreeWidget.selectedItems()[0].text(1)

            if tag =='arduino':
                self.__updateArduinoEditFormData(compID)
                self.arduinoEditForm.show()


            if tag =='switch':
                self.ardSwitchEditForm.show(compID)

            if tag == 'rot_encoder':
                self.ardRotencoderEditForm.show(compID)

            if tag =='potentiometer':
                self.ardPotentiometerEditForm.show(compID)

            if tag =='pwm':
                self.ardPWMEditForm.show(compID)

            if tag =='servo':
                self.ardServoEditForm.show(compID)

            if tag == 'dig_output':
                self.ardDigOutputEditForm.show(compID)

        self.updatingCompPanel = False

    def ardEditingFinished(self):
        """Save edits made in the Arduino edit panel back to the XML configuration.

        Called when the user finishes editing any field in the Arduino edit
        form (connected to ``editingFinished`` / ``currentIndexChanged``
        signals).  Guarded by :attr:`updatingCompPanel` and
        :attr:`_refreshingArduinoTree` to avoid writing during programmatic
        field updates.

        Reads all Arduino field values from the UI, calls
        :meth:`~lib.arduinoXMLconfig.arduinoConfig.updateArduinoData`, updates
        the tree item name, and enables the Save action.
        """
        logging.debug('ardEditingFinished, ardBaudComboBox: '+self.ardBaudComboBox.currentText())
        if self.updatingCompPanel == False and self._refreshingArduinoTree == False:
            logging.debug("updating data")
            ardData = {'port':             self.ardPortLineEdit.text(),
                        'baud':            self.ardBaudComboBox.currentText(),
                        'name':         self.ardNameLineEdit.text(),
                        'description':     self.ardDescriptionLineEdit.text(),
                        'serial_nr':     self.ardSerialNrLineEdit.text(),
                        'manufacturer': self.ardManufacturerLineEdit.text()}

            self.ardXMLconfig.updateArduinoData(ardData['serial_nr'], ardData)
            self.updateComponentName( self.ardSerialNrLineEdit.text(),self.ardNameLineEdit.text())
            self.actionSave.setEnabled(True)

    def ardTreeContextMenuRequested(self, position):
        """Display a context menu for the right-clicked Arduino tree item.

        Shows different menu options based on the XML tag of the selected item:

        * **arduino** — "Remove Arduino…"
        * **Input/output container** (e.g. ``switches``) — "Add <component type>"
        * **Component element** (e.g. ``switch``) — "Delete item…"

        Args:
            position (QPoint): The cursor position within the tree viewport,
                used to place the context menu.
        """
        logging.debug("ardTreeContextMenuRequested")
        # find which item is selected
        if len(self.arduinoTreeWidget.selectedItems()) > 0 : # check at least one item selected
            tag         = self.arduinoTreeWidget.selectedItems()[0].text(2)
            tag_descr     = self.arduinoTreeWidget.selectedItems()[0].text(0)

            logging.debug(self.arduinoTreeWidget.selectedItems()[0].text(2))

            if tag =='arduino':
                menu = QMenu()
                removeArdAction = QtWidgets.QAction('Remove Arduino...')
                removeArdAction.triggered.connect(self.removeArduino)
                menu.addAction(removeArdAction)
                menu.exec_(self.arduinoTreeWidget.viewport().mapToGlobal(position))


            if tag in lib.arduinoXMLconfig.INPUT_OUTPUT_TAGS: # to add switches, pots, pwms etc...
                menu = QMenu()
                addCompAction = QtWidgets.QAction(lib.arduinoXMLconfig.INPUT_OUTPUT_TAGS_REF[tag]['add_action'])
                addCompAction.triggered.connect(self.addCompAction)
                menu.addAction(addCompAction)
                menu.exec_(self.arduinoTreeWidget.viewport().mapToGlobal(position))

            if tag in lib.arduinoXMLconfig.INPUT_OUTPUT_ELEMS_TAGS:
                menu = QMenu()
                removeCompAction = QtWidgets.QAction("Delete item...")
                removeCompAction.triggered.connect(self.removeCompAction)
                menu.addAction(removeCompAction)
                menu.exec_(self.arduinoTreeWidget.viewport().mapToGlobal(position))

    def addCompAction(self):
        """Add a new component of the selected type to the selected Arduino.

        Reads the XML container tag and the parent Arduino serial number from
        the currently selected tree item, calls
        :meth:`~lib.arduinoXMLconfig.arduinoConfig.addInputOutput`, refreshes
        the tree, and enables the Save action.

        Slot connected to the "Add <component>" context menu action.
        """
        logging.debug("add ard item")

        selectedItem = self.arduinoTreeWidget.selectedItems()[0]
        selectedItemTag = selectedItem.text(2)
        selectedArduinoSerialNr = selectedItem.parent().parent().text(1)

        self.ardXMLconfig.addInputOutput(selectedArduinoSerialNr, selectedItemTag)
        self.refreshArduinoTree()
        self.actionSave.setEnabled(True)

    def removeCompAction(self):
        """Delete the selected component after user confirmation.

        Shows the delete confirmation dialog.  If confirmed, removes the
        component from the XML config, refreshes the tree, and enables Save.

        Slot connected to the "Delete item…" context menu action.
        """
        logging.debug("remove ard item")

        returnCode = self.deleteConfirmDialog.exec()
        if returnCode == 1:
            selectedItem = self.arduinoTreeWidget.selectedItems()[0]
            selectedItemID = selectedItem.text(1)
            selectedArduinoSerialNr = selectedItem.parent().parent().parent().text(1)

            self.ardXMLconfig.removeInputOutput(selectedArduinoSerialNr, selectedItemID)
            self.refreshArduinoTree()
            self.actionSave.setEnabled(True)

    def removeArduino(self):
        """Remove the selected Arduino board and all its components after confirmation.

        Shows the delete confirmation dialog.  If confirmed, calls
        :meth:`~lib.arduinoXMLconfig.arduinoConfig.removeArduino`, refreshes
        the tree, and enables Save.

        Slot connected to the "Remove Arduino…" context menu action.
        """
        logging.debug("remove arduino")

        returnCode = self.deleteConfirmDialog.exec()
        if returnCode == 1:
            selectedItem = self.arduinoTreeWidget.selectedItems()[0]
            selectedArduinoSerialNr = selectedItem.text(1)

            self.ardXMLconfig.removeArduino(selectedArduinoSerialNr)
            self.refreshArduinoTree()
            self.actionSave.setEnabled(True)

    def saveToXML(self):
        """Save the current XML configuration to disk and disable the Save action.

        Slot connected to the ``actionSave`` toolbar button and File menu item.
        Delegates to :meth:`~lib.arduinoXMLconfig.arduinoConfig.saveToXMLfile`.
        """
        self.ardXMLconfig.saveToXMLfile()
        self.actionSave.setEnabled(False)

    def pickArduino(self):
        """Open the Add Arduino dialog and add the selected boards to the configuration.

        Refreshes the dialog's Arduino list (excluding boards already in the
        config), shows the dialog, and — on confirmation — calls
        :meth:`~lib.arduinoXMLconfig.arduinoConfig.addArduino` for each
        checked row.  Restarts all Arduino threads and rebuilds the tree.

        Slot connected to the ``actionAdd_Arduino`` toolbar button.
        """
        self.addArduinoDialog.refreshArduinoList(self.ardXMLconfig)
        returnCode = self.addArduinoDialog.exec()

        if returnCode == 1: # add selected arduinos
            logging.debug("Adding selected arduinos")
            ardTableWidget = self.addArduinoDialog.arduinoTableWidget
            for row in range(0, ardTableWidget.rowCount()):
                if ardTableWidget.item(row,0).checkState() == QtCore.Qt.Checked :
                    self.ardXMLconfig.addArduino(ardTableWidget.item(row,1).text(),
                                                ardTableWidget.item(row,2).text(),
                                                ardTableWidget.item(row,3).text(),
                                                ardTableWidget.item(row,4).text(),
                                                ardTableWidget.item(row,5).text())
            self.actionSave.setEnabled(True)
        self.refreshArduinoList()
        self.refreshArduinoTree()
        logging.debug(returnCode)

    def editXPUDPSettings(self):
        """Open the UDP configuration dialog and apply any changes.

        Shows the :class:`~gui.pyXPUDPConfigDialog.pyXPUDPConfigDialog` modal.
        On confirmation, saves settings to the XML file and restarts the UDP
        server so changes take effect immediately.

        Slot connected to the UDP Settings menu item.
        """
        logging.debug('edit XP UDP config')
        returnCode = self.editXPUDPConfigDialog.exec()
        print(returnCode)
        logging.debug('return code:'+str(returnCode))

        if returnCode == 1:
            self.editXPUDPConfigDialog.saveToXMLfile()
            self.editXPUDPConfigDialog.restartUDPServer()


def main():
    """Application entry point — create and run the pyXPArduino Qt application.

    Creates the :class:`QApplication` and :class:`pyXPArduino` window,
    shows the window, runs :meth:`pyXPArduino.initialise`, and enters the
    Qt event loop.
    """
    app = QApplication(sys.argv)  # A new instance of QApplication
    form = pyXPArduino()
    form.show()                         # Show the form
    form.initialise()
    app.exec_()                         # and execute the app


if __name__ == '__main__':              # if we're running file directly and not importing it
    main()                              # run the main function
