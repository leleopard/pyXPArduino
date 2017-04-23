from PyQt5 import QtCore, QtGui, QtWidgets # Import the PyQt5 modules we'll need
from PyQt5.QtWidgets import QApplication, QMainWindow,QTreeWidgetItem, QMenu
import sys # We need sys so that we can pass argv to QApplication

import gui.mainwindow as mainwindow# This file holds our MainWindow and all design related things
import gui.deleteConfirmationDialog as deleteConfirmationDialog
import gui.pyXPaddArduinoDialog as pyXPaddArduinoDialog

import lib.arduinoXMLconfig
import lib.XPrefData as XPrefData

class ExampleApp(QMainWindow, mainwindow.Ui_MainWindow):
	def __init__(self):
		super(self.__class__, self).__init__()
		self.setupUi(self)  # This is defined in design.py file automatically
							# It sets up layout and widgets that are defined
		
		self.ardXMLconfig = lib.arduinoXMLconfig.arduinoConfig("ardConfig1.xml")
		self.deleteConfirmDialog = deleteConfirmationDialog.DeleteConfirmationDialog()
		self.addArduinoDialog = pyXPaddArduinoDialog.pyXPAddArduinoDialog()
		self.refreshArduinoTree()
		self.__setupSwitchEditScreen()
		
		#self.switchEditForm.hide()
		self.arduinoEditForm.hide()

	def __setupSwitchEditScreen(self):
		self.SW_PIN_comboBox.addItems(lib.arduinoXMLconfig.DIG_IO_PINS)
		self.SWON_XPCMD_comboBox.addItems(XPrefData.XP_COMMANDS)
		
		
	
	def refreshArduinoTree(self):
		boldFont = QtGui.QFont()
		boldFont.setBold(True)
		self.arduinoTreeWidget.clear()
		
		for arduino in self.ardXMLconfig.root: # cycle through arduinos
			print (arduino.tag, arduino.attrib)
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
					
		self.arduinoTreeWidget.resizeColumnToContents(0)
	
	def ardTreeSelectionChanged(self):
		print("Ard tree selection changed")
		self.switchEditForm.hide()
		self.arduinoEditForm.hide()
		
		if len(self.arduinoTreeWidget.selectedItems()) > 0:
			tag 		= self.arduinoTreeWidget.selectedItems()[0].text(2)
				
			if tag =='arduino':
				self.arduinoEditForm.show()
				ardData = self.ardXMLconfig.getArduinoData(self.arduinoTreeWidget.selectedItems()[0].text(1))
				self.ardSerialNrLineEdit.setText(ardData['serial_nr'])
				self.ardPortLineEdit.setText(ardData['port'])
				self.ardNameLineEdit.setText(ardData['name'])
				self.ardDescriptionLineEdit.setText(ardData['description'])
				self.ardManufacturerLineEdit.setText(ardData['manufacturer'])
		
	def ardEditingFinished(self):
		ardData = {'port': 			self.ardPortLineEdit.text(),
					'name': 		self.ardNameLineEdit.text(),
					'description': 	self.ardDescriptionLineEdit.text(),
					'serial_nr': 	self.ardSerialNrLineEdit.text(),
					'manufacturer': self.ardManufacturerLineEdit.text()}
					
		self.ardXMLconfig.updateArduinoData(ardData['serial_nr'], ardData)
		self.refreshArduinoTree()
		
	def ardTreeContextMenuRequested(self, position):
		# find which item is selected
		tag 		= self.arduinoTreeWidget.selectedItems()[0].text(2)
		tag_descr 	= self.arduinoTreeWidget.selectedItems()[0].text(0)
		
		print(self.arduinoTreeWidget.selectedItems()[0].text(2))
		
		if tag =='arduino':
			menu = QMenu()
			removeArdAction = QtWidgets.QAction('Remove Arduino...')
			removeArdAction.triggered.connect(self.removeArduino)
			menu.addAction(removeArdAction)
			menu.exec_(self.arduinoTreeWidget.viewport().mapToGlobal(position))
		
		
		if tag in lib.arduinoXMLconfig.INPUT_OUTPUT_TAGS:
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
		print("add ard item")
		selectedItem = self.arduinoTreeWidget.selectedItems()[0]
		selectedItemTag = selectedItem.text(2)
		selectedArduinoSerialNr = selectedItem.parent().parent().text(1)
		
		self.ardXMLconfig.addInputOutput(selectedArduinoSerialNr, selectedItemTag)
		self.refreshArduinoTree()
		
	def removeCompAction(self):
		print("remove ard item")
		
		returnCode = self.deleteConfirmDialog.exec()
		if returnCode == 1:
			selectedItem = self.arduinoTreeWidget.selectedItems()[0]
			selectedItemID = selectedItem.text(1)
			selectedArduinoSerialNr = selectedItem.parent().parent().parent().text(1)
			
			self.ardXMLconfig.removeInputOutput(selectedArduinoSerialNr, selectedItemID)
			self.refreshArduinoTree()
	
	def removeArduino(self):
		print("remove arduino")
		
		returnCode = self.deleteConfirmDialog.exec()
		if returnCode == 1:
			selectedItem = self.arduinoTreeWidget.selectedItems()[0]
			#selectedItemID = selectedItem.text(1)
			selectedArduinoSerialNr = selectedItem.text(1)
			
			self.ardXMLconfig.removeArduino(selectedArduinoSerialNr)
			self.refreshArduinoTree()
			
	def saveToXML(self):
		self.ardXMLconfig.saveToXMLfile()
		
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
					
		self.refreshArduinoTree()
		print(returnCode)
		
		
def main():
	app = QApplication(sys.argv)  # A new instance of QApplication
	form = ExampleApp()                 # We set the form to be our ExampleApp (design)
	form.show()                         # Show the form
	app.exec_()                         # and execute the app


if __name__ == '__main__':              # if we're running file directly and not importing it
	main()                              # run the main function