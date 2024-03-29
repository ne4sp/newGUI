import sys
import numpy as np
import pyqtgraph as pg

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QDialog, QMessageBox
from PySide6.QtCore import QDateTime, QDate, QTime

from ui_main4 import Ui_MainWindow
from settings4_ui import Ui_settings
from checkLog import createtemp
from createBase import buildbd, tclean, rvclean, dateclean, st

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.new_window = QDialog()
        self.ui_window = Ui_settings()

        self.ui.editButton.clicked.connect(self.open_settings_window)
        self.ui.editButton.setEnabled(False)
        self.ui.inputButton.clicked.connect(self.choose_file_input)
        self.ui.showButton.clicked.connect(self.showgp)
        self.ui.showButton.clicked.connect(self.ub3)
        self.ui.showButton.setEnabled(False)

        self.ui.leftButton.clicked.connect(self.swipe_left_gp)
        self.ui.leftButton.setEnabled(False)
        self.ui.rightButton.clicked.connect(self.swipe_right_gp)
        self.ui.rightButton.setEnabled(False)
        self.bd = []
        self.iter_k = 0
        self.iter_j = 1
        self.path = 'temp2.txt'
        self.ui.inputLine.textChanged.connect(self.unblock_btns)

    def unblock_btns(self):
        if (self.ui.inputLine.text()[:3] == 'C:/') and (self.ui.inputLine.text()[-3:] == 'log'):
            self.ui.editButton.setEnabled(True)

    def ub2(self):
        print(type(self.bd))
        if len(self.bd) > 0:
            self.ui.showButton.setEnabled(True)

    def ub3(self):
        self.ui.leftButton.setEnabled(True)
        self.ui.rightButton.setEnabled(True)

    def open_settings_window(self):
        createtemp(self.ui.inputLine.text())
        self.ui_window.setupUi(self.new_window)
        self.new_window.show()
        self.ui_window.confirmButton.clicked.connect(self.create_db)
        self.ui_window.confirmButton.clicked.connect(self.ub2)

    def create_db(self):
        db = buildbd(self.path)
        print(db)
        self.bd = db
    def choose_file_input(self):
        self.ui.inputLine.setText(QFileDialog.getOpenFileName()[0])

    def swipe_left_gp(self):
        if self.iter_j-1 < 0:
            return QMessageBox().setWindowTitle('Ошибка')
        self.iter_j -= 1
        self.iter_k -= 1
        self.showgp()

    def swipe_right_gp(self):
        self.iter_j += 1
        self.iter_k += 1
        self.showgp()

    def showgp(self):
        colors = [
            [255, 255, 255], [255, 0, 0], [0, 255, 0], [0, 0, 255], [255, 255, 0],
            [0, 255, 255], [255, 0, 255], [128, 0, 0], [128, 128, 0], [0, 128, 0],
            [128, 0, 128], [0, 128, 128], [0, 0, 128], [255, 140, 0], [139, 69, 19],
            [154, 205, 50], [0, 255, 127], [123, 104, 238], [210, 105, 30], [75, 0, 130],
            [0, 140, 255], [255, 176, 173], [212, 153, 58], [138, 208, 255], [221, 255, 0]
        ]
        bd = self.bd
        cl = 0
        x = np.arange(0, 128)
        self.ui.graphicsView.plot(clear='True')
        for i in range(25*self.iter_k, 25*self.iter_j):
            self.ui.graphicsView.plot(
                x, bd[i].lvpack, pen=pg.mkPen(color=(colors[cl][0], colors[cl][1], colors[cl][2])),
                name=bd[i].date[0] + '-' + bd[i].date[1] + "/t=" + bd[i].t + "/v=" + bd[i].rv)
            cl += 1






if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()


    sys.exit(app.exec())
