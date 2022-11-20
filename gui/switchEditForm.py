# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'switchEditForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_switchEditForm(object):
    def setupUi(self, switchEditForm):
        switchEditForm.setObjectName("switchEditForm")
        switchEditForm.resize(832, 674)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(switchEditForm.sizePolicy().hasHeightForWidth())
        switchEditForm.setSizePolicy(sizePolicy)
        self.gridLayout = QtWidgets.QGridLayout(switchEditForm)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setObjectName("gridLayout")
        self.label_15 = QtWidgets.QLabel(switchEditForm)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 9, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 26, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 12, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(switchEditForm)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 7, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(switchEditForm)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: white;\n"
"background: rgb(0, 151, 157);\n"
"padding: 3px\n"
"")
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 0, 0, 1, 6)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.SWOFF_CMDS_TABLE = QtWidgets.QTableWidget(switchEditForm)
        self.SWOFF_CMDS_TABLE.setObjectName("SWOFF_CMDS_TABLE")
        self.SWOFF_CMDS_TABLE.setColumnCount(2)
        self.SWOFF_CMDS_TABLE.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.SWOFF_CMDS_TABLE.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.SWOFF_CMDS_TABLE.setHorizontalHeaderItem(1, item)
        self.gridLayout_4.addWidget(self.SWOFF_CMDS_TABLE, 6, 0, 1, 1)
        self.SWOFF_DREFS_TABLE = QtWidgets.QTableWidget(switchEditForm)
        self.SWOFF_DREFS_TABLE.setObjectName("SWOFF_DREFS_TABLE")
        self.SWOFF_DREFS_TABLE.setColumnCount(6)
        self.SWOFF_DREFS_TABLE.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.SWOFF_DREFS_TABLE.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.SWOFF_DREFS_TABLE.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.SWOFF_DREFS_TABLE.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.SWOFF_DREFS_TABLE.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.SWOFF_DREFS_TABLE.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.SWOFF_DREFS_TABLE.setHorizontalHeaderItem(5, item)
        self.gridLayout_4.addWidget(self.SWOFF_DREFS_TABLE, 6, 1, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_12 = QtWidgets.QLabel(switchEditForm)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_6.addWidget(self.label_12)
        self.SWOFF_ADDCMD_BTN = QtWidgets.QToolButton(switchEditForm)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/plusIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.SWOFF_ADDCMD_BTN.setIcon(icon)
        self.SWOFF_ADDCMD_BTN.setAutoRaise(True)
        self.SWOFF_ADDCMD_BTN.setObjectName("SWOFF_ADDCMD_BTN")
        self.horizontalLayout_6.addWidget(self.SWOFF_ADDCMD_BTN)
        self.SWOFF_RMCMD_BTN = QtWidgets.QToolButton(switchEditForm)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/minusIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.SWOFF_RMCMD_BTN.setIcon(icon1)
        self.SWOFF_RMCMD_BTN.setAutoRaise(True)
        self.SWOFF_RMCMD_BTN.setObjectName("SWOFF_RMCMD_BTN")
        self.horizontalLayout_6.addWidget(self.SWOFF_RMCMD_BTN)
        self.testSWOFF_CMDS_button = QtWidgets.QPushButton(switchEditForm)
        self.testSWOFF_CMDS_button.setObjectName("testSWOFF_CMDS_button")
        self.horizontalLayout_6.addWidget(self.testSWOFF_CMDS_button)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.gridLayout_4.addLayout(self.horizontalLayout_6, 3, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_14 = QtWidgets.QLabel(switchEditForm)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_7.addWidget(self.label_14)
        self.SWOFF_ADDDREF_BTN = QtWidgets.QToolButton(switchEditForm)
        self.SWOFF_ADDDREF_BTN.setIcon(icon)
        self.SWOFF_ADDDREF_BTN.setAutoRaise(True)
        self.SWOFF_ADDDREF_BTN.setObjectName("SWOFF_ADDDREF_BTN")
        self.horizontalLayout_7.addWidget(self.SWOFF_ADDDREF_BTN)
        self.SWOFF_RMDREF_BTN = QtWidgets.QToolButton(switchEditForm)
        self.SWOFF_RMDREF_BTN.setIcon(icon1)
        self.SWOFF_RMDREF_BTN.setAutoRaise(True)
        self.SWOFF_RMDREF_BTN.setObjectName("SWOFF_RMDREF_BTN")
        self.horizontalLayout_7.addWidget(self.SWOFF_RMDREF_BTN)
        self.testSWOFF_DREFS_button = QtWidgets.QPushButton(switchEditForm)
        self.testSWOFF_DREFS_button.setObjectName("testSWOFF_DREFS_button")
        self.horizontalLayout_7.addWidget(self.testSWOFF_DREFS_button)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem2)
        self.gridLayout_4.addLayout(self.horizontalLayout_7, 3, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_4, 10, 0, 1, 6)
        self.label_3 = QtWidgets.QLabel(switchEditForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.SWON_CMDS_TABLE = QtWidgets.QTableWidget(switchEditForm)
        self.SWON_CMDS_TABLE.setMinimumSize(QtCore.QSize(0, 75))
        self.SWON_CMDS_TABLE.setObjectName("SWON_CMDS_TABLE")
        self.SWON_CMDS_TABLE.setColumnCount(2)
        self.SWON_CMDS_TABLE.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.SWON_CMDS_TABLE.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.SWON_CMDS_TABLE.setHorizontalHeaderItem(1, item)
        self.gridLayout_3.addWidget(self.SWON_CMDS_TABLE, 4, 1, 1, 1)
        self.SWON_DREFS_TABLE = QtWidgets.QTableWidget(switchEditForm)
        self.SWON_DREFS_TABLE.setObjectName("SWON_DREFS_TABLE")
        self.SWON_DREFS_TABLE.setColumnCount(6)
        self.SWON_DREFS_TABLE.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.SWON_DREFS_TABLE.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.SWON_DREFS_TABLE.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.SWON_DREFS_TABLE.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.SWON_DREFS_TABLE.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.SWON_DREFS_TABLE.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.SWON_DREFS_TABLE.setHorizontalHeaderItem(5, item)
        self.gridLayout_3.addWidget(self.SWON_DREFS_TABLE, 4, 4, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_10 = QtWidgets.QLabel(switchEditForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_4.addWidget(self.label_10)
        self.SWON_ADDCMD_BTN = QtWidgets.QToolButton(switchEditForm)
        self.SWON_ADDCMD_BTN.setIcon(icon)
        self.SWON_ADDCMD_BTN.setAutoRaise(True)
        self.SWON_ADDCMD_BTN.setObjectName("SWON_ADDCMD_BTN")
        self.horizontalLayout_4.addWidget(self.SWON_ADDCMD_BTN)
        self.SWON_RMCMD_BTN = QtWidgets.QToolButton(switchEditForm)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/minusIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SWON_RMCMD_BTN.setIcon(icon2)
        self.SWON_RMCMD_BTN.setAutoRaise(True)
        self.SWON_RMCMD_BTN.setObjectName("SWON_RMCMD_BTN")
        self.horizontalLayout_4.addWidget(self.SWON_RMCMD_BTN)
        self.testSWON_CMDS_button = QtWidgets.QPushButton(switchEditForm)
        self.testSWON_CMDS_button.setObjectName("testSWON_CMDS_button")
        self.horizontalLayout_4.addWidget(self.testSWON_CMDS_button)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.gridLayout_3.addLayout(self.horizontalLayout_4, 2, 1, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_11 = QtWidgets.QLabel(switchEditForm)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_5.addWidget(self.label_11)
        self.SWON_ADDDREF_BTN = QtWidgets.QToolButton(switchEditForm)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/newPrefix/plusIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SWON_ADDDREF_BTN.setIcon(icon3)
        self.SWON_ADDDREF_BTN.setAutoRaise(True)
        self.SWON_ADDDREF_BTN.setObjectName("SWON_ADDDREF_BTN")
        self.horizontalLayout_5.addWidget(self.SWON_ADDDREF_BTN)
        self.SWON_RMDREF_BTN = QtWidgets.QToolButton(switchEditForm)
        self.SWON_RMDREF_BTN.setIcon(icon2)
        self.SWON_RMDREF_BTN.setAutoRaise(True)
        self.SWON_RMDREF_BTN.setObjectName("SWON_RMDREF_BTN")
        self.horizontalLayout_5.addWidget(self.SWON_RMDREF_BTN)
        self.testSWON_DREFS_button = QtWidgets.QPushButton(switchEditForm)
        self.testSWON_DREFS_button.setObjectName("testSWON_DREFS_button")
        self.horizontalLayout_5.addWidget(self.testSWON_DREFS_button)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.gridLayout_3.addLayout(self.horizontalLayout_5, 2, 4, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_3, 8, 0, 1, 6)
        spacerItem5 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem5, 6, 0, 1, 1)
        self.nameLineEdit = QtWidgets.QLineEdit(switchEditForm)
        self.nameLineEdit.setMinimumSize(QtCore.QSize(250, 0))
        self.nameLineEdit.setMaximumSize(QtCore.QSize(350, 16777215))
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.gridLayout.addWidget(self.nameLineEdit, 1, 1, 1, 1)
        self.label_19 = QtWidgets.QLabel(switchEditForm)
        self.label_19.setObjectName("label_19")
        self.gridLayout.addWidget(self.label_19, 2, 2, 1, 1)
        self.IDlineEdit = QtWidgets.QLineEdit(switchEditForm)
        self.IDlineEdit.setEnabled(False)
        self.IDlineEdit.setMinimumSize(QtCore.QSize(250, 0))
        self.IDlineEdit.setMaximumSize(QtCore.QSize(350, 16777215))
        self.IDlineEdit.setReadOnly(True)
        self.IDlineEdit.setObjectName("IDlineEdit")
        self.gridLayout.addWidget(self.IDlineEdit, 2, 4, 1, 1)
        self.label_17 = QtWidgets.QLabel(switchEditForm)
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 1, 2, 1, 1)
        self.switchStateButton = QtWidgets.QToolButton(switchEditForm)
        self.switchStateButton.setEnabled(False)
        self.switchStateButton.setStyleSheet("border: 0px;")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/newPrefix/switch_off.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon4.addPixmap(QtGui.QPixmap(":/newPrefix/switch_on.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon4.addPixmap(QtGui.QPixmap(":/newPrefix/switch_off.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        icon4.addPixmap(QtGui.QPixmap(":/newPrefix/switch_on.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        icon4.addPixmap(QtGui.QPixmap(":/newPrefix/switch_off.png"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon4.addPixmap(QtGui.QPixmap(":/newPrefix/switch_on.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        icon4.addPixmap(QtGui.QPixmap(":/newPrefix/switch_off.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        icon4.addPixmap(QtGui.QPixmap(":/newPrefix/switch_on.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.switchStateButton.setIcon(icon4)
        self.switchStateButton.setIconSize(QtCore.QSize(66, 26))
        self.switchStateButton.setCheckable(True)
        self.switchStateButton.setAutoRaise(True)
        self.switchStateButton.setObjectName("switchStateButton")
        self.gridLayout.addWidget(self.switchStateButton, 1, 4, 1, 1)
        self.label_18 = QtWidgets.QLabel(switchEditForm)
        self.label_18.setObjectName("label_18")
        self.gridLayout.addWidget(self.label_18, 2, 0, 1, 1)
        self.PIN_comboBox = QtWidgets.QComboBox(switchEditForm)
        self.PIN_comboBox.setMaximumSize(QtCore.QSize(50, 16777215))
        self.PIN_comboBox.setObjectName("PIN_comboBox")
        self.gridLayout.addWidget(self.PIN_comboBox, 2, 1, 1, 1)

        self.retranslateUi(switchEditForm)
        self.SWON_ADDCMD_BTN.clicked.connect(switchEditForm.addSwitchOnCommand)
        self.SWON_RMCMD_BTN.clicked.connect(switchEditForm.rmSwitchOnCommand)
        self.SWON_ADDDREF_BTN.clicked.connect(switchEditForm.addSwitchOnDataref)
        self.SWON_RMDREF_BTN.clicked.connect(switchEditForm.rmSwitchOnDataref)
        self.SWOFF_ADDCMD_BTN.clicked.connect(switchEditForm.addSwitchOffCommand)
        self.SWOFF_RMCMD_BTN.clicked.connect(switchEditForm.rmSwitchOffCommand)
        self.SWOFF_ADDDREF_BTN.clicked.connect(switchEditForm.addSwitchOffDataref)
        self.SWOFF_RMDREF_BTN.clicked.connect(switchEditForm.rmSwitchOffDataref)
        self.SWON_CMDS_TABLE.cellDoubleClicked['int','int'].connect(switchEditForm.editXPCommand)
        self.SWOFF_CMDS_TABLE.cellDoubleClicked['int','int'].connect(switchEditForm.editXPCommand)
        self.nameLineEdit.editingFinished.connect(switchEditForm.updateXMLdata)
        self.PIN_comboBox.currentIndexChanged['int'].connect(switchEditForm.updateXMLdata)
        self.SWON_CMDS_TABLE.itemChanged['QTableWidgetItem*'].connect(switchEditForm.updateXMLdata)
        self.SWOFF_CMDS_TABLE.itemChanged['QTableWidgetItem*'].connect(switchEditForm.updateXMLdata)
        self.testSWON_CMDS_button.clicked.connect(switchEditForm.testOnCommands)
        self.testSWOFF_CMDS_button.clicked.connect(switchEditForm.testOffCommands)
        self.PIN_comboBox.currentTextChanged['QString'].connect(switchEditForm.updatePin)
        self.SWON_DREFS_TABLE.cellDoubleClicked['int','int'].connect(switchEditForm.editXPDataref)
        self.SWOFF_DREFS_TABLE.cellDoubleClicked['int','int'].connect(switchEditForm.editXPDataref)
        self.SWON_DREFS_TABLE.itemChanged['QTableWidgetItem*'].connect(switchEditForm.updateXMLdata)
        self.SWOFF_DREFS_TABLE.itemChanged['QTableWidgetItem*'].connect(switchEditForm.updateXMLdata)
        self.testSWOFF_DREFS_button.clicked.connect(switchEditForm.testOffDatarefs)
        self.testSWON_DREFS_button.clicked.connect(switchEditForm.testOnDatarefs)
        self.SWON_CMDS_TABLE.cellChanged['int','int'].connect(switchEditForm.activateSave)
        QtCore.QMetaObject.connectSlotsByName(switchEditForm)

    def retranslateUi(self, switchEditForm):
        _translate = QtCore.QCoreApplication.translate
        switchEditForm.setWindowTitle(_translate("switchEditForm", "Form"))
        self.label_15.setText(_translate("switchEditForm", "Switch OFF actions"))
        self.label_9.setText(_translate("switchEditForm", "Switch ON actions:"))
        self.label_8.setText(_translate("switchEditForm", "Edit switch"))
        item = self.SWOFF_CMDS_TABLE.horizontalHeaderItem(0)
        item.setText(_translate("switchEditForm", "Command"))
        item = self.SWOFF_CMDS_TABLE.horizontalHeaderItem(1)
        item.setText(_translate("switchEditForm", "Send continuously"))
        item = self.SWOFF_DREFS_TABLE.horizontalHeaderItem(0)
        item.setText(_translate("switchEditForm", "Dataref"))
        item = self.SWOFF_DREFS_TABLE.horizontalHeaderItem(1)
        item.setText(_translate("switchEditForm", "Index"))
        item = self.SWOFF_DREFS_TABLE.horizontalHeaderItem(2)
        item.setText(_translate("switchEditForm", "Set to Value"))
        item = self.SWOFF_DREFS_TABLE.horizontalHeaderItem(3)
        item.setText(_translate("switchEditForm", "Set continuously"))
        item = self.SWOFF_DREFS_TABLE.horizontalHeaderItem(4)
        item.setText(_translate("switchEditForm", "Type"))
        item = self.SWOFF_DREFS_TABLE.horizontalHeaderItem(5)
        item.setText(_translate("switchEditForm", "Unit"))
        self.label_12.setText(_translate("switchEditForm", "Send XPlane Command: "))
        self.SWOFF_ADDCMD_BTN.setText(_translate("switchEditForm", "..."))
        self.SWOFF_RMCMD_BTN.setText(_translate("switchEditForm", "..."))
        self.testSWOFF_CMDS_button.setText(_translate("switchEditForm", "Test"))
        self.label_14.setText(_translate("switchEditForm", "Set Dataref:"))
        self.SWOFF_ADDDREF_BTN.setText(_translate("switchEditForm", "..."))
        self.SWOFF_RMDREF_BTN.setText(_translate("switchEditForm", "..."))
        self.testSWOFF_DREFS_button.setText(_translate("switchEditForm", "Test"))
        self.label_3.setText(_translate("switchEditForm", "Name"))
        item = self.SWON_CMDS_TABLE.horizontalHeaderItem(0)
        item.setText(_translate("switchEditForm", "Command"))
        item = self.SWON_CMDS_TABLE.horizontalHeaderItem(1)
        item.setText(_translate("switchEditForm", "Send continuously"))
        item = self.SWON_DREFS_TABLE.horizontalHeaderItem(0)
        item.setText(_translate("switchEditForm", "Dataref"))
        item = self.SWON_DREFS_TABLE.horizontalHeaderItem(1)
        item.setText(_translate("switchEditForm", "Index"))
        item = self.SWON_DREFS_TABLE.horizontalHeaderItem(2)
        item.setText(_translate("switchEditForm", "Set to Value"))
        item = self.SWON_DREFS_TABLE.horizontalHeaderItem(3)
        item.setText(_translate("switchEditForm", "Set continuously"))
        item = self.SWON_DREFS_TABLE.horizontalHeaderItem(4)
        item.setText(_translate("switchEditForm", "Type"))
        item = self.SWON_DREFS_TABLE.horizontalHeaderItem(5)
        item.setText(_translate("switchEditForm", "Unit"))
        self.label_10.setText(_translate("switchEditForm", "Send XPlane Commands: "))
        self.SWON_ADDCMD_BTN.setText(_translate("switchEditForm", "..."))
        self.SWON_RMCMD_BTN.setText(_translate("switchEditForm", "..."))
        self.testSWON_CMDS_button.setText(_translate("switchEditForm", "Test"))
        self.label_11.setText(_translate("switchEditForm", "Set Dataref: "))
        self.SWON_ADDDREF_BTN.setText(_translate("switchEditForm", "..."))
        self.SWON_RMDREF_BTN.setText(_translate("switchEditForm", "..."))
        self.testSWON_DREFS_button.setText(_translate("switchEditForm", "Test"))
        self.label_19.setText(_translate("switchEditForm", "ID"))
        self.label_17.setText(_translate("switchEditForm", "State"))
        self.switchStateButton.setText(_translate("switchEditForm", "..."))
        self.label_18.setText(_translate("switchEditForm", "Arduino pin:"))
import resources_rc
