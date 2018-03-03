/********************************************************************************
** Form generated from reading UI file 'pwmEditForm.ui'
**
** Created by: Qt User Interface Compiler version 5.10.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_PWMEDITFORM_H
#define UI_PWMEDITFORM_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QComboBox>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QSpacerItem>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_pwmEditForm
{
public:
    QGridLayout *gridLayout;
    QLabel *PWMoutValueLabel;
    QLabel *drefInfoLabel;
    QSpacerItem *horizontalSpacer;
    QLabel *label_7;
    QLineEdit *drefLineEdit;
    QLabel *label_4;
    QSpacerItem *verticalSpacer;
    QLineEdit *drefIndexLineEdit;
    QLabel *label_19;
    QLabel *label_18;
    QPushButton *pushButton;
    QComboBox *PIN_comboBox;
    QLineEdit *IDlineEdit;
    QSpacerItem *verticalSpacer_2;
    QLabel *label_3;
    QLabel *label_6;
    QLabel *drefValueLabel;
    QLabel *label_5;
    QLabel *label_8;
    QLabel *label;
    QLineEdit *nameLineEdit;
    QLineEdit *pwmOutputLineEdit;
    QLabel *label_2;
    QLabel *drefsHelpText;

    void setupUi(QWidget *pwmEditForm)
    {
        if (pwmEditForm->objectName().isEmpty())
            pwmEditForm->setObjectName(QStringLiteral("pwmEditForm"));
        pwmEditForm->resize(832, 674);
        QSizePolicy sizePolicy(QSizePolicy::Expanding, QSizePolicy::Expanding);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(pwmEditForm->sizePolicy().hasHeightForWidth());
        pwmEditForm->setSizePolicy(sizePolicy);
        gridLayout = new QGridLayout(pwmEditForm);
        gridLayout->setObjectName(QStringLiteral("gridLayout"));
        gridLayout->setSizeConstraint(QLayout::SetDefaultConstraint);
        gridLayout->setHorizontalSpacing(1);
        PWMoutValueLabel = new QLabel(pwmEditForm);
        PWMoutValueLabel->setObjectName(QStringLiteral("PWMoutValueLabel"));

        gridLayout->addWidget(PWMoutValueLabel, 11, 6, 1, 1);

        drefInfoLabel = new QLabel(pwmEditForm);
        drefInfoLabel->setObjectName(QStringLiteral("drefInfoLabel"));
        QSizePolicy sizePolicy1(QSizePolicy::Preferred, QSizePolicy::Preferred);
        sizePolicy1.setHorizontalStretch(0);
        sizePolicy1.setVerticalStretch(0);
        sizePolicy1.setHeightForWidth(drefInfoLabel->sizePolicy().hasHeightForWidth());
        drefInfoLabel->setSizePolicy(sizePolicy1);
        drefInfoLabel->setMaximumSize(QSize(350, 16777215));
        drefInfoLabel->setWordWrap(true);

        gridLayout->addWidget(drefInfoLabel, 7, 2, 1, 1);

        horizontalSpacer = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout->addItem(horizontalSpacer, 7, 7, 1, 1);

        label_7 = new QLabel(pwmEditForm);
        label_7->setObjectName(QStringLiteral("label_7"));

        gridLayout->addWidget(label_7, 11, 5, 1, 1);

        drefLineEdit = new QLineEdit(pwmEditForm);
        drefLineEdit->setObjectName(QStringLiteral("drefLineEdit"));
        drefLineEdit->setMinimumSize(QSize(400, 0));
        drefLineEdit->setMaximumSize(QSize(350, 16777215));

        gridLayout->addWidget(drefLineEdit, 6, 2, 1, 2);

        label_4 = new QLabel(pwmEditForm);
        label_4->setObjectName(QStringLiteral("label_4"));
        label_4->setAlignment(Qt::AlignLeading|Qt::AlignLeft|Qt::AlignTop);

        gridLayout->addWidget(label_4, 11, 0, 1, 1);

        verticalSpacer = new QSpacerItem(20, 26, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout->addItem(verticalSpacer, 14, 2, 1, 1);

        drefIndexLineEdit = new QLineEdit(pwmEditForm);
        drefIndexLineEdit->setObjectName(QStringLiteral("drefIndexLineEdit"));
        drefIndexLineEdit->setMaximumSize(QSize(40, 16777215));

        gridLayout->addWidget(drefIndexLineEdit, 10, 2, 1, 1);

        label_19 = new QLabel(pwmEditForm);
        label_19->setObjectName(QStringLiteral("label_19"));

        gridLayout->addWidget(label_19, 3, 0, 1, 1);

        label_18 = new QLabel(pwmEditForm);
        label_18->setObjectName(QStringLiteral("label_18"));

        gridLayout->addWidget(label_18, 4, 0, 1, 1);

        pushButton = new QPushButton(pwmEditForm);
        pushButton->setObjectName(QStringLiteral("pushButton"));
        pushButton->setMinimumSize(QSize(25, 20));
        pushButton->setMaximumSize(QSize(50, 16777215));

        gridLayout->addWidget(pushButton, 6, 5, 1, 1);

        PIN_comboBox = new QComboBox(pwmEditForm);
        PIN_comboBox->setObjectName(QStringLiteral("PIN_comboBox"));
        PIN_comboBox->setMaximumSize(QSize(50, 16777215));

        gridLayout->addWidget(PIN_comboBox, 4, 2, 1, 1);

        IDlineEdit = new QLineEdit(pwmEditForm);
        IDlineEdit->setObjectName(QStringLiteral("IDlineEdit"));
        IDlineEdit->setEnabled(false);
        IDlineEdit->setMinimumSize(QSize(250, 0));
        IDlineEdit->setMaximumSize(QSize(350, 16777215));
        IDlineEdit->setReadOnly(true);

        gridLayout->addWidget(IDlineEdit, 3, 2, 1, 3);

        verticalSpacer_2 = new QSpacerItem(20, 10, QSizePolicy::Minimum, QSizePolicy::Fixed);

        gridLayout->addItem(verticalSpacer_2, 5, 0, 1, 1);

        label_3 = new QLabel(pwmEditForm);
        label_3->setObjectName(QStringLiteral("label_3"));
        QSizePolicy sizePolicy2(QSizePolicy::Minimum, QSizePolicy::Minimum);
        sizePolicy2.setHorizontalStretch(0);
        sizePolicy2.setVerticalStretch(0);
        sizePolicy2.setHeightForWidth(label_3->sizePolicy().hasHeightForWidth());
        label_3->setSizePolicy(sizePolicy2);
        label_3->setLayoutDirection(Qt::LeftToRight);

        gridLayout->addWidget(label_3, 2, 0, 1, 1);

        label_6 = new QLabel(pwmEditForm);
        label_6->setObjectName(QStringLiteral("label_6"));

        gridLayout->addWidget(label_6, 7, 5, 1, 1);

        drefValueLabel = new QLabel(pwmEditForm);
        drefValueLabel->setObjectName(QStringLiteral("drefValueLabel"));

        gridLayout->addWidget(drefValueLabel, 7, 6, 1, 1);

        label_5 = new QLabel(pwmEditForm);
        label_5->setObjectName(QStringLiteral("label_5"));

        gridLayout->addWidget(label_5, 7, 0, 1, 1);

        label_8 = new QLabel(pwmEditForm);
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

        gridLayout->addWidget(label_8, 0, 0, 1, 8);

        label = new QLabel(pwmEditForm);
        label->setObjectName(QStringLiteral("label"));

        gridLayout->addWidget(label, 10, 0, 1, 1);

        nameLineEdit = new QLineEdit(pwmEditForm);
        nameLineEdit->setObjectName(QStringLiteral("nameLineEdit"));
        nameLineEdit->setMinimumSize(QSize(250, 0));
        nameLineEdit->setMaximumSize(QSize(350, 16777215));

        gridLayout->addWidget(nameLineEdit, 2, 2, 1, 3);

        pwmOutputLineEdit = new QLineEdit(pwmEditForm);
        pwmOutputLineEdit->setObjectName(QStringLiteral("pwmOutputLineEdit"));
        QSizePolicy sizePolicy3(QSizePolicy::Expanding, QSizePolicy::Fixed);
        sizePolicy3.setHorizontalStretch(0);
        sizePolicy3.setVerticalStretch(0);
        sizePolicy3.setHeightForWidth(pwmOutputLineEdit->sizePolicy().hasHeightForWidth());
        pwmOutputLineEdit->setSizePolicy(sizePolicy3);
        pwmOutputLineEdit->setMinimumSize(QSize(400, 0));
        pwmOutputLineEdit->setMaximumSize(QSize(350, 16777215));
        pwmOutputLineEdit->setAlignment(Qt::AlignLeading|Qt::AlignLeft|Qt::AlignTop);

        gridLayout->addWidget(pwmOutputLineEdit, 11, 2, 1, 1);

        label_2 = new QLabel(pwmEditForm);
        label_2->setObjectName(QStringLiteral("label_2"));

        gridLayout->addWidget(label_2, 6, 0, 1, 1);

        drefsHelpText = new QLabel(pwmEditForm);
        drefsHelpText->setObjectName(QStringLiteral("drefsHelpText"));
        QSizePolicy sizePolicy4(QSizePolicy::Expanding, QSizePolicy::Minimum);
        sizePolicy4.setHorizontalStretch(0);
        sizePolicy4.setVerticalStretch(0);
        sizePolicy4.setHeightForWidth(drefsHelpText->sizePolicy().hasHeightForWidth());
        drefsHelpText->setSizePolicy(sizePolicy4);
        drefsHelpText->setMinimumSize(QSize(350, 0));
        drefsHelpText->setMaximumSize(QSize(600, 16777215));
        drefsHelpText->setTextFormat(Qt::RichText);
        drefsHelpText->setAlignment(Qt::AlignLeading|Qt::AlignLeft|Qt::AlignTop);
        drefsHelpText->setWordWrap(true);

        gridLayout->addWidget(drefsHelpText, 12, 2, 1, 5);


        retranslateUi(pwmEditForm);
        QObject::connect(nameLineEdit, SIGNAL(editingFinished()), pwmEditForm, SLOT(updateXMLdata()));
        QObject::connect(PIN_comboBox, SIGNAL(currentIndexChanged(int)), pwmEditForm, SLOT(updateXMLdata()));
        QObject::connect(PIN_comboBox, SIGNAL(currentTextChanged(QString)), pwmEditForm, SLOT(updatePin()));
        QObject::connect(pushButton, SIGNAL(clicked()), pwmEditForm, SLOT(editXPDataref()));
        QObject::connect(drefLineEdit, SIGNAL(editingFinished()), pwmEditForm, SLOT(updateXMLdata()));
        QObject::connect(pwmOutputLineEdit, SIGNAL(editingFinished()), pwmEditForm, SLOT(updateXMLdata()));
        QObject::connect(drefLineEdit, SIGNAL(textChanged(QString)), pwmEditForm, SLOT(updateXMLdata()));
        QObject::connect(drefIndexLineEdit, SIGNAL(editingFinished()), pwmEditForm, SLOT(updateXMLdata()));

        QMetaObject::connectSlotsByName(pwmEditForm);
    } // setupUi

    void retranslateUi(QWidget *pwmEditForm)
    {
        pwmEditForm->setWindowTitle(QApplication::translate("pwmEditForm", "Form", nullptr));
        PWMoutValueLabel->setText(QApplication::translate("pwmEditForm", "TextLabel", nullptr));
        drefInfoLabel->setText(QString());
        label_7->setText(QApplication::translate("pwmEditForm", " PWM Output Value  ", nullptr));
        label_4->setText(QApplication::translate("pwmEditForm", "PWM Output Values:  ", nullptr));
        label_19->setText(QApplication::translate("pwmEditForm", "ID", nullptr));
        label_18->setText(QApplication::translate("pwmEditForm", "Arduino pin:", nullptr));
        pushButton->setText(QApplication::translate("pwmEditForm", "Pick ...", nullptr));
        label_3->setText(QApplication::translate("pwmEditForm", "Name", nullptr));
        label_6->setText(QApplication::translate("pwmEditForm", " Dataref Value  ", nullptr));
        drefValueLabel->setText(QString());
        label_5->setText(QApplication::translate("pwmEditForm", "Dataref Info", nullptr));
        label_8->setText(QApplication::translate("pwmEditForm", "Edit PWM output", nullptr));
        label->setText(QApplication::translate("pwmEditForm", "Dataref index", nullptr));
        label_2->setText(QApplication::translate("pwmEditForm", "XPlane Dataref:", nullptr));
        drefsHelpText->setText(QApplication::translate("pwmEditForm", "<html><head/><body><p>Enter series of points: [Dataref input value, output PWM value]. The output value of the PWM in between 2 points will be linearly interpolated. Note the PWM output values must be between 0 (off) and 255 (fully on)</p><p>For example to set the PWM output to vary linearly between 10 and 255 when the dataref value varies between 0 and 1.0, enter: </p><p><span style=\" color:#0000ff;\">[0,10], [1.0,300]</span></p></body></html>", nullptr));
    } // retranslateUi

};

namespace Ui {
    class pwmEditForm: public Ui_pwmEditForm {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_PWMEDITFORM_H
