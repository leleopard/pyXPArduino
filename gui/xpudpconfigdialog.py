# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'xpudpconfigdialog.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(650, 464)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.XPIP_Address_LineEdit = QtWidgets.QLineEdit(Dialog)
        self.XPIP_Address_LineEdit.setMaximumSize(QtCore.QSize(150, 16777215))
        self.XPIP_Address_LineEdit.setObjectName("XPIP_Address_LineEdit")
        self.gridLayout.addWidget(self.XPIP_Address_LineEdit, 1, 2, 1, 1)
        self.IP_Address_LineEdit = QtWidgets.QLineEdit(Dialog)
        self.IP_Address_LineEdit.setMaximumSize(QtCore.QSize(150, 16777215))
        self.IP_Address_LineEdit.setObjectName("IP_Address_LineEdit")
        self.gridLayout.addWidget(self.IP_Address_LineEdit, 0, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.XP_RedirectTraffic_checkBox = QtWidgets.QCheckBox(Dialog)
        self.XP_RedirectTraffic_checkBox.setText("")
        self.XP_RedirectTraffic_checkBox.setObjectName("XP_RedirectTraffic_checkBox")
        self.gridLayout.addWidget(self.XP_RedirectTraffic_checkBox, 4, 1, 1, 1)
        self.XP_ComputerName_LineEdit = QtWidgets.QLineEdit(Dialog)
        self.XP_ComputerName_LineEdit.setObjectName("XP_ComputerName_LineEdit")
        self.gridLayout.addWidget(self.XP_ComputerName_LineEdit, 2, 1, 1, 3)
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 3, 1, 1)
        self.IP_Port_LineEdit = QtWidgets.QLineEdit(Dialog)
        self.IP_Port_LineEdit.setMaximumSize(QtCore.QSize(75, 16777215))
        self.IP_Port_LineEdit.setObjectName("IP_Port_LineEdit")
        self.gridLayout.addWidget(self.IP_Port_LineEdit, 0, 4, 1, 1)
        self.XPIP_Port_LineEdit = QtWidgets.QLineEdit(Dialog)
        self.XPIP_Port_LineEdit.setMaximumSize(QtCore.QSize(75, 16777215))
        self.XPIP_Port_LineEdit.setObjectName("XPIP_Port_LineEdit")
        self.gridLayout.addWidget(self.XPIP_Port_LineEdit, 1, 4, 1, 1)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 6, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 1, 3, 1, 1)
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 4, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem1, 3, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 5, 1, 1)
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 5, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 5, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 5, 3, 1, 1)
        self.RedIP_Address_LineEdit = QtWidgets.QLineEdit(Dialog)
        self.RedIP_Address_LineEdit.setMaximumSize(QtCore.QSize(150, 16777215))
        self.RedIP_Address_LineEdit.setObjectName("RedIP_Address_LineEdit")
        self.gridLayout.addWidget(self.RedIP_Address_LineEdit, 5, 2, 1, 1)
        self.RedIP_Port_LineEdit = QtWidgets.QLineEdit(Dialog)
        self.RedIP_Port_LineEdit.setMaximumSize(QtCore.QSize(75, 16777215))
        self.RedIP_Port_LineEdit.setObjectName("RedIP_Port_LineEdit")
        self.gridLayout.addWidget(self.RedIP_Port_LineEdit, 5, 4, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setEnabled(True)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout.addWidget(self.label_9)
        self.ADD_FWDIP_BTN = QtWidgets.QToolButton(Dialog)
        self.ADD_FWDIP_BTN.setEnabled(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/plusIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ADD_FWDIP_BTN.setIcon(icon)
        self.ADD_FWDIP_BTN.setObjectName("ADD_FWDIP_BTN")
        self.horizontalLayout.addWidget(self.ADD_FWDIP_BTN)
        self.RM_FWDIP_BTN = QtWidgets.QToolButton(Dialog)
        self.RM_FWDIP_BTN.setEnabled(True)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/minusIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.RM_FWDIP_BTN.setIcon(icon1)
        self.RM_FWDIP_BTN.setObjectName("RM_FWDIP_BTN")
        self.horizontalLayout.addWidget(self.RM_FWDIP_BTN)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.FWDIPs_TABLE = QtWidgets.QTableWidget(Dialog)
        self.FWDIPs_TABLE.setEnabled(True)
        self.FWDIPs_TABLE.setObjectName("FWDIPs_TABLE")
        self.FWDIPs_TABLE.setColumnCount(2)
        self.FWDIPs_TABLE.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.FWDIPs_TABLE.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.FWDIPs_TABLE.setHorizontalHeaderItem(1, item)
        self.verticalLayout.addWidget(self.FWDIPs_TABLE)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.UDPStatusLabel = QtWidgets.QLabel(Dialog)
        self.UDPStatusLabel.setObjectName("UDPStatusLabel")
        self.verticalLayout.addWidget(self.UDPStatusLabel)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Apply|QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        self.buttonBox.clicked['QAbstractButton*'].connect(Dialog.buttonBoxClicked)
        self.XP_RedirectTraffic_checkBox.stateChanged['int'].connect(Dialog.redirectCheckboxStateChanged)
        self.ADD_FWDIP_BTN.clicked.connect(Dialog.addFWDIP)
        self.RM_FWDIP_BTN.clicked.connect(Dialog.rmFWDIP)
        self.FWDIPs_TABLE.itemChanged['QTableWidgetItem*'].connect(Dialog.saveToXMLfile)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Edit XPlane UDP settings"))
        self.label.setText(_translate("Dialog", "Our IP Address XPlane is sending to "))
        self.XPIP_Address_LineEdit.setInputMask(_translate("Dialog", "000.000.000.000;_"))
        self.IP_Address_LineEdit.setInputMask(_translate("Dialog", "900.900.900.900"))
        self.label_3.setText(_translate("Dialog", "XPlane computer Network Name"))
        self.label_6.setText(_translate("Dialog", "Port"))
        self.label_2.setText(_translate("Dialog", "XPlane IP Address"))
        self.label_4.setText(_translate("Dialog", "IP"))
        self.label_7.setText(_translate("Dialog", "Port"))
        self.label_8.setText(_translate("Dialog", "Redirect UDP traffic to XPlane"))
        self.label_5.setText(_translate("Dialog", "IP"))
        self.label_10.setText(_translate("Dialog", "IP address we are receiving traffic to redirect "))
        self.label_11.setText(_translate("Dialog", "IP"))
        self.label_12.setText(_translate("Dialog", "Port"))
        self.label_9.setText(_translate("Dialog", "Forward XPlane UDP traffic to IP addresses"))
        self.ADD_FWDIP_BTN.setText(_translate("Dialog", "..."))
        self.RM_FWDIP_BTN.setText(_translate("Dialog", "..."))
        item = self.FWDIPs_TABLE.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "IP"))
        item = self.FWDIPs_TABLE.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Port"))
        self.UDPStatusLabel.setText(_translate("Dialog", "UDP Server status:"))

import resources_rc
