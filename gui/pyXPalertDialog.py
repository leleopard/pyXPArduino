from PyQt5 import QtCore, QtGui, QtWidgets
import gui.alert_dialog as alert_dialog

class alertDialog(QtWidgets.QDialog, alert_dialog.Ui_Dialog):
	def __init__(self):
		super(self.__class__, self).__init__()
		self.setupUi(self)  # This is defined in design.py file automatically
							# It sets up layout and widgets that are defined

	def setMessage(self, msg, msgType = 'ERROR'):
		self.msg_label.setText(msg)
		if msgType == 'ERROR':
			self.icon_label.setPixmap(QtGui.QPixmap(":/newPrefix/error_icon.png"))
			self.setWindowTitle('Error')
		else:
			self.icon_label.setPixmap(QtGui.QPixmap(":/newPrefix/attention.png"))
			self.setWindowTitle('Warning')
