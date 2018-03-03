/********************************************************************************
** Form generated from reading UI file 'rotencoderEditForm.ui'
**
** Created by: Qt User Interface Compiler version 5.10.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_ROTENCODEREDITFORM_H
#define UI_ROTENCODEREDITFORM_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QCheckBox>
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

class Ui_rotencoderEditForm
{
public:
    QGridLayout *gridLayout;
    QLabel *label_8;
    QLabel *label_3;
    QLabel *label_15;
    QLabel *label_19;
    QLabel *label_17;
    QSpacerItem *verticalSpacer_2;
    QLabel *label_18;
    QComboBox *PINA_comboBox;
    QLabel *label_9;
    QSpacerItem *verticalSpacer;
    QGridLayout *gridLayout_3;
    QTableWidget *UP_CMDS_TABLE;
    QTableWidget *UP_DREFS_TABLE;
    QHBoxLayout *horizontalLayout_4;
    QLabel *label_10;
    QToolButton *UP_ADDCMD_BTN;
    QToolButton *UP_RMCMD_BTN;
    QPushButton *testUP_CMDS_button;
    QSpacerItem *horizontalSpacer;
    QHBoxLayout *horizontalLayout_5;
    QLabel *label_11;
    QToolButton *UP_ADDDREF_BTN;
    QToolButton *UP_RMDREF_BTN;
    QPushButton *testUPON_DREFS_button;
    QSpacerItem *horizontalSpacer_2;
    QGridLayout *gridLayout_4;
    QTableWidget *DOWN_CMDS_TABLE;
    QTableWidget *DOWN_DREFS_TABLE;
    QHBoxLayout *horizontalLayout_6;
    QLabel *label_12;
    QToolButton *DOWN_ADDCMD_BTN;
    QToolButton *DOWN_RMCMD_BTN;
    QPushButton *testDOWN_CMDS_button;
    QSpacerItem *horizontalSpacer_3;
    QHBoxLayout *horizontalLayout_7;
    QLabel *label_14;
    QToolButton *DOWN_ADDDREF_BTN;
    QToolButton *DOWN_RMDREF_BTN;
    QPushButton *testDOWN_DREFS_button;
    QSpacerItem *horizontalSpacer_4;
    QComboBox *PINB_comboBox;
    QLineEdit *nameLineEdit;
    QLabel *label;
    QToolButton *switchStateButton;
    QLineEdit *IDlineEdit;
    QComboBox *steps_comboBox;
    QLabel *label_2;
    QCheckBox *acceleration_checkBox;
    QLabel *label_4;
    QLabel *label_5;
    QLineEdit *multiplierLineEdit;

    void setupUi(QWidget *rotencoderEditForm)
    {
        if (rotencoderEditForm->objectName().isEmpty())
            rotencoderEditForm->setObjectName(QStringLiteral("rotencoderEditForm"));
        rotencoderEditForm->resize(832, 674);
        QSizePolicy sizePolicy(QSizePolicy::Expanding, QSizePolicy::Expanding);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(rotencoderEditForm->sizePolicy().hasHeightForWidth());
        rotencoderEditForm->setSizePolicy(sizePolicy);
        gridLayout = new QGridLayout(rotencoderEditForm);
        gridLayout->setObjectName(QStringLiteral("gridLayout"));
        gridLayout->setSizeConstraint(QLayout::SetDefaultConstraint);
        label_8 = new QLabel(rotencoderEditForm);
        label_8->setObjectName(QStringLiteral("label_8"));
        QFont font;
        font.setPointSize(11);
        font.setBold(true);
        font.setWeight(75);
        label_8->setFont(font);
        label_8->setStyleSheet(QLatin1String("color: white;\n"
"background: rgb(0, 151, 157);\n"
"padding: 3px\n"
""));

        gridLayout->addWidget(label_8, 0, 0, 1, 5);

        label_3 = new QLabel(rotencoderEditForm);
        label_3->setObjectName(QStringLiteral("label_3"));
        QSizePolicy sizePolicy1(QSizePolicy::Minimum, QSizePolicy::Minimum);
        sizePolicy1.setHorizontalStretch(0);
        sizePolicy1.setVerticalStretch(0);
        sizePolicy1.setHeightForWidth(label_3->sizePolicy().hasHeightForWidth());
        label_3->setSizePolicy(sizePolicy1);
        label_3->setMaximumSize(QSize(110, 16777215));
        label_3->setLayoutDirection(Qt::LeftToRight);

        gridLayout->addWidget(label_3, 3, 0, 1, 1);

        label_15 = new QLabel(rotencoderEditForm);
        label_15->setObjectName(QStringLiteral("label_15"));
        label_15->setFont(font);

        gridLayout->addWidget(label_15, 12, 0, 1, 1);

        label_19 = new QLabel(rotencoderEditForm);
        label_19->setObjectName(QStringLiteral("label_19"));
        label_19->setMaximumSize(QSize(110, 16777215));

        gridLayout->addWidget(label_19, 4, 0, 1, 1);

        label_17 = new QLabel(rotencoderEditForm);
        label_17->setObjectName(QStringLiteral("label_17"));
        label_17->setMaximumSize(QSize(110, 16777215));

        gridLayout->addWidget(label_17, 1, 0, 1, 1);

        verticalSpacer_2 = new QSpacerItem(20, 10, QSizePolicy::Minimum, QSizePolicy::Fixed);

        gridLayout->addItem(verticalSpacer_2, 9, 0, 1, 1);

        label_18 = new QLabel(rotencoderEditForm);
        label_18->setObjectName(QStringLiteral("label_18"));
        label_18->setMaximumSize(QSize(110, 16777215));

        gridLayout->addWidget(label_18, 5, 0, 1, 1);

        PINA_comboBox = new QComboBox(rotencoderEditForm);
        PINA_comboBox->setObjectName(QStringLiteral("PINA_comboBox"));
        PINA_comboBox->setMaximumSize(QSize(50, 16777215));

        gridLayout->addWidget(PINA_comboBox, 5, 1, 1, 1);

        label_9 = new QLabel(rotencoderEditForm);
        label_9->setObjectName(QStringLiteral("label_9"));
        label_9->setFont(font);

        gridLayout->addWidget(label_9, 10, 0, 1, 1);

        verticalSpacer = new QSpacerItem(20, 26, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout->addItem(verticalSpacer, 15, 0, 1, 1);

        gridLayout_3 = new QGridLayout();
        gridLayout_3->setObjectName(QStringLiteral("gridLayout_3"));
        UP_CMDS_TABLE = new QTableWidget(rotencoderEditForm);
        if (UP_CMDS_TABLE->columnCount() < 3)
            UP_CMDS_TABLE->setColumnCount(3);
        QTableWidgetItem *__qtablewidgetitem = new QTableWidgetItem();
        UP_CMDS_TABLE->setHorizontalHeaderItem(0, __qtablewidgetitem);
        QTableWidgetItem *__qtablewidgetitem1 = new QTableWidgetItem();
        UP_CMDS_TABLE->setHorizontalHeaderItem(1, __qtablewidgetitem1);
        QTableWidgetItem *__qtablewidgetitem2 = new QTableWidgetItem();
        UP_CMDS_TABLE->setHorizontalHeaderItem(2, __qtablewidgetitem2);
        UP_CMDS_TABLE->setObjectName(QStringLiteral("UP_CMDS_TABLE"));
        UP_CMDS_TABLE->setMinimumSize(QSize(0, 75));

        gridLayout_3->addWidget(UP_CMDS_TABLE, 4, 1, 1, 1);

        UP_DREFS_TABLE = new QTableWidget(rotencoderEditForm);
        if (UP_DREFS_TABLE->columnCount() < 6)
            UP_DREFS_TABLE->setColumnCount(6);
        QTableWidgetItem *__qtablewidgetitem3 = new QTableWidgetItem();
        UP_DREFS_TABLE->setHorizontalHeaderItem(0, __qtablewidgetitem3);
        QTableWidgetItem *__qtablewidgetitem4 = new QTableWidgetItem();
        UP_DREFS_TABLE->setHorizontalHeaderItem(1, __qtablewidgetitem4);
        QTableWidgetItem *__qtablewidgetitem5 = new QTableWidgetItem();
        UP_DREFS_TABLE->setHorizontalHeaderItem(2, __qtablewidgetitem5);
        QTableWidgetItem *__qtablewidgetitem6 = new QTableWidgetItem();
        UP_DREFS_TABLE->setHorizontalHeaderItem(3, __qtablewidgetitem6);
        QTableWidgetItem *__qtablewidgetitem7 = new QTableWidgetItem();
        UP_DREFS_TABLE->setHorizontalHeaderItem(4, __qtablewidgetitem7);
        QTableWidgetItem *__qtablewidgetitem8 = new QTableWidgetItem();
        UP_DREFS_TABLE->setHorizontalHeaderItem(5, __qtablewidgetitem8);
        UP_DREFS_TABLE->setObjectName(QStringLiteral("UP_DREFS_TABLE"));
        UP_DREFS_TABLE->setEnabled(false);

        gridLayout_3->addWidget(UP_DREFS_TABLE, 4, 4, 1, 1);

        horizontalLayout_4 = new QHBoxLayout();
        horizontalLayout_4->setSpacing(2);
        horizontalLayout_4->setObjectName(QStringLiteral("horizontalLayout_4"));
        label_10 = new QLabel(rotencoderEditForm);
        label_10->setObjectName(QStringLiteral("label_10"));
        QSizePolicy sizePolicy2(QSizePolicy::Fixed, QSizePolicy::Preferred);
        sizePolicy2.setHorizontalStretch(0);
        sizePolicy2.setVerticalStretch(0);
        sizePolicy2.setHeightForWidth(label_10->sizePolicy().hasHeightForWidth());
        label_10->setSizePolicy(sizePolicy2);

        horizontalLayout_4->addWidget(label_10);

        UP_ADDCMD_BTN = new QToolButton(rotencoderEditForm);
        UP_ADDCMD_BTN->setObjectName(QStringLiteral("UP_ADDCMD_BTN"));
        QIcon icon;
        icon.addFile(QStringLiteral(":/newPrefix/plusIcon.png"), QSize(), QIcon::Normal, QIcon::On);
        UP_ADDCMD_BTN->setIcon(icon);
        UP_ADDCMD_BTN->setAutoRaise(true);

        horizontalLayout_4->addWidget(UP_ADDCMD_BTN);

        UP_RMCMD_BTN = new QToolButton(rotencoderEditForm);
        UP_RMCMD_BTN->setObjectName(QStringLiteral("UP_RMCMD_BTN"));
        QIcon icon1;
        icon1.addFile(QStringLiteral(":/newPrefix/minusIcon.png"), QSize(), QIcon::Normal, QIcon::Off);
        UP_RMCMD_BTN->setIcon(icon1);
        UP_RMCMD_BTN->setAutoRaise(true);

        horizontalLayout_4->addWidget(UP_RMCMD_BTN);

        testUP_CMDS_button = new QPushButton(rotencoderEditForm);
        testUP_CMDS_button->setObjectName(QStringLiteral("testUP_CMDS_button"));

        horizontalLayout_4->addWidget(testUP_CMDS_button);

        horizontalSpacer = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_4->addItem(horizontalSpacer);


        gridLayout_3->addLayout(horizontalLayout_4, 2, 1, 1, 1);

        horizontalLayout_5 = new QHBoxLayout();
        horizontalLayout_5->setObjectName(QStringLiteral("horizontalLayout_5"));
        label_11 = new QLabel(rotencoderEditForm);
        label_11->setObjectName(QStringLiteral("label_11"));

        horizontalLayout_5->addWidget(label_11);

        UP_ADDDREF_BTN = new QToolButton(rotencoderEditForm);
        UP_ADDDREF_BTN->setObjectName(QStringLiteral("UP_ADDDREF_BTN"));
        UP_ADDDREF_BTN->setEnabled(false);
        QIcon icon2;
        icon2.addFile(QStringLiteral(":/newPrefix/plusIcon.png"), QSize(), QIcon::Normal, QIcon::Off);
        UP_ADDDREF_BTN->setIcon(icon2);
        UP_ADDDREF_BTN->setAutoRaise(true);

        horizontalLayout_5->addWidget(UP_ADDDREF_BTN);

        UP_RMDREF_BTN = new QToolButton(rotencoderEditForm);
        UP_RMDREF_BTN->setObjectName(QStringLiteral("UP_RMDREF_BTN"));
        UP_RMDREF_BTN->setEnabled(false);
        UP_RMDREF_BTN->setIcon(icon1);
        UP_RMDREF_BTN->setAutoRaise(true);

        horizontalLayout_5->addWidget(UP_RMDREF_BTN);

        testUPON_DREFS_button = new QPushButton(rotencoderEditForm);
        testUPON_DREFS_button->setObjectName(QStringLiteral("testUPON_DREFS_button"));
        testUPON_DREFS_button->setEnabled(false);

        horizontalLayout_5->addWidget(testUPON_DREFS_button);

        horizontalSpacer_2 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_5->addItem(horizontalSpacer_2);


        gridLayout_3->addLayout(horizontalLayout_5, 2, 4, 1, 1);


        gridLayout->addLayout(gridLayout_3, 11, 0, 1, 5);

        gridLayout_4 = new QGridLayout();
        gridLayout_4->setObjectName(QStringLiteral("gridLayout_4"));
        DOWN_CMDS_TABLE = new QTableWidget(rotencoderEditForm);
        if (DOWN_CMDS_TABLE->columnCount() < 3)
            DOWN_CMDS_TABLE->setColumnCount(3);
        QTableWidgetItem *__qtablewidgetitem9 = new QTableWidgetItem();
        DOWN_CMDS_TABLE->setHorizontalHeaderItem(0, __qtablewidgetitem9);
        QTableWidgetItem *__qtablewidgetitem10 = new QTableWidgetItem();
        DOWN_CMDS_TABLE->setHorizontalHeaderItem(1, __qtablewidgetitem10);
        QTableWidgetItem *__qtablewidgetitem11 = new QTableWidgetItem();
        DOWN_CMDS_TABLE->setHorizontalHeaderItem(2, __qtablewidgetitem11);
        DOWN_CMDS_TABLE->setObjectName(QStringLiteral("DOWN_CMDS_TABLE"));

        gridLayout_4->addWidget(DOWN_CMDS_TABLE, 6, 0, 1, 1);

        DOWN_DREFS_TABLE = new QTableWidget(rotencoderEditForm);
        if (DOWN_DREFS_TABLE->columnCount() < 6)
            DOWN_DREFS_TABLE->setColumnCount(6);
        QTableWidgetItem *__qtablewidgetitem12 = new QTableWidgetItem();
        DOWN_DREFS_TABLE->setHorizontalHeaderItem(0, __qtablewidgetitem12);
        QTableWidgetItem *__qtablewidgetitem13 = new QTableWidgetItem();
        DOWN_DREFS_TABLE->setHorizontalHeaderItem(1, __qtablewidgetitem13);
        QTableWidgetItem *__qtablewidgetitem14 = new QTableWidgetItem();
        DOWN_DREFS_TABLE->setHorizontalHeaderItem(2, __qtablewidgetitem14);
        QTableWidgetItem *__qtablewidgetitem15 = new QTableWidgetItem();
        DOWN_DREFS_TABLE->setHorizontalHeaderItem(3, __qtablewidgetitem15);
        QTableWidgetItem *__qtablewidgetitem16 = new QTableWidgetItem();
        DOWN_DREFS_TABLE->setHorizontalHeaderItem(4, __qtablewidgetitem16);
        QTableWidgetItem *__qtablewidgetitem17 = new QTableWidgetItem();
        DOWN_DREFS_TABLE->setHorizontalHeaderItem(5, __qtablewidgetitem17);
        DOWN_DREFS_TABLE->setObjectName(QStringLiteral("DOWN_DREFS_TABLE"));
        DOWN_DREFS_TABLE->setEnabled(false);

        gridLayout_4->addWidget(DOWN_DREFS_TABLE, 6, 1, 1, 1);

        horizontalLayout_6 = new QHBoxLayout();
        horizontalLayout_6->setObjectName(QStringLiteral("horizontalLayout_6"));
        label_12 = new QLabel(rotencoderEditForm);
        label_12->setObjectName(QStringLiteral("label_12"));

        horizontalLayout_6->addWidget(label_12);

        DOWN_ADDCMD_BTN = new QToolButton(rotencoderEditForm);
        DOWN_ADDCMD_BTN->setObjectName(QStringLiteral("DOWN_ADDCMD_BTN"));
        DOWN_ADDCMD_BTN->setIcon(icon);
        DOWN_ADDCMD_BTN->setAutoRaise(true);

        horizontalLayout_6->addWidget(DOWN_ADDCMD_BTN);

        DOWN_RMCMD_BTN = new QToolButton(rotencoderEditForm);
        DOWN_RMCMD_BTN->setObjectName(QStringLiteral("DOWN_RMCMD_BTN"));
        QIcon icon3;
        icon3.addFile(QStringLiteral(":/newPrefix/minusIcon.png"), QSize(), QIcon::Normal, QIcon::On);
        DOWN_RMCMD_BTN->setIcon(icon3);
        DOWN_RMCMD_BTN->setAutoRaise(true);

        horizontalLayout_6->addWidget(DOWN_RMCMD_BTN);

        testDOWN_CMDS_button = new QPushButton(rotencoderEditForm);
        testDOWN_CMDS_button->setObjectName(QStringLiteral("testDOWN_CMDS_button"));

        horizontalLayout_6->addWidget(testDOWN_CMDS_button);

        horizontalSpacer_3 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_6->addItem(horizontalSpacer_3);


        gridLayout_4->addLayout(horizontalLayout_6, 3, 0, 1, 1);

        horizontalLayout_7 = new QHBoxLayout();
        horizontalLayout_7->setObjectName(QStringLiteral("horizontalLayout_7"));
        label_14 = new QLabel(rotencoderEditForm);
        label_14->setObjectName(QStringLiteral("label_14"));

        horizontalLayout_7->addWidget(label_14);

        DOWN_ADDDREF_BTN = new QToolButton(rotencoderEditForm);
        DOWN_ADDDREF_BTN->setObjectName(QStringLiteral("DOWN_ADDDREF_BTN"));
        DOWN_ADDDREF_BTN->setEnabled(false);
        DOWN_ADDDREF_BTN->setIcon(icon);
        DOWN_ADDDREF_BTN->setAutoRaise(true);

        horizontalLayout_7->addWidget(DOWN_ADDDREF_BTN);

        DOWN_RMDREF_BTN = new QToolButton(rotencoderEditForm);
        DOWN_RMDREF_BTN->setObjectName(QStringLiteral("DOWN_RMDREF_BTN"));
        DOWN_RMDREF_BTN->setEnabled(false);
        DOWN_RMDREF_BTN->setIcon(icon3);
        DOWN_RMDREF_BTN->setAutoRaise(true);

        horizontalLayout_7->addWidget(DOWN_RMDREF_BTN);

        testDOWN_DREFS_button = new QPushButton(rotencoderEditForm);
        testDOWN_DREFS_button->setObjectName(QStringLiteral("testDOWN_DREFS_button"));
        testDOWN_DREFS_button->setEnabled(false);

        horizontalLayout_7->addWidget(testDOWN_DREFS_button);

        horizontalSpacer_4 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_7->addItem(horizontalSpacer_4);


        gridLayout_4->addLayout(horizontalLayout_7, 3, 1, 1, 1);


        gridLayout->addLayout(gridLayout_4, 13, 0, 1, 5);

        PINB_comboBox = new QComboBox(rotencoderEditForm);
        PINB_comboBox->setObjectName(QStringLiteral("PINB_comboBox"));
        PINB_comboBox->setMaximumSize(QSize(50, 16777215));

        gridLayout->addWidget(PINB_comboBox, 7, 1, 1, 1);

        nameLineEdit = new QLineEdit(rotencoderEditForm);
        nameLineEdit->setObjectName(QStringLiteral("nameLineEdit"));
        nameLineEdit->setMinimumSize(QSize(250, 0));
        nameLineEdit->setMaximumSize(QSize(350, 16777215));

        gridLayout->addWidget(nameLineEdit, 3, 1, 1, 3);

        label = new QLabel(rotencoderEditForm);
        label->setObjectName(QStringLiteral("label"));
        label->setMaximumSize(QSize(110, 16777215));

        gridLayout->addWidget(label, 7, 0, 1, 1);

        switchStateButton = new QToolButton(rotencoderEditForm);
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

        IDlineEdit = new QLineEdit(rotencoderEditForm);
        IDlineEdit->setObjectName(QStringLiteral("IDlineEdit"));
        IDlineEdit->setEnabled(false);
        IDlineEdit->setMinimumSize(QSize(250, 0));
        IDlineEdit->setMaximumSize(QSize(350, 16777215));
        IDlineEdit->setReadOnly(true);

        gridLayout->addWidget(IDlineEdit, 4, 1, 1, 3);

        steps_comboBox = new QComboBox(rotencoderEditForm);
        steps_comboBox->setObjectName(QStringLiteral("steps_comboBox"));
        steps_comboBox->setMaximumSize(QSize(50, 16777215));

        gridLayout->addWidget(steps_comboBox, 5, 3, 1, 1);

        label_2 = new QLabel(rotencoderEditForm);
        label_2->setObjectName(QStringLiteral("label_2"));
        label_2->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);

        gridLayout->addWidget(label_2, 5, 2, 1, 1);

        acceleration_checkBox = new QCheckBox(rotencoderEditForm);
        acceleration_checkBox->setObjectName(QStringLiteral("acceleration_checkBox"));

        gridLayout->addWidget(acceleration_checkBox, 7, 3, 1, 1);

        label_4 = new QLabel(rotencoderEditForm);
        label_4->setObjectName(QStringLiteral("label_4"));
        label_4->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);

        gridLayout->addWidget(label_4, 7, 2, 1, 1);

        label_5 = new QLabel(rotencoderEditForm);
        label_5->setObjectName(QStringLiteral("label_5"));
        label_5->setMaximumSize(QSize(110, 16777215));

        gridLayout->addWidget(label_5, 8, 0, 1, 1);

        multiplierLineEdit = new QLineEdit(rotencoderEditForm);
        multiplierLineEdit->setObjectName(QStringLiteral("multiplierLineEdit"));
        multiplierLineEdit->setMaximumSize(QSize(50, 16777215));

        gridLayout->addWidget(multiplierLineEdit, 8, 1, 1, 1);


        retranslateUi(rotencoderEditForm);
        QObject::connect(UP_ADDCMD_BTN, SIGNAL(clicked()), rotencoderEditForm, SLOT(addRotencUpCommand()));
        QObject::connect(UP_RMCMD_BTN, SIGNAL(clicked()), rotencoderEditForm, SLOT(rmRotencUpCommand()));
        QObject::connect(UP_ADDDREF_BTN, SIGNAL(clicked()), rotencoderEditForm, SLOT(addRotencUpDataref()));
        QObject::connect(UP_RMDREF_BTN, SIGNAL(clicked()), rotencoderEditForm, SLOT(rmRotencUpDataref()));
        QObject::connect(DOWN_ADDCMD_BTN, SIGNAL(clicked()), rotencoderEditForm, SLOT(addRotencDownCommand()));
        QObject::connect(DOWN_RMCMD_BTN, SIGNAL(clicked()), rotencoderEditForm, SLOT(rmRotencDownCommand()));
        QObject::connect(DOWN_ADDDREF_BTN, SIGNAL(clicked()), rotencoderEditForm, SLOT(addRotencDownDataref()));
        QObject::connect(DOWN_RMDREF_BTN, SIGNAL(clicked()), rotencoderEditForm, SLOT(rmRotencDownDataref()));
        QObject::connect(UP_CMDS_TABLE, SIGNAL(cellDoubleClicked(int,int)), rotencoderEditForm, SLOT(editXPCommand()));
        QObject::connect(DOWN_CMDS_TABLE, SIGNAL(cellDoubleClicked(int,int)), rotencoderEditForm, SLOT(editXPCommand()));
        QObject::connect(nameLineEdit, SIGNAL(editingFinished()), rotencoderEditForm, SLOT(updateXMLdata()));
        QObject::connect(PINA_comboBox, SIGNAL(currentIndexChanged(int)), rotencoderEditForm, SLOT(updateXMLdata()));
        QObject::connect(UP_CMDS_TABLE, SIGNAL(itemChanged(QTableWidgetItem*)), rotencoderEditForm, SLOT(updateXMLdata()));
        QObject::connect(DOWN_CMDS_TABLE, SIGNAL(itemChanged(QTableWidgetItem*)), rotencoderEditForm, SLOT(updateXMLdata()));
        QObject::connect(testUP_CMDS_button, SIGNAL(clicked()), rotencoderEditForm, SLOT(testOnCommands()));
        QObject::connect(testDOWN_CMDS_button, SIGNAL(clicked()), rotencoderEditForm, SLOT(testOffCommands()));
        QObject::connect(PINA_comboBox, SIGNAL(currentTextChanged(QString)), rotencoderEditForm, SLOT(updatePin()));
        QObject::connect(UP_DREFS_TABLE, SIGNAL(cellDoubleClicked(int,int)), rotencoderEditForm, SLOT(editXPDataref()));
        QObject::connect(DOWN_DREFS_TABLE, SIGNAL(cellDoubleClicked(int,int)), rotencoderEditForm, SLOT(editXPDataref()));
        QObject::connect(UP_DREFS_TABLE, SIGNAL(itemChanged(QTableWidgetItem*)), rotencoderEditForm, SLOT(updateXMLdata()));
        QObject::connect(DOWN_DREFS_TABLE, SIGNAL(itemChanged(QTableWidgetItem*)), rotencoderEditForm, SLOT(updateXMLdata()));
        QObject::connect(testDOWN_DREFS_button, SIGNAL(clicked()), rotencoderEditForm, SLOT(testOffDatarefs()));
        QObject::connect(testUPON_DREFS_button, SIGNAL(clicked()), rotencoderEditForm, SLOT(testOnDatarefs()));
        QObject::connect(UP_CMDS_TABLE, SIGNAL(cellChanged(int,int)), rotencoderEditForm, SLOT(activateSave()));
        QObject::connect(PINB_comboBox, SIGNAL(currentIndexChanged(int)), rotencoderEditForm, SLOT(updateXMLdata()));
        QObject::connect(PINB_comboBox, SIGNAL(currentTextChanged(QString)), rotencoderEditForm, SLOT(updatePin()));
        QObject::connect(steps_comboBox, SIGNAL(currentIndexChanged(QString)), rotencoderEditForm, SLOT(updateXMLdata()));
        QObject::connect(steps_comboBox, SIGNAL(currentTextChanged(QString)), rotencoderEditForm, SLOT(updatePin()));
        QObject::connect(multiplierLineEdit, SIGNAL(editingFinished()), rotencoderEditForm, SLOT(updateXMLdata()));
        QObject::connect(acceleration_checkBox, SIGNAL(stateChanged(int)), rotencoderEditForm, SLOT(updateXMLdata()));

        QMetaObject::connectSlotsByName(rotencoderEditForm);
    } // setupUi

    void retranslateUi(QWidget *rotencoderEditForm)
    {
        rotencoderEditForm->setWindowTitle(QApplication::translate("rotencoderEditForm", "Form", nullptr));
        label_8->setText(QApplication::translate("rotencoderEditForm", "Edit rotary encoder", nullptr));
        label_3->setText(QApplication::translate("rotencoderEditForm", "Name", nullptr));
        label_15->setText(QApplication::translate("rotencoderEditForm", "Rotary encoder DOWN actions", nullptr));
        label_19->setText(QApplication::translate("rotencoderEditForm", "ID", nullptr));
        label_17->setText(QApplication::translate("rotencoderEditForm", "State", nullptr));
        label_18->setText(QApplication::translate("rotencoderEditForm", "Arduino pin A:", nullptr));
        label_9->setText(QApplication::translate("rotencoderEditForm", "Rotary encoder UP actions:", nullptr));
        QTableWidgetItem *___qtablewidgetitem = UP_CMDS_TABLE->horizontalHeaderItem(0);
        ___qtablewidgetitem->setText(QApplication::translate("rotencoderEditForm", "Command", nullptr));
        QTableWidgetItem *___qtablewidgetitem1 = UP_CMDS_TABLE->horizontalHeaderItem(1);
        ___qtablewidgetitem1->setText(QApplication::translate("rotencoderEditForm", "Send continuously", nullptr));
        QTableWidgetItem *___qtablewidgetitem2 = UP_CMDS_TABLE->horizontalHeaderItem(2);
        ___qtablewidgetitem2->setText(QApplication::translate("rotencoderEditForm", "Nr times send per step", nullptr));
        QTableWidgetItem *___qtablewidgetitem3 = UP_DREFS_TABLE->horizontalHeaderItem(0);
        ___qtablewidgetitem3->setText(QApplication::translate("rotencoderEditForm", "Dataref", nullptr));
        QTableWidgetItem *___qtablewidgetitem4 = UP_DREFS_TABLE->horizontalHeaderItem(1);
        ___qtablewidgetitem4->setText(QApplication::translate("rotencoderEditForm", "Index", nullptr));
        QTableWidgetItem *___qtablewidgetitem5 = UP_DREFS_TABLE->horizontalHeaderItem(2);
        ___qtablewidgetitem5->setText(QApplication::translate("rotencoderEditForm", "Set to Value", nullptr));
        QTableWidgetItem *___qtablewidgetitem6 = UP_DREFS_TABLE->horizontalHeaderItem(3);
        ___qtablewidgetitem6->setText(QApplication::translate("rotencoderEditForm", "Set continuously", nullptr));
        QTableWidgetItem *___qtablewidgetitem7 = UP_DREFS_TABLE->horizontalHeaderItem(4);
        ___qtablewidgetitem7->setText(QApplication::translate("rotencoderEditForm", "Type", nullptr));
        QTableWidgetItem *___qtablewidgetitem8 = UP_DREFS_TABLE->horizontalHeaderItem(5);
        ___qtablewidgetitem8->setText(QApplication::translate("rotencoderEditForm", "Unit", nullptr));
        label_10->setText(QApplication::translate("rotencoderEditForm", "Send XPlane Commands: ", nullptr));
        UP_ADDCMD_BTN->setText(QApplication::translate("rotencoderEditForm", "...", nullptr));
        UP_RMCMD_BTN->setText(QApplication::translate("rotencoderEditForm", "...", nullptr));
        testUP_CMDS_button->setText(QApplication::translate("rotencoderEditForm", "Test", nullptr));
        label_11->setText(QApplication::translate("rotencoderEditForm", "Set Dataref: ", nullptr));
        UP_ADDDREF_BTN->setText(QApplication::translate("rotencoderEditForm", "...", nullptr));
        UP_RMDREF_BTN->setText(QApplication::translate("rotencoderEditForm", "...", nullptr));
        testUPON_DREFS_button->setText(QApplication::translate("rotencoderEditForm", "Test", nullptr));
        QTableWidgetItem *___qtablewidgetitem9 = DOWN_CMDS_TABLE->horizontalHeaderItem(0);
        ___qtablewidgetitem9->setText(QApplication::translate("rotencoderEditForm", "Command", nullptr));
        QTableWidgetItem *___qtablewidgetitem10 = DOWN_CMDS_TABLE->horizontalHeaderItem(1);
        ___qtablewidgetitem10->setText(QApplication::translate("rotencoderEditForm", "Send continuously", nullptr));
        QTableWidgetItem *___qtablewidgetitem11 = DOWN_CMDS_TABLE->horizontalHeaderItem(2);
        ___qtablewidgetitem11->setText(QApplication::translate("rotencoderEditForm", "Nr times send per step", nullptr));
        QTableWidgetItem *___qtablewidgetitem12 = DOWN_DREFS_TABLE->horizontalHeaderItem(0);
        ___qtablewidgetitem12->setText(QApplication::translate("rotencoderEditForm", "Dataref", nullptr));
        QTableWidgetItem *___qtablewidgetitem13 = DOWN_DREFS_TABLE->horizontalHeaderItem(1);
        ___qtablewidgetitem13->setText(QApplication::translate("rotencoderEditForm", "Index", nullptr));
        QTableWidgetItem *___qtablewidgetitem14 = DOWN_DREFS_TABLE->horizontalHeaderItem(2);
        ___qtablewidgetitem14->setText(QApplication::translate("rotencoderEditForm", "Set to Value", nullptr));
        QTableWidgetItem *___qtablewidgetitem15 = DOWN_DREFS_TABLE->horizontalHeaderItem(3);
        ___qtablewidgetitem15->setText(QApplication::translate("rotencoderEditForm", "Set continuously", nullptr));
        QTableWidgetItem *___qtablewidgetitem16 = DOWN_DREFS_TABLE->horizontalHeaderItem(4);
        ___qtablewidgetitem16->setText(QApplication::translate("rotencoderEditForm", "Type", nullptr));
        QTableWidgetItem *___qtablewidgetitem17 = DOWN_DREFS_TABLE->horizontalHeaderItem(5);
        ___qtablewidgetitem17->setText(QApplication::translate("rotencoderEditForm", "Unit", nullptr));
        label_12->setText(QApplication::translate("rotencoderEditForm", "Send XPlane Command: ", nullptr));
        DOWN_ADDCMD_BTN->setText(QApplication::translate("rotencoderEditForm", "...", nullptr));
        DOWN_RMCMD_BTN->setText(QApplication::translate("rotencoderEditForm", "...", nullptr));
        testDOWN_CMDS_button->setText(QApplication::translate("rotencoderEditForm", "Test", nullptr));
        label_14->setText(QApplication::translate("rotencoderEditForm", "Set Dataref:", nullptr));
        DOWN_ADDDREF_BTN->setText(QApplication::translate("rotencoderEditForm", "...", nullptr));
        DOWN_RMDREF_BTN->setText(QApplication::translate("rotencoderEditForm", "...", nullptr));
        testDOWN_DREFS_button->setText(QApplication::translate("rotencoderEditForm", "Test", nullptr));
        label->setText(QApplication::translate("rotencoderEditForm", "Arduino pin B:", nullptr));
        switchStateButton->setText(QApplication::translate("rotencoderEditForm", "...", nullptr));
        label_2->setText(QApplication::translate("rotencoderEditForm", "Steps per notch: ", nullptr));
        acceleration_checkBox->setText(QString());
        label_4->setText(QApplication::translate("rotencoderEditForm", "Acceleration", nullptr));
        label_5->setText(QApplication::translate("rotencoderEditForm", "Multiplier", nullptr));
        multiplierLineEdit->setText(QApplication::translate("rotencoderEditForm", "1.0", nullptr));
    } // retranslateUi

};

namespace Ui {
    class rotencoderEditForm: public Ui_rotencoderEditForm {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_ROTENCODEREDITFORM_H
