/********************************************************************************
** Form generated from reading UI file 'switchEditForm.ui'
**
** Created by: Qt User Interface Compiler version 5.8.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_SWITCHEDITFORM_H
#define UI_SWITCHEDITFORM_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QComboBox>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QSpacerItem>
#include <QtWidgets/QTableWidget>
#include <QtWidgets/QToolButton>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_switchEditForm
{
public:
    QGridLayout *gridLayout;
    QLabel *label_8;
    QLabel *label_17;
    QSpacerItem *verticalSpacer_2;
    QLabel *label_19;
    QLabel *label_9;
    QLabel *label_15;
    QLabel *label_3;
    QLabel *label_18;
    QSpacerItem *verticalSpacer;
    QComboBox *PIN_comboBox;
    QGridLayout *gridLayout_3;
    QTableWidget *SWON_CMDS_TABLE;
    QTableWidget *SWON_DREFS_TABLE;
    QHBoxLayout *horizontalLayout_4;
    QLabel *label_10;
    QToolButton *SWON_ADDCMD_BTN;
    QToolButton *SWON_RMCMD_BTN;
    QPushButton *testSWON_CMDS_button;
    QSpacerItem *horizontalSpacer;
    QHBoxLayout *horizontalLayout_5;
    QLabel *label_11;
    QToolButton *SWON_ADDDREF_BTN;
    QToolButton *SWON_RMDREF_BTN;
    QPushButton *testSWON_DREFS_button;
    QSpacerItem *horizontalSpacer_2;
    QGridLayout *gridLayout_4;
    QTableWidget *SWOFF_CMDS_TABLE;
    QTableWidget *SWOFF_DREFS_TABLE;
    QHBoxLayout *horizontalLayout_6;
    QLabel *label_12;
    QToolButton *SWOFF_ADDCMD_BTN;
    QToolButton *SWOFF_RMCMD_BTN;
    QPushButton *testSWOFF_CMDS_button;
    QSpacerItem *horizontalSpacer_3;
    QHBoxLayout *horizontalLayout_7;
    QLabel *label_14;
    QToolButton *SWOFF_ADDDREF_BTN;
    QToolButton *SWOFF_RMDREF_BTN;
    QPushButton *testSWOFF_DREFS_button;
    QSpacerItem *horizontalSpacer_4;
    QLineEdit *nameLineEdit;
    QLineEdit *IDlineEdit;
    QToolButton *switchStateButton;

    void setupUi(QWidget *switchEditForm)
    {
        if (switchEditForm->objectName().isEmpty())
            switchEditForm->setObjectName(QStringLiteral("switchEditForm"));
        switchEditForm->resize(832, 674);
        QSizePolicy sizePolicy(QSizePolicy::Expanding, QSizePolicy::Expanding);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(switchEditForm->sizePolicy().hasHeightForWidth());
        switchEditForm->setSizePolicy(sizePolicy);
        gridLayout = new QGridLayout(switchEditForm);
        gridLayout->setObjectName(QStringLiteral("gridLayout"));
        gridLayout->setSizeConstraint(QLayout::SetDefaultConstraint);
        label_8 = new QLabel(switchEditForm);
        label_8->setObjectName(QStringLiteral("label_8"));
        QFont font;
        font.setPointSize(10);
        font.setBold(true);
        font.setWeight(75);
        label_8->setFont(font);
        label_8->setStyleSheet(QLatin1String("color: white;\n"
"background: rgb(0, 151, 157);\n"
"padding: 3px\n"
""));

        gridLayout->addWidget(label_8, 0, 0, 1, 5);

        label_17 = new QLabel(switchEditForm);
        label_17->setObjectName(QStringLiteral("label_17"));

        gridLayout->addWidget(label_17, 1, 0, 1, 1);

        verticalSpacer_2 = new QSpacerItem(20, 10, QSizePolicy::Minimum, QSizePolicy::Fixed);

        gridLayout->addItem(verticalSpacer_2, 6, 0, 1, 1);

        label_19 = new QLabel(switchEditForm);
        label_19->setObjectName(QStringLiteral("label_19"));

        gridLayout->addWidget(label_19, 4, 0, 1, 1);

        label_9 = new QLabel(switchEditForm);
        label_9->setObjectName(QStringLiteral("label_9"));
        QFont font1;
        font1.setPointSize(9);
        font1.setBold(true);
        font1.setWeight(75);
        label_9->setFont(font1);

        gridLayout->addWidget(label_9, 7, 0, 1, 1);

        label_15 = new QLabel(switchEditForm);
        label_15->setObjectName(QStringLiteral("label_15"));
        label_15->setFont(font1);

        gridLayout->addWidget(label_15, 9, 0, 1, 1);

        label_3 = new QLabel(switchEditForm);
        label_3->setObjectName(QStringLiteral("label_3"));
        QSizePolicy sizePolicy1(QSizePolicy::Minimum, QSizePolicy::Minimum);
        sizePolicy1.setHorizontalStretch(0);
        sizePolicy1.setVerticalStretch(0);
        sizePolicy1.setHeightForWidth(label_3->sizePolicy().hasHeightForWidth());
        label_3->setSizePolicy(sizePolicy1);
        label_3->setLayoutDirection(Qt::LeftToRight);

        gridLayout->addWidget(label_3, 3, 0, 1, 1);

        label_18 = new QLabel(switchEditForm);
        label_18->setObjectName(QStringLiteral("label_18"));

        gridLayout->addWidget(label_18, 5, 0, 1, 1);

        verticalSpacer = new QSpacerItem(20, 26, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout->addItem(verticalSpacer, 12, 0, 1, 1);

        PIN_comboBox = new QComboBox(switchEditForm);
        PIN_comboBox->setObjectName(QStringLiteral("PIN_comboBox"));
        PIN_comboBox->setMaximumSize(QSize(50, 16777215));

        gridLayout->addWidget(PIN_comboBox, 5, 1, 1, 1);

        gridLayout_3 = new QGridLayout();
        gridLayout_3->setObjectName(QStringLiteral("gridLayout_3"));
        SWON_CMDS_TABLE = new QTableWidget(switchEditForm);
        if (SWON_CMDS_TABLE->columnCount() < 1)
            SWON_CMDS_TABLE->setColumnCount(1);
        QTableWidgetItem *__qtablewidgetitem = new QTableWidgetItem();
        SWON_CMDS_TABLE->setHorizontalHeaderItem(0, __qtablewidgetitem);
        SWON_CMDS_TABLE->setObjectName(QStringLiteral("SWON_CMDS_TABLE"));
        SWON_CMDS_TABLE->setMinimumSize(QSize(0, 75));

        gridLayout_3->addWidget(SWON_CMDS_TABLE, 4, 1, 1, 1);

        SWON_DREFS_TABLE = new QTableWidget(switchEditForm);
        if (SWON_DREFS_TABLE->columnCount() < 5)
            SWON_DREFS_TABLE->setColumnCount(5);
        QTableWidgetItem *__qtablewidgetitem1 = new QTableWidgetItem();
        SWON_DREFS_TABLE->setHorizontalHeaderItem(0, __qtablewidgetitem1);
        QTableWidgetItem *__qtablewidgetitem2 = new QTableWidgetItem();
        SWON_DREFS_TABLE->setHorizontalHeaderItem(1, __qtablewidgetitem2);
        QTableWidgetItem *__qtablewidgetitem3 = new QTableWidgetItem();
        SWON_DREFS_TABLE->setHorizontalHeaderItem(2, __qtablewidgetitem3);
        QTableWidgetItem *__qtablewidgetitem4 = new QTableWidgetItem();
        SWON_DREFS_TABLE->setHorizontalHeaderItem(3, __qtablewidgetitem4);
        QTableWidgetItem *__qtablewidgetitem5 = new QTableWidgetItem();
        SWON_DREFS_TABLE->setHorizontalHeaderItem(4, __qtablewidgetitem5);
        SWON_DREFS_TABLE->setObjectName(QStringLiteral("SWON_DREFS_TABLE"));

        gridLayout_3->addWidget(SWON_DREFS_TABLE, 4, 4, 1, 1);

        horizontalLayout_4 = new QHBoxLayout();
        horizontalLayout_4->setSpacing(2);
        horizontalLayout_4->setObjectName(QStringLiteral("horizontalLayout_4"));
        label_10 = new QLabel(switchEditForm);
        label_10->setObjectName(QStringLiteral("label_10"));
        QSizePolicy sizePolicy2(QSizePolicy::Fixed, QSizePolicy::Preferred);
        sizePolicy2.setHorizontalStretch(0);
        sizePolicy2.setVerticalStretch(0);
        sizePolicy2.setHeightForWidth(label_10->sizePolicy().hasHeightForWidth());
        label_10->setSizePolicy(sizePolicy2);

        horizontalLayout_4->addWidget(label_10);

        SWON_ADDCMD_BTN = new QToolButton(switchEditForm);
        SWON_ADDCMD_BTN->setObjectName(QStringLiteral("SWON_ADDCMD_BTN"));
        QIcon icon;
        icon.addFile(QStringLiteral(":/newPrefix/plusIcon.png"), QSize(), QIcon::Normal, QIcon::On);
        SWON_ADDCMD_BTN->setIcon(icon);
        SWON_ADDCMD_BTN->setAutoRaise(true);

        horizontalLayout_4->addWidget(SWON_ADDCMD_BTN);

        SWON_RMCMD_BTN = new QToolButton(switchEditForm);
        SWON_RMCMD_BTN->setObjectName(QStringLiteral("SWON_RMCMD_BTN"));
        QIcon icon1;
        icon1.addFile(QStringLiteral(":/newPrefix/minusIcon.png"), QSize(), QIcon::Normal, QIcon::Off);
        SWON_RMCMD_BTN->setIcon(icon1);
        SWON_RMCMD_BTN->setAutoRaise(true);

        horizontalLayout_4->addWidget(SWON_RMCMD_BTN);

        testSWON_CMDS_button = new QPushButton(switchEditForm);
        testSWON_CMDS_button->setObjectName(QStringLiteral("testSWON_CMDS_button"));

        horizontalLayout_4->addWidget(testSWON_CMDS_button);

        horizontalSpacer = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_4->addItem(horizontalSpacer);


        gridLayout_3->addLayout(horizontalLayout_4, 2, 1, 1, 1);

        horizontalLayout_5 = new QHBoxLayout();
        horizontalLayout_5->setObjectName(QStringLiteral("horizontalLayout_5"));
        label_11 = new QLabel(switchEditForm);
        label_11->setObjectName(QStringLiteral("label_11"));

        horizontalLayout_5->addWidget(label_11);

        SWON_ADDDREF_BTN = new QToolButton(switchEditForm);
        SWON_ADDDREF_BTN->setObjectName(QStringLiteral("SWON_ADDDREF_BTN"));
        QIcon icon2;
        icon2.addFile(QStringLiteral(":/newPrefix/plusIcon.png"), QSize(), QIcon::Normal, QIcon::Off);
        SWON_ADDDREF_BTN->setIcon(icon2);
        SWON_ADDDREF_BTN->setAutoRaise(true);

        horizontalLayout_5->addWidget(SWON_ADDDREF_BTN);

        SWON_RMDREF_BTN = new QToolButton(switchEditForm);
        SWON_RMDREF_BTN->setObjectName(QStringLiteral("SWON_RMDREF_BTN"));
        SWON_RMDREF_BTN->setIcon(icon1);
        SWON_RMDREF_BTN->setAutoRaise(true);

        horizontalLayout_5->addWidget(SWON_RMDREF_BTN);

        testSWON_DREFS_button = new QPushButton(switchEditForm);
        testSWON_DREFS_button->setObjectName(QStringLiteral("testSWON_DREFS_button"));

        horizontalLayout_5->addWidget(testSWON_DREFS_button);

        horizontalSpacer_2 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_5->addItem(horizontalSpacer_2);


        gridLayout_3->addLayout(horizontalLayout_5, 2, 4, 1, 1);


        gridLayout->addLayout(gridLayout_3, 8, 0, 1, 5);

        gridLayout_4 = new QGridLayout();
        gridLayout_4->setObjectName(QStringLiteral("gridLayout_4"));
        SWOFF_CMDS_TABLE = new QTableWidget(switchEditForm);
        if (SWOFF_CMDS_TABLE->columnCount() < 1)
            SWOFF_CMDS_TABLE->setColumnCount(1);
        QTableWidgetItem *__qtablewidgetitem6 = new QTableWidgetItem();
        SWOFF_CMDS_TABLE->setHorizontalHeaderItem(0, __qtablewidgetitem6);
        SWOFF_CMDS_TABLE->setObjectName(QStringLiteral("SWOFF_CMDS_TABLE"));

        gridLayout_4->addWidget(SWOFF_CMDS_TABLE, 6, 0, 1, 1);

        SWOFF_DREFS_TABLE = new QTableWidget(switchEditForm);
        if (SWOFF_DREFS_TABLE->columnCount() < 5)
            SWOFF_DREFS_TABLE->setColumnCount(5);
        QTableWidgetItem *__qtablewidgetitem7 = new QTableWidgetItem();
        SWOFF_DREFS_TABLE->setHorizontalHeaderItem(0, __qtablewidgetitem7);
        QTableWidgetItem *__qtablewidgetitem8 = new QTableWidgetItem();
        SWOFF_DREFS_TABLE->setHorizontalHeaderItem(1, __qtablewidgetitem8);
        QTableWidgetItem *__qtablewidgetitem9 = new QTableWidgetItem();
        SWOFF_DREFS_TABLE->setHorizontalHeaderItem(2, __qtablewidgetitem9);
        QTableWidgetItem *__qtablewidgetitem10 = new QTableWidgetItem();
        SWOFF_DREFS_TABLE->setHorizontalHeaderItem(3, __qtablewidgetitem10);
        QTableWidgetItem *__qtablewidgetitem11 = new QTableWidgetItem();
        SWOFF_DREFS_TABLE->setHorizontalHeaderItem(4, __qtablewidgetitem11);
        SWOFF_DREFS_TABLE->setObjectName(QStringLiteral("SWOFF_DREFS_TABLE"));

        gridLayout_4->addWidget(SWOFF_DREFS_TABLE, 6, 1, 1, 1);

        horizontalLayout_6 = new QHBoxLayout();
        horizontalLayout_6->setObjectName(QStringLiteral("horizontalLayout_6"));
        label_12 = new QLabel(switchEditForm);
        label_12->setObjectName(QStringLiteral("label_12"));

        horizontalLayout_6->addWidget(label_12);

        SWOFF_ADDCMD_BTN = new QToolButton(switchEditForm);
        SWOFF_ADDCMD_BTN->setObjectName(QStringLiteral("SWOFF_ADDCMD_BTN"));
        SWOFF_ADDCMD_BTN->setIcon(icon);
        SWOFF_ADDCMD_BTN->setAutoRaise(true);

        horizontalLayout_6->addWidget(SWOFF_ADDCMD_BTN);

        SWOFF_RMCMD_BTN = new QToolButton(switchEditForm);
        SWOFF_RMCMD_BTN->setObjectName(QStringLiteral("SWOFF_RMCMD_BTN"));
        QIcon icon3;
        icon3.addFile(QStringLiteral(":/newPrefix/minusIcon.png"), QSize(), QIcon::Normal, QIcon::On);
        SWOFF_RMCMD_BTN->setIcon(icon3);
        SWOFF_RMCMD_BTN->setAutoRaise(true);

        horizontalLayout_6->addWidget(SWOFF_RMCMD_BTN);

        testSWOFF_CMDS_button = new QPushButton(switchEditForm);
        testSWOFF_CMDS_button->setObjectName(QStringLiteral("testSWOFF_CMDS_button"));

        horizontalLayout_6->addWidget(testSWOFF_CMDS_button);

        horizontalSpacer_3 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_6->addItem(horizontalSpacer_3);


        gridLayout_4->addLayout(horizontalLayout_6, 3, 0, 1, 1);

        horizontalLayout_7 = new QHBoxLayout();
        horizontalLayout_7->setObjectName(QStringLiteral("horizontalLayout_7"));
        label_14 = new QLabel(switchEditForm);
        label_14->setObjectName(QStringLiteral("label_14"));

        horizontalLayout_7->addWidget(label_14);

        SWOFF_ADDDREF_BTN = new QToolButton(switchEditForm);
        SWOFF_ADDDREF_BTN->setObjectName(QStringLiteral("SWOFF_ADDDREF_BTN"));
        SWOFF_ADDDREF_BTN->setIcon(icon);
        SWOFF_ADDDREF_BTN->setAutoRaise(true);

        horizontalLayout_7->addWidget(SWOFF_ADDDREF_BTN);

        SWOFF_RMDREF_BTN = new QToolButton(switchEditForm);
        SWOFF_RMDREF_BTN->setObjectName(QStringLiteral("SWOFF_RMDREF_BTN"));
        SWOFF_RMDREF_BTN->setIcon(icon3);
        SWOFF_RMDREF_BTN->setAutoRaise(true);

        horizontalLayout_7->addWidget(SWOFF_RMDREF_BTN);

        testSWOFF_DREFS_button = new QPushButton(switchEditForm);
        testSWOFF_DREFS_button->setObjectName(QStringLiteral("testSWOFF_DREFS_button"));

        horizontalLayout_7->addWidget(testSWOFF_DREFS_button);

        horizontalSpacer_4 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_7->addItem(horizontalSpacer_4);


        gridLayout_4->addLayout(horizontalLayout_7, 3, 1, 1, 1);


        gridLayout->addLayout(gridLayout_4, 10, 0, 1, 5);

        nameLineEdit = new QLineEdit(switchEditForm);
        nameLineEdit->setObjectName(QStringLiteral("nameLineEdit"));
        nameLineEdit->setMinimumSize(QSize(250, 0));
        nameLineEdit->setMaximumSize(QSize(350, 16777215));

        gridLayout->addWidget(nameLineEdit, 3, 1, 1, 3);

        IDlineEdit = new QLineEdit(switchEditForm);
        IDlineEdit->setObjectName(QStringLiteral("IDlineEdit"));
        IDlineEdit->setEnabled(false);
        IDlineEdit->setMinimumSize(QSize(250, 0));
        IDlineEdit->setMaximumSize(QSize(350, 16777215));
        IDlineEdit->setReadOnly(true);

        gridLayout->addWidget(IDlineEdit, 4, 1, 1, 3);

        switchStateButton = new QToolButton(switchEditForm);
        switchStateButton->setObjectName(QStringLiteral("switchStateButton"));
        switchStateButton->setEnabled(false);
        switchStateButton->setStyleSheet(QStringLiteral("border: 0px;"));
        QIcon icon4;
        icon4.addFile(QStringLiteral(":/newPrefix/switch_off.png"), QSize(), QIcon::Normal, QIcon::Off);
        icon4.addFile(QStringLiteral(":/newPrefix/switch_on.png"), QSize(), QIcon::Normal, QIcon::On);
        icon4.addFile(QStringLiteral(":/newPrefix/switch_off.png"), QSize(), QIcon::Disabled, QIcon::Off);
        icon4.addFile(QStringLiteral(":/newPrefix/switch_on.png"), QSize(), QIcon::Disabled, QIcon::On);
        icon4.addFile(QStringLiteral(":/newPrefix/switch_off.png"), QSize(), QIcon::Active, QIcon::Off);
        icon4.addFile(QStringLiteral(":/newPrefix/switch_on.png"), QSize(), QIcon::Active, QIcon::On);
        icon4.addFile(QStringLiteral(":/newPrefix/switch_off.png"), QSize(), QIcon::Selected, QIcon::Off);
        icon4.addFile(QStringLiteral(":/newPrefix/switch_on.png"), QSize(), QIcon::Selected, QIcon::On);
        switchStateButton->setIcon(icon4);
        switchStateButton->setIconSize(QSize(66, 26));
        switchStateButton->setCheckable(true);
        switchStateButton->setAutoRaise(true);

        gridLayout->addWidget(switchStateButton, 1, 1, 1, 1);


        retranslateUi(switchEditForm);
        QObject::connect(SWON_ADDCMD_BTN, SIGNAL(clicked()), switchEditForm, SLOT(addSwitchOnCommand()));
        QObject::connect(SWON_RMCMD_BTN, SIGNAL(clicked()), switchEditForm, SLOT(rmSwitchOnCommand()));
        QObject::connect(SWON_ADDDREF_BTN, SIGNAL(clicked()), switchEditForm, SLOT(addSwitchOnDataref()));
        QObject::connect(SWON_RMDREF_BTN, SIGNAL(clicked()), switchEditForm, SLOT(rmSwitchOnDataref()));
        QObject::connect(SWOFF_ADDCMD_BTN, SIGNAL(clicked()), switchEditForm, SLOT(addSwitchOffCommand()));
        QObject::connect(SWOFF_RMCMD_BTN, SIGNAL(clicked()), switchEditForm, SLOT(rmSwitchOffCommand()));
        QObject::connect(SWOFF_ADDDREF_BTN, SIGNAL(clicked()), switchEditForm, SLOT(addSwitchOffDataref()));
        QObject::connect(SWOFF_RMDREF_BTN, SIGNAL(clicked()), switchEditForm, SLOT(rmSwitchOffDataref()));
        QObject::connect(SWON_CMDS_TABLE, SIGNAL(cellDoubleClicked(int,int)), switchEditForm, SLOT(editXPCommand()));
        QObject::connect(SWOFF_CMDS_TABLE, SIGNAL(cellDoubleClicked(int,int)), switchEditForm, SLOT(editXPCommand()));
        QObject::connect(nameLineEdit, SIGNAL(editingFinished()), switchEditForm, SLOT(updateXMLdata()));
        QObject::connect(PIN_comboBox, SIGNAL(currentIndexChanged(int)), switchEditForm, SLOT(updateXMLdata()));
        QObject::connect(SWON_CMDS_TABLE, SIGNAL(itemChanged(QTableWidgetItem*)), switchEditForm, SLOT(updateXMLdata()));
        QObject::connect(SWOFF_CMDS_TABLE, SIGNAL(itemChanged(QTableWidgetItem*)), switchEditForm, SLOT(updateXMLdata()));
        QObject::connect(testSWON_CMDS_button, SIGNAL(clicked()), switchEditForm, SLOT(testOnCommands()));
        QObject::connect(testSWOFF_CMDS_button, SIGNAL(clicked()), switchEditForm, SLOT(testOffCommands()));
        QObject::connect(PIN_comboBox, SIGNAL(currentTextChanged(QString)), switchEditForm, SLOT(updatePin()));
        QObject::connect(SWON_DREFS_TABLE, SIGNAL(cellDoubleClicked(int,int)), switchEditForm, SLOT(editXPDataref()));
        QObject::connect(SWOFF_DREFS_TABLE, SIGNAL(cellDoubleClicked(int,int)), switchEditForm, SLOT(editXPDataref()));
        QObject::connect(SWON_DREFS_TABLE, SIGNAL(itemChanged(QTableWidgetItem*)), switchEditForm, SLOT(updateXMLdata()));
        QObject::connect(SWOFF_DREFS_TABLE, SIGNAL(itemChanged(QTableWidgetItem*)), switchEditForm, SLOT(updateXMLdata()));
        QObject::connect(testSWOFF_DREFS_button, SIGNAL(clicked()), switchEditForm, SLOT(testOffDatarefs()));
        QObject::connect(testSWON_DREFS_button, SIGNAL(clicked()), switchEditForm, SLOT(testOnDatarefs()));
        QObject::connect(SWON_CMDS_TABLE, SIGNAL(cellChanged(int,int)), switchEditForm, SLOT(activateSave()));

        QMetaObject::connectSlotsByName(switchEditForm);
    } // setupUi

    void retranslateUi(QWidget *switchEditForm)
    {
        switchEditForm->setWindowTitle(QApplication::translate("switchEditForm", "Form", Q_NULLPTR));
        label_8->setText(QApplication::translate("switchEditForm", "Edit switch", Q_NULLPTR));
        label_17->setText(QApplication::translate("switchEditForm", "State", Q_NULLPTR));
        label_19->setText(QApplication::translate("switchEditForm", "ID", Q_NULLPTR));
        label_9->setText(QApplication::translate("switchEditForm", "Switch ON actions:", Q_NULLPTR));
        label_15->setText(QApplication::translate("switchEditForm", "Switch OFF actions", Q_NULLPTR));
        label_3->setText(QApplication::translate("switchEditForm", "Name", Q_NULLPTR));
        label_18->setText(QApplication::translate("switchEditForm", "Arduino pin:", Q_NULLPTR));
        QTableWidgetItem *___qtablewidgetitem = SWON_CMDS_TABLE->horizontalHeaderItem(0);
        ___qtablewidgetitem->setText(QApplication::translate("switchEditForm", "Command", Q_NULLPTR));
        QTableWidgetItem *___qtablewidgetitem1 = SWON_DREFS_TABLE->horizontalHeaderItem(0);
        ___qtablewidgetitem1->setText(QApplication::translate("switchEditForm", "Dataref", Q_NULLPTR));
        QTableWidgetItem *___qtablewidgetitem2 = SWON_DREFS_TABLE->horizontalHeaderItem(1);
        ___qtablewidgetitem2->setText(QApplication::translate("switchEditForm", "Index", Q_NULLPTR));
        QTableWidgetItem *___qtablewidgetitem3 = SWON_DREFS_TABLE->horizontalHeaderItem(2);
        ___qtablewidgetitem3->setText(QApplication::translate("switchEditForm", "Set to Value", Q_NULLPTR));
        QTableWidgetItem *___qtablewidgetitem4 = SWON_DREFS_TABLE->horizontalHeaderItem(3);
        ___qtablewidgetitem4->setText(QApplication::translate("switchEditForm", "Type", Q_NULLPTR));
        QTableWidgetItem *___qtablewidgetitem5 = SWON_DREFS_TABLE->horizontalHeaderItem(4);
        ___qtablewidgetitem5->setText(QApplication::translate("switchEditForm", "Unit", Q_NULLPTR));
        label_10->setText(QApplication::translate("switchEditForm", "Send XPlane Commands: ", Q_NULLPTR));
        SWON_ADDCMD_BTN->setText(QApplication::translate("switchEditForm", "...", Q_NULLPTR));
        SWON_RMCMD_BTN->setText(QApplication::translate("switchEditForm", "...", Q_NULLPTR));
        testSWON_CMDS_button->setText(QApplication::translate("switchEditForm", "Test", Q_NULLPTR));
        label_11->setText(QApplication::translate("switchEditForm", "Set Dataref: ", Q_NULLPTR));
        SWON_ADDDREF_BTN->setText(QApplication::translate("switchEditForm", "...", Q_NULLPTR));
        SWON_RMDREF_BTN->setText(QApplication::translate("switchEditForm", "...", Q_NULLPTR));
        testSWON_DREFS_button->setText(QApplication::translate("switchEditForm", "Test", Q_NULLPTR));
        QTableWidgetItem *___qtablewidgetitem6 = SWOFF_CMDS_TABLE->horizontalHeaderItem(0);
        ___qtablewidgetitem6->setText(QApplication::translate("switchEditForm", "Command", Q_NULLPTR));
        QTableWidgetItem *___qtablewidgetitem7 = SWOFF_DREFS_TABLE->horizontalHeaderItem(0);
        ___qtablewidgetitem7->setText(QApplication::translate("switchEditForm", "Dataref", Q_NULLPTR));
        QTableWidgetItem *___qtablewidgetitem8 = SWOFF_DREFS_TABLE->horizontalHeaderItem(1);
        ___qtablewidgetitem8->setText(QApplication::translate("switchEditForm", "Index", Q_NULLPTR));
        QTableWidgetItem *___qtablewidgetitem9 = SWOFF_DREFS_TABLE->horizontalHeaderItem(2);
        ___qtablewidgetitem9->setText(QApplication::translate("switchEditForm", "Set to Value", Q_NULLPTR));
        QTableWidgetItem *___qtablewidgetitem10 = SWOFF_DREFS_TABLE->horizontalHeaderItem(3);
        ___qtablewidgetitem10->setText(QApplication::translate("switchEditForm", "Type", Q_NULLPTR));
        QTableWidgetItem *___qtablewidgetitem11 = SWOFF_DREFS_TABLE->horizontalHeaderItem(4);
        ___qtablewidgetitem11->setText(QApplication::translate("switchEditForm", "Unit", Q_NULLPTR));
        label_12->setText(QApplication::translate("switchEditForm", "Send XPlane Command: ", Q_NULLPTR));
        SWOFF_ADDCMD_BTN->setText(QApplication::translate("switchEditForm", "...", Q_NULLPTR));
        SWOFF_RMCMD_BTN->setText(QApplication::translate("switchEditForm", "...", Q_NULLPTR));
        testSWOFF_CMDS_button->setText(QApplication::translate("switchEditForm", "Test", Q_NULLPTR));
        label_14->setText(QApplication::translate("switchEditForm", "Set Dataref:", Q_NULLPTR));
        SWOFF_ADDDREF_BTN->setText(QApplication::translate("switchEditForm", "...", Q_NULLPTR));
        SWOFF_RMDREF_BTN->setText(QApplication::translate("switchEditForm", "...", Q_NULLPTR));
        testSWOFF_DREFS_button->setText(QApplication::translate("switchEditForm", "Test", Q_NULLPTR));
        switchStateButton->setText(QApplication::translate("switchEditForm", "...", Q_NULLPTR));
    } // retranslateUi

};

namespace Ui {
    class switchEditForm: public Ui_switchEditForm {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_SWITCHEDITFORM_H
