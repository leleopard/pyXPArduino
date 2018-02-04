# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1213, 805)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/plane_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(4, 4, 4, 4)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setMinimumSize(QtCore.QSize(0, 0))
        self.splitter.setBaseSize(QtCore.QSize(0, 0))
        self.splitter.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.splitter.setAutoFillBackground(False)
        self.splitter.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setChildrenCollapsible(False)
        self.splitter.setObjectName("splitter")
        self.widget = QtWidgets.QWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(100, 400))
        self.widget.setMaximumSize(QtCore.QSize(400, 16777215))
        self.widget.setBaseSize(QtCore.QSize(0, 0))
        self.widget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.arduinoTreeWidget = QtWidgets.QTreeWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.arduinoTreeWidget.sizePolicy().hasHeightForWidth())
        self.arduinoTreeWidget.setSizePolicy(sizePolicy)
        self.arduinoTreeWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.arduinoTreeWidget.setBaseSize(QtCore.QSize(0, 0))
        self.arduinoTreeWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.arduinoTreeWidget.setColumnCount(2)
        self.arduinoTreeWidget.setObjectName("arduinoTreeWidget")
        self.horizontalLayout_2.addWidget(self.arduinoTreeWidget)
        self.editPaneWidget = QtWidgets.QWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editPaneWidget.sizePolicy().hasHeightForWidth())
        self.editPaneWidget.setSizePolicy(sizePolicy)
        self.editPaneWidget.setMinimumSize(QtCore.QSize(500, 0))
        self.editPaneWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.editPaneWidget.setObjectName("editPaneWidget")
        self.horizontalLayoutEditPane = QtWidgets.QHBoxLayout(self.editPaneWidget)
        self.horizontalLayoutEditPane.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayoutEditPane.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayoutEditPane.setObjectName("horizontalLayoutEditPane")
        self.arduinoEditForm = QtWidgets.QWidget(self.editPaneWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.arduinoEditForm.sizePolicy().hasHeightForWidth())
        self.arduinoEditForm.setSizePolicy(sizePolicy)
        self.arduinoEditForm.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.arduinoEditForm.setObjectName("arduinoEditForm")
        self.formLayout = QtWidgets.QFormLayout(self.arduinoEditForm)
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.arduinoEditForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setObjectName("label")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.label)
        self.ardNameLineEdit = QtWidgets.QLineEdit(self.arduinoEditForm)
        self.ardNameLineEdit.setMaximumSize(QtCore.QSize(350, 16777215))
        self.ardNameLineEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ardNameLineEdit.setObjectName("ardNameLineEdit")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.ardNameLineEdit)
        self.label_4 = QtWidgets.QLabel(self.arduinoEditForm)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.ardPortLineEdit = QtWidgets.QLineEdit(self.arduinoEditForm)
        self.ardPortLineEdit.setEnabled(False)
        self.ardPortLineEdit.setMaximumSize(QtCore.QSize(100, 16777215))
        self.ardPortLineEdit.setReadOnly(True)
        self.ardPortLineEdit.setObjectName("ardPortLineEdit")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.FieldRole, self.ardPortLineEdit)
        self.label_5 = QtWidgets.QLabel(self.arduinoEditForm)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(14, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.ardSerialNrLineEdit = QtWidgets.QLineEdit(self.arduinoEditForm)
        self.ardSerialNrLineEdit.setEnabled(False)
        self.ardSerialNrLineEdit.setMinimumSize(QtCore.QSize(250, 0))
        self.ardSerialNrLineEdit.setMaximumSize(QtCore.QSize(350, 16777215))
        self.ardSerialNrLineEdit.setReadOnly(True)
        self.ardSerialNrLineEdit.setObjectName("ardSerialNrLineEdit")
        self.formLayout.setWidget(14, QtWidgets.QFormLayout.FieldRole, self.ardSerialNrLineEdit)
        self.label_2 = QtWidgets.QLabel(self.arduinoEditForm)
        self.label_2.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(16, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.ardDescriptionLineEdit = QtWidgets.QLineEdit(self.arduinoEditForm)
        self.ardDescriptionLineEdit.setEnabled(False)
        self.ardDescriptionLineEdit.setMinimumSize(QtCore.QSize(250, 0))
        self.ardDescriptionLineEdit.setMaximumSize(QtCore.QSize(350, 16777215))
        self.ardDescriptionLineEdit.setBaseSize(QtCore.QSize(0, 0))
        self.ardDescriptionLineEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ardDescriptionLineEdit.setReadOnly(True)
        self.ardDescriptionLineEdit.setObjectName("ardDescriptionLineEdit")
        self.formLayout.setWidget(16, QtWidgets.QFormLayout.FieldRole, self.ardDescriptionLineEdit)
        self.label_6 = QtWidgets.QLabel(self.arduinoEditForm)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(17, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.ardManufacturerLineEdit = QtWidgets.QLineEdit(self.arduinoEditForm)
        self.ardManufacturerLineEdit.setEnabled(False)
        self.ardManufacturerLineEdit.setMinimumSize(QtCore.QSize(250, 0))
        self.ardManufacturerLineEdit.setMaximumSize(QtCore.QSize(350, 16777215))
        self.ardManufacturerLineEdit.setFrame(True)
        self.ardManufacturerLineEdit.setReadOnly(True)
        self.ardManufacturerLineEdit.setObjectName("ardManufacturerLineEdit")
        self.formLayout.setWidget(17, QtWidgets.QFormLayout.FieldRole, self.ardManufacturerLineEdit)
        self.label_3 = QtWidgets.QLabel(self.arduinoEditForm)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.ardBaudComboBox = QtWidgets.QComboBox(self.arduinoEditForm)
        self.ardBaudComboBox.setMaximumSize(QtCore.QSize(150, 16777215))
        self.ardBaudComboBox.setObjectName("ardBaudComboBox")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.ardBaudComboBox)
        self.label_7 = QtWidgets.QLabel(self.arduinoEditForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAutoFillBackground(False)
        self.label_7.setStyleSheet("color: white;\n"
"background: rgb(0, 151, 157);\n"
"padding: 3px\n"
"\n"
"")
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.SpanningRole, self.label_7)
        self.label_10 = QtWidgets.QLabel(self.arduinoEditForm)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_10)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.formLayout.setItem(8, QtWidgets.QFormLayout.LabelRole, spacerItem)
        self.label_8 = QtWidgets.QLabel(self.arduinoEditForm)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: white;\n"
"background: rgb(0, 151, 157);\n"
"padding: 3px")
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.label_8)
        self.label_9 = QtWidgets.QLabel(self.arduinoEditForm)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.ardFirmwareVersionLabel = QtWidgets.QLabel(self.arduinoEditForm)
        self.ardFirmwareVersionLabel.setStyleSheet("color:blue;")
        self.ardFirmwareVersionLabel.setText("")
        self.ardFirmwareVersionLabel.setObjectName("ardFirmwareVersionLabel")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.ardFirmwareVersionLabel)
        self.ardStatusTitleLabel = QtWidgets.QLabel(self.arduinoEditForm)
        self.ardStatusTitleLabel.setObjectName("ardStatusTitleLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.ardStatusTitleLabel)
        self.ardStatusLabel = QtWidgets.QLabel(self.arduinoEditForm)
        self.ardStatusLabel.setText("")
        self.ardStatusLabel.setObjectName("ardStatusLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.ardStatusLabel)
        self.ardSerialConnStatusLabel = QtWidgets.QLabel(self.arduinoEditForm)
        self.ardSerialConnStatusLabel.setMaximumSize(QtCore.QSize(150, 16777215))
        self.ardSerialConnStatusLabel.setText("")
        self.ardSerialConnStatusLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ardSerialConnStatusLabel.setObjectName("ardSerialConnStatusLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.ardSerialConnStatusLabel)
        self.horizontalLayoutEditPane.addWidget(self.arduinoEditForm)
        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1213, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuArduino = QtWidgets.QMenu(self.menubar)
        self.menuArduino.setObjectName("menuArduino")
        self.menuX_Plane = QtWidgets.QMenu(self.menubar)
        self.menuX_Plane.setObjectName("menuX_Plane")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionQuit = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/quit.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionQuit.setIcon(icon1)
        self.actionQuit.setObjectName("actionQuit")
        self.actionAdd_Arduino = QtWidgets.QAction(MainWindow)
        self.actionAdd_Arduino.setObjectName("actionAdd_Arduino")
        self.actionUDP_Settings = QtWidgets.QAction(MainWindow)
        self.actionUDP_Settings.setObjectName("actionUDP_Settings")
        self.actionAdd_component = QtWidgets.QAction(MainWindow)
        self.actionAdd_component.setObjectName("actionAdd_component")
        self.actionSave = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/save_active.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionSave.setIcon(icon2)
        self.actionSave.setObjectName("actionSave")
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionQuit)
        self.menuArduino.addAction(self.actionAdd_Arduino)
        self.menuArduino.addAction(self.actionAdd_component)
        self.menuX_Plane.addAction(self.actionUDP_Settings)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuArduino.menuAction())
        self.menubar.addAction(self.menuX_Plane.menuAction())
        self.toolBar.addAction(self.actionSave)

        self.retranslateUi(MainWindow)
        self.arduinoTreeWidget.customContextMenuRequested['QPoint'].connect(MainWindow.ardTreeContextMenuRequested)
        self.actionQuit.triggered.connect(MainWindow.close)
        self.actionSave.triggered.connect(MainWindow.saveToXML)
        self.actionAdd_Arduino.triggered.connect(MainWindow.pickArduino)
        self.arduinoTreeWidget.itemSelectionChanged.connect(MainWindow.ardTreeSelectionChanged)
        self.ardNameLineEdit.editingFinished.connect(MainWindow.ardEditingFinished)
        self.ardBaudComboBox.currentIndexChanged['int'].connect(MainWindow.ardEditingFinished)
        self.actionUDP_Settings.triggered.connect(MainWindow.editXPUDPSettings)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "pyXPArduino"))
        self.arduinoTreeWidget.headerItem().setText(0, _translate("MainWindow", "Name"))
        self.arduinoTreeWidget.headerItem().setText(1, _translate("MainWindow", "Serial nr"))
        self.label.setText(_translate("MainWindow", "Name"))
        self.label_4.setText(_translate("MainWindow", "Port"))
        self.label_5.setText(_translate("MainWindow", "Serial Number  "))
        self.label_2.setText(_translate("MainWindow", "Description"))
        self.label_6.setText(_translate("MainWindow", "Manufacturer"))
        self.label_3.setText(_translate("MainWindow", "Baud"))
        self.label_7.setText(_translate("MainWindow", "Edit Arduino Settings"))
        self.label_10.setText(_translate("MainWindow", "Arduino firmware version"))
        self.label_8.setText(_translate("MainWindow", "Arduino status"))
        self.label_9.setText(_translate("MainWindow", "Serial Connection Status"))
        self.ardStatusTitleLabel.setText(_translate("MainWindow", "Arduino Status"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuArduino.setTitle(_translate("MainWindow", "Arduino"))
        self.menuX_Plane.setTitle(_translate("MainWindow", "X Plane"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionAdd_Arduino.setText(_translate("MainWindow", "Add Arduino"))
        self.actionUDP_Settings.setText(_translate("MainWindow", "UDP Settings"))
        self.actionAdd_component.setText(_translate("MainWindow", "Add component"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))

import resources_rc
