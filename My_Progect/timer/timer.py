# импорт всей библиотеки
import time
from threading import Thread

from tkinter import *
from tkinter import ttk

hours = 0
minutes = 0
seconds = 0

pause = True


def stop_timer():
    global pause
    pause = False
    global hours
    global minutes
    global seconds
    hours = int(hours_label["text"])
    minutes = int(minuts_label["text"])
    seconds = int(seconds_label["text"])


def reset_timer():
    global hours
    hours = 0
    global minutes
    minutes = 0
    global seconds
    seconds = 0
    hours_label.config(text=f"{hours}")
    minuts_label.config(text=f"{minutes}")
    seconds_label.config(text=f"{seconds}")


def start_timer():
    times = varInput.get()
    times = times.split(":")
    print(times)
    global hours
    global minutes
    global seconds
    if hours == 0 and minutes == 0 and seconds == 0:
        hours = int(times[0])
        minutes = int(times[1])
        seconds = int(times[2])
    else:
        pass
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

        hours_label.config(text=f"{hours}")
        minuts_label.config(text=f"{minutes}")
        seconds_label.config(text=f"{seconds}")
        print(f"{hours}:{minutes}" + ":" + str(seconds))


# определение(создание) функции
def start_new_thread():
    Thread(
        target=start_timer
    ).start()  # Используйте для вызова функции в отдельный поток, тогда остальная часть окна не
    # будет виснуть


# вызов функции
# start_new_thread()

# ссылка на функцию
# start_new_thread

# инициализация инстанса - создание объекта ткинтер
root = Tk()

# создание главного окна
frm = ttk.Frame(root, padding=100)
root.title("Таймер с интерфейсом на Python")
root.geometry("640x480")
frm.grid()
# Мы пишем таймер

# поле для ввода отсчета времени
varInput = StringVar()
Label(width=37, font="15", text="Пример ввода: 1:12:30").place(x=0, y=20)
Entry(width=37, font="15", textvariable=varInput).place(x=30, y=50)

# часы
hours_label = ttk.Label(frm, text="00")
hours_label.grid(column=0, row=0)

# двоеточие
ttk.Label(frm, text=":").grid(column=1, row=0)

# минуты
minuts_label = ttk.Label(frm, text="00")
minuts_label.grid(column=2, row=0)

# двоеточие
ttk.Label(frm, text=":").grid(column=3, row=0)

# секунды
seconds_label = ttk.Label(frm, text="00")
seconds_label.grid(column=4, row=0)

# кнопка стоп
Button(text="stop",  # текст кнопки
       background="#555",  # фоновый цвет кнопки
       foreground="#ccc",  # цвет текста
       padx="20",  # отступ от границ до содержимого по горизонтали
       pady="8",  # отступ от границ до содержимого по вертикали
       font="16",  # высота шрифта
       command=stop_timer,  # ОБЯЗАТЕЛЬНО ПЕРЕДАВАТЬ ССЫЛКУ НА ФУНКЦИЮ
       ).grid(column=0, row=1)

# кнопка сброс
Button(text="reset",  # текст кнопки
       background="#555",  # фоновый цвет кнопки
       foreground="#ccc",  # цвет текста
       padx="20",  # отступ от границ до содержимого по горизонтали
       pady="8",  # отступ от границ до содержимого по вертикали
       font="16",  # высота шрифта
       command=reset_timer,  # ОБЯЗАТЕЛЬНО ПЕРЕДАВАТЬ ССЫЛКУ НА ФУНКЦИЮ
       ).grid(column=1, row=1)

# кнопка старт
Button(text="start",  # текст кнопки
       background="#555",  # фоновый цвет кнопки
       foreground="#ccc",  # цвет текста
       padx="20",  # отступ от границ до содержимого по горизонтали
       pady="8",  # отступ от границ до содержимого по вертикали
       font="16",  # высота шрифта
       command=start_new_thread,  # ОБЯЗАТЕЛЬНО ПЕРЕДАВАТЬ ССЫЛКУ НА ФУНКЦИЮ
       ).grid(column=2, row=1)



root.mainloop()
