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
        Dialog.resize(809, 550)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label.setObjectName("label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label)
        self.filterCommandsLineEdit = QtWidgets.QLineEdit(Dialog)
        self.filterCommandsLineEdit.setMinimumSize(QtCore.QSize(200, 0))
        self.filterCommandsLineEdit.setMaximumSize(QtCore.QSize(300, 300))
        self.filterCommandsLineEdit.setObjectName("filterCommandsLineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.filterCommandsLineEdit)
        self.selectCategoryComboBox = QtWidgets.QComboBox(Dialog)
        self.selectCategoryComboBox.setMinimumSize(QtCore.QSize(250, 0))
        self.selectCategoryComboBox.setMaximumSize(QtCore.QSize(300, 30))
        self.selectCategoryComboBox.setObjectName("selectCategoryComboBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.selectCategoryComboBox)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.commandsTableWidget = QtWidgets.QTableWidget(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.commandsTableWidget.sizePolicy().hasHeightForWidth())
        self.commandsTableWidget.setSizePolicy(sizePolicy)
        self.commandsTableWidget.setMinimumSize(QtCore.QSize(0, 200))
        self.commandsTableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.commandsTableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.commandsTableWidget.setObjectName("commandsTableWidget")
        self.commandsTableWidget.setColumnCount(3)
        self.commandsTableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.commandsTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.commandsTableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.commandsTableWidget.setHorizontalHeaderItem(2, item)
        self.commandsTableWidget.verticalHeader().setDefaultSectionSize(25)
        self.verticalLayout_2.addWidget(self.commandsTableWidget)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        self.selectCategoryComboBox.currentIndexChanged['QString'].connect(Dialog.refreshCommandList)
        self.filterCommandsLineEdit.textChanged['QString'].connect(Dialog.refreshCommandList)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Select XPlane Command"))
        self.label.setText(_translate("Dialog", "Search:"))
        self.label_2.setText(_translate("Dialog", "Filter Category: "))
        item = self.commandsTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Category"))
        item = self.commandsTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Command"))
        item = self.commandsTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Description"))

