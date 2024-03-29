# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings2.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDateTimeEdit, QDialog,
    QDialogButtonBox, QDoubleSpinBox, QGridLayout, QHBoxLayout,
    QLabel, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(195, 278)
        self.gridLayout_2 = QGridLayout(Dialog)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.changeDate1 = QDateTimeEdit(Dialog)
        self.changeDate1.setObjectName(u"changeDate1")
        self.changeDate1.setMinimumDateTime(QDateTime(QDate(2024, 3, 12), QTime(10, 10, 10)))
        self.changeDate1.setCalendarPopup(False)

        self.horizontalLayout.addWidget(self.changeDate1)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.changeDate2 = QDateTimeEdit(Dialog)
        self.changeDate2.setObjectName(u"changeDate2")
        self.changeDate2.setMinimumDateTime(QDateTime(QDate(2024, 3, 12), QTime(10, 10, 10)))
        self.changeDate2.setCalendarPopup(False)

        self.horizontalLayout_2.addWidget(self.changeDate2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_4.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.t1Change = QDoubleSpinBox(Dialog)
        self.t1Change.setObjectName(u"t1Change")

        self.horizontalLayout_3.addWidget(self.t1Change)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.t2Change = QDoubleSpinBox(Dialog)
        self.t2Change.setObjectName(u"t2Change")

        self.horizontalLayout_4.addWidget(self.t2Change)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_5.addWidget(self.label_5)

        self.rv1Change = QDoubleSpinBox(Dialog)
        self.rv1Change.setObjectName(u"rv1Change")

        self.horizontalLayout_5.addWidget(self.rv1Change)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_6.addWidget(self.label_6)

        self.rv2Change = QDoubleSpinBox(Dialog)
        self.rv2Change.setObjectName(u"rv2Change")

        self.horizontalLayout_6.addWidget(self.rv2Change)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)


        self.gridLayout.addLayout(self.verticalLayout_4, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.gridLayout_2.addWidget(self.buttonBox, 1, 0, 1, 1)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi


    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"settings", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"from", None))
        self.changeDate1.setDisplayFormat(QCoreApplication.translate("Dialog", u"yyyy/MM/dd H:mm", None))
        self.changeDate2.setDisplayFormat(QCoreApplication.translate("Dialog", u"yyyy/MM/dd H:mm", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"to", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"t1", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"t2", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"rv1", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"rv2", None))
    # retranslateUi

