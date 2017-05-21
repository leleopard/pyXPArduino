LOGGING_LEVEL = "WARNIN"
import logging
LOGGING_FORMAT= '%(asctime)s %(levelname)-8s %(name)-20s %(funcName)-20s  %(message)s'

logging.basicConfig(format=LOGGING_FORMAT, level=logging.INFO)

from PyQt5 import QtCore, QtGui, QtWidgets # Import the PyQt5 modules we'll need
from PyQt5.QtWidgets import QApplication, QMainWindow,QTreeWidgetItem, QMenu
import sys # We need sys so that we can pass argv to QApplication

import gui.mainwindow as mainwindow# This file holds our MainWindow and all design related things
import gui.deleteConfirmationDialog as deleteConfirmationDialog
import gui.pyXPaddArduinoDialog as pyXPaddArduinoDialog
import gui.pyXPpickXPCommandDialog as pyXPpickXPCommandDialog
import gui.pyXPswitchEditForm as pyXPswitchEditForm
import gui.pyXPpotentiometerEditForm as pyXPpotentiometerEditForm

import lib.arduinoXMLconfig
import lib.XPrefData as XPrefData
import lib.XPlaneUDPServer as XPUDP
import lib.arduinoSerial as ardSerial
import lib.Arduino as Arduino




