#!/usr/bin/env python3
# coding=utf-8

import sys
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import pyqtSlot
from PyQt5 import uic,QtGui
import random

class Example(QWidget):

    def __init__(self):
        super().__init__()
        QWidget.__init__(self)
        self.initUI()

    def initUI(self):
        self.table = QTableWidget(self)
        btn1 = QPushButton("Заполнить", self)
        btn2 = QPushButton("Выполнить", self)
        self.label = QLabel(self)
        self.setWindowIcon(QtGui.QIcon('images/logo.png'))

        self.table.setGeometry(10, 10, 540, 160)
        btn1.setGeometry(560, 10, 140, 40)
        self.table.setColumnCount(5)
        self.table.setRowCount(4)
        btn2.setGeometry(560, 60, 140, 40)
        self.label.setGeometry(10, 180, 520, 40)

        btn1.clicked.connect(self.btn1Click)
        btn2.clicked.connect(self.btn2Click)

        self.setGeometry(400, 400, 780, 350)
        self.setWindowTitle('Задание 3')
        self.show()

    def btn1Click(self):
        x = 0
        while x < 5:
            y = 0
            while y < 4:
                self.table.setItem(y, x, QTableWidgetItem(str(random.randint(-9,9))))
                y = y + 1
            x = x + 1
    def btn2Click(self):
        zero = 0
        x = 0
        while x < 5:
            y = 0
            while y < 4:
                v = int(self.table.item(y, x).text())
                if v == 0: zero = zero + 1
                y = y + 1
            x = x + 1
        x = 0
        while x < 5:
            y = 0
            while y < 4:
                v = int(self.table.item(y, x).text())
                if v < 0: self.table.setItem(y, x, QTableWidgetItem(str(zero)))
                y = y + 1
            x = x + 1
    def buttonExit(self):
       QApplication.exit()
if __name__=='__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
