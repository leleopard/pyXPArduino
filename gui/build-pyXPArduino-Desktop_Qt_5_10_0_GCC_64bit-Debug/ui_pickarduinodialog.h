/********************************************************************************
** Form generated from reading UI file 'pickarduinodialog.ui'
**
** Created by: Qt User Interface Compiler version 5.10.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_PICKARDUINODIALOG_H
#define UI_PICKARDUINODIALOG_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QDialog>
#include <QtWidgets/QDialogButtonBox>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QTableWidget>
#include <QtWidgets/QVBoxLayout>

QT_BEGIN_NAMESPACE

class Ui_AddArduinoDialog
{
public:
    QVBoxLayout *verticalLayout;
    QTableWidget *arduinoTableWidget;
    QDialogButtonBox *buttonBox;

    void setupUi(QDialog *AddArduinoDialog)
    {
        if (AddArduinoDialog->objectName().isEmpty())
            AddArduinoDialog->setObjectName(QStringLiteral("AddArduinoDialog"));
        AddArduinoDialog->resize(691, 300);
        verticalLayout = new QVBoxLayout(AddArduinoDialog);
        verticalLayout->setObjectName(QStringLiteral("verticalLayout"));
        arduinoTableWidget = new QTableWidget(AddArduinoDialog);
        if (arduinoTableWidget->columnCount() < 6)
            arduinoTableWidget->setColumnCount(6);
        QTableWidgetItem *__qtablewidgetitem = new QTableWidgetItem();
        arduinoTableWidget->setHorizontalHeaderItem(0, __qtablewidgetitem);
        QTableWidgetItem *__qtablewidgetitem1 = new QTableWidgetItem();
        arduinoTableWidget->setHorizontalHeaderItem(1, __qtablewidgetitem1);
        QTableWidgetItem *__qtablewidgetitem2 = new QTableWidgetItem();
        arduinoTableWidget->setHorizontalHeaderItem(2, __qtablewidgetitem2);
        QTableWidgetItem *__qtablewidgetitem3 = new QTableWidgetItem();
        arduinoTableWidget->setHorizontalHeaderItem(3, __qtablewidgetitem3);
        QTableWidgetItem *__qtablewidgetitem4 = new QTableWidgetItem();
        arduinoTableWidget->setHorizontalHeaderItem(4, __qtablewidgetitem4);
        QTableWidgetItem *__qtablewidgetitem5 = new QTableWidgetItem();
        arduinoTableWidget->setHorizontalHeaderItem(5, __qtablewidgetitem5);
        arduinoTableWidget->setObjectName(QStringLiteral("arduinoTableWidget"));

        verticalLayout->addWidget(arduinoTableWidget);

        buttonBox = new QDialogButtonBox(AddArduinoDialog);
        buttonBox->setObjectName(QStringLiteral("buttonBox"));
        buttonBox->setOrientation(Qt::Horizontal);
        buttonBox->setStandardButtons(QDialogButtonBox::Cancel|QDialogButtonBox::Ok);

        verticalLayout->addWidget(buttonBox);


        retranslateUi(AddArduinoDialog);
        QObject::connect(buttonBox, SIGNAL(accepted()), AddArduinoDialog, SLOT(accept()));
        QObject::connect(buttonBox, SIGNAL(rejected()), AddArduinoDialog, SLOT(reject()));

        QMetaObject::connectSlotsByName(AddArduinoDialog);
    } // setupUi

    void retranslateUi(QDialog *AddArduinoDialog)
    {
        AddArduinoDialog->setWindowTitle(QApplication::translate("AddArduinoDialog", "Add Arduino", nullptr));
        QTableWidgetItem *___qtablewidgetitem = arduinoTableWidget->horizontalHeaderItem(0);
        ___qtablewidgetitem->setText(QApplication::translate("AddArduinoDialog", "Select", nullptr));
        QTableWidgetItem *___qtablewidgetitem1 = arduinoTableWidget->horizontalHeaderItem(1);
        ___qtablewidgetitem1->setText(QApplication::translate("AddArduinoDialog", "Port", nullptr));
        QTableWidgetItem *___qtablewidgetitem2 = arduinoTableWidget->horizontalHeaderItem(2);
        ___qtablewidgetitem2->setText(QApplication::translate("AddArduinoDialog", "Name", nullptr));
        QTableWidgetItem *___qtablewidgetitem3 = arduinoTableWidget->horizontalHeaderItem(3);
        ___qtablewidgetitem3->setText(QApplication::translate("AddArduinoDialog", "Description", nullptr));
        QTableWidgetItem *___qtablewidgetitem4 = arduinoTableWidget->horizontalHeaderItem(4);
        ___qtablewidgetitem4->setText(QApplication::translate("AddArduinoDialog", "Serial Number", nullptr));
        QTableWidgetItem *___qtablewidgetitem5 = arduinoTableWidget->horizontalHeaderItem(5);
        ___qtablewidgetitem5->setText(QApplication::translate("AddArduinoDialog", "Manufacturer", nullptr));
    } // retranslateUi

};

namespace Ui {
    class AddArduinoDialog: public Ui_AddArduinoDialog {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_PICKARDUINODIALOG_H
