LOGGING_LEVEL = "WARNIN"
import logging
import logging.config
#LOGGING_FORMAT= '%(asctime)s %(levelname)-8s %(name)-10s %(module)-30s %(funcName)-30s  %(message)s'
logging.config.fileConfig('config/logging.conf')
#logging.basicConfig(format=LOGGING_FORMAT, level=logging.DEBUG)

import os, getpass

from PyQt5 import QtCore, QtGui, QtWidgets # Import the PyQt5 modules we'll need
from PyQt5.QtWidgets import QApplication, QMainWindow,QTreeWidgetItem, QMenu
import sys # We need sys so that we can pass argv to QApplication

import gui.mainwindow as mainwindow# This file holds our MainWindow and all design related things
import gui.deleteConfirmationDialog as deleteConfirmationDialog
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

VERSION = "v1.1"
XMLconfigFile = 'config/UDPSettings.xml'

class pyXPArduino(QMainWindow, mainwindow.Ui_MainWindow):
	def __init__(self):
		super(self.__class__, self).__init__()
		self.setupUi(self)  # This is defined in design.py file automatically
							# It sets up layout and widgets that are defined

		#self.showMaximized()

		self.timer = QtCore.QTimer()
		self.timer.timeout.connect(self.updateMessages)
		self.timer.start(500)
		self.setWindowTitle("pyXPArduino "+VERSION)
		logging.debug("Running as user: "+getpass.getuser())

		XPUDP.pyXPUDPServer.initialiseUDPXMLConfig(XMLconfigFile)

		XPUDP.pyXPUDPServer.start()

		self.updatingCompPanel = True

		self.ardXMLconfig = lib.arduinoXMLconfig.arduinoConfig("config/ardConfig1.xml")
		self.ardXMLconfig.registerArduinoAttributeChangedCallback(self.handleArduinoAttributeChange)

		self.arduinoList = []

		self.refreshArduinoList()

		self.deleteConfirmDialog = deleteConfirmationDialog.DeleteConfirmationDialog()
		self.addArduinoDialog = pyXPaddArduinoDialog.pyXPAddArduinoDialog()
		self.pickXPCommandDialog = pyXPpickXPCommandDialog.pyXPpickXPCommandDialog()
		self.editXPUDPConfigDialog = pyXPUDPConfigDialog.pyXPUDPConfigDialog(XMLconfigFile)
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

		self.actionSave.setEnabled(False)
		self.updatingCompPanel = False

	def refreshArduinoList(self):
		self.arduinoList = []

		for arduino in self.ardXMLconfig.getArduinoList():
		#serialNumber, PORT, BAUD, XPUDPServer, arduinoXMLconfig)
			self.arduinoList.append(Arduino.Arduino(arduino['serial_nr'],
													XPUDP.pyXPUDPServer,
													self.ardXMLconfig
													))
		for arduino in self.arduinoList:
			arduino.start()
			arduino.updateComponentList('*', '', arduino.ardSerialNumber, 'pin')


	def closeEvent(self, event):
		XPUDP.pyXPUDPServer.quit()
		for arduino in self.arduinoList:
			arduino.quit()


	def ardSwitchChanged(self, pin, value):
		logging.debug("ard switch changed callback, pin", pin)

	def updateMessages(self):
		self.statusBar().showMessage(XPUDP.pyXPUDPServer.statusMsg)

	def refreshArduinoTree(self):
		logging.debug ("refreshArduinoTree")

		boldFont = QtGui.QFont()
		boldFont.setBold(True)
		self.arduinoTreeWidget.clear()

		for arduino in self.ardXMLconfig.root: # cycle through arduinos
			#logging.debug (arduino.tag, arduino.attrib)
			ardTreeElem = QTreeWidgetItem([ arduino.attrib['name'], arduino.attrib['serial_nr'], arduino.tag ])
			ardTreeElem.setFont(0, boldFont)

			if arduino.attrib['connected'] == 'Connected':
				ardTreeElem.setIcon(0, QtGui.QIcon("Resources/ardIcon2.png"))
			else:
				ardTreeElem.setIcon(0, QtGui.QIcon("Resources/ardIconDisconnected.png"))

			self.arduinoTreeWidget.addTopLevelItem(ardTreeElem)
			ardTreeElem.setExpanded(True)

			for inoutputs in arduino: # cycle through input outputs
				inoutputsTreeElem = QTreeWidgetItem([ inoutputs.attrib['description'], '', inoutputs.tag ])
				if inoutputs.tag == "inputs":
					inoutputsTreeElem.setIcon(0, QtGui.QIcon("Resources/inputIcon.png"))
				if inoutputs.tag == "outputs":
					inoutputsTreeElem.setIcon(0, QtGui.QIcon("Resources/outputIcon.png"))

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


	def updateComponentName(self, compID,compName):
		items = self.arduinoTreeWidget.findItems (compID, QtCore.Qt.MatchExactly|QtCore.Qt.MatchRecursive,1)
		if len(items)>0:
			items[0].setText(0, compName)
			#print (items)

	def handleArduinoAttributeChange(self, ardSerialNr, attribute):
		logging.info('ard attribute changed')
		self.__updateArduinoEditFormData(ardSerialNr)

	def __updateArduinoEditFormData(self, ardID):
		ardData = self.ardXMLconfig.getArduinoData(ardID)
		logging.info("ard data:"+str(ardData))
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
				items[0].setIcon(0, QtGui.QIcon("Resources/ardIcon2.png"))
		else:
			self.ardSerialConnStatusLabel.setStyleSheet("QLabel { font-weight: bold; background-color : red; color : white; }")
			items = self.arduinoTreeWidget.findItems (ardID, QtCore.Qt.MatchExactly|QtCore.Qt.MatchRecursive,1)
			if len(items)>0:
				items[0].setIcon(0, QtGui.QIcon("Resources/ardIconDisconnected.png"))

		if ardData['ard_status'] == 'Running':
			self.ardStatusLabel.setStyleSheet("QLabel { background-color : green; color : white; }")
			items = self.arduinoTreeWidget.findItems (ardID, QtCore.Qt.MatchExactly|QtCore.Qt.MatchRecursive,1)
			if len(items)>0:
				items[0].setIcon(0, QtGui.QIcon("Resources/ardIcon2.png"))
		else:
			self.ardStatusLabel.setStyleSheet("QLabel { font-weight: bold; background-color : red; color : white; }")
			items = self.arduinoTreeWidget.findItems (ardID, QtCore.Qt.MatchExactly|QtCore.Qt.MatchRecursive,1)
			if len(items)>0:
				items[0].setIcon(0, QtGui.QIcon("Resources/ardIconDisconnected.png"))

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
			tag 		= self.arduinoTreeWidget.selectedItems()[0].text(2)
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
		if self.updatingCompPanel == False:
			ardData = {'port': 			self.ardPortLineEdit.text(),
						'baud':			self.ardBaudComboBox.currentText(),
						'name': 		self.ardNameLineEdit.text(),
						'description': 	self.ardDescriptionLineEdit.text(),
						'serial_nr': 	self.ardSerialNrLineEdit.text(),
						'manufacturer': self.ardManufacturerLineEdit.text()}

			self.ardXMLconfig.updateArduinoData(ardData['serial_nr'], ardData)
			#self.refreshArduinoTree()
			self.updateComponentName( self.ardSerialNrLineEdit.text(),self.ardNameLineEdit.text())
			self.actionSave.setEnabled(True)

	def ardTreeContextMenuRequested(self, position):
		logging.debug("ardTreeContextMenuRequested")
		# find which item is selected
		if len(self.arduinoTreeWidget.selectedItems()) > 0 : # check at least one item selected
			tag 		= self.arduinoTreeWidget.selectedItems()[0].text(2)
			tag_descr 	= self.arduinoTreeWidget.selectedItems()[0].text(0)

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
			ardTableWidget = self.addArduinoDialog.arduinoTableWidget
			for row in range(0, ardTableWidget.rowCount()):
				if ardTableWidget.item(row,0).checkState() == QtCore.Qt.Checked :
					self.ardXMLconfig.addArduino(ardTableWidget.item(row,1).text(),
												ardTableWidget.item(row,2).text(),
												ardTableWidget.item(row,3).text(),
												ardTableWidget.item(row,4).text(),
												ardTableWidget.item(row,5).text())
			self.actionSave.setEnabled(True)
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
	app.exec_()                         # and execute the app


if __name__ == '__main__':              # if we're running file directly and not importing it
	main()                              # run the main function
