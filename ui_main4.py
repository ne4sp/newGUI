# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main4.ui'
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
from PySide6.QtWidgets import (QApplication, QGraphicsView, QGridLayout, QHBoxLayout,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QWidget)
import pyqtgraph as pg

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QSize(800, 600))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.leftButton = QPushButton(self.centralwidget)
        self.leftButton.setObjectName(u"leftButton")

        self.horizontalLayout_3.addWidget(self.leftButton)

        self.rightButton = QPushButton(self.centralwidget)
        self.rightButton.setObjectName(u"rightButton")

        self.horizontalLayout_3.addWidget(self.rightButton)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.editButton = QPushButton(self.centralwidget)
        self.editButton.setObjectName(u"editButton")

        self.horizontalLayout_2.addWidget(self.editButton)

        self.showButton = QPushButton(self.centralwidget)
        self.showButton.setObjectName(u"showButton")

        self.horizontalLayout_2.addWidget(self.showButton)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)


        self.gridLayout.addLayout(self.horizontalLayout_4, 1, 3, 1, 1)

        self.graphicsView = pg.PlotWidget(self.centralwidget)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.addLegend()

        self.gridLayout.addWidget(self.graphicsView, 0, 2, 1, 2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.inputButton = QPushButton(self.centralwidget)
        self.inputButton.setObjectName(u"inputButton")

        self.horizontalLayout.addWidget(self.inputButton)

        self.inputLine = QLineEdit(self.centralwidget)
        self.inputLine.setObjectName(u"inputLine")

        self.horizontalLayout.addWidget(self.inputLine)


        self.gridLayout.addLayout(self.horizontalLayout, 1, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"DUK Graphics", None))
        self.leftButton.setText(QCoreApplication.translate("MainWindow", u"<-", None))
        self.rightButton.setText(QCoreApplication.translate("MainWindow", u"->", None))
        self.editButton.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.showButton.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0440\u0430\u0444\u0438\u043a", None))
        self.inputButton.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
        self.inputLine.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043f\u0443\u0442\u044c \u043a .log \u0444\u0430\u0439\u043b\u0443", None))
    # retranslateUi

