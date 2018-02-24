from PyQt5 import QtCore, QtGui, QtWidgets
import gui.unsavedchanges_confirmationdialog as unsavedchanges_confirmationdialog

import lib.arduinoXMLconfig

class unsavedChangesConfirmationDialog(QtWidgets.QDialog, unsavedchanges_confirmationdialog.Ui_confirmationDialog):
	def __init__(self):
		super(self.__class__, self).__init__()
		self.setupUi(self)  # This is defined in design.py file automatically
							# It sets up layout and widgets that are defined
