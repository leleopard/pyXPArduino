/********************************************************************************
** Form generated from reading UI file 'pickXPCommandDialog.ui'
**
** Created by: Qt User Interface Compiler version 5.8.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_PICKXPCOMMANDDIALOG_H
#define UI_PICKXPCOMMANDDIALOG_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QComboBox>
#include <QtWidgets/QDialog>
#include <QtWidgets/QDialogButtonBox>
#include <QtWidgets/QFormLayout>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QTableWidget>
#include <QtWidgets/QVBoxLayout>

QT_BEGIN_NAMESPACE

class Ui_Dialog
{
public:
    QVBoxLayout *verticalLayout;
    QVBoxLayout *verticalLayout_2;
    QFormLayout *formLayout;
    QLabel *label;
    QLineEdit *filterCommandsLineEdit;
    QComboBox *selectCategoryComboBox;
    QLabel *label_2;
    QLabel *label_3;
    QLineEdit *commandLineEdit;
    QTableWidget *commandsTableWidget;
    QDialogButtonBox *buttonBox;

    void setupUi(QDialog *Dialog)
    {
        if (Dialog->objectName().isEmpty())
            Dialog->setObjectName(QStringLiteral("Dialog"));
        Dialog->resize(809, 550);
        QSizePolicy sizePolicy(QSizePolicy::Preferred, QSizePolicy::Preferred);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(Dialog->sizePolicy().hasHeightForWidth());
        Dialog->setSizePolicy(sizePolicy);
        verticalLayout = new QVBoxLayout(Dialog);
        verticalLayout->setObjectName(QStringLiteral("verticalLayout"));
        verticalLayout_2 = new QVBoxLayout();
        verticalLayout_2->setObjectName(QStringLiteral("verticalLayout_2"));
        verticalLayout_2->setSizeConstraint(QLayout::SetDefaultConstraint);
        formLayout = new QFormLayout();
        formLayout->setObjectName(QStringLiteral("formLayout"));
        formLayout->setSizeConstraint(QLayout::SetFixedSize);
        formLayout->setFormAlignment(Qt::AlignLeading|Qt::AlignLeft|Qt::AlignVCenter);
        label = new QLabel(Dialog);
        label->setObjectName(QStringLiteral("label"));
        sizePolicy.setHeightForWidth(label->sizePolicy().hasHeightForWidth());
        label->setSizePolicy(sizePolicy);
        label->setMaximumSize(QSize(16777215, 30));

        formLayout->setWidget(4, QFormLayout::LabelRole, label);

        filterCommandsLineEdit = new QLineEdit(Dialog);
        filterCommandsLineEdit->setObjectName(QStringLiteral("filterCommandsLineEdit"));
        filterCommandsLineEdit->setMinimumSize(QSize(200, 0));
        filterCommandsLineEdit->setMaximumSize(QSize(300, 300));

        formLayout->setWidget(4, QFormLayout::FieldRole, filterCommandsLineEdit);

        selectCategoryComboBox = new QComboBox(Dialog);
        selectCategoryComboBox->setObjectName(QStringLiteral("selectCategoryComboBox"));
        selectCategoryComboBox->setMinimumSize(QSize(250, 0));
        selectCategoryComboBox->setMaximumSize(QSize(300, 30));

        formLayout->setWidget(3, QFormLayout::FieldRole, selectCategoryComboBox);

        label_2 = new QLabel(Dialog);
        label_2->setObjectName(QStringLiteral("label_2"));
        label_2->setMaximumSize(QSize(16777215, 30));

        formLayout->setWidget(3, QFormLayout::LabelRole, label_2);

        label_3 = new QLabel(Dialog);
        label_3->setObjectName(QStringLiteral("label_3"));

        formLayout->setWidget(1, QFormLayout::LabelRole, label_3);

        commandLineEdit = new QLineEdit(Dialog);
        commandLineEdit->setObjectName(QStringLiteral("commandLineEdit"));
        commandLineEdit->setMinimumSize(QSize(200, 0));
        commandLineEdit->setMaximumSize(QSize(300, 16777215));

        formLayout->setWidget(1, QFormLayout::FieldRole, commandLineEdit);


        verticalLayout_2->addLayout(formLayout);

        commandsTableWidget = new QTableWidget(Dialog);
        if (commandsTableWidget->columnCount() < 3)
            commandsTableWidget->setColumnCount(3);
        QTableWidgetItem *__qtablewidgetitem = new QTableWidgetItem();
        commandsTableWidget->setHorizontalHeaderItem(0, __qtablewidgetitem);
        QTableWidgetItem *__qtablewidgetitem1 = new QTableWidgetItem();
        commandsTableWidget->setHorizontalHeaderItem(1, __qtablewidgetitem1);
        QTableWidgetItem *__qtablewidgetitem2 = new QTableWidgetItem();
        commandsTableWidget->setHorizontalHeaderItem(2, __qtablewidgetitem2);
        commandsTableWidget->setObjectName(QStringLiteral("commandsTableWidget"));
        QSizePolicy sizePolicy1(QSizePolicy::Expanding, QSizePolicy::Expanding);
        sizePolicy1.setHorizontalStretch(0);
        sizePolicy1.setVerticalStretch(10);
        sizePolicy1.setHeightForWidth(commandsTableWidget->sizePolicy().hasHeightForWidth());
        commandsTableWidget->setSizePolicy(sizePolicy1);
        commandsTableWidget->setMinimumSize(QSize(0, 200));
        commandsTableWidget->setEditTriggers(QAbstractItemView::NoEditTriggers);
        commandsTableWidget->setSelectionMode(QAbstractItemView::SingleSelection);
        commandsTableWidget->setSelectionBehavior(QAbstractItemView::SelectRows);
        commandsTableWidget->verticalHeader()->setDefaultSectionSize(25);

        verticalLayout_2->addWidget(commandsTableWidget);


        verticalLayout->addLayout(verticalLayout_2);

        buttonBox = new QDialogButtonBox(Dialog);
        buttonBox->setObjectName(QStringLiteral("buttonBox"));
        buttonBox->setOrientation(Qt::Horizontal);
        buttonBox->setStandardButtons(QDialogButtonBox::Cancel|QDialogButtonBox::Ok);

        verticalLayout->addWidget(buttonBox);


        retranslateUi(Dialog);
        QObject::connect(buttonBox, SIGNAL(accepted()), Dialog, SLOT(accept()));
        QObject::connect(buttonBox, SIGNAL(rejected()), Dialog, SLOT(reject()));
        QObject::connect(selectCategoryComboBox, SIGNAL(currentIndexChanged(QString)), Dialog, SLOT(refreshCommandList()));
        QObject::connect(filterCommandsLineEdit, SIGNAL(textChanged(QString)), Dialog, SLOT(refreshCommandList()));
        QObject::connect(commandsTableWidget, SIGNAL(cellDoubleClicked(int,int)), Dialog, SLOT(pickCommand()));

        QMetaObject::connectSlotsByName(Dialog);
    } // setupUi

    void retranslateUi(QDialog *Dialog)
    {
        Dialog->setWindowTitle(QApplication::translate("Dialog", "Select XPlane Command", Q_NULLPTR));
        label->setText(QApplication::translate("Dialog", "Search:", Q_NULLPTR));
        label_2->setText(QApplication::translate("Dialog", "Filter Category: ", Q_NULLPTR));
        label_3->setText(QApplication::translate("Dialog", "Command:", Q_NULLPTR));
        QTableWidgetItem *___qtablewidgetitem = commandsTableWidget->horizontalHeaderItem(0);
        ___qtablewidgetitem->setText(QApplication::translate("Dialog", "Category", Q_NULLPTR));
        QTableWidgetItem *___qtablewidgetitem1 = commandsTableWidget->horizontalHeaderItem(1);
        ___qtablewidgetitem1->setText(QApplication::translate("Dialog", "Command", Q_NULLPTR));
        QTableWidgetItem *___qtablewidgetitem2 = commandsTableWidget->horizontalHeaderItem(2);
        ___qtablewidgetitem2->setText(QApplication::translate("Dialog", "Description", Q_NULLPTR));
    } // retranslateUi

};

namespace Ui {
    class Dialog: public Ui_Dialog {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_PICKXPCOMMANDDIALOG_H
