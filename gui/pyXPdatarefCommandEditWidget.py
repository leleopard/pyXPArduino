from PyQt5 import QtCore, QtGui, QtWidgets


class datarefCommandEditWidget(QtWidgets.QWidget):
	def __init__(self, parent = None):
		super(datarefCommandEditWidget, self).__init__(parent)
		self.lineEdit = QtWidgets.QLineEdit(parent)
		self.lineEdit.setContentsMargins(0, 0, 0, 0)
		self.lineEdit.setFrame(False)

		self.lookupDREFCMDbutton = QtWidgets.QToolButton(parent)
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(":/newPrefix/find.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.lookupDREFCMDbutton.setIcon(icon)
		self.lookupDREFCMDbutton.setAutoRaise(True)

		hbox = QtWidgets.QHBoxLayout(self)
		# remove the inner margin
		hbox.setContentsMargins(0, 0, 0, 0)
		hbox.setSpacing(0)
		hbox.addWidget(self.lineEdit)
		hbox.addWidget(self.lookupDREFCMDbutton)
