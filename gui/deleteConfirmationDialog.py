from PyQt5 import QtCore, QtGui, QtWidgets
import gui.confirmationdialog as confirmationdialog

import lib.arduinoXMLconfig

class DeleteConfirmationDialog(QtWidgets.QDialog, confirmationdialog.Ui_deleteConfirmationDialog):
	def __init__(self):
		super(self.__class__, self).__init__()
		self.setupUi(self)  # This is defined in design.py file automatically
							# It sets up layout and widgets that are defined
		
		
		