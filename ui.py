# импорт всей библиотеки
import time

# импорт всех функций, классов и переменных из библиотеки ! Может вызвать коллизию имён !
# from tkinter import *

# импорт всей библиотеки с присовением псевдонима
# import tkinter as tk


# импорт отдельной функции из модуля(из нашего файла)
# from .calc import calc_3


# импортируем библиотеку для работы с окнами(интерфейсом) все библиотеки: tkinter pyqt5 pyside6


# import tkinter
# import tkinter.ttk as ttk
# root = tkinter.Tk()
# frm = ttk.Frame(root, padding=10)
# frm.grid()
# ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
# ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
# root.mainloop()

from tkinter import *
from tkinter import ttk

# инициализация инстанса - создание объекта ткинтер
root = Tk()

# создание главного окна
frm = ttk.Frame(root, padding=100)
root.title("Таймер с интерфейсом на Python")
root.geometry("640x480")
frm.grid()
# Мы пишем таймер

# часы
ttk.Label(frm, text="00").grid(column=0, row=0)

# двоеточие
ttk.Label(frm, text=":").grid(column=1, row=0)

# минуты
ttk.Label(frm, text="00").grid(column=2, row=0)

# двоеточие
ttk.Label(frm, text=":").grid(column=3, row=0)

# секунды
ttk.Label(frm, text="00").grid(column=4, row=0)

# кнопка стоп
Button(text="stop",  # текст кнопки
       background="#555",  # фоновый цвет кнопки
       foreground="#ccc",  # цвет текста
       padx="20",  # отступ от границ до содержимого по горизонтали
       pady="8",  # отступ от границ до содержимого по вертикали
       font="16"  # высота шрифта
       ).grid(column=1, row=1)

result = "something"


def print_to_console():
    hours = 0
    minutes = 0
    seconds = 0

    # код до цикла
    while True:
        # seconds = seconds + 1
        seconds += 1

        if seconds > 59:
            minutes += 1
            seconds = 0

        if minutes > 59:
            hours += 1
            minutes = 0

        if hours > 23:
            seconds = 0
            minutes = 0
            hours = 0

        time.sleep(0.00001)
        print(f"{hours}:{minutes}" + ":" + str(seconds))


# кнопка старт
Button(text="start",  # текст кнопки
       background="#555",  # фоновый цвет кнопки
       foreground="#ccc",  # цвет текста
       padx="20",  # отступ от границ до содержимого по горизонтали
       pady="8",  # отступ от границ до содержимого по вертикали
       font="16",  # высота шрифта
       command=print_to_console,
       ).grid(column=3, row=1)

# ttk.Label(frm, text="Any").grid(column=0, row=1)
# ttk.Label(frm, text="Alex").grid(column=1, row=1)
# ttk.Label(frm, text="Ivan").grid(column=2, row=1)

# 0    1    2     3    4      5
# 1   Any    :   Alex  :     Ivan


# ttk.Label(frm, text="Hello World!").grid(column=0, row=0)

# ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)

# print_to_console("something")

root.mainloop()