# -*- coding: utf-8 -*-








# my_file = open("BabyFile.bat", "w+")
# my_file.write("deactivate\ncall env/Scripts/activate.bat\npython -m pip install --upgrade pip\npip freeze > requirement.txt\ncmd")
# my_file.close()



# import os
# # os.system('dir c:\\')
# # os.system('cmd')
# import subprocess
#
import os
import sys
import threading
from time import *
from threading import Thread
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLabel, QLineEdit, QPushButton, QCheckBox
from PySide6.QtGui import QPalette, QColor
from PySide6 import QtCore, QtWidgets
import time

import sys

from PySide6.QtCore import QSize, Qt


# os.system('cmd')


class MainWindow(QWidget):  # MainWindow - класс наследник(дочерний) от класса QWidget(родитель)
    def __init__(self, width=640, height=480, title="title"):
        QWidget.__init__(self)  # тут происходит вызов конструктора для родителя
        self.setWindowTitle(title)
        self.resize(width, height)

        self.layout = QGridLayout()  # экземпляр класса интерфейса grid(сетка)
        self.setLayout(self.layout)  # вкладываем QGridLayout -> MainWindow(QWidget)

        self.label_check = QLabel('Создайте свое первое виртуальное окружение')  # экзампляр строки текста
        self.layout.addWidget(self.label_check, 0, 0)

        self.label_info = QLabel('Нет новостей')  # экзампляр строки текста
        self.layout.addWidget(self.label_info, 1, 0)

        self.push_button_create = QPushButton('Создать')
        self.layout.addWidget(self.push_button_create, 2, 0)
        self.push_button_create.clicked.connect(self.create_and_log_in_virtual_start)

        self.push_button_log_in = QPushButton('Войти')
        self.layout.addWidget(self.push_button_log_in, 2, 1)
        self.push_button_log_in.clicked.connect(self.log_in_virtual_start)

        self.push_button_log_out = QPushButton('Выйти из виртуального окружения')
        self.layout.addWidget(self.push_button_log_out, 2, 2)
        self.push_button_log_out.clicked.connect(self.log_out_virtual)

        self.push_button_freeze = QPushButton('Заморозить библиотеки')
        self.layout.addWidget(self.push_button_freeze, 2, 3)
        self.push_button_freeze.clicked.connect(self.freeze_virtual_start)

        self.widget = QCheckBox()
        self.widget.setCheckState(Qt.Checked)
        self.layout.addWidget(self.widget, 3, 4)



        # For tristate: widget.setCheckState(Qt.PartiallyChecked)
        # Or: widget.setTriState(True)
        # self.widget.clicked.connect(self.show_state)


        # self.label_check = QLabel('00:00:00')  # экзампляр строки текста
        # self.layout.addWidget(self.label_check, 1, 0)

        self.show()

    def create_and_log_in_virtual(self):

        os.system('python -m venv env')
        os.system('pip install --upgrade pip')
        # os.system('disconect_virtual.bat')
        self.label_info.setText('Была создана папка под виртуальное окружение')
        time.sleep(3)

        # print(activ)
        self.label_info.setText('Вы вошли в виртуальное окружение')

    def log_out_virtual(self):
        os.system('deactivate')
        self.label_info.setText('Вы вышли из виртуального окружения')
        time.sleep(2)
        self.label_info.setText('Нет новостей')

    def log_in_virtual(self):
        try:
            os.system('call env/Scripts/activate.bat')
            self.label_info.setText('Вы вошли в виртуального окружения')
            time.sleep(2)
            self.label_info.setText('Нет новостей')
        except:
            self.label_info.setText('Виртуальное окружение не создано')
            time.sleep(2)
            self.label_info.setText('Нет новостей')

    def freeze_virtual(self):
        os.system('activ.bat')
        self.label_info.setText('Вы заморозили библиотеки и модули')
        time.sleep(2)
        self.label_info.setText('Нет новостей')

    def create_and_log_in_virtual_start(self):
        Thread(target=self.create_and_log_in_virtual).start()

    def log_out_virtual_start(self):
        Thread(target=self.log_out_virtual).start()

    def log_in_virtual_start(self):
        Thread(target=self.log_in_virtual).start()

    def freeze_virtual_start(self):
        Thread(target=self.freeze_virtual).start()

        # self.push_button_stop = QPushButton('stop')  # экзампляр строки ввода текста
        # self.layout.addWidget(self.push_button_stop, 2, 2)  # вкладываем QLineEdit -> QGridLayout
        # # self.push_button_stop.clicked.connect(self.)
        # self.push_button_reset = QPushButton('reset')  # экзампляр строки ввода текста
        # self.layout.addWidget(self.push_button_reset, 2, 3)  # вкладываем QLineEdit -> QGridLayout
        # # self.push_button_reset.clicked.connect(self.)
        # self.push_button_start = QPushButton('start')  # экзампляр строки ввода текста
        # self.layout.addWidget(self.push_button_start, 2, 4)  # вкладываем QLineEdit -> QGridLayout
        # # self.push_button_start.clicked.connect(self.)


app = QApplication(sys.argv)
mw = MainWindow(640, 480, 'Работа с виртуальным окружением')
app.exec()
