# To distribute, run: pyinstaller pyXPArduino.spec --clean
# on mac:
#
#
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

import lib.arduinoXMLconfig
import lib.XPrefData as XPrefData
import pyxpudpserver as XPUDP
import lib.arduinoSerial as ardSerial
import lib.Arduino as Arduino

VERSION = "v1.2"
mainConfigFile = os.path.join(working_dir,'config/config.xml')
UDPconfigFile = os.path.join(working_dir,'config/UDPSettings.xml')
instrumentsFolder = os.path.join(working_dir,'instruments')

class pyXPArduino(QMainWindow, mainwindow.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)  # This is defined in design.py file automatically
                            # It sets up layout and widgets that are defined

        #self.showMaximized()
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

        self.ardBaudComboBox.addItems(lib.arduinoXMLconfig.ARD_BAUD)

        self.refreshArduinoTree()
        self.ardSwitchEditForm.hide()
        self.arduinoEditForm.hide()
        self.ardPotentiometerEditForm.hide()
        self.ardPWMEditForm.hide()
        self.ardDigOutputEditForm.hide()
        self.ardServoEditForm.hide()
        self.ardRotencoderEditForm.hide()

        self.refreshInstrumentTree()
        
        self.actionSave.setEnabled(False)
        self.updatingCompPanel = False

    def loadConfig(self):
        self.xmlcfgtree = ET.parse(mainConfigFile)
        self.xmlcfgroot = self.xmlcfgtree.getroot()

        ardTags = self.xmlcfgroot.findall(".//ardConfigFilePath")
        if len(ardTags) > 0: # arduino config file tag
            self.ardConfigFile = ardTags[0].text
            logging.info("arduino config file located at: "+str(self.ardConfigFile))
            self.statusBarArdXMLfileName.setText("Ard config file: "+str(self.ardConfigFile))

    def handleArdFileLoadedStatusChanged(self, status):
        if status == True:
            self.actionAdd_Arduino.setEnabled(True)
            self.arduinoTreeWidget.setEnabled(True)
        else:
            self.actionAdd_Arduino.setEnabled(False)
            self.arduinoTreeWidget.setEnabled(False)

    def openArduinoConfigFile(self):
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

            if filename[0] is not '': # if a file has been selected
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

            if filename[0] is not '': # if a file has been selected
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
        for arduino in self.arduinoList: # first stop all arduinos
            arduino.quit()

        self.arduinoList = [] # reset the list

        for arduino in self.ardXMLconfig.getArduinoList(): #re populate the list
        #serialNumber, PORT, BAUD, XPUDPServer, arduinoXMLconfig)
            self.arduinoList.append(Arduino.Arduino(arduino['serial_nr'],
                                                    XPUDP.pyXPUDPServer,
                                                    self.ardXMLconfig
                                                    ))
        for arduino in self.arduinoList: # start all arduinos
            arduino.start()
            arduino.updateComponentList('*', '', arduino.ardSerialNumber, 'pin')


    def closeEvent(self, event):
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
        logging.debug("ard switch changed callback, pin", pin)

    def updateMessages(self):
        self.statusBarUDPServerStatus.setText(XPUDP.pyXPUDPServer.statusMsg)

    def refreshInstrumentTree(self):
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
        pass
        
    def refreshArduinoTree(self):
        self._refreshingArduinoTree = True
        logging.debug ("refreshArduinoTree")

        boldFont = QtGui.QFont()
        boldFont.setBold(True)
        self.arduinoTreeWidget.clear()
        if self.ardXMLconfig.configFileLoaded == True:
            for arduino in self.ardXMLconfig.root: # cycle through arduinos
                #logging.debug (arduino.tag, arduino.attrib)
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
                            #inputOutputTreeElem.setFlags(QtCore.Qt.ItemIsEditable)
                            inputOutputTypesTreeElem.addChild(inputOutputTreeElem)

                            #inputOutputTreeElem.setIcon(0, QtGui.QIcon("Resources/small_switch_on.png"))

        self.arduinoTreeWidget.resizeColumnToContents(0)
        self._refreshingArduinoTree = False

    def updateComponentName(self, compID,compName):
        items = self.arduinoTreeWidget.findItems (compID, QtCore.Qt.MatchExactly|QtCore.Qt.MatchRecursive,1)
        if len(items)>0:
            items[0].setText(0, compName)
            #print (items)

    def handleArduinoAttributeChange(self, ardSerialNr, attribute):
        logging.debug('ard attribute changed')
        if self._refreshingArduinoTree == False:
            self.__updateArduinoEditFormData(ardSerialNr)

    def __updateArduinoEditFormData(self, ardID):
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

    ## Saves the changes made in the Arduino Edit screen - called when user finishes editing the name.
    #
    def ardEditingFinished(self):
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
            #self.refreshArduinoTree()
            self.updateComponentName( self.ardSerialNrLineEdit.text(),self.ardNameLineEdit.text())
            self.actionSave.setEnabled(True)

    def ardTreeContextMenuRequested(self, position):
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

    ## slot called to add a component (switch, potentiometer, etc...)
    # finds the tag of the item selected in the tree, and corresponding arduino unique ID.
    # adds the new component in the xml data structure, and calls a full refresh of the tree
    def addCompAction(self):
        logging.debug("add ard item")

        selectedItem = self.arduinoTreeWidget.selectedItems()[0]
        selectedItemTag = selectedItem.text(2)
        selectedArduinoSerialNr = selectedItem.parent().parent().text(1)

        self.ardXMLconfig.addInputOutput(selectedArduinoSerialNr, selectedItemTag)
        self.refreshArduinoTree()
        self.actionSave.setEnabled(True)

    def removeCompAction(self):
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
        logging.debug("remove arduino")

        returnCode = self.deleteConfirmDialog.exec()
        if returnCode == 1:
            selectedItem = self.arduinoTreeWidget.selectedItems()[0]
            #selectedItemID = selectedItem.text(1)
            selectedArduinoSerialNr = selectedItem.text(1)

            self.ardXMLconfig.removeArduino(selectedArduinoSerialNr)
            self.refreshArduinoTree()
            self.actionSave.setEnabled(True)

    def saveToXML(self):
        self.ardXMLconfig.saveToXMLfile()
        self.actionSave.setEnabled(False)

    def pickArduino(self):
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
        logging.debug('edit XP UDP config')
        returnCode = self.editXPUDPConfigDialog.exec()
        print(returnCode)
        logging.debug('return code:'+str(returnCode))

        if returnCode == 1:
            self.editXPUDPConfigDialog.saveToXMLfile()
            self.editXPUDPConfigDialog.restartUDPServer()

def main():
    app = QApplication(sys.argv)  # A new instance of QApplication
    form = pyXPArduino()
    form.show()                         # Show the form
    form.initialise()
    app.exec_()                         # and execute the app


if __name__ == '__main__':              # if we're running file directly and not importing it
    main()                              # run the main function
