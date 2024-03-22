# -*- coding: utf-8 -*-
import numpy as np
import pyqtgraph as pg
################################################################################
## Form generated from reading UI file 'ui_main.ui'
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
from PySide6.QtWidgets import (QApplication, QGraphicsView, QHBoxLayout, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QWidget, QFileDialog)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.showButton = QPushButton(self.centralwidget)
        self.showButton.setObjectName(u"showButton")
        self.showButton.clicked.connect(self.showclk())
        self.showButton.setGeometry(QRect(690, 550, 101, 41))
        self.graphicsView = pg.PlotWidget(self.centralwidget)
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView.setGeometry(QRect(-10, -10, 821, 551))
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 560, 281, 26))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.inputButton = QPushButton(self.widget)
        self.inputButton.setObjectName(u"inputButton")
        self.inputButton.clicked.connect(self.the_button_was_clicked)

        self.horizontalLayout.addWidget(self.inputButton)

        self.inputLine = QLineEdit(self.widget)
        self.inputLine.setObjectName(u"inputLine")

        self.horizontalLayout.addWidget(self.inputLine)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def the_button_was_clicked(self):
        self.inputLine.setText(QFileDialog.getOpenFileName()[0])

    def showclk(self):
        x = 1
        y = 2
        self.graphicsView.plot(
            x, y,
            pen='r', symbol='o', symbolPen='r', symbolBrush=0.2, name='_red')
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"DUK Graphics", None))
        self.showButton.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0440\u0430\u0444\u0438\u043a", None))
        self.inputButton.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
        self.inputLine.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043f\u0443\u0442\u044c \u043a .log \u0444\u0430\u0439\u043b\u0443", None))
    # retranslateUi

