import logging

from PyQt5 import QtCore, QtGui, QtWidgets
import gui.servoEditForm as servoEditForm

import lib.XPrefData as XPrefData
import gui.pyXPpickXPCommandDialog as pyXPpickXPCommandDialog
import gui.pyXPpickXPDatarefDialog as pyXPpickXPDatarefDialog

import lib.arduinoXMLconfig

import pyxpudpserver as XPUDP
import time

class pyXPservoEditForm(QtWidgets.QWidget, servoEditForm.Ui_servoEditForm):
	nameUpdated = QtCore.pyqtSignal(str,str)
	pinUpdated = QtCore.pyqtSignal(str)

	def __init__(self,widget, ardXMLconfig, actionSave):
		super(self.__class__, self).__init__(widget)
		self.repopulating = False
		self.lastTimeCompStateWidgetUpdated = time.time()
		self.setupUi(self)  # This is defined in design.py file automatically
							# It sets up layout and widgets that are defined
		self.actionSave = actionSave
		self.componentID = ''
		self.componentType = "servo"
		self.ardXMLconfig = ardXMLconfig
		self.ardXMLconfig.registerComponentAttributeChangedCallback(self.updateStateWidget)
		self.pickXPCommandDialog = pyXPpickXPCommandDialog.pyXPpickXPCommandDialog()
		self.pickXPDatarefDialog = pyXPpickXPDatarefDialog.pyXPpickXPDatarefDialog()

		self.PIN_comboBox.addItems(lib.arduinoXMLconfig.SERVO_PINS)

		self.timer = QtCore.QTimer()
		self.timer.timeout.connect(self.updateStateWidget)
		self.timer.start(50)


	def show(self, componentID, ardSerialNr = None):
		self.repopulating = True
		self.componentID = componentID
		componentData = self.ardXMLconfig.getComponentData(componentID, self.componentType)

		self.nameLineEdit.setText(componentData['name'])
		self.IDlineEdit.setText(componentData['id'])
		pinIndex = self.PIN_comboBox.findText(componentData['pin'])
		self.PIN_comboBox.setCurrentIndex(pinIndex)

		state = componentData['state']

		self.pwmOutputLineEdit.setText('')
		self.drefLineEdit.setText('')
		self.drefIndexLineEdit.setText('')
		self.drefInfoLabel.setText('')

		actions = componentData['actions']
		if len(actions) >= 1:
			dataref = actions[0]['cmddref']
			self.pwmOutputLineEdit.setText(actions[0]['setToValue'])
			self.drefLineEdit.setText(dataref)
			self.drefIndexLineEdit.setText(actions[0]['index'])

			drefdata = XPrefData.getXPDataref(dataref)
			drefdescr = drefdata[2] + ", " + drefdata[4]+ ", " + drefdata[5]
			self.drefInfoLabel.setText(drefdescr)

		self.repopulating = False
		super().show()

	def hide(self):
		super().hide()

	def updateStateWidget(self, componentType = None, componentID = None, ardSerialNr = None, attribute = 'state'):
		dataref = self.drefLineEdit.text()
		index = self.drefIndexLineEdit.text()
		drefValue = XPUDP.pyXPUDPServer.getData(dataref + "[" + index + "]")

		self.drefValueLabel.setText("{0:.4f}".format(drefValue))

	def activateSave(self):
		if self.repopulating == False:
			self.actionSave.setEnabled(True)


	def updateXMLdata(self):
		if self.repopulating == False:
			actions = []
			actioncmddref = self.drefLineEdit.text()
			drefIndex = self.drefIndexLineEdit.text()
			setToValue = self.pwmOutputLineEdit.text()

			actions.append({'state':'on',
							  'action_type':'dref',
							  'cmddref':actioncmddref,
							  'index':drefIndex,
							  'setToValue':  setToValue })

			self.ardXMLconfig.updateComponentData(self.componentID, self.componentType,
																{'id':self.IDlineEdit.text(),
																'name':self.nameLineEdit.text(),
																'pin':self.PIN_comboBox.currentText()},
																actions)

			self.nameUpdated.emit(self.IDlineEdit.text(), self.nameLineEdit.text())
			self.actionSave.setEnabled(True)

	def updatePin(self):
		logging.debug("servo pin updated")
		self.pinUpdated.emit(self.IDlineEdit.text())



	## slot intended to be called from a QTableWidget. The row and cell passed in argument will be assumed to be the XPlane command to edit
	#
	def editXPDataref(self):
		logging.debug("Edit XP dref")
		text = self.drefLineEdit.text()

		self.pickXPDatarefDialog.datarefLineEdit.setText(text)

		returnCode = self.pickXPDatarefDialog.exec()

		if returnCode == 1: # command selected
			dataref = self.pickXPDatarefDialog.datarefLineEdit.text()
			self.drefLineEdit.setText(dataref)
			drefdata = XPrefData.getXPDataref(dataref)
			drefdescr = drefdata[2] + ", " + drefdata[4]+ ", " + drefdata[5]
			self.drefInfoLabel.setText(drefdescr)
			self.actionSave.setEnabled(True)
