from PyQt5 import QtCore, QtGui, QtWidgets
import logging
import gui.pickarduinodialog as pickarduinodialog

import lib.arduinoXMLconfig
import lib.serialArduinoUtils


class pyXPAddArduinoDialog(QtWidgets.QDialog, pickarduinodialog.Ui_AddArduinoDialog):
	def __init__(self):
		super(self.__class__, self).__init__()
		self.setupUi(self)  # This is defined in design.py file automatically
							# It sets up layout and widgets that are defined
							
							
	def refreshArduinoList(self, ardXMLconfig):
		self.arduinoTableWidget.setRowCount(0)
		list = lib.serialArduinoUtils.listArduinosSerial()
		index = 0
		for p in list:
			description = str(p.description)
			if "Ard" in description:
				logging.info("FOUND ARDUINO")
				serial_number = str(p.serial_number)
				if ardXMLconfig.getArduinoData(serial_number) == None :  # only display the arduino if it is not already in our list
					data = [False, str(p.device),"NAME"+str(index), description, str(p.serial_number), str(p.manufacturer)]
					self.arduinoTableWidget.insertRow(index)
					item = QtWidgets.QTableWidgetItem()
					#item.setFlags(QtCore.Qt.ItemIsEditable)
					item.setCheckState(QtCore.Qt.Unchecked)
					item.setTextAlignment(QtCore.Qt.AlignHCenter)
					self.arduinoTableWidget.setItem(index,0, item)
					
					item = QtWidgets.QTableWidgetItem(str(p.device))
					item.setFlags(QtCore.Qt.ItemIsEditable)
					self.arduinoTableWidget.setItem(index,1, item)
					self.arduinoTableWidget.setItem(index,2,QtWidgets.QTableWidgetItem("NAME "+str(index)) )
					item = QtWidgets.QTableWidgetItem(description)
					item.setFlags(QtCore.Qt.ItemIsEditable)
					self.arduinoTableWidget.setItem(index,3,item )
					item = QtWidgets.QTableWidgetItem(serial_number)
					item.setFlags(QtCore.Qt.ItemIsEditable)
					self.arduinoTableWidget.setItem(index,4,item )
					item = QtWidgets.QTableWidgetItem(str(p.manufacturer))
					item.setFlags(QtCore.Qt.ItemIsEditable)
					self.arduinoTableWidget.setItem(index,5,item )
					
					index = index + 1
			logging.info (p.description,  p.serial_number, str(p.hwid), str(p.vid), str(p.pid), p.manufacturer)
		
		self.arduinoTableWidget.resizeColumnsToContents()
		self.arduinoTableWidget.resizeRowsToContents()
		self.arduinoTableWidget.verticalHeader().hide()
		