class pyXPArduino(QMainWindow, mainwindow.Ui_MainWindow):
	def __init__(self):
		super(self.__class__, self).__init__()
		self.setupUi(self)  # This is defined in design.py file automatically
							# It sets up layout and widgets that are defined
		self.timer = QtCore.QTimer()
		self.timer.timeout.connect(self.updateMessages)
		self.timer.start(500)
		
		XPUDP.pyXPUDPServer.initialiseUDP(('127.0.0.1',49008), ('192.168.1.1',49000), 'STEPHANE-PC')
		XPUDP.pyXPUDPServer.start()
		
		self.updatingCompPanel = False
		
		self.ardXMLconfig = lib.arduinoXMLconfig.arduinoConfig("ardConfig1.xml")
		self.arduinoList = []
		
		self.refreshArduinoList()
		
		self.deleteConfirmDialog = deleteConfirmationDialog.DeleteConfirmationDialog()
		self.addArduinoDialog = pyXPaddArduinoDialog.pyXPAddArduinoDialog()
		self.pickXPCommandDialog = pyXPpickXPCommandDialog.pyXPpickXPCommandDialog()
		#switch edit form
		self.ardSwitchEditForm = pyXPswitchEditForm.pyXPswitchEditForm(self.editPaneWidget, self.ardXMLconfig, self.actionSave)
		self.horizontalLayoutEditPane.addWidget(self.ardSwitchEditForm)
		self.ardSwitchEditForm.nameUpdated.connect(self.updateSwitchName)
		#potentiometer edit form
		self.ardPotentiometerEditForm = pyXPpotentiometerEditForm.pyXPpotentiometerEditForm(self.editPaneWidget, self.ardXMLconfig, self.actionSave)
		self.horizontalLayoutEditPane.addWidget(self.ardPotentiometerEditForm)
		#self.ardSwitchEditForm.nameUpdated.connect(self.updateSwitchName)
		
		self.ardBaudComboBox.addItems(lib.arduinoXMLconfig.ARD_BAUD)
		
		self.refreshArduinoTree()
		self.ardSwitchEditForm.hide()
		self.arduinoEditForm.hide()
		self.ardPotentiometerEditForm.hide()
		
		self.actionSave.setEnabled(False)
		
		
	def refreshArduinoList(self):
		self.arduinoList = []
		
		for arduino in self.ardXMLconfig.getArduinoList():
		#serialNumber, PORT, BAUD, XPUDPServer, arduinoXMLconfig)
			self.arduinoList.append(Arduino.Arduino(arduino['serial_nr'],
													arduino['port'],
													int(arduino['baud']),
													XPUDP.pyXPUDPServer,
													self.ardXMLconfig
													))
		for arduino in self.arduinoList:
			arduino.updateComponentList('*', '', arduino.ardSerialNumber, 'pin')
		
	def closeEvent(self, event):
		XPUDP.pyXPUDPServer.quit()
		for arduino in self.arduinoList:
			arduino.quit()
		
	
	def ardSwitchChanged(self, pin, value):
		print("ard switch changed callback, pin", pin)
	
	def updateMessages(self):
		self.statusBar().showMessage(XPUDP.pyXPUDPServer.statusMsg)
		
	def refreshArduinoTree(self):
		print ("refreshArduinoTree")

		boldFont = QtGui.QFont()
		boldFont.setBold(True)
		self.arduinoTreeWidget.clear()
		
		for arduino in self.ardXMLconfig.root: # cycle through arduinos
			#print (arduino.tag, arduino.attrib)
			ardTreeElem = QTreeWidgetItem([ arduino.attrib['name'], arduino.attrib['serial_nr'], arduino.tag ])
			ardTreeElem.setFont(0, boldFont)
			ardTreeElem.setIcon(0, QtGui.QIcon("Resources/ardIcon.png"))
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
		

	def updateSwitchName(self, switchID,switchName):
		items = self.arduinoTreeWidget.findItems (switchID, QtCore.Qt.MatchExactly|QtCore.Qt.MatchRecursive,1)
		if len(items)>0:
			items[0].setText(0, switchName)
			#print (items)
	
	
	def ardTreeSelectionChanged(self):
		self.updatingCompPanel = True
		print("Ard tree selection changed")
		self.ardSwitchEditForm.hide()
		self.arduinoEditForm.hide()
		self.ardPotentiometerEditForm.hide()
		
		if len(self.arduinoTreeWidget.selectedItems()) > 0:
			tag 		= self.arduinoTreeWidget.selectedItems()[0].text(2)
			compID = self.arduinoTreeWidget.selectedItems()[0].text(1)
			
			if tag =='arduino':
				self.arduinoEditForm.show()
				ardData = self.ardXMLconfig.getArduinoData(compID)
				self.ardSerialNrLineEdit.setText(ardData['serial_nr'])
				self.ardBaudComboBox.setCurrentText(ardData['baud'])
				self.ardPortLineEdit.setText(ardData['port'])
				self.ardNameLineEdit.setText(ardData['name'])
				self.ardDescriptionLineEdit.setText(ardData['description'])
				self.ardManufacturerLineEdit.setText(ardData['manufacturer'])
			
			if tag =='switch':
				self.ardSwitchEditForm.show(compID)
			
			if tag =='potentiometer':
				self.ardPotentiometerEditForm.show(compID)
		
		self.updatingCompPanel = False
	
	## Saves the changes made in the Arduino Edit screen - called when user finishes editing the name.
	#	
	def ardEditingFinished(self):
		if self.updatingCompPanel == False:
			ardData = {'port': 			self.ardPortLineEdit.text(),
						'baud':			self.ardBaudComboBox.currentText(),
						'name': 		self.ardNameLineEdit.text(),
						'description': 	self.ardDescriptionLineEdit.text(),
						'serial_nr': 	self.ardSerialNrLineEdit.text(),
						'manufacturer': self.ardManufacturerLineEdit.text()}
						
			self.ardXMLconfig.updateArduinoData(ardData['serial_nr'], ardData)
			self.refreshArduinoTree()
			self.actionSave.setEnabled(True)
		
	def ardTreeContextMenuRequested(self, position):
		print("ardTreeContextMenuRequested")
		# find which item is selected
		if len(self.arduinoTreeWidget.selectedItems()) > 0 : # check at least one item selected 
			tag 		= self.arduinoTreeWidget.selectedItems()[0].text(2)
			tag_descr 	= self.arduinoTreeWidget.selectedItems()[0].text(0)
			
			print(self.arduinoTreeWidget.selectedItems()[0].text(2))
			
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
		print("add ard item")
		selectedItem = self.arduinoTreeWidget.selectedItems()[0]
		selectedItemTag = selectedItem.text(2)
		selectedArduinoSerialNr = selectedItem.parent().parent().text(1)
		
		self.ardXMLconfig.addInputOutput(selectedArduinoSerialNr, selectedItemTag)
		self.refreshArduinoTree()
		self.actionSave.setEnabled(True)
		
	def removeCompAction(self):
		print("remove ard item")
		
		returnCode = self.deleteConfirmDialog.exec()
		if returnCode == 1:
			selectedItem = self.arduinoTreeWidget.selectedItems()[0]
			selectedItemID = selectedItem.text(1)
			selectedArduinoSerialNr = selectedItem.parent().parent().parent().text(1)
			
			self.ardXMLconfig.removeInputOutput(selectedArduinoSerialNr, selectedItemID)
			self.refreshArduinoTree()
			self.actionSave.setEnabled(True)
	
	def removeArduino(self):
		print("remove arduino")
		
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
		print(returnCode)
		
		
def main():
	app = QApplication(sys.argv)  # A new instance of QApplication
	form = pyXPArduino()                 
	form.show()                         # Show the form
	app.exec_()                         # and execute the app


if __name__ == '__main__':              # if we're running file directly and not importing it
	main()                              # run the main function