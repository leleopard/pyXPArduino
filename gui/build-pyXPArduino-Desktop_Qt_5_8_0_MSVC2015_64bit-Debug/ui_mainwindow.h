/********************************************************************************
** Form generated from reading UI file 'mainwindow.ui'
**
** Created by: Qt User Interface Compiler version 5.8.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QComboBox>
#include <QtWidgets/QFormLayout>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenu>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QSplitter>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QToolBar>
#include <QtWidgets/QTreeWidget>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QAction *actionQuit;
    QAction *actionAdd_Arduino;
    QAction *actionUDP_Settings;
    QAction *actionAdd_component;
    QAction *actionSave;
    QWidget *centralwidget;
    QGridLayout *gridLayout;
    QSplitter *splitter;
    QWidget *widget;
    QHBoxLayout *horizontalLayout_2;
    QTreeWidget *arduinoTreeWidget;
    QWidget *editPaneWidget;
    QHBoxLayout *horizontalLayoutEditPane;
    QWidget *arduinoEditForm;
    QFormLayout *formLayout;
    QLabel *label_7;
    QLabel *label;
    QLineEdit *ardNameLineEdit;
    QLabel *label_4;
    QLineEdit *ardPortLineEdit;
    QLabel *label_5;
    QLineEdit *ardSerialNrLineEdit;
    QLabel *label_2;
    QLineEdit *ardDescriptionLineEdit;
    QLabel *label_6;
    QLineEdit *ardManufacturerLineEdit;
    QLabel *label_3;
    QComboBox *ardBaudComboBox;
    QMenuBar *menubar;
    QMenu *menuFile;
    QMenu *menuArduino;
    QMenu *menuX_Plane;
    QStatusBar *statusbar;
    QToolBar *toolBar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QStringLiteral("MainWindow"));
        MainWindow->resize(1213, 805);
        QSizePolicy sizePolicy(QSizePolicy::Expanding, QSizePolicy::Expanding);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(MainWindow->sizePolicy().hasHeightForWidth());
        MainWindow->setSizePolicy(sizePolicy);
        MainWindow->setMinimumSize(QSize(0, 0));
        QIcon icon;
        icon.addFile(QStringLiteral(":/newPrefix/plane_icon.png"), QSize(), QIcon::Normal, QIcon::Off);
        MainWindow->setWindowIcon(icon);
        actionQuit = new QAction(MainWindow);
        actionQuit->setObjectName(QStringLiteral("actionQuit"));
        QIcon icon1;
        icon1.addFile(QStringLiteral(":/newPrefix/quit.png"), QSize(), QIcon::Normal, QIcon::On);
        actionQuit->setIcon(icon1);
        actionAdd_Arduino = new QAction(MainWindow);
        actionAdd_Arduino->setObjectName(QStringLiteral("actionAdd_Arduino"));
        actionUDP_Settings = new QAction(MainWindow);
        actionUDP_Settings->setObjectName(QStringLiteral("actionUDP_Settings"));
        actionAdd_component = new QAction(MainWindow);
        actionAdd_component->setObjectName(QStringLiteral("actionAdd_component"));
        actionSave = new QAction(MainWindow);
        actionSave->setObjectName(QStringLiteral("actionSave"));
        QIcon icon2;
        icon2.addFile(QStringLiteral(":/newPrefix/save_active.png"), QSize(), QIcon::Normal, QIcon::On);
        actionSave->setIcon(icon2);
        centralwidget = new QWidget(MainWindow);
        centralwidget->setObjectName(QStringLiteral("centralwidget"));
        QSizePolicy sizePolicy1(QSizePolicy::Preferred, QSizePolicy::Preferred);
        sizePolicy1.setHorizontalStretch(0);
        sizePolicy1.setVerticalStretch(0);
        sizePolicy1.setHeightForWidth(centralwidget->sizePolicy().hasHeightForWidth());
        centralwidget->setSizePolicy(sizePolicy1);
        gridLayout = new QGridLayout(centralwidget);
        gridLayout->setObjectName(QStringLiteral("gridLayout"));
        gridLayout->setContentsMargins(4, 4, 4, 4);
        splitter = new QSplitter(centralwidget);
        splitter->setObjectName(QStringLiteral("splitter"));
        QSizePolicy sizePolicy2(QSizePolicy::Minimum, QSizePolicy::MinimumExpanding);
        sizePolicy2.setHorizontalStretch(0);
        sizePolicy2.setVerticalStretch(0);
        sizePolicy2.setHeightForWidth(splitter->sizePolicy().hasHeightForWidth());
        splitter->setSizePolicy(sizePolicy2);
        splitter->setMinimumSize(QSize(0, 0));
        splitter->setBaseSize(QSize(0, 0));
        splitter->setCursor(QCursor(Qt::ArrowCursor));
        splitter->setAutoFillBackground(false);
        splitter->setFrameShape(QFrame::NoFrame);
        splitter->setOrientation(Qt::Horizontal);
        splitter->setChildrenCollapsible(false);
        widget = new QWidget(splitter);
        widget->setObjectName(QStringLiteral("widget"));
        QSizePolicy sizePolicy3(QSizePolicy::MinimumExpanding, QSizePolicy::MinimumExpanding);
        sizePolicy3.setHorizontalStretch(0);
        sizePolicy3.setVerticalStretch(0);
        sizePolicy3.setHeightForWidth(widget->sizePolicy().hasHeightForWidth());
        widget->setSizePolicy(sizePolicy3);
        widget->setMinimumSize(QSize(100, 400));
        widget->setMaximumSize(QSize(400, 16777215));
        widget->setBaseSize(QSize(0, 0));
        widget->setLayoutDirection(Qt::LeftToRight);
        horizontalLayout_2 = new QHBoxLayout(widget);
        horizontalLayout_2->setSpacing(0);
        horizontalLayout_2->setObjectName(QStringLiteral("horizontalLayout_2"));
        horizontalLayout_2->setSizeConstraint(QLayout::SetDefaultConstraint);
        horizontalLayout_2->setContentsMargins(0, 0, 0, 0);
        arduinoTreeWidget = new QTreeWidget(widget);
        arduinoTreeWidget->setObjectName(QStringLiteral("arduinoTreeWidget"));
        sizePolicy3.setHeightForWidth(arduinoTreeWidget->sizePolicy().hasHeightForWidth());
        arduinoTreeWidget->setSizePolicy(sizePolicy3);
        arduinoTreeWidget->setMinimumSize(QSize(0, 0));
        arduinoTreeWidget->setBaseSize(QSize(0, 0));
        arduinoTreeWidget->setContextMenuPolicy(Qt::CustomContextMenu);
        arduinoTreeWidget->setColumnCount(2);

        horizontalLayout_2->addWidget(arduinoTreeWidget);

        splitter->addWidget(widget);
        editPaneWidget = new QWidget(splitter);
        editPaneWidget->setObjectName(QStringLiteral("editPaneWidget"));
        QSizePolicy sizePolicy4(QSizePolicy::Expanding, QSizePolicy::Expanding);
        sizePolicy4.setHorizontalStretch(3);
        sizePolicy4.setVerticalStretch(0);
        sizePolicy4.setHeightForWidth(editPaneWidget->sizePolicy().hasHeightForWidth());
        editPaneWidget->setSizePolicy(sizePolicy4);
        editPaneWidget->setMinimumSize(QSize(500, 0));
        editPaneWidget->setLayoutDirection(Qt::LeftToRight);
        horizontalLayoutEditPane = new QHBoxLayout(editPaneWidget);
        horizontalLayoutEditPane->setObjectName(QStringLiteral("horizontalLayoutEditPane"));
        horizontalLayoutEditPane->setSizeConstraint(QLayout::SetDefaultConstraint);
        arduinoEditForm = new QWidget(editPaneWidget);
        arduinoEditForm->setObjectName(QStringLiteral("arduinoEditForm"));
        QSizePolicy sizePolicy5(QSizePolicy::Expanding, QSizePolicy::Preferred);
        sizePolicy5.setHorizontalStretch(0);
        sizePolicy5.setVerticalStretch(0);
        sizePolicy5.setHeightForWidth(arduinoEditForm->sizePolicy().hasHeightForWidth());
        arduinoEditForm->setSizePolicy(sizePolicy5);
        arduinoEditForm->setLayoutDirection(Qt::LeftToRight);
        formLayout = new QFormLayout(arduinoEditForm);
        formLayout->setObjectName(QStringLiteral("formLayout"));
        formLayout->setSizeConstraint(QLayout::SetDefaultConstraint);
        label_7 = new QLabel(arduinoEditForm);
        label_7->setObjectName(QStringLiteral("label_7"));
        sizePolicy5.setHeightForWidth(label_7->sizePolicy().hasHeightForWidth());
        label_7->setSizePolicy(sizePolicy5);
        QFont font;
        font.setPointSize(10);
        font.setBold(true);
        font.setWeight(75);
        label_7->setFont(font);
        label_7->setAutoFillBackground(false);
        label_7->setStyleSheet(QLatin1String("color: white;\n"
"background: rgb(0, 151, 157);\n"
"padding: 3px\n"
"\n"
""));
        label_7->setMargin(1);

        formLayout->setWidget(0, QFormLayout::SpanningRole, label_7);

        label = new QLabel(arduinoEditForm);
        label->setObjectName(QStringLiteral("label"));
        QSizePolicy sizePolicy6(QSizePolicy::Minimum, QSizePolicy::Minimum);
        sizePolicy6.setHorizontalStretch(0);
        sizePolicy6.setVerticalStretch(0);
        sizePolicy6.setHeightForWidth(label->sizePolicy().hasHeightForWidth());
        label->setSizePolicy(sizePolicy6);
        label->setMaximumSize(QSize(200, 16777215));
        label->setLayoutDirection(Qt::LeftToRight);

        formLayout->setWidget(1, QFormLayout::LabelRole, label);

        ardNameLineEdit = new QLineEdit(arduinoEditForm);
        ardNameLineEdit->setObjectName(QStringLiteral("ardNameLineEdit"));
        ardNameLineEdit->setMaximumSize(QSize(350, 16777215));
        ardNameLineEdit->setLayoutDirection(Qt::LeftToRight);

        formLayout->setWidget(1, QFormLayout::FieldRole, ardNameLineEdit);

        label_4 = new QLabel(arduinoEditForm);
        label_4->setObjectName(QStringLiteral("label_4"));

        formLayout->setWidget(4, QFormLayout::LabelRole, label_4);

        ardPortLineEdit = new QLineEdit(arduinoEditForm);
        ardPortLineEdit->setObjectName(QStringLiteral("ardPortLineEdit"));
        ardPortLineEdit->setEnabled(false);
        ardPortLineEdit->setMaximumSize(QSize(100, 16777215));
        ardPortLineEdit->setReadOnly(true);

        formLayout->setWidget(4, QFormLayout::FieldRole, ardPortLineEdit);

        label_5 = new QLabel(arduinoEditForm);
        label_5->setObjectName(QStringLiteral("label_5"));

        formLayout->setWidget(5, QFormLayout::LabelRole, label_5);

        ardSerialNrLineEdit = new QLineEdit(arduinoEditForm);
        ardSerialNrLineEdit->setObjectName(QStringLiteral("ardSerialNrLineEdit"));
        ardSerialNrLineEdit->setEnabled(false);
        ardSerialNrLineEdit->setMinimumSize(QSize(250, 0));
        ardSerialNrLineEdit->setMaximumSize(QSize(350, 16777215));
        ardSerialNrLineEdit->setReadOnly(true);

        formLayout->setWidget(5, QFormLayout::FieldRole, ardSerialNrLineEdit);

        label_2 = new QLabel(arduinoEditForm);
        label_2->setObjectName(QStringLiteral("label_2"));
        label_2->setMaximumSize(QSize(200, 16777215));

        formLayout->setWidget(7, QFormLayout::LabelRole, label_2);

        ardDescriptionLineEdit = new QLineEdit(arduinoEditForm);
        ardDescriptionLineEdit->setObjectName(QStringLiteral("ardDescriptionLineEdit"));
        ardDescriptionLineEdit->setEnabled(false);
        ardDescriptionLineEdit->setMinimumSize(QSize(250, 0));
        ardDescriptionLineEdit->setMaximumSize(QSize(350, 16777215));
        ardDescriptionLineEdit->setBaseSize(QSize(0, 0));
        ardDescriptionLineEdit->setLayoutDirection(Qt::LeftToRight);
        ardDescriptionLineEdit->setReadOnly(true);

        formLayout->setWidget(7, QFormLayout::FieldRole, ardDescriptionLineEdit);

        label_6 = new QLabel(arduinoEditForm);
        label_6->setObjectName(QStringLiteral("label_6"));

        formLayout->setWidget(8, QFormLayout::LabelRole, label_6);

        ardManufacturerLineEdit = new QLineEdit(arduinoEditForm);
        ardManufacturerLineEdit->setObjectName(QStringLiteral("ardManufacturerLineEdit"));
        ardManufacturerLineEdit->setEnabled(false);
        ardManufacturerLineEdit->setMinimumSize(QSize(250, 0));
        ardManufacturerLineEdit->setMaximumSize(QSize(350, 16777215));
        ardManufacturerLineEdit->setFrame(true);
        ardManufacturerLineEdit->setReadOnly(true);

        formLayout->setWidget(8, QFormLayout::FieldRole, ardManufacturerLineEdit);

        label_3 = new QLabel(arduinoEditForm);
        label_3->setObjectName(QStringLiteral("label_3"));

        formLayout->setWidget(2, QFormLayout::LabelRole, label_3);

        ardBaudComboBox = new QComboBox(arduinoEditForm);
        ardBaudComboBox->setObjectName(QStringLiteral("ardBaudComboBox"));
        ardBaudComboBox->setMaximumSize(QSize(150, 16777215));

        formLayout->setWidget(2, QFormLayout::FieldRole, ardBaudComboBox);


        horizontalLayoutEditPane->addWidget(arduinoEditForm);

        splitter->addWidget(editPaneWidget);

        gridLayout->addWidget(splitter, 0, 0, 1, 1);

        MainWindow->setCentralWidget(centralwidget);
        menubar = new QMenuBar(MainWindow);
        menubar->setObjectName(QStringLiteral("menubar"));
        menubar->setGeometry(QRect(0, 0, 1213, 21));
        menuFile = new QMenu(menubar);
        menuFile->setObjectName(QStringLiteral("menuFile"));
        menuArduino = new QMenu(menubar);
        menuArduino->setObjectName(QStringLiteral("menuArduino"));
        menuX_Plane = new QMenu(menubar);
        menuX_Plane->setObjectName(QStringLiteral("menuX_Plane"));
        MainWindow->setMenuBar(menubar);
        statusbar = new QStatusBar(MainWindow);
        statusbar->setObjectName(QStringLiteral("statusbar"));
        MainWindow->setStatusBar(statusbar);
        toolBar = new QToolBar(MainWindow);
        toolBar->setObjectName(QStringLiteral("toolBar"));
        MainWindow->addToolBar(Qt::TopToolBarArea, toolBar);

        menubar->addAction(menuFile->menuAction());
        menubar->addAction(menuArduino->menuAction());
        menubar->addAction(menuX_Plane->menuAction());
        menuFile->addAction(actionSave);
        menuFile->addAction(actionQuit);
        menuArduino->addAction(actionAdd_Arduino);
        menuArduino->addAction(actionAdd_component);
        menuX_Plane->addAction(actionUDP_Settings);
        toolBar->addAction(actionSave);

        retranslateUi(MainWindow);
        QObject::connect(arduinoTreeWidget, SIGNAL(customContextMenuRequested(QPoint)), MainWindow, SLOT(ardTreeContextMenuRequested()));
        QObject::connect(actionQuit, SIGNAL(triggered()), MainWindow, SLOT(close()));
        QObject::connect(actionSave, SIGNAL(triggered()), MainWindow, SLOT(saveToXML()));
        QObject::connect(actionAdd_Arduino, SIGNAL(triggered()), MainWindow, SLOT(pickArduino()));
        QObject::connect(arduinoTreeWidget, SIGNAL(itemSelectionChanged()), MainWindow, SLOT(ardTreeSelectionChanged()));
        QObject::connect(ardNameLineEdit, SIGNAL(editingFinished()), MainWindow, SLOT(ardEditingFinished()));
        QObject::connect(ardBaudComboBox, SIGNAL(currentIndexChanged(int)), MainWindow, SLOT(ardEditingFinished()));
        QObject::connect(actionUDP_Settings, SIGNAL(triggered()), MainWindow, SLOT(editXPUDPSettings()));

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QApplication::translate("MainWindow", "pyXPArduino", Q_NULLPTR));
        actionQuit->setText(QApplication::translate("MainWindow", "Quit", Q_NULLPTR));
        actionAdd_Arduino->setText(QApplication::translate("MainWindow", "Add Arduino", Q_NULLPTR));
        actionUDP_Settings->setText(QApplication::translate("MainWindow", "UDP Settings", Q_NULLPTR));
        actionAdd_component->setText(QApplication::translate("MainWindow", "Add component", Q_NULLPTR));
        actionSave->setText(QApplication::translate("MainWindow", "Save", Q_NULLPTR));
        actionSave->setShortcut(QApplication::translate("MainWindow", "Ctrl+S", Q_NULLPTR));
        QTreeWidgetItem *___qtreewidgetitem = arduinoTreeWidget->headerItem();
        ___qtreewidgetitem->setText(1, QApplication::translate("MainWindow", "Serial nr", Q_NULLPTR));
        ___qtreewidgetitem->setText(0, QApplication::translate("MainWindow", "Name", Q_NULLPTR));
        label_7->setText(QApplication::translate("MainWindow", "Edit Arduino Settings", Q_NULLPTR));
        label->setText(QApplication::translate("MainWindow", "Name", Q_NULLPTR));
        label_4->setText(QApplication::translate("MainWindow", "Port", Q_NULLPTR));
        label_5->setText(QApplication::translate("MainWindow", "Serial Number  ", Q_NULLPTR));
        label_2->setText(QApplication::translate("MainWindow", "Description", Q_NULLPTR));
        label_6->setText(QApplication::translate("MainWindow", "Manufacturer", Q_NULLPTR));
        label_3->setText(QApplication::translate("MainWindow", "Baud", Q_NULLPTR));
        menuFile->setTitle(QApplication::translate("MainWindow", "File", Q_NULLPTR));
        menuArduino->setTitle(QApplication::translate("MainWindow", "Arduino", Q_NULLPTR));
        menuX_Plane->setTitle(QApplication::translate("MainWindow", "X Plane", Q_NULLPTR));
        toolBar->setWindowTitle(QApplication::translate("MainWindow", "toolBar", Q_NULLPTR));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
