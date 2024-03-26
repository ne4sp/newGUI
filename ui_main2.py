# -*- coding: utf-8 -*-
import numpy as np
################################################################################
## Form generated from reading UI file 'ui_main2.ui'
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
    QLineEdit, QMainWindow, QPushButton, QFileDialog, QSizePolicy,
    QWidget)
import pyqtgraph as pg
from checkLog import createtemp
from createBase import buildbd

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
        self.graphicsView = pg.PlotWidget(self.centralwidget)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.addLegend()

        self.gridLayout.addWidget(self.graphicsView, 0, 0, 1, 2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.inputButton = QPushButton(self.centralwidget)
        self.inputButton.setObjectName(u"inputButton")
        self.inputButton.clicked.connect(self.the_button_was_clicked)

        self.horizontalLayout.addWidget(self.inputButton)

        self.inputLine = QLineEdit(self.centralwidget)
        self.inputLine.setObjectName(u"inputLine")

        self.horizontalLayout.addWidget(self.inputLine)


        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.showButton = QPushButton(self.centralwidget)
        self.showButton.setObjectName(u"showButton")
        self.showButton.clicked.connect(self.showclk)

        self.gridLayout.addWidget(self.showButton, 1, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def the_button_was_clicked(self):
        self.inputLine.setText(QFileDialog.getOpenFileName()[0])


    def showclk(self):
        colors = [
            [0, 0, 0], [255, 0, 0], [0, 255, 0], [0, 0, 255], [255, 255, 0],
            [0, 255, 255], [255, 0, 255], [128, 0, 0], [128, 128, 0], [0, 128, 0],
            [128, 0, 128], [0, 128, 128], [0, 0, 128], [255, 140, 0], [139, 69, 19],
            [154, 205, 50], [0, 255, 127], [123, 104, 238], [210, 105, 30], [75, 0, 130],
            [0, 140, 255], [255, 176, 173], [212, 153, 58], [138, 208, 255], [221, 255, 0]
        ]
        createtemp(self.inputLine.text())
        bd = buildbd('temp2.txt')
        a = 255
        b = 0
        c = 0
        x = np.arange(0, 128)
        self.graphicsView.setBackground("w")
        for i in range(25):
            a -= 10
            b += 10
            c += 10
            self.graphicsView.plot(
                x, bd[i].lvpack, pen=pg.mkPen(color=(colors[i][0], colors[i][1], colors[i][2])), name=bd[i].date[0] + '-' + bd[i].date[1] + "/t=" + bd[i].t + "/v=" + bd[i].rv)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"DUK Graphics", None))
        self.inputButton.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
        self.inputLine.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043f\u0443\u0442\u044c \u043a .log \u0444\u0430\u0439\u043b\u0443", None))
        self.showButton.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0440\u0430\u0444\u0438\u043a", None))
    # retranslateUi

