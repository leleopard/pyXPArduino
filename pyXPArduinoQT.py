from PyQt5 import QtGui, QtWidgets # Import the PyQt4 module we'll need
#from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import QApplication, QMainWindow,QTreeWidgetItem, QMenu
import sys # We need sys so that we can pass argv to QApplication

import gui.mainwindow as mainwindow# This file holds our MainWindow and all design related things
              # it also keeps events etc that we defined in Qt Designer
import lib.arduinoXMLconfig

class ExampleApp(QMainWindow, mainwindow.Ui_MainWindow):
	def __init__(self):
		super(self.__class__, self).__init__()
		self.setupUi(self)  # This is defined in design.py file automatically
							# It sets up layout and widgets that are defined
		
		self.ardXMLconfig = lib.arduinoXMLconfig.arduinoConfig("ardConfig1.xml")
		
		self.refreshArduinoTree()
		

	def refreshArduinoTree(self):
		boldFont = QtGui.QFont()
		boldFont.setBold(True)
		
		for arduino in self.ardXMLconfig.root: # cycle through arduinos
			print (arduino.tag, arduino.attrib)
			ardTreeElem = QTreeWidgetItem([ arduino.attrib['name'], arduino.attrib['serial_nr'], arduino.tag ])
			ardTreeElem.setFont(0, boldFont)
			self.arduinoTreeWidget.addTopLevelItem(ardTreeElem)
			
			for inoutputs in arduino: # cycle through input outputs
				inoutputsTreeElem = QTreeWidgetItem([ inoutputs.attrib['description'], '', inoutputs.tag ])
				ardTreeElem.addChild(inoutputsTreeElem)
				
				for inputOutputTypes in inoutputs:  # iterate through input and output types
					inputOutputTypesTreeElem = QTreeWidgetItem([ inputOutputTypes.attrib['description'], '', inputOutputTypes.tag ])
					inoutputsTreeElem.addChild(inputOutputTypesTreeElem)
		
	def ardTreeContextMenuRequested(self, position):
		print("its me!!")
		# find which item is selected
		tag 		= self.arduinoTreeWidget.selectedItems()[0].text(2)
		tag_descr 	= self.arduinoTreeWidget.selectedItems()[0].text(0)
		
		print(self.arduinoTreeWidget.selectedItems()[0].text(2))
		
		if tag in lib.arduinoXMLconfig.INPUT_OUTPUT_TAGS:
			menu = QMenu()
			addCompAction = QtWidgets.QAction(lib.arduinoXMLconfig.INPUT_OUTPUT_TAGS_ACTIONS[tag])
			addCompAction.triggered.connect(self.addCompAction)
			menu.addAction(addCompAction)
			menu.exec_(self.arduinoTreeWidget.viewport().mapToGlobal(position))
		
	def addCompAction(self):
		print("add ard item")
		selectedItem = self.arduinoTreeWidget.selectedItems()[0]
		selectedArduinoSerialNr = selectedItem.parent().parent().text(1)
		
		print("Arduino serial nr:", selectedArduinoSerialNr)
		
		print(self.ardXMLconfig.root.findall("[@serial_nr='"+selectedArduinoSerialNr+"']"))
		
		
		
def main():
	app = QApplication(sys.argv)  # A new instance of QApplication
	form = ExampleApp()                 # We set the form to be our ExampleApp (design)
	form.show()                         # Show the form
	app.exec_()                         # and execute the app


if __name__ == '__main__':              # if we're running file directly and not importing it
	main()                              # run the main function