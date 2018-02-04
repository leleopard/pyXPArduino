# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pickarduinodialog.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AddArduinoDialog(object):
    def setupUi(self, AddArduinoDialog):
        AddArduinoDialog.setObjectName("AddArduinoDialog")
        AddArduinoDialog.resize(691, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(AddArduinoDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.arduinoTableWidget = QtWidgets.QTableWidget(AddArduinoDialog)
        self.arduinoTableWidget.setObjectName("arduinoTableWidget")
        self.arduinoTableWidget.setColumnCount(6)
        self.arduinoTableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.arduinoTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.arduinoTableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.arduinoTableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.arduinoTableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.arduinoTableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.arduinoTableWidget.setHorizontalHeaderItem(5, item)
        self.verticalLayout.addWidget(self.arduinoTableWidget)
        self.buttonBox = QtWidgets.QDialogButtonBox(AddArduinoDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(AddArduinoDialog)
        self.buttonBox.accepted.connect(AddArduinoDialog.accept)
        self.buttonBox.rejected.connect(AddArduinoDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(AddArduinoDialog)

    def retranslateUi(self, AddArduinoDialog):
        _translate = QtCore.QCoreApplication.translate
        AddArduinoDialog.setWindowTitle(_translate("AddArduinoDialog", "Add Arduino"))
        item = self.arduinoTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("AddArduinoDialog", "Select"))
        item = self.arduinoTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("AddArduinoDialog", "Port"))
        item = self.arduinoTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("AddArduinoDialog", "Name"))
        item = self.arduinoTableWidget.horizontalHeaderItem(3)
        item.setText(_translate("AddArduinoDialog", "Description"))
        item = self.arduinoTableWidget.horizontalHeaderItem(4)
        item.setText(_translate("AddArduinoDialog", "Serial Number"))
        item = self.arduinoTableWidget.horizontalHeaderItem(5)
        item.setText(_translate("AddArduinoDialog", "Manufacturer"))

