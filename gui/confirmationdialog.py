# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'confirmationdialog.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_deleteConfirmationDialog(object):
    def setupUi(self, deleteConfirmationDialog):
        deleteConfirmationDialog.setObjectName("deleteConfirmationDialog")
        deleteConfirmationDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        deleteConfirmationDialog.resize(333, 98)
        deleteConfirmationDialog.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(deleteConfirmationDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(deleteConfirmationDialog)
        self.label.setMaximumSize(QtCore.QSize(32, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/newPrefix/attention.png"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(deleteConfirmationDialog)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(deleteConfirmationDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Yes)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(deleteConfirmationDialog)
        self.buttonBox.accepted.connect(deleteConfirmationDialog.accept)
        self.buttonBox.rejected.connect(deleteConfirmationDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(deleteConfirmationDialog)

    def retranslateUi(self, deleteConfirmationDialog):
        _translate = QtCore.QCoreApplication.translate
        deleteConfirmationDialog.setWindowTitle(_translate("deleteConfirmationDialog", "Delete Item"))
        self.label_2.setText(_translate("deleteConfirmationDialog", "Are you sure you want to delete the item?"))

import resources_rc
