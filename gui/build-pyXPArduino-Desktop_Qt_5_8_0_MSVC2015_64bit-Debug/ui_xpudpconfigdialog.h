/********************************************************************************
** Form generated from reading UI file 'xpudpconfigdialog.ui'
**
** Created by: Qt User Interface Compiler version 5.8.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_XPUDPCONFIGDIALOG_H
#define UI_XPUDPCONFIGDIALOG_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QCheckBox>
#include <QtWidgets/QDialog>
#include <QtWidgets/QDialogButtonBox>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QSpacerItem>
#include <QtWidgets/QTableWidget>
#include <QtWidgets/QToolButton>
#include <QtWidgets/QVBoxLayout>

QT_BEGIN_NAMESPACE

class Ui_Dialog
{
public:
    QVBoxLayout *verticalLayout;
    QGridLayout *gridLayout;
    QLabel *label;
    QLineEdit *XPIP_Address_LineEdit;
    QLineEdit *IP_Address_LineEdit;
    QLabel *label_3;
    QCheckBox *XP_RedirectTraffic_checkBox;
    QLineEdit *XP_ComputerName_LineEdit;
    QLabel *label_6;
    QLineEdit *IP_Port_LineEdit;
    QLineEdit *XPIP_Port_LineEdit;
    QLabel *label_2;
    QSpacerItem *verticalSpacer_3;
    QLabel *label_4;
    QLabel *label_7;
    QLabel *label_8;
    QLabel *label_5;
    QSpacerItem *verticalSpacer_2;
    QSpacerItem *horizontalSpacer_2;
    QLabel *label_10;
    QLabel *label_11;
    QLabel *label_12;
    QLineEdit *RedIP_Address_LineEdit;
    QLineEdit *RedIP_Port_LineEdit;
    QHBoxLayout *horizontalLayout;
    QLabel *label_9;
    QToolButton *toolButton_2;
    QToolButton *toolButton;
    QSpacerItem *horizontalSpacer;
    QTableWidget *tableWidget;
    QSpacerItem *verticalSpacer;
    QLabel *UDPStatusLabel;
    QDialogButtonBox *buttonBox;

    void setupUi(QDialog *Dialog)
    {
        if (Dialog->objectName().isEmpty())
            Dialog->setObjectName(QStringLiteral("Dialog"));
        Dialog->resize(650, 464);
        verticalLayout = new QVBoxLayout(Dialog);
        verticalLayout->setObjectName(QStringLiteral("verticalLayout"));
        gridLayout = new QGridLayout();
        gridLayout->setObjectName(QStringLiteral("gridLayout"));
        label = new QLabel(Dialog);
        label->setObjectName(QStringLiteral("label"));

        gridLayout->addWidget(label, 0, 0, 1, 1);

        XPIP_Address_LineEdit = new QLineEdit(Dialog);
        XPIP_Address_LineEdit->setObjectName(QStringLiteral("XPIP_Address_LineEdit"));
        XPIP_Address_LineEdit->setMaximumSize(QSize(150, 16777215));

        gridLayout->addWidget(XPIP_Address_LineEdit, 1, 2, 1, 1);

        IP_Address_LineEdit = new QLineEdit(Dialog);
        IP_Address_LineEdit->setObjectName(QStringLiteral("IP_Address_LineEdit"));
        IP_Address_LineEdit->setMaximumSize(QSize(150, 16777215));

        gridLayout->addWidget(IP_Address_LineEdit, 0, 2, 1, 1);

        label_3 = new QLabel(Dialog);
        label_3->setObjectName(QStringLiteral("label_3"));

        gridLayout->addWidget(label_3, 2, 0, 1, 1);

        XP_RedirectTraffic_checkBox = new QCheckBox(Dialog);
        XP_RedirectTraffic_checkBox->setObjectName(QStringLiteral("XP_RedirectTraffic_checkBox"));

        gridLayout->addWidget(XP_RedirectTraffic_checkBox, 4, 1, 1, 1);

        XP_ComputerName_LineEdit = new QLineEdit(Dialog);
        XP_ComputerName_LineEdit->setObjectName(QStringLiteral("XP_ComputerName_LineEdit"));

        gridLayout->addWidget(XP_ComputerName_LineEdit, 2, 1, 1, 3);

        label_6 = new QLabel(Dialog);
        label_6->setObjectName(QStringLiteral("label_6"));

        gridLayout->addWidget(label_6, 0, 3, 1, 1);

        IP_Port_LineEdit = new QLineEdit(Dialog);
        IP_Port_LineEdit->setObjectName(QStringLiteral("IP_Port_LineEdit"));
        IP_Port_LineEdit->setMaximumSize(QSize(75, 16777215));

        gridLayout->addWidget(IP_Port_LineEdit, 0, 4, 1, 1);

        XPIP_Port_LineEdit = new QLineEdit(Dialog);
        XPIP_Port_LineEdit->setObjectName(QStringLiteral("XPIP_Port_LineEdit"));
        XPIP_Port_LineEdit->setMaximumSize(QSize(75, 16777215));

        gridLayout->addWidget(XPIP_Port_LineEdit, 1, 4, 1, 1);

        label_2 = new QLabel(Dialog);
        label_2->setObjectName(QStringLiteral("label_2"));

        gridLayout->addWidget(label_2, 1, 0, 1, 1);

        verticalSpacer_3 = new QSpacerItem(20, 10, QSizePolicy::Minimum, QSizePolicy::Fixed);

        gridLayout->addItem(verticalSpacer_3, 6, 0, 1, 1);

        label_4 = new QLabel(Dialog);
        label_4->setObjectName(QStringLiteral("label_4"));

        gridLayout->addWidget(label_4, 0, 1, 1, 1);

        label_7 = new QLabel(Dialog);
        label_7->setObjectName(QStringLiteral("label_7"));

        gridLayout->addWidget(label_7, 1, 3, 1, 1);

        label_8 = new QLabel(Dialog);
        label_8->setObjectName(QStringLiteral("label_8"));

        gridLayout->addWidget(label_8, 4, 0, 1, 1);

        label_5 = new QLabel(Dialog);
        label_5->setObjectName(QStringLiteral("label_5"));

        gridLayout->addWidget(label_5, 1, 1, 1, 1);

        verticalSpacer_2 = new QSpacerItem(20, 10, QSizePolicy::Minimum, QSizePolicy::Fixed);

        gridLayout->addItem(verticalSpacer_2, 3, 0, 1, 1);

        horizontalSpacer_2 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout->addItem(horizontalSpacer_2, 0, 5, 1, 1);

        label_10 = new QLabel(Dialog);
        label_10->setObjectName(QStringLiteral("label_10"));

        gridLayout->addWidget(label_10, 5, 0, 1, 1);

        label_11 = new QLabel(Dialog);
        label_11->setObjectName(QStringLiteral("label_11"));

        gridLayout->addWidget(label_11, 5, 1, 1, 1);

        label_12 = new QLabel(Dialog);
        label_12->setObjectName(QStringLiteral("label_12"));

        gridLayout->addWidget(label_12, 5, 3, 1, 1);

        RedIP_Address_LineEdit = new QLineEdit(Dialog);
        RedIP_Address_LineEdit->setObjectName(QStringLiteral("RedIP_Address_LineEdit"));
        RedIP_Address_LineEdit->setMaximumSize(QSize(150, 16777215));

        gridLayout->addWidget(RedIP_Address_LineEdit, 5, 2, 1, 1);

        RedIP_Port_LineEdit = new QLineEdit(Dialog);
        RedIP_Port_LineEdit->setObjectName(QStringLiteral("RedIP_Port_LineEdit"));
        RedIP_Port_LineEdit->setMaximumSize(QSize(75, 16777215));

        gridLayout->addWidget(RedIP_Port_LineEdit, 5, 4, 1, 1);


        verticalLayout->addLayout(gridLayout);

        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setObjectName(QStringLiteral("horizontalLayout"));
        label_9 = new QLabel(Dialog);
        label_9->setObjectName(QStringLiteral("label_9"));
        label_9->setEnabled(false);

        horizontalLayout->addWidget(label_9);

        toolButton_2 = new QToolButton(Dialog);
        toolButton_2->setObjectName(QStringLiteral("toolButton_2"));
        toolButton_2->setEnabled(false);
        QIcon icon;
        icon.addFile(QStringLiteral(":/newPrefix/plusIcon.png"), QSize(), QIcon::Normal, QIcon::Off);
        toolButton_2->setIcon(icon);

        horizontalLayout->addWidget(toolButton_2);

        toolButton = new QToolButton(Dialog);
        toolButton->setObjectName(QStringLiteral("toolButton"));
        toolButton->setEnabled(false);
        QIcon icon1;
        icon1.addFile(QStringLiteral(":/newPrefix/minusIcon.png"), QSize(), QIcon::Normal, QIcon::Off);
        toolButton->setIcon(icon1);

        horizontalLayout->addWidget(toolButton);

        horizontalSpacer = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout->addItem(horizontalSpacer);


        verticalLayout->addLayout(horizontalLayout);

        tableWidget = new QTableWidget(Dialog);
        if (tableWidget->columnCount() < 2)
            tableWidget->setColumnCount(2);
        QTableWidgetItem *__qtablewidgetitem = new QTableWidgetItem();
        tableWidget->setHorizontalHeaderItem(0, __qtablewidgetitem);
        QTableWidgetItem *__qtablewidgetitem1 = new QTableWidgetItem();
        tableWidget->setHorizontalHeaderItem(1, __qtablewidgetitem1);
        tableWidget->setObjectName(QStringLiteral("tableWidget"));
        tableWidget->setEnabled(false);

        verticalLayout->addWidget(tableWidget);

        verticalSpacer = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        verticalLayout->addItem(verticalSpacer);

        UDPStatusLabel = new QLabel(Dialog);
        UDPStatusLabel->setObjectName(QStringLiteral("UDPStatusLabel"));

        verticalLayout->addWidget(UDPStatusLabel);

        buttonBox = new QDialogButtonBox(Dialog);
        buttonBox->setObjectName(QStringLiteral("buttonBox"));
        buttonBox->setOrientation(Qt::Horizontal);
        buttonBox->setStandardButtons(QDialogButtonBox::Apply|QDialogButtonBox::Cancel|QDialogButtonBox::Ok);

        verticalLayout->addWidget(buttonBox);


        retranslateUi(Dialog);
        QObject::connect(buttonBox, SIGNAL(accepted()), Dialog, SLOT(accept()));
        QObject::connect(buttonBox, SIGNAL(rejected()), Dialog, SLOT(reject()));
        QObject::connect(buttonBox, SIGNAL(clicked(QAbstractButton*)), Dialog, SLOT(buttonBoxClicked()));
        QObject::connect(XP_RedirectTraffic_checkBox, SIGNAL(stateChanged(int)), Dialog, SLOT(redirectCheckboxStateChanged()));

        QMetaObject::connectSlotsByName(Dialog);
    } // setupUi

    void retranslateUi(QDialog *Dialog)
    {
        Dialog->setWindowTitle(QApplication::translate("Dialog", "Edit XPlane UDP settings", Q_NULLPTR));
        label->setText(QApplication::translate("Dialog", "Our IP Address XPlane is sending to ", Q_NULLPTR));
        label_3->setText(QApplication::translate("Dialog", "XPlane computer Network Name", Q_NULLPTR));
        XP_RedirectTraffic_checkBox->setText(QString());
        label_6->setText(QApplication::translate("Dialog", "Port", Q_NULLPTR));
        label_2->setText(QApplication::translate("Dialog", "XPlane IP Address", Q_NULLPTR));
        label_4->setText(QApplication::translate("Dialog", "IP", Q_NULLPTR));
        label_7->setText(QApplication::translate("Dialog", "Port", Q_NULLPTR));
        label_8->setText(QApplication::translate("Dialog", "Redirect UDP traffic to XPlane", Q_NULLPTR));
        label_5->setText(QApplication::translate("Dialog", "IP", Q_NULLPTR));
        label_10->setText(QApplication::translate("Dialog", "IP address we are receiving traffic to redirect ", Q_NULLPTR));
        label_11->setText(QApplication::translate("Dialog", "IP", Q_NULLPTR));
        label_12->setText(QApplication::translate("Dialog", "Port", Q_NULLPTR));
        label_9->setText(QApplication::translate("Dialog", "Forward XPlane UDP traffic to IP addresses", Q_NULLPTR));
        toolButton_2->setText(QApplication::translate("Dialog", "...", Q_NULLPTR));
        toolButton->setText(QApplication::translate("Dialog", "...", Q_NULLPTR));
        QTableWidgetItem *___qtablewidgetitem = tableWidget->horizontalHeaderItem(0);
        ___qtablewidgetitem->setText(QApplication::translate("Dialog", "IP", Q_NULLPTR));
        QTableWidgetItem *___qtablewidgetitem1 = tableWidget->horizontalHeaderItem(1);
        ___qtablewidgetitem1->setText(QApplication::translate("Dialog", "Port", Q_NULLPTR));
        UDPStatusLabel->setText(QApplication::translate("Dialog", "UDP Server status:", Q_NULLPTR));
    } // retranslateUi

};

namespace Ui {
    class Dialog: public Ui_Dialog {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_XPUDPCONFIGDIALOG_H
