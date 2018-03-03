/********************************************************************************
** Form generated from reading UI file 'pickXPDatarefDialog.ui'
**
** Created by: Qt User Interface Compiler version 5.10.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_PICKXPDATAREFDIALOG_H
#define UI_PICKXPDATAREFDIALOG_H

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
    QLineEdit *filterDatarefsLineEdit;
    QComboBox *selectCategoryComboBox;
    QLabel *label_2;
    QLabel *label_3;
    QLineEdit *datarefLineEdit;
    QTableWidget *datarefTableWidget;
    QDialogButtonBox *buttonBox;

    void setupUi(QDialog *Dialog)
    {
        if (Dialog->objectName().isEmpty())
            Dialog->setObjectName(QStringLiteral("Dialog"));
        Dialog->resize(1105, 550);
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

        filterDatarefsLineEdit = new QLineEdit(Dialog);
        filterDatarefsLineEdit->setObjectName(QStringLiteral("filterDatarefsLineEdit"));
        filterDatarefsLineEdit->setMinimumSize(QSize(200, 0));
        filterDatarefsLineEdit->setMaximumSize(QSize(300, 300));

        formLayout->setWidget(4, QFormLayout::FieldRole, filterDatarefsLineEdit);

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

        datarefLineEdit = new QLineEdit(Dialog);
        datarefLineEdit->setObjectName(QStringLiteral("datarefLineEdit"));
        datarefLineEdit->setMinimumSize(QSize(200, 0));
        datarefLineEdit->setMaximumSize(QSize(300, 16777215));

        formLayout->setWidget(1, QFormLayout::FieldRole, datarefLineEdit);


        verticalLayout_2->addLayout(formLayout);

        datarefTableWidget = new QTableWidget(Dialog);
        if (datarefTableWidget->columnCount() < 6)
            datarefTableWidget->setColumnCount(6);
        QTableWidgetItem *__qtablewidgetitem = new QTableWidgetItem();
        datarefTableWidget->setHorizontalHeaderItem(0, __qtablewidgetitem);
        QTableWidgetItem *__qtablewidgetitem1 = new QTableWidgetItem();
        datarefTableWidget->setHorizontalHeaderItem(1, __qtablewidgetitem1);
        QTableWidgetItem *__qtablewidgetitem2 = new QTableWidgetItem();
        datarefTableWidget->setHorizontalHeaderItem(2, __qtablewidgetitem2);
        QTableWidgetItem *__qtablewidgetitem3 = new QTableWidgetItem();
        datarefTableWidget->setHorizontalHeaderItem(3, __qtablewidgetitem3);
        QTableWidgetItem *__qtablewidgetitem4 = new QTableWidgetItem();
        datarefTableWidget->setHorizontalHeaderItem(4, __qtablewidgetitem4);
        QTableWidgetItem *__qtablewidgetitem5 = new QTableWidgetItem();
        datarefTableWidget->setHorizontalHeaderItem(5, __qtablewidgetitem5);
        datarefTableWidget->setObjectName(QStringLiteral("datarefTableWidget"));
        QSizePolicy sizePolicy1(QSizePolicy::Expanding, QSizePolicy::Expanding);
        sizePolicy1.setHorizontalStretch(0);
        sizePolicy1.setVerticalStretch(10);
        sizePolicy1.setHeightForWidth(datarefTableWidget->sizePolicy().hasHeightForWidth());
        datarefTableWidget->setSizePolicy(sizePolicy1);
        datarefTableWidget->setMinimumSize(QSize(0, 200));
        datarefTableWidget->setEditTriggers(QAbstractItemView::NoEditTriggers);
        datarefTableWidget->setSelectionMode(QAbstractItemView::SingleSelection);
        datarefTableWidget->setSelectionBehavior(QAbstractItemView::SelectRows);
        datarefTableWidget->verticalHeader()->setDefaultSectionSize(25);

        verticalLayout_2->addWidget(datarefTableWidget);


        verticalLayout->addLayout(verticalLayout_2);

        buttonBox = new QDialogButtonBox(Dialog);
        buttonBox->setObjectName(QStringLiteral("buttonBox"));
        buttonBox->setOrientation(Qt::Horizontal);
        buttonBox->setStandardButtons(QDialogButtonBox::Cancel|QDialogButtonBox::Ok);

        verticalLayout->addWidget(buttonBox);


        retranslateUi(Dialog);
        QObject::connect(buttonBox, SIGNAL(accepted()), Dialog, SLOT(accept()));
        QObject::connect(buttonBox, SIGNAL(rejected()), Dialog, SLOT(reject()));
        QObject::connect(selectCategoryComboBox, SIGNAL(currentIndexChanged(QString)), Dialog, SLOT(refreshDatarefList()));
        QObject::connect(filterDatarefsLineEdit, SIGNAL(textChanged(QString)), Dialog, SLOT(refreshDatarefList()));
        QObject::connect(datarefTableWidget, SIGNAL(cellDoubleClicked(int,int)), Dialog, SLOT(pickDataref()));

        QMetaObject::connectSlotsByName(Dialog);
    } // setupUi

    void retranslateUi(QDialog *Dialog)
    {
        Dialog->setWindowTitle(QApplication::translate("Dialog", "Select XPlane Dataref", nullptr));
        label->setText(QApplication::translate("Dialog", "Search:", nullptr));
        label_2->setText(QApplication::translate("Dialog", "Filter Category: ", nullptr));
        label_3->setText(QApplication::translate("Dialog", "Dataref:", nullptr));
        QTableWidgetItem *___qtablewidgetitem = datarefTableWidget->horizontalHeaderItem(0);
        ___qtablewidgetitem->setText(QApplication::translate("Dialog", "Category", nullptr));
        QTableWidgetItem *___qtablewidgetitem1 = datarefTableWidget->horizontalHeaderItem(1);
        ___qtablewidgetitem1->setText(QApplication::translate("Dialog", "Dataref", nullptr));
        QTableWidgetItem *___qtablewidgetitem2 = datarefTableWidget->horizontalHeaderItem(2);
        ___qtablewidgetitem2->setText(QApplication::translate("Dialog", "Type", nullptr));
        QTableWidgetItem *___qtablewidgetitem3 = datarefTableWidget->horizontalHeaderItem(3);
        ___qtablewidgetitem3->setText(QApplication::translate("Dialog", "Writable", nullptr));
        QTableWidgetItem *___qtablewidgetitem4 = datarefTableWidget->horizontalHeaderItem(4);
        ___qtablewidgetitem4->setText(QApplication::translate("Dialog", "Unit", nullptr));
        QTableWidgetItem *___qtablewidgetitem5 = datarefTableWidget->horizontalHeaderItem(5);
        ___qtablewidgetitem5->setText(QApplication::translate("Dialog", "Description", nullptr));
    } // retranslateUi

};

namespace Ui {
    class Dialog: public Ui_Dialog {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_PICKXPDATAREFDIALOG_H
