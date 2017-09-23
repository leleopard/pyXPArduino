import logging

from PyQt5 import QtCore, QtGui, QtWidgets
import gui.rotencoderEditForm as rotencoderEditForm

import lib.XPrefData as XPrefData
import gui.pyXPpickXPCommandDialog as pyXPpickXPCommandDialog
import gui.pyXPpickXPDatarefDialog as pyXPpickXPDatarefDialog

import lib.arduinoXMLconfig

import lib.XPlaneUDPServer as XPUDP

logger = logging.getLogger('gui')

class pyXProtencoderEditForm(QtWidgets.QWidget, rotencoderEditForm.Ui_rotencoderEditForm):
	nameUpdated = QtCore.pyqtSignal(str,str)
	pinUpdated = QtCore.pyqtSignal(str)
	
	def __init__(self,widget, ardXMLconfig, actionSave):
		super(self.__class__, self).__init__(widget)
		self.repopulating = False
		self.setupUi(self)  # This is defined in design.py file automatically
							# It sets up layout and widgets that are defined
		self.actionSave = actionSave
		self.componentID = ''
		self.componentType = "rot_encoder"
		self.ardXMLconfig = ardXMLconfig
		self.ardXMLconfig.registerComponentAttributeChangedCallback(self.updateStateWidget)
		self.pickXPCommandDialog = pyXPpickXPCommandDialog.pyXPpickXPCommandDialog()
		self.pickXPDatarefDialog = pyXPpickXPDatarefDialog.pyXPpickXPDatarefDialog()
		self.PINA_comboBox.addItems(lib.arduinoXMLconfig.DIG_IO_PINS)
		self.PINB_comboBox.addItems(lib.arduinoXMLconfig.DIG_IO_PINS)
		self.steps_comboBox.addItems(['1','2','4'])
		
	def show(self, componentID, ardSerialNr = None):
		self.repopulating = True
		self.componentID = componentID
		componentData = self.ardXMLconfig.getComponentData(componentID, self.componentType)
		
		self.nameLineEdit.setText(componentData['name'])
		self.IDlineEdit.setText(componentData['id'])
		pinIndex = self.PINA_comboBox.findText(componentData['pin'])
		self.PINA_comboBox.setCurrentIndex(pinIndex)
		
		pinIndex = self.PINB_comboBox.findText(componentData['pin2'])
		self.PINB_comboBox.setCurrentIndex(pinIndex)
		
		stepsIndex = self.steps_comboBox.findText(componentData['stepsPerNotch'])
		self.steps_comboBox.setCurrentIndex(stepsIndex)
		
		################### TO UPDATE
		switchState = componentData['state']
		if switchState == 'on':
			self.switchStateButton.setChecked(True) 
		else:
			self.switchStateButton.setChecked(False) 
		######################
		
		self.UP_CMDS_TABLE.setRowCount(0)
		self.DOWN_CMDS_TABLE.setRowCount(0)
		
		actions = componentData['actions']
		for action in actions:
			if action['state'] == 'up':
				if action['action_type'] == 'cmd':
					index = self.UP_CMDS_TABLE.rowCount()
					self.UP_CMDS_TABLE.insertRow(index)
					item = QtWidgets.QTableWidgetItem(action['cmddref'])
					self.UP_CMDS_TABLE.setItem(index,0, item)
					
					check_state = QtCore.Qt.Unchecked
					if action['continuous'] == 'True':
						check_state = QtCore.Qt.Checked
					
					item = QtWidgets.QTableWidgetItem()
					item.setCheckState(check_state)
					self.UP_CMDS_TABLE.setItem(index,1, item)
					
					
				if action['action_type'] == 'dref':
					index = self.UP_DREFS_TABLE.rowCount()
					self.UP_DREFS_TABLE.insertRow(index)
					item = QtWidgets.QTableWidgetItem(action['cmddref'])
					self.UP_DREFS_TABLE.setItem(index,0, item)
					item = QtWidgets.QTableWidgetItem(action['index'])
					self.UP_DREFS_TABLE.setItem(index,1, item)
					item = QtWidgets.QTableWidgetItem(action['setToValue'])
					self.UP_DREFS_TABLE.setItem(index,2, item)
					
					check_state = QtCore.Qt.Unchecked
					if action['continuous'] == 'True':
						check_state = QtCore.Qt.Checked
						
					item = QtWidgets.QTableWidgetItem()
					item.setCheckState(check_state)
					self.UP_DREFS_TABLE.setItem(index,3, item)
					
					drefList = XPrefData.getXPDatarefList(None, action['cmddref'])
					if len(drefList) > 0: # we have found the dataref
						item = QtWidgets.QTableWidgetItem(drefList[0][2]) # type
						self.UP_DREFS_TABLE.setItem(index, 4, item)
						
						item = QtWidgets.QTableWidgetItem(drefList[0][4]) # unit
						self.UP_DREFS_TABLE.setItem(index, 5, item)
						
			if action['state'] == 'down':
				if action['action_type'] == 'cmd':
					index = self.DOWN_CMDS_TABLE.rowCount()
					self.DOWN_CMDS_TABLE.insertRow(index)
					item = QtWidgets.QTableWidgetItem(action['cmddref'])
					self.DOWN_CMDS_TABLE.setItem(index,0, item)
					
					check_state = QtCore.Qt.Unchecked
					if action['continuous'] == 'True':
						check_state = QtCore.Qt.Checked
						
					item = QtWidgets.QTableWidgetItem()
					item.setCheckState(check_state)
					self.DOWN_CMDS_TABLE.setItem(index,1, item)
					
				if action['action_type'] == 'dref':
					index = self.DOWN_DREFS_TABLE.rowCount()
					self.DOWN_DREFS_TABLE.insertRow(index)
					item = QtWidgets.QTableWidgetItem(action['cmddref'])
					self.DOWN_DREFS_TABLE.setItem(index,0, item)
					item = QtWidgets.QTableWidgetItem(action['index'])
					self.DOWN_DREFS_TABLE.setItem(index,1, item)
					item = QtWidgets.QTableWidgetItem(action['setToValue'])
					self.DOWN_DREFS_TABLE.setItem(index,2, item)
					
					check_state = QtCore.Qt.Unchecked
					if action['continuous'] == 'True':
						check_state = QtCore.Qt.Checked
					
					item = QtWidgets.QTableWidgetItem()
					item.setCheckState(check_state)
					self.DOWN_DREFS_TABLE.setItem(index,3, item)
					
					drefList = XPrefData.getXPDatarefList(None, action['cmddref'])
					if len(drefList) > 0: # we have found the dataref
						item = QtWidgets.QTableWidgetItem(drefList[0][2]) # type
						self.DOWN_DREFS_TABLE.setItem(index, 4, item)
						
						item = QtWidgets.QTableWidgetItem(drefList[0][4]) # unit
						self.DOWN_DREFS_TABLE.setItem(index, 5, item)
				
		self.UP_CMDS_TABLE.setColumnWidth(0,350)
		self.UP_CMDS_TABLE.setColumnWidth(1,125)
		self.UP_CMDS_TABLE.resizeRowsToContents()
		self.DOWN_CMDS_TABLE.setColumnWidth(0,350)
		self.DOWN_CMDS_TABLE.setColumnWidth(1,125)
		self.DOWN_CMDS_TABLE.resizeRowsToContents()
		self.UP_DREFS_TABLE.resizeColumnsToContents()
		self.DOWN_DREFS_TABLE.resizeColumnsToContents()
		self.UP_DREFS_TABLE.resizeRowsToContents()
		self.DOWN_DREFS_TABLE.resizeRowsToContents()
		
		self.repopulating = False
		super().show()
	
	def hide(self):
		self.UP_CMDS_TABLE.setRowCount(0)
		self.DOWN_CMDS_TABLE.setRowCount(0)
		self.UP_DREFS_TABLE.setRowCount(0)
		self.DOWN_DREFS_TABLE.setRowCount(0)
		super().hide()
		
	def updateStateWidget(self, componentType, componentID, ardSerialNr = None, attribute = 'state'):
		logging.debug ('Update rot encoder widget'+componentType)
		if componentType == 'rot_encoder' and componentID == self.componentID and attribute == 'state':
			componentData = self.ardXMLconfig.getComponentData(componentID, self.componentType)
			state = componentData['state']
			if state == 'up':
				self.switchStateButton.setChecked(True) 
			else:
				self.switchStateButton.setChecked(False) 
		
	def activateSave(self):
		if self.repopulating == False:
			self.actionSave.setEnabled(True)
	
	def testOnCommands(self):
		for i in range(0, self.UP_CMDS_TABLE.rowCount()):
			item = self.UP_CMDS_TABLE.item(i,0)
			actioncmddref = ''
			if item != None:
				actioncmddref = self.UP_CMDS_TABLE.item(i,0).text()
				XPUDP.pyXPUDPServer.sendXPCmd(actioncmddref)
	
	def testOffCommands(self):
		for i in range(0, self.DOWN_CMDS_TABLE.rowCount()):
			item = self.DOWN_CMDS_TABLE.item(i,0)
			actioncmddref = ''
			if item != None:
				actioncmddref = self.DOWN_CMDS_TABLE.item(i,0).text()
				XPUDP.pyXPUDPServer.sendXPCmd(actioncmddref)
	
	def testOnDatarefs(self):
		for i in range(0, self.UP_DREFS_TABLE.rowCount()):
			item = self.UP_DREFS_TABLE.item(i,0)
			actioncmddref = ''
			if item != None:
				actioncmddref = self.UP_DREFS_TABLE.item(i,0).text()
				
				index = '0'
				setToValue = '0.0'
				
				item2 = self.UP_DREFS_TABLE.item(i,1)
				if item2 != None:
					index = self.UP_DREFS_TABLE.item(i,1).text()
				
				item2 = self.UP_DREFS_TABLE.item(i,2)
				if item2 != None:
					setToValue = self.UP_DREFS_TABLE.item(i,2).text()
				
				XPUDP.pyXPUDPServer.sendXPDref(actioncmddref, index, setToValue)
				
	def testOffDatarefs(self):
		for i in range(0, self.DOWN_DREFS_TABLE.rowCount()):
			item = self.DOWN_DREFS_TABLE.item(i,0)
			actioncmddref = ''
			if item != None:
				actioncmddref = self.DOWN_DREFS_TABLE.item(i,0).text()
				
				index = '0'
				setToValue = '0.0'
				
				item2 = self.DOWN_DREFS_TABLE.item(i,1)
				if item2 != None:
					index = self.DOWN_DREFS_TABLE.item(i,1).text()
				
				item2 = self.DOWN_DREFS_TABLE.item(i,2)
				if item2 != None:
					setToValue = self.DOWN_DREFS_TABLE.item(i,2).text()
				
				XPUDP.pyXPUDPServer.sendXPDref(actioncmddref, index, setToValue)
	
	def updateXMLdata(self):
		if self.repopulating == False:
			actions = []
			index = 0
			for i in range(0, self.UP_CMDS_TABLE.rowCount()):
				item = self.UP_CMDS_TABLE.item(i,0)
				actioncmddref = ''
				if item != None:
					actioncmddref = self.UP_CMDS_TABLE.item(i,0).text()
				
				action_continuous = 'False'
				if self.UP_CMDS_TABLE.item(i,1) != None:
					if self.UP_CMDS_TABLE.item(i,1).checkState() == QtCore.Qt.Checked:
						action_continuous = 'True'
					
				actions.append({'state':'up', 
							  'action_type':'cmd', 
							  'cmddref':actioncmddref,
							  'continuous':action_continuous})
				index = i
			
			for i in range(0, self.DOWN_CMDS_TABLE.rowCount()):
				item = self.DOWN_CMDS_TABLE.item(i,0)
				actioncmddref = ''
				if item != None:
					actioncmddref = self.DOWN_CMDS_TABLE.item(i,0).text()
					
				action_continuous = 'False'
				if self.DOWN_CMDS_TABLE.item(i,1) != None:
					if self.DOWN_CMDS_TABLE.item(i,1).checkState() == QtCore.Qt.Checked:
						action_continuous = 'True'
						
				actions.append({'state':'down', 
							  'action_type':'cmd', 
							  'cmddref':actioncmddref,
							  'continuous':action_continuous})
			
			for i in range(0, self.UP_DREFS_TABLE.rowCount()):
				item = self.UP_DREFS_TABLE.item(i,0)
				actioncmddref = ''
				if item != None:
					actioncmddref = self.UP_DREFS_TABLE.item(i,0).text()
				
				item = self.UP_DREFS_TABLE.item(i,1)
				drefIndex = ''
				if item != None:
					drefIndex = self.UP_DREFS_TABLE.item(i,1).text()
					
				item = self.UP_DREFS_TABLE.item(i,2)
				setToValue = ''
				if item != None:
					setToValue = self.UP_DREFS_TABLE.item(i,2).text()
				
				action_continuous = 'False'
				item = self.UP_DREFS_TABLE.item(i,3)
				if item != None:
					if self.UP_DREFS_TABLE.item(i,3).checkState() == QtCore.Qt.Checked:
						action_continuous = 'True'
				
				actions.append({'state':'up', 
							  'action_type':'dref', 
							  'cmddref':actioncmddref, 
							  'index':drefIndex,
							  'setToValue':  setToValue,
							  'continuous':action_continuous })
				index = i
			
			for i in range(0, self.DOWN_DREFS_TABLE.rowCount()):
				item = self.DOWN_DREFS_TABLE.item(i,0)
				actioncmddref = ''
				if item != None:
					actioncmddref = self.DOWN_DREFS_TABLE.item(i,0).text()
				
				item = self.DOWN_DREFS_TABLE.item(i,1)
				drefIndex = ''
				if item != None:
					drefIndex = self.DOWN_DREFS_TABLE.item(i,1).text()
					
				item = self.DOWN_DREFS_TABLE.item(i,2)
				setToValue = ''
				if item != None:
					setToValue = self.DOWN_DREFS_TABLE.item(i,2).text()
				
				action_continuous = 'False'
				item = self.DOWN_DREFS_TABLE.item(i,3)
				if item != None:
					if self.DOWN_DREFS_TABLE.item(i,3).checkState() == QtCore.Qt.Checked:
						action_continuous = 'True'
				
				actions.append({'state':'down', 
							  'action_type':'dref', 
							  'cmddref':actioncmddref, 
							  'index':drefIndex,
							  'setToValue':  setToValue,
							  'continuous':action_continuous })
				index = i
			
			self.ardXMLconfig.updateComponentData(self.componentID, self.componentType,
																{'id':self.IDlineEdit.text(),
																'name':self.nameLineEdit.text(),
																'pin':self.PINA_comboBox.currentText(),
																'pin2':self.PINB_comboBox.currentText(),
																'stepsPerNotch': self.steps_comboBox.currentText()},
																actions)
																
			self.nameUpdated.emit(self.IDlineEdit.text(), self.nameLineEdit.text())
			self.actionSave.setEnabled(True)
	
	def updatePin(self):
		logger.debug("rot encoder pin updated")
		self.pinUpdated.emit(self.IDlineEdit.text())
		
	def addRotencUpCommand(self):
		logger.debug("ADD ROT UP COMMAND")
		self.UP_CMDS_TABLE.insertRow(self.UP_CMDS_TABLE.rowCount())
		self.UP_CMDS_TABLE.resizeRowsToContents()
		self.updateXMLdata()
		self.actionSave.setEnabled(True)
		
	def rmRotencUpCommand(self):
		row = self.UP_CMDS_TABLE.currentRow()
		self.UP_CMDS_TABLE.removeRow(row)
		self.updateXMLdata()
		self.actionSave.setEnabled(True)
	
	def addRotencUpDataref(self):
		self.UP_DREFS_TABLE.insertRow(self.UP_DREFS_TABLE.rowCount())
		self.UP_DREFS_TABLE.resizeRowsToContents()
		self.updateXMLdata()
		self.actionSave.setEnabled(True)
		
	def rmRotencUpDataref(self):
		row = self.UP_DREFS_TABLE.currentRow()
		self.UP_DREFS_TABLE.removeRow(row)
		self.updateXMLdata()
		self.actionSave.setEnabled(True)
		
	def addRotencDownCommand(self):
		self.DOWN_CMDS_TABLE.insertRow(self.DOWN_CMDS_TABLE.rowCount())
		self.DOWN_CMDS_TABLE.resizeRowsToContents()
		self.updateXMLdata()
		self.actionSave.setEnabled(True)
		
	def rmRotencDownCommand(self):
		row = self.DOWN_CMDS_TABLE.currentRow()
		self.DOWN_CMDS_TABLE.removeRow(row)
		self.updateXMLdata()
		self.actionSave.setEnabled(True)
		
	def addRotencDownDataref(self):
		self.DOWN_DREFS_TABLE.insertRow(self.DOWN_DREFS_TABLE.rowCount())
		self.DOWN_DREFS_TABLE.resizeRowsToContents()
		self.updateXMLdata()
		self.actionSave.setEnabled(True)
		
	def rmRotencDownDataref(self):
		row = self.DOWN_DREFS_TABLE.currentRow()
		self.DOWN_DREFS_TABLE.removeRow(row)
		self.updateXMLdata()
		self.actionSave.setEnabled(True)
		
	## slot intended to be called from a QTableWidget. The row and cell passed in argument will be assumed to be the XPlane command to edit
	#
	def editXPCommand(self, row, column):
		logging.info("Edit XP cmd, row:", row, " column:", column)
		if column == 0:
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
				self.actionSave.setEnabled(True)
			
	## slot intended to be called from a QTableWidget. The row and cell passed in argument will be assumed to be the XPlane command to edit
	#
	def editXPDataref(self, row, column):
		logging.info("Edit XP dref, row:"+ str(row)+ " column:" +str(column))
		if column == 0: #only edit dref if first column
			callingQwidgetTable = self.sender()
			item = callingQwidgetTable.item(row, column)
			if item == None:
				text = ''
			else:
				text = callingQwidgetTable.item(row, column).text()
				
			self.pickXPDatarefDialog.datarefLineEdit.setText(text)
			
			returnCode = self.pickXPDatarefDialog.exec()
			
			if returnCode == 1: # command selected
				dataref = self.pickXPDatarefDialog.datarefLineEdit.text()
				item = QtWidgets.QTableWidgetItem(dataref)
				callingQwidgetTable.setItem(row, column, item)
				
				# default index to 0
				item = QtWidgets.QTableWidgetItem('0')
				callingQwidgetTable.setItem(row, 1, item)
				
				# default Set to value to 0.0
				item = QtWidgets.QTableWidgetItem('0.0')
				callingQwidgetTable.setItem(row, 2, item)
				
				
				# retrieve dref data
				drefList = XPrefData.getXPDatarefList(None, dataref)
				if len(drefList) > 0: # we have found the dataref
					item = QtWidgets.QTableWidgetItem(drefList[0][2]) # type
					callingQwidgetTable.setItem(row, 3, item)
					
					item = QtWidgets.QTableWidgetItem(drefList[0][4]) # unit
					callingQwidgetTable.setItem(row, 4, item)
				
				callingQwidgetTable.resizeColumnsToContents()
				self.actionSave.setEnabled(True)