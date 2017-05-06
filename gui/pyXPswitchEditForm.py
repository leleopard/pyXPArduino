from PyQt5 import QtCore, QtGui, QtWidgets
import gui.switchEditForm as switchEditForm

import lib.XPrefData as XPrefData
import gui.pyXPpickXPCommandDialog as pyXPpickXPCommandDialog
import lib.arduinoXMLconfig


class pyXPswitchEditForm(QtWidgets.QWidget, switchEditForm.Ui_switchEditForm):
	switchNameUpdated = QtCore.pyqtSignal(str,str)
	
	def __init__(self,widget, ardXMLconfig):
		super(self.__class__, self).__init__(widget)
		self.setupUi(self)  # This is defined in design.py file automatically
							# It sets up layout and widgets that are defined
		self.switchID = ''
		self.ardXMLconfig = ardXMLconfig
		self.pickXPCommandDialog = pyXPpickXPCommandDialog.pyXPpickXPCommandDialog()
		self.SW_PIN_comboBox.addItems(lib.arduinoXMLconfig.DIG_IO_PINS)
	
		
	def show(self, switchID):
		print("show switch ID:", switchID)
		self.switchID = switchID
		switchData = self.ardXMLconfig.getSwitchData(switchID)
		print(switchData)
		self.SWEDIT_nameLineEdit.setText(switchData['name'])
		self.SWEDIT_IDlineEdit.setText(switchData['id'])
		pinIndex = self.SW_PIN_comboBox.findText(switchData['pin'])
		self.SW_PIN_comboBox.setCurrentIndex(pinIndex)
		
		self.SWON_CMDS_TABLE.setRowCount(0)
		self.SWOFF_CMDS_TABLE.setRowCount(0)
		
		actions = switchData['actions']
		for action in actions:
			if action['switch_state'] == 'on':
				if action['action_type'] == 'cmd':
					index = self.SWON_CMDS_TABLE.rowCount()
					self.SWON_CMDS_TABLE.insertRow(index)
					item = QtWidgets.QTableWidgetItem(action['cmddref'])
					self.SWON_CMDS_TABLE.setItem(index,0, item)
					
			if action['switch_state'] == 'off':
				if action['action_type'] == 'cmd':
					index = self.SWOFF_CMDS_TABLE.rowCount()
					self.SWOFF_CMDS_TABLE.insertRow(index)
					item = QtWidgets.QTableWidgetItem(action['cmddref'])
					self.SWOFF_CMDS_TABLE.setItem(index,0, item)
				
		self.SWON_CMDS_TABLE.setColumnWidth(0,350)
		self.SWON_CMDS_TABLE.resizeRowsToContents()
		self.SWOFF_CMDS_TABLE.setColumnWidth(0,350)
		self.SWOFF_CMDS_TABLE.resizeRowsToContents()
		
				
		super().show()
		
	def hide(self):
		self.SWON_CMDS_TABLE.setRowCount(0)
		self.SWOFF_CMDS_TABLE.setRowCount(0)
		super().hide()
		
	def updateSwitchXMLdata(self):
		print("updateSwitchXMLdata")
		actions = []
		index = 0
		for i in range(0, self.SWON_CMDS_TABLE.rowCount()):
			item = self.SWON_CMDS_TABLE.item(i,0)
			actioncmddref = ''
			if item != None:
				actioncmddref = self.SWON_CMDS_TABLE.item(i,0).text()
				
			actions.append({'switch_state':'on', 
						  'action_type':'cmd', 
						  'cmddref':actioncmddref})
			index = i
		
		for i in range(0, self.SWOFF_CMDS_TABLE.rowCount()):
			item = self.SWOFF_CMDS_TABLE.item(i,0)
			actioncmddref = ''
			if item != None:
				actioncmddref = self.SWOFF_CMDS_TABLE.item(i,0).text()
				
			actions.append({'switch_state':'off', 
						  'action_type':'cmd', 
						  'cmddref':actioncmddref})
		
		self.ardXMLconfig.updateSwitchData(self.switchID, {'id':self.SWEDIT_IDlineEdit.text(),
															'name':self.SWEDIT_nameLineEdit.text(),
															'pin':self.SW_PIN_comboBox.currentText()},
															actions)
															
		self.switchNameUpdated.emit(self.SWEDIT_IDlineEdit.text(), self.SWEDIT_nameLineEdit.text())
		
	def addSwitchOnCommand(self):
		print("ADD SW ON COMMAND")
		self.SWON_CMDS_TABLE.insertRow(self.SWON_CMDS_TABLE.rowCount())
		self.SWON_CMDS_TABLE.resizeRowsToContents()
		self.updateSwitchXMLdata()
		
	def rmSwitchOnCommand(self):
		row = self.SWON_CMDS_TABLE.currentRow()
		self.SWON_CMDS_TABLE.removeRow(row)
		self.updateSwitchXMLdata()
	
	def addSwitchOnDataref(self):
		self.SWON_DREFS_TABLE.insertRow(self.SWON_DREFS_TABLE.rowCount())
		self.SWON_DREFS_TABLE.resizeRowsToContents()
		self.updateSwitchXMLdata()
		
	def rmSwitchOnDataref(self):
		row = self.SWON_DREFS_TABLE.currentRow()
		self.SWON_DREFS_TABLE.removeRow(row)
		self.updateSwitchXMLdata()
		
	def addSwitchOffCommand(self):
		self.SWOFF_CMDS_TABLE.insertRow(self.SWOFF_CMDS_TABLE.rowCount())
		self.SWOFF_CMDS_TABLE.resizeRowsToContents()
		self.updateSwitchXMLdata()
		
	def rmSwitchOffCommand(self):
		row = self.SWOFF_CMDS_TABLE.currentRow()
		self.SWOFF_CMDS_TABLE.removeRow(row)
		self.updateSwitchXMLdata()
		
	def addSwitchOffDataref(self):
		self.SWOFF_DREFS_TABLE.insertRow(self.SWOFF_DREFS_TABLE.rowCount())
		self.SWOFF_DREFS_TABLE.resizeRowsToContents()
		self.updateSwitchXMLdata()
		
	def rmSwitchOffDataref(self):
		row = self.SWOFF_DREFS_TABLE.currentRow()
		self.SWOFF_DREFS_TABLE.removeRow(row)
		self.updateSwitchXMLdata()
		
	## slot intended to be called from a QTableWidget. The row and cell passed in argument will be assumed to be the XPlane command to edit
	#
	def editXPCommand(self, row, column):
		print("Edit XP cmd, row:", row, " column:", column)
		callingQwidgetTable = self.sender()
		item = callingQwidgetTable.item(row, column)
		if item == None:
			text = ''
		else:
			text = callingQwidgetTable.item(row, column).text()
			
		self.pickXPCommandDialog.commandLineEdit.setText(text)
		
		returnCode = self.pickXPCommandDialog.exec()
		
		if returnCode == 1: # command selected
			item = QtWidgets.QTableWidgetItem(self.pickXPCommandDialog.commandLineEdit.text())
			callingQwidgetTable.setItem(row, column, item)