import logging
from PyQt5 import QtCore, QtGui, QtWidgets
import gui.pyXPalertDialog as pyXPalertDialog

class pyXPQTableLogger(logging.Handler):
	def __init__(self):
		super(pyXPQTableLogger, self).__init__()
		self.widget = None
		print(self)
		formatter = logging.Formatter('%(asctime)s %(levelname)-8s %(name)-15s %(module)-30s %(funcName)-30s  %(message)s')
		self.setFormatter(formatter)

	def setupQtWidget(self, parent):
		self.widget = QtWidgets.QTableWidget(parent)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		self.widget.setSizePolicy(sizePolicy)
		self.widget.setColumnCount(4)
		self.widget.setRowCount(0)
		font = QtGui.QFontDatabase.systemFont(QtGui.QFontDatabase.FixedFont)
		font.setPointSize(9)
		self.widget.setFont(font)
		self.widget.verticalHeader().setDefaultSectionSize(20)
		self.widget.horizontalHeader().hide()
		self.widget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
		self.widget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows);
		self.widget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection);

		self.alertDialog = pyXPalertDialog.alertDialog()

	def emit(self, record):
		#print(self)
		msg = self.format(record)
		#print('logging message: '+msg)
		if self.widget is not None:
			self.widget.insertRow(0)
			item = QtWidgets.QTableWidgetItem(str(record.asctime))
			self.widget.setItem(0,0,item )
			self.widget.resizeColumnToContents(0)

			item = QtWidgets.QTableWidgetItem(str(record.levelname))
			self.widget.setItem(0,1,item )
			self.widget.resizeColumnToContents(1)

			item = QtWidgets.QTableWidgetItem(str(record.module))
			self.widget.setItem(0,2,item )
			self.widget.resizeColumnToContents(2)

			item = QtWidgets.QTableWidgetItem(str(record.msg))
			self.widget.setItem(0,3,item )
			self.widget.resizeColumnToContents(3)

			color = None
			if record.levelname == 'WARNING':
				color = QtGui.QColor(255,230,150)
			if record.levelname == 'ERROR':
				color = QtGui.QColor(255,125,125)
				self.alertDialog.setMessage(str(record.msg))
				self.alertDialog.exec()

			if color is not None:
				for i in range (0,4):
					self.widget.item(0,i).setBackground(color)

			#self.widget.resizeRowToContents(0)
			#self.widget.setRowHeight(0,12)
			#self.widget.resizeRowsToContents()


	def write(self, m):
		pass
