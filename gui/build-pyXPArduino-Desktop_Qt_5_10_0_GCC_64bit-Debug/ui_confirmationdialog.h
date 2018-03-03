/********************************************************************************
** Form generated from reading UI file 'confirmationdialog.ui'
**
** Created by: Qt User Interface Compiler version 5.10.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_CONFIRMATIONDIALOG_H
#define UI_CONFIRMATIONDIALOG_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QDialog>
#include <QtWidgets/QDialogButtonBox>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QVBoxLayout>

QT_BEGIN_NAMESPACE

class Ui_deleteConfirmationDialog
{
public:
    QVBoxLayout *verticalLayout;
    QHBoxLayout *horizontalLayout;
    QLabel *label;
    QLabel *label_2;
    QDialogButtonBox *buttonBox;

    void setupUi(QDialog *deleteConfirmationDialog)
    {
        if (deleteConfirmationDialog->objectName().isEmpty())
            deleteConfirmationDialog->setObjectName(QStringLiteral("deleteConfirmationDialog"));
        deleteConfirmationDialog->setWindowModality(Qt::ApplicationModal);
        deleteConfirmationDialog->resize(385, 98);
        deleteConfirmationDialog->setModal(true);
        verticalLayout = new QVBoxLayout(deleteConfirmationDialog);
        verticalLayout->setObjectName(QStringLiteral("verticalLayout"));
        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setObjectName(QStringLiteral("horizontalLayout"));
        label = new QLabel(deleteConfirmationDialog);
        label->setObjectName(QStringLiteral("label"));
        label->setMaximumSize(QSize(32, 16777215));
        QFont font;
        font.setPointSize(9);
        font.setBold(true);
        font.setWeight(75);
        label->setFont(font);
        label->setPixmap(QPixmap(QString::fromUtf8(":/newPrefix/attention.png")));
        label->setAlignment(Qt::AlignCenter);

        horizontalLayout->addWidget(label);

        label_2 = new QLabel(deleteConfirmationDialog);
        label_2->setObjectName(QStringLiteral("label_2"));
        QFont font1;
        font1.setPointSize(11);
        font1.setBold(true);
        font1.setWeight(75);
        label_2->setFont(font1);

        horizontalLayout->addWidget(label_2);


        verticalLayout->addLayout(horizontalLayout);

        buttonBox = new QDialogButtonBox(deleteConfirmationDialog);
        buttonBox->setObjectName(QStringLiteral("buttonBox"));
        buttonBox->setOrientation(Qt::Horizontal);
        buttonBox->setStandardButtons(QDialogButtonBox::Cancel|QDialogButtonBox::Yes);

        verticalLayout->addWidget(buttonBox);


        retranslateUi(deleteConfirmationDialog);
        QObject::connect(buttonBox, SIGNAL(accepted()), deleteConfirmationDialog, SLOT(accept()));
        QObject::connect(buttonBox, SIGNAL(rejected()), deleteConfirmationDialog, SLOT(reject()));

        QMetaObject::connectSlotsByName(deleteConfirmationDialog);
    } // setupUi

    void retranslateUi(QDialog *deleteConfirmationDialog)
    {
        deleteConfirmationDialog->setWindowTitle(QApplication::translate("deleteConfirmationDialog", "Delete Item", nullptr));
        label->setText(QString());
        label_2->setText(QApplication::translate("deleteConfirmationDialog", "Are you sure you want to delete the item?", nullptr));
    } // retranslateUi

};

namespace Ui {
    class deleteConfirmationDialog: public Ui_deleteConfirmationDialog {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_CONFIRMATIONDIALOG_H
