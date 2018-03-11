import logging

from PyQt5 import QtCore, QtGui, QtWidgets
import gui.switchEditForm as switchEditForm
import gui.pyXPdatarefCommandEditWidget as pyXPdatarefCommandEditWidget

import lib.XPrefData as XPrefData
import gui.pyXPpickXPCommandDialog as pyXPpickXPCommandDialog
import gui.pyXPpickXPDatarefDialog as pyXPpickXPDatarefDialog

import lib.arduinoXMLconfig

import pyxpudpserver as XPUDP

class pyXPswitchEditForm(QtWidgets.QWidget, switchEditForm.Ui_switchEditForm):
	nameUpdated = QtCore.pyqtSignal(str,str)
	pinUpdated = QtCore.pyqtSignal(str)

	def __init__(self,widget, ardXMLconfig, actionSave):
		super(self.__class__, self).__init__(widget)
		self.repopulating = False
		self.setupUi(self)  # This is defined in design.py file automatically
							# It sets up layout and widgets that are defined
		self.actionSave = actionSave
		self.componentID = ''
		self.componentType = "switch"
		self.ardXMLconfig = ardXMLconfig
		self.ardXMLconfig.registerComponentAttributeChangedCallback(self.updateStateWidget)
		self.pickXPCommandDialog = pyXPpickXPCommandDialog.pyXPpickXPCommandDialog()
		self.pickXPDatarefDialog = pyXPpickXPDatarefDialog.pyXPpickXPDatarefDialog()
		self.PIN_comboBox.addItems(lib.arduinoXMLconfig.DIG_IO_PINS)

		self.testSWON_CMDS_button.hide()
		self.testSWOFF_CMDS_button.hide()
		self.testSWON_DREFS_button.hide()
		self.testSWOFF_DREFS_button.hide()

		self.DREFCMD_COLSIZE = 300



	def show(self, componentID, ardSerialNr = None):
		self.repopulating = True
		self.componentID = componentID
		componentData = self.ardXMLconfig.getComponentData(componentID, self.componentType)

		self.nameLineEdit.setText(componentData['name'])
		self.IDlineEdit.setText(componentData['id'])
		pinIndex = self.PIN_comboBox.findText(componentData['pin'])
		self.PIN_comboBox.setCurrentIndex(pinIndex)

		switchState = componentData['state']
		if switchState == 'on':
			self.switchStateButton.setChecked(True)
		else:
			self.switchStateButton.setChecked(False)

		self.SWON_CMDS_TABLE.setRowCount(0)
		self.SWOFF_CMDS_TABLE.setRowCount(0)

		actions = componentData['actions']
		for action in actions:
			if action['state'] == 'on':
				if action['action_type'] == 'cmd':
					index = self.SWON_CMDS_TABLE.rowCount()
					self.SWON_CMDS_TABLE.insertRow(index)
					editWidget = pyXPdatarefCommandEditWidget.datarefCommandEditWidget(self.SWON_CMDS_TABLE)
					editWidget.lineEdit.setText(action['cmddref'])
					editWidget.lineEdit.editingFinished.connect(self.updateXMLdata)
					editWidget.lookupDREFCMDbutton.clicked.connect(self.editXPCommand)
					self.SWON_CMDS_TABLE.setCellWidget(index,0, editWidget)

					check_state = QtCore.Qt.Unchecked
					if action['continuous'] == 'True':
						check_state = QtCore.Qt.Checked

					item = QtWidgets.QTableWidgetItem()
					item.setCheckState(check_state)
					self.SWON_CMDS_TABLE.setItem(index,1, item)

				if action['action_type'] == 'dref':
					index = self.SWON_DREFS_TABLE.rowCount()
					self.SWON_DREFS_TABLE.insertRow(index)
					editWidget = pyXPdatarefCommandEditWidget.datarefCommandEditWidget(self.SWON_DREFS_TABLE)
					editWidget.lineEdit.setText(action['cmddref'])
					editWidget.lineEdit.editingFinished.connect(self.updateXMLdata)
					editWidget.lookupDREFCMDbutton.clicked.connect(self.editXPDataref)
					self.SWON_DREFS_TABLE.setCellWidget(index,0, editWidget)

					item = QtWidgets.QTableWidgetItem(action['index'])
					self.SWON_DREFS_TABLE.setItem(index,1, item)
					item = QtWidgets.QTableWidgetItem(action['setToValue'])
					self.SWON_DREFS_TABLE.setItem(index,2, item)

					check_state = QtCore.Qt.Unchecked
					if action['continuous'] == 'True':
						check_state = QtCore.Qt.Checked

					item = QtWidgets.QTableWidgetItem()
					item.setCheckState(check_state)
					self.SWON_DREFS_TABLE.setItem(index,3, item)

					drefList = XPrefData.getXPDatarefList(None, action['cmddref'])
					if len(drefList) > 0: # we have found the dataref
						item = QtWidgets.QTableWidgetItem(drefList[0][2]) # type
						self.SWON_DREFS_TABLE.setItem(index, 4, item)

						item = QtWidgets.QTableWidgetItem(drefList[0][4]) # unit
						self.SWON_DREFS_TABLE.setItem(index, 5, item)

			if action['state'] == 'off':
				if action['action_type'] == 'cmd':
					index = self.SWOFF_CMDS_TABLE.rowCount()
					self.SWOFF_CMDS_TABLE.insertRow(index)
					editWidget = pyXPdatarefCommandEditWidget.datarefCommandEditWidget(self.SWOFF_CMDS_TABLE)
					editWidget.lineEdit.setText(action['cmddref'])
					editWidget.lineEdit.editingFinished.connect(self.updateXMLdata)
					editWidget.lookupDREFCMDbutton.clicked.connect(self.editXPCommand)
					self.SWOFF_CMDS_TABLE.setCellWidget(index,0, editWidget)

					check_state = QtCore.Qt.Unchecked
					if action['continuous'] == 'True':
						check_state = QtCore.Qt.Checked

					item = QtWidgets.QTableWidgetItem()
					item.setCheckState(check_state)
					self.SWOFF_CMDS_TABLE.setItem(index,1, item)

				if action['action_type'] == 'dref':
					index = self.SWOFF_DREFS_TABLE.rowCount()
					self.SWOFF_DREFS_TABLE.insertRow(index)
					editWidget = pyXPdatarefCommandEditWidget.datarefCommandEditWidget(self.SWOFF_DREFS_TABLE)
					editWidget.lineEdit.setText(action['cmddref'])
					editWidget.lineEdit.editingFinished.connect(self.updateXMLdata)
					editWidget.lookupDREFCMDbutton.clicked.connect(self.editXPDataref)
					self.SWOFF_DREFS_TABLE.setCellWidget(index,0, editWidget)
					item = QtWidgets.QTableWidgetItem(action['index'])
					self.SWOFF_DREFS_TABLE.setItem(index,1, item)
					item = QtWidgets.QTableWidgetItem(action['setToValue'])
					self.SWOFF_DREFS_TABLE.setItem(index,2, item)

					check_state = QtCore.Qt.Unchecked
					if action['continuous'] == 'True':
						check_state = QtCore.Qt.Checked

					item = QtWidgets.QTableWidgetItem()
					item.setCheckState(check_state)
					self.SWOFF_DREFS_TABLE.setItem(index,3, item)

					drefList = XPrefData.getXPDatarefList(None, action['cmddref'])
					if len(drefList) > 0: # we have found the dataref
						item = QtWidgets.QTableWidgetItem(drefList[0][2]) # type
						self.SWOFF_DREFS_TABLE.setItem(index, 4, item)

						item = QtWidgets.QTableWidgetItem(drefList[0][4]) # unit
						self.SWOFF_DREFS_TABLE.setItem(index, 5, item)

		self.SWON_CMDS_TABLE.resizeColumnsToContents()
		self.SWON_CMDS_TABLE.resizeRowsToContents()
		self.SWON_CMDS_TABLE.setColumnWidth(0,self.DREFCMD_COLSIZE)

		self.SWOFF_CMDS_TABLE.resizeColumnsToContents()
		self.SWOFF_CMDS_TABLE.resizeRowsToContents()
		self.SWOFF_CMDS_TABLE.setColumnWidth(0,self.DREFCMD_COLSIZE)

		self.SWOFF_DREFS_TABLE.resizeRowsToContents()
		self.SWOFF_DREFS_TABLE.resizeColumnsToContents()
		self.SWOFF_DREFS_TABLE.setColumnWidth(0,self.DREFCMD_COLSIZE)

		self.SWON_DREFS_TABLE.resizeRowsToContents()
		self.SWON_DREFS_TABLE.resizeColumnsToContents()
		self.SWON_DREFS_TABLE.setColumnWidth(0,self.DREFCMD_COLSIZE)

		self.repopulating = False
		super().show()

	def hide(self):
		self.SWON_CMDS_TABLE.setRowCount(0)
		self.SWOFF_CMDS_TABLE.setRowCount(0)
		self.SWON_DREFS_TABLE.setRowCount(0)
		self.SWOFF_DREFS_TABLE.setRowCount(0)
		super().hide()

	def updateStateWidget(self, componentType, componentID, ardSerialNr = None, attribute = 'state'):
		logging.debug ('Update switch widget'+componentType)
		if componentType == 'switch' and componentID == self.componentID and attribute == 'state':
			componentData = self.ardXMLconfig.getComponentData(componentID, self.componentType)
			state = componentData['state']
			if state == 'on':
				self.switchStateButton.setChecked(True)
			else:
				self.switchStateButton.setChecked(False)

	def activateSave(self):
		if self.repopulating == False:
			self.actionSave.setEnabled(True)

	def testOnCommands(self):
		for i in range(0, self.SWON_CMDS_TABLE.rowCount()):
			item = self.SWON_CMDS_TABLE.item(i,0)
			actioncmddref = ''
			if item != None:
				actioncmddref = self.SWON_CMDS_TABLE.item(i,0).text()
				XPUDP.pyXPUDPServer.sendXPCmd(actioncmddref)

	def testOffCommands(self):
		for i in range(0, self.SWOFF_CMDS_TABLE.rowCount()):
			item = self.SWOFF_CMDS_TABLE.item(i,0)
			actioncmddref = ''
			if item != None:
				actioncmddref = self.SWOFF_CMDS_TABLE.item(i,0).text()
				XPUDP.pyXPUDPServer.sendXPCmd(actioncmddref)

	def testOnDatarefs(self):
		for i in range(0, self.SWON_DREFS_TABLE.rowCount()):
			item = self.SWON_DREFS_TABLE.item(i,0)
			actioncmddref = ''
			if item != None:
				actioncmddref = self.SWON_DREFS_TABLE.item(i,0).text()

				index = '0'
				setToValue = '0.0'

				item2 = self.SWON_DREFS_TABLE.item(i,1)
				if item2 != None:
					index = self.SWON_DREFS_TABLE.item(i,1).text()

				item2 = self.SWON_DREFS_TABLE.item(i,2)
				if item2 != None:
					setToValue = self.SWON_DREFS_TABLE.item(i,2).text()

				XPUDP.pyXPUDPServer.sendXPDref(actioncmddref, index, setToValue)

	def testOffDatarefs(self):
		for i in range(0, self.SWOFF_DREFS_TABLE.rowCount()):
			item = self.SWOFF_DREFS_TABLE.item(i,0)
			actioncmddref = ''
			if item != None:
				actioncmddref = self.SWOFF_DREFS_TABLE.item(i,0).text()

				index = '0'
				setToValue = '0.0'

				item2 = self.SWOFF_DREFS_TABLE.item(i,1)
				if item2 != None:
					index = self.SWOFF_DREFS_TABLE.item(i,1).text()

				item2 = self.SWOFF_DREFS_TABLE.item(i,2)
				if item2 != None:
					setToValue = self.SWOFF_DREFS_TABLE.item(i,2).text()

				XPUDP.pyXPUDPServer.sendXPDref(actioncmddref, index, setToValue)

	def updateXMLdata(self):
		if self.repopulating == False:
			actions = []
			index = 0
			for i in range(0, self.SWON_CMDS_TABLE.rowCount()):
				actioncmddref = self.SWON_CMDS_TABLE.cellWidget(i,0).lineEdit.text()

				action_continuous = 'False'
				if self.SWON_CMDS_TABLE.item(i,1) != None:
					if self.SWON_CMDS_TABLE.item(i,1).checkState() == QtCore.Qt.Checked:
						action_continuous = 'True'

				actions.append({'state':'on',
							  'action_type':'cmd',
							  'cmddref':actioncmddref,
							  'continuous':action_continuous})
				index = i

			for i in range(0, self.SWOFF_CMDS_TABLE.rowCount()):
				actioncmddref = self.SWOFF_CMDS_TABLE.cellWidget(i,0).lineEdit.text()

				action_continuous = 'False'
				if self.SWOFF_CMDS_TABLE.item(i,1) != None:
					if self.SWOFF_CMDS_TABLE.item(i,1).checkState() == QtCore.Qt.Checked:
						action_continuous = 'True'

				actions.append({'state':'off',
							  'action_type':'cmd',
							  'cmddref':actioncmddref,
							  'continuous':action_continuous})

			for i in range(0, self.SWON_DREFS_TABLE.rowCount()):
				actioncmddref = self.SWON_DREFS_TABLE.cellWidget(i,0).lineEdit.text()

				item = self.SWON_DREFS_TABLE.item(i,1)
				drefIndex = ''
				if item != None:
					drefIndex = self.SWON_DREFS_TABLE.item(i,1).text()

				item = self.SWON_DREFS_TABLE.item(i,2)
				setToValue = ''
				if item != None:
					setToValue = self.SWON_DREFS_TABLE.item(i,2).text()

				action_continuous = 'False'
				item = self.SWON_DREFS_TABLE.item(i,3)
				if item != None:
					if self.SWON_DREFS_TABLE.item(i,3).checkState() == QtCore.Qt.Checked:
						action_continuous = 'True'

				actions.append({'state':'on',
							  'action_type':'dref',
							  'cmddref':actioncmddref,
							  'index':drefIndex,
							  'setToValue':  setToValue,
							  'continuous':action_continuous })
				index = i

			for i in range(0, self.SWOFF_DREFS_TABLE.rowCount()):
				actioncmddref = self.SWOFF_DREFS_TABLE.cellWidget(i,0).lineEdit.text()

				item = self.SWOFF_DREFS_TABLE.item(i,1)
				drefIndex = ''
				if item != None:
					drefIndex = self.SWOFF_DREFS_TABLE.item(i,1).text()

				item = self.SWOFF_DREFS_TABLE.item(i,2)
				setToValue = ''
				if item != None:
					setToValue = self.SWOFF_DREFS_TABLE.item(i,2).text()

				action_continuous = 'False'
				item = self.SWOFF_DREFS_TABLE.item(i,3)
				if item != None:
					if self.SWOFF_DREFS_TABLE.item(i,3).checkState() == QtCore.Qt.Checked:
						action_continuous = 'True'

				actions.append({'state':'off',
							  'action_type':'dref',
							  'cmddref':actioncmddref,
							  'index':drefIndex,
							  'setToValue':  setToValue,
							  'continuous':action_continuous })
				index = i

			self.ardXMLconfig.updateComponentData(self.componentID, self.componentType,
																{'id':self.IDlineEdit.text(),
																'name':self.nameLineEdit.text(),
																'pin':self.PIN_comboBox.currentText()},
																actions)

			self.nameUpdated.emit(self.IDlineEdit.text(), self.nameLineEdit.text())
			self.actionSave.setEnabled(True)

	def updatePin(self):
		self.pinUpdated.emit(self.IDlineEdit.text())

	def addSwitchOnCommand(self):
		index = self.SWON_CMDS_TABLE.rowCount()
		self.SWON_CMDS_TABLE.insertRow(index)
		editWidget = pyXPdatarefCommandEditWidget.datarefCommandEditWidget(self.SWON_CMDS_TABLE)
		editWidget.lineEdit.setText('')
		editWidget.lineEdit.editingFinished.connect(self.updateXMLdata)
		editWidget.lookupDREFCMDbutton.clicked.connect(self.editXPCommand)
		self.SWON_CMDS_TABLE.setCellWidget(index,0, editWidget)

		check_state = QtCore.Qt.Unchecked
		item = QtWidgets.QTableWidgetItem()
		item.setCheckState(check_state)
		self.SWON_CMDS_TABLE.setItem(index,1, item)
		self.SWON_CMDS_TABLE.resizeColumnsToContents()
		self.SWON_CMDS_TABLE.resizeRowsToContents()
		self.SWON_CMDS_TABLE.setColumnWidth(0,self.DREFCMD_COLSIZE)

		self.updateXMLdata()
		self.actionSave.setEnabled(True)

	def rmSwitchOnCommand(self):
		row = self.SWON_CMDS_TABLE.currentRow()
		self.SWON_CMDS_TABLE.removeRow(row)
		self.updateXMLdata()
		self.actionSave.setEnabled(True)

	def addSwitchOnDataref(self):
		index = self.SWON_DREFS_TABLE.rowCount()
		self.SWON_DREFS_TABLE.insertRow(index)
		editWidget = pyXPdatarefCommandEditWidget.datarefCommandEditWidget(self.SWON_DREFS_TABLE)
		editWidget.lineEdit.setText('')
		editWidget.lineEdit.editingFinished.connect(self.updateXMLdata)
		editWidget.lookupDREFCMDbutton.clicked.connect(self.editXPDataref)
		self.SWON_DREFS_TABLE.setCellWidget(index,0, editWidget)

		item = QtWidgets.QTableWidgetItem('0')
		self.SWON_DREFS_TABLE.setItem(index,1, item)
		item = QtWidgets.QTableWidgetItem('0.0')
		self.SWON_DREFS_TABLE.setItem(index,2, item)

		check_state = QtCore.Qt.Unchecked
		item = QtWidgets.QTableWidgetItem()
		item.setCheckState(check_state)
		self.SWON_DREFS_TABLE.setItem(index,3, item)
		self.SWON_DREFS_TABLE.resizeColumnsToContents()
		self.SWON_DREFS_TABLE.resizeRowsToContents()
		self.SWON_DREFS_TABLE.setColumnWidth(0,self.DREFCMD_COLSIZE)

		self.updateXMLdata()
		self.actionSave.setEnabled(True)

	def rmSwitchOnDataref(self):
		row = self.SWON_DREFS_TABLE.currentRow()
		self.SWON_DREFS_TABLE.removeRow(row)
		self.updateXMLdata()
		self.actionSave.setEnabled(True)

	def addSwitchOffCommand(self):
		index = self.SWOFF_CMDS_TABLE.rowCount()
		self.SWOFF_CMDS_TABLE.insertRow(index)
		editWidget = pyXPdatarefCommandEditWidget.datarefCommandEditWidget(self.SWOFF_CMDS_TABLE)
		editWidget.lineEdit.setText('')
		editWidget.lineEdit.editingFinished.connect(self.updateXMLdata)
		editWidget.lookupDREFCMDbutton.clicked.connect(self.editXPCommand)
		self.SWOFF_CMDS_TABLE.setCellWidget(index,0, editWidget)

		check_state = QtCore.Qt.Unchecked
		item = QtWidgets.QTableWidgetItem()
		item.setCheckState(check_state)
		self.SWOFF_CMDS_TABLE.setItem(index,1, item)

		self.SWOFF_CMDS_TABLE.resizeColumnsToContents()
		self.SWOFF_CMDS_TABLE.resizeRowsToContents()
		self.SWOFF_CMDS_TABLE.setColumnWidth(0,self.DREFCMD_COLSIZE)

		self.updateXMLdata()
		self.actionSave.setEnabled(True)

	def rmSwitchOffCommand(self):
		row = self.SWOFF_CMDS_TABLE.currentRow()
		self.SWOFF_CMDS_TABLE.removeRow(row)
		self.updateXMLdata()
		self.actionSave.setEnabled(True)

	def addSwitchOffDataref(self):
		index = self.SWOFF_DREFS_TABLE.rowCount()
		self.SWOFF_DREFS_TABLE.insertRow(index)
		editWidget = pyXPdatarefCommandEditWidget.datarefCommandEditWidget(self.SWOFF_DREFS_TABLE)
		editWidget.lineEdit.setText('')
		editWidget.lineEdit.editingFinished.connect(self.updateXMLdata)
		editWidget.lookupDREFCMDbutton.clicked.connect(self.editXPDataref)
		self.SWOFF_DREFS_TABLE.setCellWidget(index,0, editWidget)

		item = QtWidgets.QTableWidgetItem('0')
		self.SWOFF_DREFS_TABLE.setItem(index,1, item)
		item = QtWidgets.QTableWidgetItem('0.0')
		self.SWOFF_DREFS_TABLE.setItem(index,2, item)

		check_state = QtCore.Qt.Unchecked
		item = QtWidgets.QTableWidgetItem()
		item.setCheckState(check_state)
		self.SWOFF_DREFS_TABLE.setItem(index,3, item)

		self.SWOFF_DREFS_TABLE.resizeColumnsToContents()
		self.SWOFF_DREFS_TABLE.resizeRowsToContents()
		self.SWOFF_DREFS_TABLE.setColumnWidth(0,self.DREFCMD_COLSIZE)

		self.updateXMLdata()
		self.actionSave.setEnabled(True)

	def rmSwitchOffDataref(self):
		row = self.SWOFF_DREFS_TABLE.currentRow()
		self.SWOFF_DREFS_TABLE.removeRow(row)
		self.updateXMLdata()
		self.actionSave.setEnabled(True)

	##
	#
	def editXPCommand(self):
		callingQwidgetButton = self.sender()
		parentitem = callingQwidgetButton.parent()
		text = parentitem.lineEdit.text()

		self.pickXPCommandDialog.commandLineEdit.setText(text)

		returnCode = self.pickXPCommandDialog.exec()

		if returnCode == 1: # command selected
			parentitem.lineEdit.setText(self.pickXPCommandDialog.commandLineEdit.text())
			self.updateXMLdata()
			self.actionSave.setEnabled(True)

	##
	#
	def editXPDataref(self):
		callingQwidgetButton = self.sender()

		parentitem = callingQwidgetButton.parent()
		parenttable = parentitem.parentTable
		logging.debug("parent table: "+str(parenttable))
		index = parenttable.indexAt(parentitem.pos())
		row = index.row()
		logging.debug("edit XP dataref row: "+str(row))
		text = parentitem.lineEdit.text()

		self.pickXPDatarefDialog.datarefLineEdit.setText(text)

		returnCode = self.pickXPDatarefDialog.exec()

		if returnCode == 1: # command selected
			dataref = self.pickXPDatarefDialog.datarefLineEdit.text()
			parentitem.lineEdit.setText(dataref)

			# default index to 0
			item = QtWidgets.QTableWidgetItem('0')
			parenttable.setItem(row, 1, item)

			# default Set to value to 0.0
			item = QtWidgets.QTableWidgetItem('0.0')
			parenttable.setItem(row, 2, item)


			# retrieve dref data
			drefList = XPrefData.getXPDatarefList(None, dataref)
			if len(drefList) > 0: # we have found the dataref
				item = QtWidgets.QTableWidgetItem(drefList[0][2]) # type
				parenttable.setItem(row, 4, item)

				item = QtWidgets.QTableWidgetItem(drefList[0][4]) # unit
				parenttable.setItem(row, 5, item)

			parenttable.resizeColumnsToContents()
			parenttable.setColumnWidth(0,self.DREFCMD_COLSIZE)

			self.updateXMLdata()
			self.actionSave.setEnabled(True)
