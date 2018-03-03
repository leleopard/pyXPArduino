/********************************************************************************
** Form generated from reading UI file 'unsavedchanges_confirmationdialog.ui'
**
** Created by: Qt User Interface Compiler version 5.10.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_UNSAVEDCHANGES_CONFIRMATIONDIALOG_H
#define UI_UNSAVEDCHANGES_CONFIRMATIONDIALOG_H

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

class Ui_confirmationDialog
{
public:
    QVBoxLayout *verticalLayout;
    QHBoxLayout *horizontalLayout;
    QLabel *label;
    QLabel *label_2;
    QDialogButtonBox *buttonBox;

    void setupUi(QDialog *confirmationDialog)
    {
        if (confirmationDialog->objectName().isEmpty())
            confirmationDialog->setObjectName(QStringLiteral("confirmationDialog"));
        confirmationDialog->setWindowModality(Qt::ApplicationModal);
        confirmationDialog->resize(385, 98);
        confirmationDialog->setModal(true);
        verticalLayout = new QVBoxLayout(confirmationDialog);
        verticalLayout->setObjectName(QStringLiteral("verticalLayout"));
        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setObjectName(QStringLiteral("horizontalLayout"));
        label = new QLabel(confirmationDialog);
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

        label_2 = new QLabel(confirmationDialog);
        label_2->setObjectName(QStringLiteral("label_2"));
        QFont font1;
        font1.setPointSize(11);
        font1.setBold(true);
        font1.setWeight(75);
        label_2->setFont(font1);
        label_2->setWordWrap(true);

        horizontalLayout->addWidget(label_2);


        verticalLayout->addLayout(horizontalLayout);

        buttonBox = new QDialogButtonBox(confirmationDialog);
        buttonBox->setObjectName(QStringLiteral("buttonBox"));
        buttonBox->setOrientation(Qt::Horizontal);
        buttonBox->setStandardButtons(QDialogButtonBox::Cancel|QDialogButtonBox::Yes);

        verticalLayout->addWidget(buttonBox);


        retranslateUi(confirmationDialog);
        QObject::connect(buttonBox, SIGNAL(accepted()), confirmationDialog, SLOT(accept()));
        QObject::connect(buttonBox, SIGNAL(rejected()), confirmationDialog, SLOT(reject()));

        QMetaObject::connectSlotsByName(confirmationDialog);
    } // setupUi

    void retranslateUi(QDialog *confirmationDialog)
    {
        confirmationDialog->setWindowTitle(QApplication::translate("confirmationDialog", "Delete Item", nullptr));
        label->setText(QString());
        label_2->setText(QApplication::translate("confirmationDialog", "You have unsaved changes, these will be lost! Are you sure you want to continue?", nullptr));
    } // retranslateUi

};

namespace Ui {
    class confirmationDialog: public Ui_confirmationDialog {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_UNSAVEDCHANGES_CONFIRMATIONDIALOG_H
