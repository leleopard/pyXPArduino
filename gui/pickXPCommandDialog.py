# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/pickXPCommandDialog.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(682, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.categoryListWidget = QtWidgets.QListWidget(Dialog)
        self.categoryListWidget.setMaximumSize(QtCore.QSize(250, 16777215))
        self.categoryListWidget.setObjectName("categoryListWidget")
        self.horizontalLayout.addWidget(self.categoryListWidget)
        self.commandsTableWidget = QtWidgets.QTableWidget(Dialog)
        self.commandsTableWidget.setObjectName("commandsTableWidget")
        self.commandsTableWidget.setColumnCount(2)
        self.commandsTableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.commandsTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.commandsTableWidget.setHorizontalHeaderItem(1, item)
        self.horizontalLayout.addWidget(self.commandsTableWidget)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Select XPlane Command"))
        item = self.commandsTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Dataref"))
        item = self.commandsTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Description"))

