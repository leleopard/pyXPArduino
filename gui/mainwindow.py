# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1213, 805)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
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
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
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
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.label_7)
        self.label = QtWidgets.QLabel(self.arduinoEditForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.ardNameLineEdit = QtWidgets.QLineEdit(self.arduinoEditForm)
        self.ardNameLineEdit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.ardNameLineEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ardNameLineEdit.setObjectName("ardNameLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.ardNameLineEdit)
        self.label_4 = QtWidgets.QLabel(self.arduinoEditForm)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.ardPortLineEdit = QtWidgets.QLineEdit(self.arduinoEditForm)
        self.ardPortLineEdit.setEnabled(False)
        self.ardPortLineEdit.setMaximumSize(QtCore.QSize(100, 16777215))
        self.ardPortLineEdit.setReadOnly(True)
        self.ardPortLineEdit.setObjectName("ardPortLineEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.ardPortLineEdit)
        self.label_5 = QtWidgets.QLabel(self.arduinoEditForm)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.ardSerialNrLineEdit = QtWidgets.QLineEdit(self.arduinoEditForm)
        self.ardSerialNrLineEdit.setEnabled(False)
        self.ardSerialNrLineEdit.setMinimumSize(QtCore.QSize(250, 0))
        self.ardSerialNrLineEdit.setMaximumSize(QtCore.QSize(350, 16777215))
        self.ardSerialNrLineEdit.setReadOnly(True)
        self.ardSerialNrLineEdit.setObjectName("ardSerialNrLineEdit")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.ardSerialNrLineEdit)
        self.label_2 = QtWidgets.QLabel(self.arduinoEditForm)
        self.label_2.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.ardDescriptionLineEdit = QtWidgets.QLineEdit(self.arduinoEditForm)
        self.ardDescriptionLineEdit.setEnabled(False)
        self.ardDescriptionLineEdit.setMinimumSize(QtCore.QSize(250, 0))
        self.ardDescriptionLineEdit.setMaximumSize(QtCore.QSize(350, 16777215))
        self.ardDescriptionLineEdit.setBaseSize(QtCore.QSize(0, 0))
        self.ardDescriptionLineEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ardDescriptionLineEdit.setReadOnly(True)
        self.ardDescriptionLineEdit.setObjectName("ardDescriptionLineEdit")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.ardDescriptionLineEdit)
        self.label_6 = QtWidgets.QLabel(self.arduinoEditForm)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.ardManufacturerLineEdit = QtWidgets.QLineEdit(self.arduinoEditForm)
        self.ardManufacturerLineEdit.setEnabled(False)
        self.ardManufacturerLineEdit.setMinimumSize(QtCore.QSize(250, 0))
        self.ardManufacturerLineEdit.setMaximumSize(QtCore.QSize(350, 16777215))
        self.ardManufacturerLineEdit.setFrame(True)
        self.ardManufacturerLineEdit.setReadOnly(True)
        self.ardManufacturerLineEdit.setObjectName("ardManufacturerLineEdit")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.ardManufacturerLineEdit)
        self.horizontalLayoutEditPane.addWidget(self.arduinoEditForm)
        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1213, 21))
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
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionAdd_Arduino = QtWidgets.QAction(MainWindow)
        self.actionAdd_Arduino.setObjectName("actionAdd_Arduino")
        self.actionUDP_Settings = QtWidgets.QAction(MainWindow)
        self.actionUDP_Settings.setObjectName("actionUDP_Settings")
        self.actionAdd_component = QtWidgets.QAction(MainWindow)
        self.actionAdd_component.setObjectName("actionAdd_component")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionQuit)
        self.menuArduino.addAction(self.actionAdd_Arduino)
        self.menuArduino.addAction(self.actionAdd_component)
        self.menuX_Plane.addAction(self.actionUDP_Settings)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuArduino.menuAction())
        self.menubar.addAction(self.menuX_Plane.menuAction())

        self.retranslateUi(MainWindow)
        self.arduinoTreeWidget.customContextMenuRequested['QPoint'].connect(MainWindow.ardTreeContextMenuRequested)
        self.actionQuit.triggered.connect(MainWindow.close)
        self.actionSave.triggered.connect(MainWindow.saveToXML)
        self.actionAdd_Arduino.triggered.connect(MainWindow.pickArduino)
        self.arduinoTreeWidget.itemSelectionChanged.connect(MainWindow.ardTreeSelectionChanged)
        self.ardNameLineEdit.editingFinished.connect(MainWindow.ardEditingFinished)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.arduinoTreeWidget.headerItem().setText(0, _translate("MainWindow", "Name"))
        self.arduinoTreeWidget.headerItem().setText(1, _translate("MainWindow", "Serial nr"))
        self.label_7.setText(_translate("MainWindow", "Edit Arduino Settings"))
        self.label.setText(_translate("MainWindow", "Name"))
        self.label_4.setText(_translate("MainWindow", "Port"))
        self.label_5.setText(_translate("MainWindow", "Serial Number  "))
        self.label_2.setText(_translate("MainWindow", "Description"))
        self.label_6.setText(_translate("MainWindow", "Manufacturer"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuArduino.setTitle(_translate("MainWindow", "Arduino"))
        self.menuX_Plane.setTitle(_translate("MainWindow", "X Plane"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionAdd_Arduino.setText(_translate("MainWindow", "Add Arduino"))
        self.actionUDP_Settings.setText(_translate("MainWindow", "UDP Settings"))
        self.actionAdd_component.setText(_translate("MainWindow", "Add component"))
        self.actionSave.setText(_translate("MainWindow", "Save"))

import resources_rc
