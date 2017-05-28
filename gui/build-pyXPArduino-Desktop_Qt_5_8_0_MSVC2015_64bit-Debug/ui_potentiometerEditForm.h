/********************************************************************************
** Form generated from reading UI file 'potentiometerEditForm.ui'
**
** Created by: Qt User Interface Compiler version 5.8.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_POTENTIOMETEREDITFORM_H
#define UI_POTENTIOMETEREDITFORM_H

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
#include <QtWidgets/QSlider>
#include <QtWidgets/QSpacerItem>
#include <QtWidgets/QTableWidget>
#include <QtWidgets/QToolButton>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_potentiometerEditForm
{
public:
    QGridLayout *gridLayout;
    QGridLayout *gridLayout_3;
    QHBoxLayout *horizontalLayout_4;
    QLabel *label_11;
    QToolButton *ADDDREF_BTN;
    QToolButton *RMDREF_BTN;
    QSpacerItem *horizontalSpacer_2;
    QHBoxLayout *horizontalLayout_5;
    QTableWidget *DREFS_TABLE;
    QLabel *drefsHelpText;
    QLineEdit *nameLineEdit;
    QGridLayout *gridLayout_4;
    QTableWidget *CMDS_TABLE;
    QHBoxLayout *horizontalLayout_6;
    QLabel *label_12;
    QToolButton *ADDCMD_BTN;
    QToolButton *RMCMD_BTN;
    QSpacerItem *horizontalSpacer_3;
    QHBoxLayout *horizontalLayout_7;
    QLabel *label;
    QLineEdit *IDlineEdit;
    QComboBox *PIN_comboBox;
    QLabel *label_8;
    QSpacerItem *verticalSpacer_2;
    QLabel *label_17;
    QLabel *label_15;
    QLabel *label_3;
    QLabel *label_9;
    QLabel *label_18;
    QLabel *label_19;
    QSpacerItem *verticalSpacer;
    QSlider *valueSlider;
    QLabel *valueLabel;
    QSpacerItem *horizontalSpacer_5;

    void setupUi(QWidget *potentiometerEditForm)
    {
        if (potentiometerEditForm->objectName().isEmpty())
            potentiometerEditForm->setObjectName(QStringLiteral("potentiometerEditForm"));
        potentiometerEditForm->resize(832, 674);
        QSizePolicy sizePolicy(QSizePolicy::Expanding, QSizePolicy::Expanding);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(potentiometerEditForm->sizePolicy().hasHeightForWidth());
        potentiometerEditForm->setSizePolicy(sizePolicy);
        gridLayout = new QGridLayout(potentiometerEditForm);
        gridLayout->setObjectName(QStringLiteral("gridLayout"));
        gridLayout->setSizeConstraint(QLayout::SetDefaultConstraint);
        gridLayout_3 = new QGridLayout();
        gridLayout_3->setObjectName(QStringLiteral("gridLayout_3"));
        horizontalLayout_4 = new QHBoxLayout();
        horizontalLayout_4->setSpacing(2);
        horizontalLayout_4->setObjectName(QStringLiteral("horizontalLayout_4"));
        label_11 = new QLabel(potentiometerEditForm);
        label_11->setObjectName(QStringLiteral("label_11"));

        horizontalLayout_4->addWidget(label_11);

        ADDDREF_BTN = new QToolButton(potentiometerEditForm);
        ADDDREF_BTN->setObjectName(QStringLiteral("ADDDREF_BTN"));
        QIcon icon;
        icon.addFile(QStringLiteral(":/newPrefix/plusIcon.png"), QSize(), QIcon::Normal, QIcon::Off);
        ADDDREF_BTN->setIcon(icon);
        ADDDREF_BTN->setAutoRaise(true);

        horizontalLayout_4->addWidget(ADDDREF_BTN);

        RMDREF_BTN = new QToolButton(potentiometerEditForm);
        RMDREF_BTN->setObjectName(QStringLiteral("RMDREF_BTN"));
        QIcon icon1;
        icon1.addFile(QStringLiteral(":/newPrefix/minusIcon.png"), QSize(), QIcon::Normal, QIcon::Off);
        RMDREF_BTN->setIcon(icon1);
        RMDREF_BTN->setAutoRaise(true);

        horizontalLayout_4->addWidget(RMDREF_BTN);

        horizontalSpacer_2 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_4->addItem(horizontalSpacer_2);


        gridLayout_3->addLayout(horizontalLayout_4, 2, 1, 1, 1);

        horizontalLayout_5 = new QHBoxLayout();
        horizontalLayout_5->setObjectName(QStringLiteral("horizontalLayout_5"));

        gridLayout_3->addLayout(horizontalLayout_5, 2, 4, 1, 1);

        DREFS_TABLE = new QTableWidget(potentiometerEditForm);
        if (DREFS_TABLE->columnCount() < 5)
            DREFS_TABLE->setColumnCount(5);
        QTableWidgetItem *__qtablewidgetitem = new QTableWidgetItem();
        DREFS_TABLE->setHorizontalHeaderItem(0, __qtablewidgetitem);
        QTableWidgetItem *__qtablewidgetitem1 = new QTableWidgetItem();
        DREFS_TABLE->setHorizontalHeaderItem(1, __qtablewidgetitem1);
        QTableWidgetItem *__qtablewidgetitem2 = new QTableWidgetItem();
        DREFS_TABLE->setHorizontalHeaderItem(2, __qtablewidgetitem2);
        QTableWidgetItem *__qtablewidgetitem3 = new QTableWidgetItem();
        DREFS_TABLE->setHorizontalHeaderItem(3, __qtablewidgetitem3);
        QTableWidgetItem *__qtablewidgetitem4 = new QTableWidgetItem();
        DREFS_TABLE->setHorizontalHeaderItem(4, __qtablewidgetitem4);
        DREFS_TABLE->setObjectName(QStringLiteral("DREFS_TABLE"));

        gridLayout_3->addWidget(DREFS_TABLE, 3, 1, 1, 1);

        drefsHelpText = new QLabel(potentiometerEditForm);
        drefsHelpText->setObjectName(QStringLiteral("drefsHelpText"));
        drefsHelpText->setMinimumSize(QSize(250, 0));
        drefsHelpText->setMaximumSize(QSize(300, 16777215));
        drefsHelpText->setTextFormat(Qt::RichText);
        drefsHelpText->setAlignment(Qt::AlignLeading|Qt::AlignLeft|Qt::AlignTop);
        drefsHelpText->setWordWrap(true);

        gridLayout_3->addWidget(drefsHelpText, 3, 3, 1, 2);


        gridLayout->addLayout(gridLayout_3, 8, 0, 1, 6);

        nameLineEdit = new QLineEdit(potentiometerEditForm);
        nameLineEdit->setObjectName(QStringLiteral("nameLineEdit"));
        nameLineEdit->setMinimumSize(QSize(250, 0));
        nameLineEdit->setMaximumSize(QSize(350, 16777215));

        gridLayout->addWidget(nameLineEdit, 3, 2, 1, 3);

        gridLayout_4 = new QGridLayout();
        gridLayout_4->setObjectName(QStringLiteral("gridLayout_4"));
        CMDS_TABLE = new QTableWidget(potentiometerEditForm);
        if (CMDS_TABLE->columnCount() < 2)
            CMDS_TABLE->setColumnCount(2);
        QTableWidgetItem *__qtablewidgetitem5 = new QTableWidgetItem();
        CMDS_TABLE->setHorizontalHeaderItem(0, __qtablewidgetitem5);
        QTableWidgetItem *__qtablewidgetitem6 = new QTableWidgetItem();
        CMDS_TABLE->setHorizontalHeaderItem(1, __qtablewidgetitem6);
        CMDS_TABLE->setObjectName(QStringLiteral("CMDS_TABLE"));
        CMDS_TABLE->setToolTipDuration(3);

        gridLayout_4->addWidget(CMDS_TABLE, 6, 0, 1, 1);

        horizontalLayout_6 = new QHBoxLayout();
        horizontalLayout_6->setObjectName(QStringLiteral("horizontalLayout_6"));
        label_12 = new QLabel(potentiometerEditForm);
        label_12->setObjectName(QStringLiteral("label_12"));

        horizontalLayout_6->addWidget(label_12);

        ADDCMD_BTN = new QToolButton(potentiometerEditForm);
        ADDCMD_BTN->setObjectName(QStringLiteral("ADDCMD_BTN"));
        QIcon icon2;
        icon2.addFile(QStringLiteral(":/newPrefix/plusIcon.png"), QSize(), QIcon::Normal, QIcon::On);
        ADDCMD_BTN->setIcon(icon2);
        ADDCMD_BTN->setAutoRaise(true);

        horizontalLayout_6->addWidget(ADDCMD_BTN);

        RMCMD_BTN = new QToolButton(potentiometerEditForm);
        RMCMD_BTN->setObjectName(QStringLiteral("RMCMD_BTN"));
        QIcon icon3;
        icon3.addFile(QStringLiteral(":/newPrefix/minusIcon.png"), QSize(), QIcon::Normal, QIcon::On);
        RMCMD_BTN->setIcon(icon3);
        RMCMD_BTN->setAutoRaise(true);

        horizontalLayout_6->addWidget(RMCMD_BTN);

        horizontalSpacer_3 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_6->addItem(horizontalSpacer_3);


        gridLayout_4->addLayout(horizontalLayout_6, 3, 0, 1, 1);

        horizontalLayout_7 = new QHBoxLayout();
        horizontalLayout_7->setObjectName(QStringLiteral("horizontalLayout_7"));

        gridLayout_4->addLayout(horizontalLayout_7, 3, 1, 1, 1);

        label = new QLabel(potentiometerEditForm);
        label->setObjectName(QStringLiteral("label"));
        label->setMinimumSize(QSize(250, 0));
        label->setMaximumSize(QSize(300, 16777215));
        label->setTextFormat(Qt::RichText);
        label->setAlignment(Qt::AlignLeading|Qt::AlignLeft|Qt::AlignTop);
        label->setWordWrap(true);

        gridLayout_4->addWidget(label, 6, 1, 1, 1);


        gridLayout->addLayout(gridLayout_4, 10, 0, 1, 6);

        IDlineEdit = new QLineEdit(potentiometerEditForm);
        IDlineEdit->setObjectName(QStringLiteral("IDlineEdit"));
        IDlineEdit->setEnabled(false);
        IDlineEdit->setMinimumSize(QSize(250, 0));
        IDlineEdit->setMaximumSize(QSize(350, 16777215));
        IDlineEdit->setReadOnly(true);

        gridLayout->addWidget(IDlineEdit, 4, 2, 1, 3);

        PIN_comboBox = new QComboBox(potentiometerEditForm);
        PIN_comboBox->setObjectName(QStringLiteral("PIN_comboBox"));
        PIN_comboBox->setMaximumSize(QSize(50, 16777215));

        gridLayout->addWidget(PIN_comboBox, 5, 2, 1, 1);

        label_8 = new QLabel(potentiometerEditForm);
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

        gridLayout->addWidget(label_8, 0, 0, 1, 6);

        verticalSpacer_2 = new QSpacerItem(20, 10, QSizePolicy::Minimum, QSizePolicy::Fixed);

        gridLayout->addItem(verticalSpacer_2, 6, 0, 1, 1);

        label_17 = new QLabel(potentiometerEditForm);
        label_17->setObjectName(QStringLiteral("label_17"));

        gridLayout->addWidget(label_17, 1, 0, 1, 1);

        label_15 = new QLabel(potentiometerEditForm);
        label_15->setObjectName(QStringLiteral("label_15"));
        QFont font1;
        font1.setPointSize(9);
        font1.setBold(true);
        font1.setWeight(75);
        label_15->setFont(font1);

        gridLayout->addWidget(label_15, 9, 0, 1, 1);

        label_3 = new QLabel(potentiometerEditForm);
        label_3->setObjectName(QStringLiteral("label_3"));
        QSizePolicy sizePolicy1(QSizePolicy::Minimum, QSizePolicy::Minimum);
        sizePolicy1.setHorizontalStretch(0);
        sizePolicy1.setVerticalStretch(0);
        sizePolicy1.setHeightForWidth(label_3->sizePolicy().hasHeightForWidth());
        label_3->setSizePolicy(sizePolicy1);
        label_3->setLayoutDirection(Qt::LeftToRight);

        gridLayout->addWidget(label_3, 3, 0, 1, 1);

        label_9 = new QLabel(potentiometerEditForm);
        label_9->setObjectName(QStringLiteral("label_9"));
        label_9->setFont(font1);

        gridLayout->addWidget(label_9, 7, 0, 1, 1);

        label_18 = new QLabel(potentiometerEditForm);
        label_18->setObjectName(QStringLiteral("label_18"));

        gridLayout->addWidget(label_18, 5, 0, 1, 1);

        label_19 = new QLabel(potentiometerEditForm);
        label_19->setObjectName(QStringLiteral("label_19"));

        gridLayout->addWidget(label_19, 4, 0, 1, 1);

        verticalSpacer = new QSpacerItem(20, 26, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout->addItem(verticalSpacer, 12, 0, 1, 1);

        valueSlider = new QSlider(potentiometerEditForm);
        valueSlider->setObjectName(QStringLiteral("valueSlider"));
        valueSlider->setEnabled(false);
        valueSlider->setMaximumSize(QSize(200, 16777215));
        valueSlider->setStyleSheet(QLatin1String("QSlider::groove:horizontal {\n"
"    border: 1px solid #999999;\n"
"    height: 8px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, stop:1 #c4c4c4);\n"
"    margin: 2px 0;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
"    border: 1px solid #5c5c5c;\n"
"    width: 5px;\n"
"    margin: -2px 0; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal{\n"
"	border: 1px solid #999999;\n"
"    height: 8px;     \n"
"	background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #00979d, stop:1 #007579);\n"
"    margin: 2px 0;\n"
"}"));
        valueSlider->setMaximum(1023);
        valueSlider->setOrientation(Qt::Horizontal);
        valueSlider->setInvertedAppearance(false);
        valueSlider->setTickPosition(QSlider::TicksAbove);
        valueSlider->setTickInterval(128);

        gridLayout->addWidget(valueSlider, 1, 4, 1, 1);

        valueLabel = new QLabel(potentiometerEditForm);
        valueLabel->setObjectName(QStringLiteral("valueLabel"));
        valueLabel->setMinimumSize(QSize(40, 0));

        gridLayout->addWidget(valueLabel, 1, 2, 1, 1);

        horizontalSpacer_5 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout->addItem(horizontalSpacer_5, 1, 5, 1, 1);


        retranslateUi(potentiometerEditForm);
        QObject::connect(ADDDREF_BTN, SIGNAL(clicked()), potentiometerEditForm, SLOT(addDataref()));
        QObject::connect(RMDREF_BTN, SIGNAL(clicked()), potentiometerEditForm, SLOT(rmDataref()));
        QObject::connect(ADDCMD_BTN, SIGNAL(clicked()), potentiometerEditForm, SLOT(addCommand()));
        QObject::connect(RMCMD_BTN, SIGNAL(clicked()), potentiometerEditForm, SLOT(rmCommand()));
        QObject::connect(CMDS_TABLE, SIGNAL(cellDoubleClicked(int,int)), potentiometerEditForm, SLOT(editXPCommand()));
        QObject::connect(nameLineEdit, SIGNAL(editingFinished()), potentiometerEditForm, SLOT(updateXMLdata()));
        QObject::connect(PIN_comboBox, SIGNAL(currentIndexChanged(int)), potentiometerEditForm, SLOT(updateXMLdata()));
        QObject::connect(CMDS_TABLE, SIGNAL(itemChanged(QTableWidgetItem*)), potentiometerEditForm, SLOT(updateXMLdata()));
        QObject::connect(PIN_comboBox, SIGNAL(currentTextChanged(QString)), potentiometerEditForm, SLOT(updatePin()));
        QObject::connect(DREFS_TABLE, SIGNAL(cellDoubleClicked(int,int)), potentiometerEditForm, SLOT(editXPDataref()));
        QObject::connect(DREFS_TABLE, SIGNAL(itemChanged(QTableWidgetItem*)), potentiometerEditForm, SLOT(updateXMLdata()));

        QMetaObject::connectSlotsByName(potentiometerEditForm);
    } // setupUi

    void retranslateUi(QWidget *potentiometerEditForm)
    {
        potentiometerEditForm->setWindowTitle(QApplication::translate("potentiometerEditForm", "Form", Q_NULLPTR));
        label_11->setText(QApplication::translate("potentiometerEditForm", "Set Dataref: ", Q_NULLPTR));
        ADDDREF_BTN->setText(QApplication::translate("potentiometerEditForm", "...", Q_NULLPTR));
        RMDREF_BTN->setText(QApplication::translate("potentiometerEditForm", "...", Q_NULLPTR));
        QTableWidgetItem *___qtablewidgetitem = DREFS_TABLE->horizontalHeaderItem(0);
        ___qtablewidgetitem->setText(QApplication::translate("potentiometerEditForm", "Dataref", Q_NULLPTR));
        QTableWidgetItem *___qtablewidgetitem1 = DREFS_TABLE->horizontalHeaderItem(1);
        ___qtablewidgetitem1->setText(QApplication::translate("potentiometerEditForm", "Index", Q_NULLPTR));
        QTableWidgetItem *___qtablewidgetitem2 = DREFS_TABLE->horizontalHeaderItem(2);
        ___qtablewidgetitem2->setText(QApplication::translate("potentiometerEditForm", "Set to Value", Q_NULLPTR));
        QTableWidgetItem *___qtablewidgetitem3 = DREFS_TABLE->horizontalHeaderItem(3);
        ___qtablewidgetitem3->setText(QApplication::translate("potentiometerEditForm", "Type", Q_NULLPTR));
        QTableWidgetItem *___qtablewidgetitem4 = DREFS_TABLE->horizontalHeaderItem(4);
        ___qtablewidgetitem4->setText(QApplication::translate("potentiometerEditForm", "Unit", Q_NULLPTR));
        drefsHelpText->setText(QApplication::translate("potentiometerEditForm", "<html><head/><body><p>Enter series of points [pot input value, output dataref value]. The output value of the dataref in between 2 points will be linearly interpolated. </p><p>Note that the potentiometer value varies between 0 and 1023 (this is the raw output reading from the ADC of the arduino)</p><p>For example to set the dataref to vary linearly between 10 and 300 when the potentiometer value varies between 0 and 1023, enter: </p><p><span style=\" color:#0000ff;\">[0,10], [1023,300]</span></p></body></html>", Q_NULLPTR));
        QTableWidgetItem *___qtablewidgetitem5 = CMDS_TABLE->horizontalHeaderItem(0);
        ___qtablewidgetitem5->setText(QApplication::translate("potentiometerEditForm", "Command", Q_NULLPTR));
        QTableWidgetItem *___qtablewidgetitem6 = CMDS_TABLE->horizontalHeaderItem(1);
        ___qtablewidgetitem6->setText(QApplication::translate("potentiometerEditForm", "Send if pot value is in intervals", Q_NULLPTR));
#ifndef QT_NO_TOOLTIP
        ___qtablewidgetitem6->setToolTip(QApplication::translate("potentiometerEditForm", "<html><head/><body><p>Enter intervals where the command should be sent. </p><p>For example to send the command if the pot value is between 0 and 200 or between 600 and 800, enter: </p><p><span style=\" color:#0000ff;\">(0,200), (600,800)</span></p></body></html>", Q_NULLPTR));
#endif // QT_NO_TOOLTIP
#ifndef QT_NO_TOOLTIP
        CMDS_TABLE->setToolTip(QApplication::translate("potentiometerEditForm", "<html><head/><body><p>Enter intervals where the command should be sent. </p><p>For example to send the command if the pot value is between 0 and 200 or between 600 and 800, enter: </p><p><span style=\" color:#0000ff;\">(0,200), (600,800)</span></p></body></html>", Q_NULLPTR));
#endif // QT_NO_TOOLTIP
        label_12->setText(QApplication::translate("potentiometerEditForm", "Send XPlane Command: ", Q_NULLPTR));
        ADDCMD_BTN->setText(QApplication::translate("potentiometerEditForm", "...", Q_NULLPTR));
        RMCMD_BTN->setText(QApplication::translate("potentiometerEditForm", "...", Q_NULLPTR));
        label->setText(QApplication::translate("potentiometerEditForm", "<html><head/><body><p>Enter intervals where the command should be sent. </p><p>For example to send the command if the pot value is between 0 and 200 or between 600 and 800, enter: </p><p><span style=\" color:#0000ff;\">[0,200], [600,800]</span></p></body></html>", Q_NULLPTR));
        label_8->setText(QApplication::translate("potentiometerEditForm", "Edit potentiometer", Q_NULLPTR));
        label_17->setText(QApplication::translate("potentiometerEditForm", "Value", Q_NULLPTR));
        label_15->setText(QApplication::translate("potentiometerEditForm", "Command actions:", Q_NULLPTR));
        label_3->setText(QApplication::translate("potentiometerEditForm", "Name", Q_NULLPTR));
        label_9->setText(QApplication::translate("potentiometerEditForm", "Dataref Actions:", Q_NULLPTR));
        label_18->setText(QApplication::translate("potentiometerEditForm", "Arduino pin:", Q_NULLPTR));
        label_19->setText(QApplication::translate("potentiometerEditForm", "ID", Q_NULLPTR));
        valueLabel->setText(QApplication::translate("potentiometerEditForm", "0", Q_NULLPTR));
    } // retranslateUi

};

namespace Ui {
    class potentiometerEditForm: public Ui_potentiometerEditForm {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_POTENTIOMETEREDITFORM_H
