# -*- coding: utf-8 -*-
import sys
import threading
from time import *
from threading import Thread
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLabel, QLineEdit, QPushButton
from PySide6.QtGui import QPalette, QColor
from PySide6 import QtCore, QtWidgets
import time

import sys

from PySide6.QtCore import QSize, Qt





class MainWindow(QWidget):  # MainWindow - класс наследник(дочерний) от класса QWidget(родитель)
    def __init__(self, width=640, height=480, title="title"):
        QWidget.__init__(self)  # тут происходит вызов конструктора для родителя
        self.setWindowTitle(title)
        self.resize(width, height)

        self.layout = QGridLayout()  # экземпляр класса интерфейса grid(сетка)
        self.setLayout(self.layout)  # вкладываем QGridLayout -> MainWindow(QWidget)

        self.line_edit_path = QLineEdit('1:30:30')  # экзампляр строки ввода текста
        self.layout.addWidget(self.line_edit_path, 0, 0)  # вкладываем QLineEdit -> QGridLayout

        self.label_check = QLabel('00:00:00')  # экзампляр строки текста
        self.layout.addWidget(self.label_check, 1, 0)

        self.push_button_stop = QPushButton('stop')  # экзампляр строки ввода текста
        self.layout.addWidget(self.push_button_stop, 2, 2)  # вкладываем QLineEdit -> QGridLayout
        self.push_button_stop.clicked.connect(self.stop_timer)
        self.push_button_reset = QPushButton('reset')  # экзампляр строки ввода текста
        self.layout.addWidget(self.push_button_reset, 2, 3)  # вкладываем QLineEdit -> QGridLayout
        self.push_button_reset.clicked.connect(self.reset_timer)
        self.push_button_start = QPushButton('start')  # экзампляр строки ввода текста
        self.layout.addWidget(self.push_button_start, 2, 4)  # вкладываем QLineEdit -> QGridLayout
        self.push_button_start.clicked.connect(self.start)
        self.show()


    def start(self):
        Thread(target=self.start_timer).start()

    def stop_timer(self):
        global pause
        pause = False
        global hours
        global minutes
        global seconds
        global summa
        summa = self.label_check.text()

    def reset_timer(self):
        global summa
        summa = "00:00:00"
        self.label_check.setText(summa)


    def start_timer(self):
        value = self.line_edit_path.text()
        print(value)
        times = value
        times = times.split(":")
        print(times)
        global hours
        global minutes
        global seconds

        hours = int(times[0])
        minutes = int(times[1])
        seconds = int(times[2])

        global pause

        pause = True

        # код до цикла
        while pause:
            # seconds = seconds + 1
            seconds -= 1

            if seconds < 1:
                minutes -= 1
                seconds = 59

            if minutes < 1:
                hours -= 1
                minutes = 59

            if hours < 1:
                seconds = 0
                minutes = 0
                hours = 0

            time.sleep(0.05)

            summa = str(hours) + ":" + str(minutes) + ":" + str(seconds)
            self.label_check.setText(summa)
            print(f"{hours}:{minutes}" + ":" + str(seconds))









app = QApplication(sys.argv)
mw = MainWindow(640, 480, 'My App')
app.exec()