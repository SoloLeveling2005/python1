# -*- coding: utf-8 -*-

# ИМПОРТИРУЕМ БИБЛИОТЕКИ


# Импортируем библиотеку для работы с комндной строкой Windows
import sys
import os.path
import os

# Импортируем библиотеки многопоточности
import threading
from threading import Thread

# Импортируем библиотеки для создания презентабельности проекта
from PySide6 import QtCore, QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLabel, QLineEdit, QPushButton, QCheckBox
from PySide6.QtGui import QPalette, QColor
from PySide6.QtCore import QSize, Qt

# Импортируем библиотеку для работы со временем
import time

# КОНТЕНТ

status_in_virtual = False
#  Очищаем старый скрипт чтобы не возникло ошибок
file = open("script.bat", "w+")
file.write("")
file.close()
#  Очищаем прошлый скрипт чтобы не возникло ошибок

class MainWindow(QWidget):  # MainWindow - класс наследник(дочерний) от класса QWidget(родитель)
    def __init__(self, width=640, height=480, title="title"):
        QWidget.__init__(self)  # тут происходит вызов конструктора для родителя
        self.setWindowTitle(title)
        self.resize(width, height)

        self.layout = QGridLayout()
        self.setLayout(self.layout)

        self.input = QLineEdit()
        self.layout.addWidget(self.input, 0, 0)

        self.label_create = QLabel('Введите название папки, чтобы создать ее:')
        self.layout.addWidget(self.label_create, 1, 0)
        self.push_button_create = QPushButton('Создать')
        self.layout.addWidget(self.push_button_create, 2, 0)
        self.push_button_create.clicked.connect(self.create_and_log_in_virtual_start)

        self.label_log_in = QLabel('Введите название папки, чтобы войти:')
        self.layout.addWidget(self.label_log_in, 3, 0)
        self.push_button_log_in = QPushButton('Войти')
        self.layout.addWidget(self.push_button_log_in, 4, 0)
        self.push_button_log_in.clicked.connect(self.log_in_virtual_start)
        # self.push_button_log_in.setStyleSheet("background-color:rgba(128, 128, 128, 0.3);color:rgba(0, 0, 0, 0.3);")

        self.label_log_out = QLabel('Выйти из виртуального окружения:')
        self.layout.addWidget(self.label_log_out, 5, 0)
        self.push_button_log_out = QPushButton('Выйти')
        self.layout.addWidget(self.push_button_log_out, 6, 0)
        self.push_button_log_out.clicked.connect(self.log_out_virtual_start)
        self.push_button_log_out.setStyleSheet("background-color:rgba(128, 128, 128, 0.3);color:rgba(0, 0, 0, 0.3);")


        self.label_pip = QLabel('Введите название библиотеки для загрузки:')
        self.layout.addWidget(self.label_pip, 7, 0)
        self.push_button_pip = QPushButton('Загрузить')
        self.layout.addWidget(self.push_button_pip, 8, 0)
        self.push_button_pip.clicked.connect(self.pip_library)
        self.push_button_pip.setStyleSheet("background-color:rgba(128, 128, 128, 0.3);color:rgba(0, 0, 0, 0.3);")


        self.label_freeze = QLabel('Заморозить модули и библиотеки:')
        self.layout.addWidget(self.label_freeze, 9, 0)
        self.push_button_freeze = QPushButton('Заморозить')
        self.layout.addWidget(self.push_button_freeze, 10, 0)
        self.push_button_freeze.clicked.connect(self.freeze)
        self.push_button_freeze.setStyleSheet("background-color:rgba(128, 128, 128, 0.3);color:rgba(0, 0, 0, 0.3);")

        self.label_pip_freeze = QLabel('Разморозить модули и библиотеки:')
        self.layout.addWidget(self.label_pip_freeze, 11, 0)
        self.push_button_pip_freeze = QPushButton('Разморозить')
        self.layout.addWidget(self.push_button_pip_freeze, 12, 0)
        self.push_button_pip_freeze.clicked.connect(self.pip_freeze)
        self.push_button_pip_freeze.setStyleSheet("background-color:rgba(128, 128, 128, 0.3);color:rgba(0, 0, 0, 0.3);")

        self.label_info = QLabel('Нет новостей')
        self.layout.addWidget(self.label_info, 15, 0)



        self.show()

    def start_creating_a_virtual_environment(self):
        # print(no)
        name_virtual_environment = self.input.text()
        if len(name_virtual_environment) < 1:
            self.label_info.setText('Имя слишком коротко')
            time.sleep(3)
            self.label_info.setText('Нет новостей')
        else:
            python_venv = str('python -m venv ' + str(name_virtual_environment))
            file = open("script.bat", "w+")
            file.write(python_venv)
            file.close()
            os.system('script.bat')

            self.label_info.setText('Была создана папка под виртуальное окружение')
            # self.push_button_log_in.setStyleSheet("background-color:;color:;")


    def start_log_in_a_virtual_environment(self):
        name_virtual_environment = self.input.text()
        if len(name_virtual_environment) < 1:
            self.label_info.setText('Имя слишком коротко')
            time.sleep(3)
            self.label_info.setText('Нет новостей')
        else:
            if os.path.exists(name_virtual_environment) is True:
                python_venv = str('call '+str(name_virtual_environment)+'/Scripts/activate.bat')
                file = open("log_in.bat", "w+")
                file.write(python_venv)
                file.close()
                os.system('log_in.bat')

                self.label_info.setText('Вы вошли в виртуального окружения')
                self.push_button_log_out.setStyleSheet("background-color:;color:;")
                self.push_button_freeze.setStyleSheet("background-color:;color:;")
                self.push_button_pip.setStyleSheet("background-color:;color:;")
                self.push_button_pip_freeze.setStyleSheet("background-color:;color:;")

                time.sleep(3)
                self.label_info.setText('Нет новостей')
                print("Вошли")
                global status_in_virtual
                status_in_virtual = True

            else:
                self.label_info.setText('Виртуальное окружение на создано')
                time.sleep(3)
                self.label_info.setText('Нет новостей')

    def start_log_out_a_virtual_environment(self):
        if status_in_virtual == True:
            file = open("log_in.bat", "w+")
            file.write("")
            file.close()

            self.label_info.setText('Вы вышли из виртуального окружения')
            self.push_button_log_out.setStyleSheet("background-color:rgba(128, 128, 128, 0.3);color:rgba(0, 0, 0, 0.3);")
            self.push_button_freeze.setStyleSheet("background-color:rgba(128, 128, 128, 0.3);color:rgba(0, 0, 0, 0.3);")
            self.push_button_pip.setStyleSheet("background-color:rgba(128, 128, 128, 0.3);color:rgba(0, 0, 0, 0.3);")
            self.push_button_pip_freeze.setStyleSheet("background-color:rgba(128, 128, 128, 0.3);color:rgba(0, 0, 0, 0.3);")

            time.sleep(3)
            self.label_info.setText('Нет новостей')
            print("Вышли")


    def start_freeze(self):
        if status_in_virtual == True:
            self.label_info.setText('Начинаем заморозку')
            file_text = open('log_in.bat', 'r').read()
            text = file_text+" \npython -m pip install --upgrade pip \npip freeze > requirement.txt"
            file = open("script.bat", "w+")
            file.write(text)
            file.close()
            os.system('script.bat')
            self.label_info.setText('Вы заморозили библиотеки и модули')
            time.sleep(3)
            self.label_info.setText('Нет новостей')

    def start_pip_freeze(self):
        name_virtual_environment = self.input.text()
        if status_in_virtual == True:
            if len(name_virtual_environment) < 1:
                self.label_info.setText('Имя слишком коротко')
                time.sleep(3)
                self.label_info.setText('Нет новостей')
            else:
                if os.path.exists(name_virtual_environment) is True:
                    file_text = open('log_in.bat', 'r').read()
                    file = open("script.bat", "w+")
                    text = file_text + "\npython -m pip install --upgrade pip \npip install -r requirement.txt"
                    file.write(text)
                    file.close()
                    os.system('script.bat')
                    self.label_info.setText('Вы разморозили библиотеки и модули')
                    time.sleep(3)
                    self.label_info.setText('Нет новостей')

    def start_pip_library(self):
        if status_in_virtual == True:
            name_virtual_environment = self.input.text()
            file_text = open('log_in.bat', 'r').read()
            file = open("pip_library.bat", "w+")
            file.write(str(file_text)+"\npython -m pip install --upgrade pip \npip install " + str(name_virtual_environment))
            file.close()
            os.system('pip_library.bat')

            self.label_info.setText('Вы загрузили библиотеку или модуль ' + str(name_virtual_environment))
            time.sleep(3)
            self.label_info.setText('Нет новостей')



    def create_and_log_in_virtual_start(self):
        Thread(target=self.start_creating_a_virtual_environment).start()

    def log_in_virtual_start(self):
        Thread(target=self.start_log_in_a_virtual_environment).start()

    def log_out_virtual_start(self):
        Thread(target=self.start_log_out_a_virtual_environment).start()

    def freeze(self):
        Thread(target=self.start_freeze).start()

    def pip_library(self):
        Thread(target=self.start_pip_library).start()

    def pip_freeze(self):
        Thread(target=self.start_pip_freeze).start()
    # def freeze_virtual_start(self):
    #     Thread(target=self.freeze_virtual).start()
    # file_text = open('script.bat','r').read()
    # print(os.path.exists("file"))  # Проверка на существование папки
app = QApplication(sys.argv)
mw = MainWindow(440, 280, 'Работа с виртуальным окружением')
app.exec()
