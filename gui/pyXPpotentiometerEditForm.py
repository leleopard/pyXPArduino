import logging

from PyQt5 import QtCore, QtGui, QtWidgets
import gui.potentiometerEditForm as potentiometerEditForm
import gui.pyXPdatarefCommandEditWidget as pyXPdatarefCommandEditWidget
import lib.XPrefData as XPrefData
import gui.pyXPpickXPCommandDialog as pyXPpickXPCommandDialog
import gui.pyXPpickXPDatarefDialog as pyXPpickXPDatarefDialog

import lib.arduinoXMLconfig

import pyxpudpserver as XPUDP
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

		#self.CMDS_TABLE.setItemDelegateForColumn(0, MyDelegate(self))


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
				editWidget = pyXPdatarefCommandEditWidget.datarefCommandEditWidget(self)
				editWidget.lineEdit.setText(action['cmddref'])
				editWidget.lineEdit.editingFinished.connect(self.updateXMLdata)
				editWidget.lookupDREFCMDbutton.clicked.connect(self.editXPCommand)
				self.CMDS_TABLE.setCellWidget(index,0, editWidget)

				item = QtWidgets.QTableWidgetItem(action['state'])
				item.setToolTip('<html><head/><body><p>Enter intervals where the command should be sent. </p><p>For example to send the command if the pot value is between 0 and 200 or between 600 and 800, enter: </p><p><span style=" color:#0000ff;">[0,200], [600,800]</span></p></body></html>')
				self.CMDS_TABLE.setItem(index,1, item)

			if action['action_type'] == 'dref':
				index = self.DREFS_TABLE.rowCount()
				self.DREFS_TABLE.insertRow(index)
				editWidget = pyXPdatarefCommandEditWidget.datarefCommandEditWidget(self)
				editWidget.lineEdit.setText(action['cmddref'])
				editWidget.lineEdit.editingFinished.connect(self.updateXMLdata)
				editWidget.lookupDREFCMDbutton.clicked.connect(self.editXPDataref)
				self.DREFS_TABLE.setCellWidget(index,0, editWidget)

				item = QtWidgets.QTableWidgetItem(action['index'])
				self.DREFS_TABLE.setItem(index,1, item)
				item = QtWidgets.QTableWidgetItem(action['setToValue'])
				item.setToolTip('<html><head/><body><p>Enter series of points [pot input value, output dataref value]. The output value of the dataref in between 2 points will be linearly interpolated. </p><p>Note that the potentiometer value varies between 0 and 1023 (this is the raw output reading from the ADC of the arduino)</p><p>For example to set the dataref to vary linearly between 10 and 300 when the potentiometer value varies between 0 and 1023, enter: </p><p><span style=" color:#0000ff;">[0,10], [1023,300]</span></p></body></html>')
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
				item = self.CMDS_TABLE.cellWidget(i,0)
				actioncmddref = ''
				if item != None:
					actioncmddref = self.CMDS_TABLE.cellWidget(i,0).lineEdit.text()
					#logging.warning("actioncmddref: "+str(actioncmddref))
				item = self.CMDS_TABLE.item(i,1)
				state = ''
				if item != None:
					state = self.CMDS_TABLE.item(i,1).text()

				actions.append({'state':state,
							  'action_type':'cmd',
							  'cmddref':actioncmddref})
				index = i
				#logging.warning("actions: "+str(actions))

			for i in range(0, self.DREFS_TABLE.rowCount()):
				item = self.DREFS_TABLE.item(i,0)
				actioncmddref = ''
				actioncmddref = self.DREFS_TABLE.cellWidget(i,0).lineEdit.text()
				#logging.warning("Update XML data; DREF table actioncmddref = "+actioncmddref)

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
		logging.debug("ADD POT COMMAND")
		index = self.CMDS_TABLE.rowCount()
		self.CMDS_TABLE.insertRow(index)
		editWidget = pyXPdatarefCommandEditWidget.datarefCommandEditWidget(self)
		editWidget.lineEdit.setText('')
		editWidget.lineEdit.editingFinished.connect(self.updateXMLdata)
		editWidget.lookupDREFCMDbutton.clicked.connect(self.editXPCommand)
		self.CMDS_TABLE.setCellWidget(index,0, editWidget)
		item = QtWidgets.QTableWidgetItem('')
		item.setToolTip('<html><head/><body><p>Enter intervals where the command should be sent. </p><p>For example to send the command if the pot value is between 0 and 200 or between 600 and 800, enter: </p><p><span style=" color:#0000ff;">[0,200], [600,800]</span></p></body></html>')
		self.CMDS_TABLE.setItem(index,1, item)
		self.CMDS_TABLE.resizeRowsToContents()
		self.updateXMLdata()
		self.actionSave.setEnabled(True)

	def rmCommand(self):
		row = self.CMDS_TABLE.currentRow()
		self.CMDS_TABLE.removeRow(row)
		self.updateXMLdata()
		self.actionSave.setEnabled(True)

	def addDataref(self):
		index = self.DREFS_TABLE.rowCount()
		self.DREFS_TABLE.insertRow(index)
		editWidget = pyXPdatarefCommandEditWidget.datarefCommandEditWidget(self)
		editWidget.lineEdit.setText('')
		editWidget.lineEdit.editingFinished.connect(self.updateXMLdata)
		editWidget.lookupDREFCMDbutton.clicked.connect(self.editXPDataref)
		self.DREFS_TABLE.setCellWidget(index,0, editWidget)

		item = QtWidgets.QTableWidgetItem('0')
		self.DREFS_TABLE.setItem(index,1, item)
		item = QtWidgets.QTableWidgetItem('0.0')
		item.setToolTip('<html><head/><body><p>Enter series of points [pot input value, output dataref value]. The output value of the dataref in between 2 points will be linearly interpolated. </p><p>Note that the potentiometer value varies between 0 and 1023 (this is the raw output reading from the ADC of the arduino)</p><p>For example to set the dataref to vary linearly between 10 and 300 when the potentiometer value varies between 0 and 1023, enter: </p><p><span style=" color:#0000ff;">[0,10], [1023,300]</span></p></body></html>')
		self.DREFS_TABLE.setItem(index,2, item)

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

	## slot intended to be called from a QTableWidget. The row and cell passed in argument will be assumed to be the XPlane command to edit
	#
	def editXPDataref(self):
		callingQwidgetButton = self.sender()

		parentitem = callingQwidgetButton.parent()
		index = self.DREFS_TABLE.indexAt(parentitem.pos())
		row = index.row()
		logging.warning("edit XP dataref row: "+str(row))
		text = parentitem.lineEdit.text()

		self.pickXPDatarefDialog.datarefLineEdit.setText(text)

		returnCode = self.pickXPDatarefDialog.exec()

		if returnCode == 1: # command selected
			parentitem.lineEdit.setText(self.pickXPDatarefDialog.datarefLineEdit.text())

			# default index to 0
			item = QtWidgets.QTableWidgetItem('0')
			self.DREFS_TABLE.setItem(row, 1, item)

			# default Set to value to 0.0
			item = QtWidgets.QTableWidgetItem('0.0')
			self.DREFS_TABLE.setItem(row, 2, item)

			# retrieve dref data
			drefList = XPrefData.getXPDatarefList(None, self.pickXPDatarefDialog.datarefLineEdit.text())
			if len(drefList) > 0: # we have found the dataref
				item = QtWidgets.QTableWidgetItem(drefList[0][2]) # type
				self.DREFS_TABLE.setItem(row, 3, item)

				item = QtWidgets.QTableWidgetItem(drefList[0][4]) # unit
				self.DREFS_TABLE.setItem(row, 4, item)

			self.updateXMLdata()
			self.actionSave.setEnabled(True)
