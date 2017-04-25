from PyQt5 import QtCore, QtGui, QtWidgets
import gui.pickXPCommandDialog as pickXPCommandDialog



class pyXPpickXPCommandDialog(QtWidgets.QDialog, pickXPCommandDialog.Ui_Dialog):
	def __init__(self):
		super(self.__class__, self).__init__()
		self.setupUi(self)  # This is defined in design.py file automatically
							# It sets up layout and widgets that are defined