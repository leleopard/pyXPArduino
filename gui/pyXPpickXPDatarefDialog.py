from PyQt5 import QtCore, QtGui, QtWidgets
import gui.pickXPDatarefDialog as pickXPDatarefDialog

import lib.XPrefData as XPrefData
import logging


class pyXPpickXPDatarefDialog(QtWidgets.QDialog, pickXPDatarefDialog.Ui_Dialog):
	def __init__(self):
		super(self.__class__, self).__init__()
		self.setupUi(self)  # This is defined in design.py file automatically
							# It sets up layout and widgets that are defined
		self.selectCategoryComboBox.addItems(list(XPrefData.XP_DATAREFS_CATEGORIES.keys()))
	
	def refreshDatarefList(self):
		logging.info("category combobox changed")
		
		self.datarefTableWidget.setRowCount(0)
		
		datarefslist = XPrefData.getXPDatarefList(self.selectCategoryComboBox.currentText(),
												self.filterDatarefsLineEdit.text())
		
		index = 0
		for dataref in datarefslist:
			self.datarefTableWidget.insertRow(index)
			
			item = QtWidgets.QTableWidgetItem(dataref[0])
			self.datarefTableWidget.setItem(index,0,item )
			
			item = QtWidgets.QTableWidgetItem(dataref[1])
			self.datarefTableWidget.setItem(index,1,item )
			
			item = QtWidgets.QTableWidgetItem(dataref[2])
			self.datarefTableWidget.setItem(index,2,item )
			
			item = QtWidgets.QTableWidgetItem(dataref[3])
			self.datarefTableWidget.setItem(index,3,item )
			
			item = QtWidgets.QTableWidgetItem(dataref[4])
			self.datarefTableWidget.setItem(index,4,item )
			
			item = QtWidgets.QTableWidgetItem(dataref[5])
			self.datarefTableWidget.setItem(index,5,item )
			
			index = index+1
			
		self.datarefTableWidget.resizeColumnsToContents()
		#self.datarefTableWidget.resizeRowsToContents()
		self.datarefTableWidget.verticalHeader().hide()
		
	def pickDataref(self):
		logging.info("pick dataref")
		row = self.datarefTableWidget.currentRow()
		self.datarefLineEdit.setText(self.datarefTableWidget.item(row,1).text())
		
	