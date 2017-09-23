import logging

from PyQt5 import QtCore, QtGui, QtWidgets
import gui.potentiometerEditForm as potentiometerEditForm

import lib.XPrefData as XPrefData
import gui.pyXPpickXPCommandDialog as pyXPpickXPCommandDialog
import gui.pyXPpickXPDatarefDialog as pyXPpickXPDatarefDialog

import lib.arduinoXMLconfig

import lib.XPlaneUDPServer as XPUDP
import time

class pyXPpotentiometerEditForm(QtWidgets.QWidget, potentiometerEditForm.Ui_potentiometerEditForm):
	nameUpdated = QtCore.pyqtSignal(str,str)
	pinUpdated = QtCore.pyqtSignal(str)
	
	def __init__(self,widget, ardXMLconfig, actionSave):
		super(self.__class__, self).__init__(widget)
		self.lastTimeCompStateWidgetUpdated = time.time()
		self.repopulating = False
		self.setupUi(self)  # This is defined in design.py file automatically
							# It sets up layout and widgets that are defined
		self.actionSave = actionSave
		self.componentID = ''
		self.componentType = "potentiometer"
		self.ardXMLconfig = ardXMLconfig
		self.ardXMLconfig.registerComponentAttributeChangedCallback(self.updateStateWidget)
		self.pickXPCommandDialog = pyXPpickXPCommandDialog.pyXPpickXPCommandDialog()
		self.pickXPDatarefDialog = pyXPpickXPDatarefDialog.pyXPpickXPDatarefDialog()
		self.PIN_comboBox.addItems(lib.arduinoXMLconfig.POT_PINS)
		

		
	def show(self, componentID, ardSerialNr = None):
		self.repopulating = True
		self.componentID = componentID
		componentData = self.ardXMLconfig.getComponentData(componentID, self.componentType)
		
		self.nameLineEdit.setText(componentData['name'])
		self.IDlineEdit.setText(componentData['id'])
		pinIndex = self.PIN_comboBox.findText(componentData['pin'])
		self.PIN_comboBox.setCurrentIndex(pinIndex)
		
		state = componentData['state']
		self.valueLabel.setText(state)
		try:
			self.valueSlider.setValue(int(state))
		except:
			logging.warning('could not convert state to int, state value: '+ state)
			
		self.CMDS_TABLE.setRowCount(0)
		
		actions = componentData['actions']
		for action in actions:
			if action['action_type'] == 'cmd':
				index = self.CMDS_TABLE.rowCount()
				self.CMDS_TABLE.insertRow(index)
				item = QtWidgets.QTableWidgetItem(action['cmddref'])
				self.CMDS_TABLE.setItem(index,0, item)
				item = QtWidgets.QTableWidgetItem(action['state'])
				self.CMDS_TABLE.setItem(index,1, item)
				
			if action['action_type'] == 'dref':
				index = self.DREFS_TABLE.rowCount()
				self.DREFS_TABLE.insertRow(index)
				item = QtWidgets.QTableWidgetItem(action['cmddref'])
				self.DREFS_TABLE.setItem(index,0, item)
				item = QtWidgets.QTableWidgetItem(action['index'])
				self.DREFS_TABLE.setItem(index,1, item)
				item = QtWidgets.QTableWidgetItem(action['setToValue'])
				self.DREFS_TABLE.setItem(index,2, item)
				
				drefList = XPrefData.getXPDatarefList(None, action['cmddref'])
				if len(drefList) > 0: # we have found the dataref
					item = QtWidgets.QTableWidgetItem(drefList[0][2]) # type
					self.DREFS_TABLE.setItem(index, 3, item)
					
					item = QtWidgets.QTableWidgetItem(drefList[0][4]) # unit
					self.DREFS_TABLE.setItem(index, 4, item)
						
				
		self.CMDS_TABLE.setColumnWidth(0,350)
		self.CMDS_TABLE.setColumnWidth(1,300)
		self.CMDS_TABLE.resizeRowsToContents()
		
		self.DREFS_TABLE.setColumnWidth(0,350)
		self.DREFS_TABLE.setColumnWidth(1,50)
		self.DREFS_TABLE.setColumnWidth(2,300)
		self.DREFS_TABLE.setColumnWidth(3,60)
		self.DREFS_TABLE.setColumnWidth(4,150)
		
		self.DREFS_TABLE.resizeRowsToContents()
		
		self.repopulating = False
		super().show()
	
	def hide(self):
		self.CMDS_TABLE.setRowCount(0)
		self.DREFS_TABLE.setRowCount(0)
		super().hide()
		
	def updateStateWidget(self, componentType, componentID, ardSerialNr = None, attribute = 'state'):
		if (time.time() - self.lastTimeCompStateWidgetUpdated) >= 0.001:
			self.lastTimeCompStateWidgetUpdated = time.time()
			logging.debug('update state widget'+componentType+componentID)
			if componentType == 'potentiometer' and componentID == self.componentID and attribute == 'state':
				componentData = self.ardXMLconfig.getComponentData(componentID, self.componentType)
				state = componentData['state']
				logging.debug('update state widget to value: '+state)
				self.valueLabel.setText(state)
				try:
					self.valueSlider.setValue(int(state))
				except:
					logging.warning('could not convert state to int, state value: '+ state)
					
	def activateSave(self):
		if self.repopulating == False:
			self.actionSave.setEnabled(True)
	
	def testCommands(self):
		for i in range(0, self.CMDS_TABLE.rowCount()):
			item = self.CMDS_TABLE.item(i,0)
			actioncmddref = ''
			if item != None:
				actioncmddref = self.CMDS_TABLE.item(i,0).text()
				XPUDP.pyXPUDPServer.sendXPCmd(actioncmddref)
		
	def testDatarefs(self):
		for i in range(0, self.DREFS_TABLE.rowCount()):
			item = self.DREFS_TABLE.item(i,0)
			actioncmddref = ''
			if item != None:
				actioncmddref = self.DREFS_TABLE.item(i,0).text()
				
				index = '0'
				setToValue = '0.0'
				
				item2 = self.DREFS_TABLE.item(i,1)
				if item2 != None:
					index = self.DREFS_TABLE.item(i,1).text()
				
				item2 = self.DREFS_TABLE.item(i,2)
				if item2 != None:
					setToValue = self.DREFS_TABLE.item(i,2).text()
				
				XPUDP.pyXPUDPServer.sendXPDref(actioncmddref, index, setToValue)
				
	
	def updateXMLdata(self):
		if self.repopulating == False:
			actions = []
			index = 0
			for i in range(0, self.CMDS_TABLE.rowCount()):
				item = self.CMDS_TABLE.item(i,0)
				actioncmddref = ''
				if item != None:
					actioncmddref = self.CMDS_TABLE.item(i,0).text()
				
				item = self.CMDS_TABLE.item(i,1)
				state = ''
				if item != None:
					state = self.CMDS_TABLE.item(i,1).text()
				
				actions.append({'state':state, 
							  'action_type':'cmd', 
							  'cmddref':actioncmddref})
				index = i
			
			for i in range(0, self.DREFS_TABLE.rowCount()):
				item = self.DREFS_TABLE.item(i,0)
				actioncmddref = ''
				if item != None:
					actioncmddref = self.DREFS_TABLE.item(i,0).text()
				
				item = self.DREFS_TABLE.item(i,1)
				drefIndex = ''
				if item != None:
					drefIndex = self.DREFS_TABLE.item(i,1).text()
					
				item = self.DREFS_TABLE.item(i,2)
				setToValue = ''
				if item != None:
					setToValue = self.DREFS_TABLE.item(i,2).text()
				
				actions.append({'state':'on', 
							  'action_type':'dref', 
							  'cmddref':actioncmddref, 
							  'index':drefIndex,
							  'setToValue':  setToValue })
				index = i
			
			self.ardXMLconfig.updateComponentData(self.componentID, self.componentType,
																{'id':self.IDlineEdit.text(),
																'name':self.nameLineEdit.text(),
																'pin':self.PIN_comboBox.currentText()},
																actions)
																
			self.nameUpdated.emit(self.IDlineEdit.text(), self.nameLineEdit.text())
			self.actionSave.setEnabled(True)
	
	def updatePin(self):
		logging.debug("pot pin updated")
		self.pinUpdated.emit(self.IDlineEdit.text())
		
	def addCommand(self):
		logging.debug("ADD SW ON COMMAND")
		self.CMDS_TABLE.insertRow(self.CMDS_TABLE.rowCount())
		self.CMDS_TABLE.resizeRowsToContents()
		self.updateXMLdata()
		self.actionSave.setEnabled(True)
		
	def rmCommand(self):
		row = self.CMDS_TABLE.currentRow()
		self.CMDS_TABLE.removeRow(row)
		self.updateXMLdata()
		self.actionSave.setEnabled(True)
	
	def addDataref(self):
		self.DREFS_TABLE.insertRow(self.DREFS_TABLE.rowCount())
		self.DREFS_TABLE.resizeRowsToContents()
		self.updateXMLdata()
		self.actionSave.setEnabled(True)
		
	def rmDataref(self):
		row = self.DREFS_TABLE.currentRow()
		self.DREFS_TABLE.removeRow(row)
		self.updateXMLdata()
		self.actionSave.setEnabled(True)
			
	## slot intended to be called from a QTableWidget. The row and cell passed in argument will be assumed to be the XPlane command to edit
	#
	def editXPCommand(self, row, column):
		logging.debug("Edit XP cmd, row:", row, " column:", column)
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
		logging.debug("Edit XP dref, row:"+ str(row)+ " column:" +str(column))
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
				
				self.actionSave.setEnabled(True)