from PyQt5 import QtCore, QtGui, QtWidgets
import gui.pickXPCommandDialog as pickXPCommandDialog

import lib.XPrefData as XPrefData


class pyXPpickXPCommandDialog(QtWidgets.QDialog, pickXPCommandDialog.Ui_Dialog):
	def __init__(self):
		super(self.__class__, self).__init__()
		self.setupUi(self)  # This is defined in design.py file automatically
							# It sets up layout and widgets that are defined
		self.selectCategoryComboBox.addItems(list(XPrefData.XP_COMMANDS_CATEGORIES.keys()))
	
	def refreshCommandList(self):
		print("category combobox changed")
		
		self.commandsTableWidget.setRowCount(0)
		
		commandslist = XPrefData.getXPCommandList(self.selectCategoryComboBox.currentText(),
												self.filterCommandsLineEdit.text())
		
		index = 0
		for command in commandslist:
			self.commandsTableWidget.insertRow(index)
			
			item = QtWidgets.QTableWidgetItem(command[0])
			item.setFlags(QtCore.Qt.ItemIsEnabled)
			item.setFlags(QtCore.Qt.ItemIsSelectable)
			self.commandsTableWidget.setItem(index,0,item )
			
			item = QtWidgets.QTableWidgetItem(command[1])
			item.setFlags(QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsSelectable)
			#item.setFlags(QtCore.Qt.ItemIsEditable)
			self.commandsTableWidget.setItem(index,1,item )
			
			item = QtWidgets.QTableWidgetItem(command[2])
			item.setFlags(QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsSelectable)
			#item.setFlags(QtCore.Qt.ItemIsEditable)
			self.commandsTableWidget.setItem(index,2,item )
					
			index = index+1
			
		self.commandsTableWidget.resizeColumnsToContents()
		self.commandsTableWidget.resizeRowsToContents()
		#self.commandsTableWidget.verticalHeader().hide()