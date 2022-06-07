# импорт всей библиотеки
# -*- coding: utf-8 -*-
import time
from threading import Thread
from tkinter import *
from tkinter import ttk
import datetime
import tkinter as tk
# import tk as tk

# root = Tk()

# создание главного окна
# frm = ttk.Frame(root)
# root.title("ToDo")
# root.geometry("640x480")
# root.resizable(width=False, height=False)
# frm.grid()

from tkinter import *
from tkinter import Tk, Canvas, Frame, BOTH

import canvas as canvas



window = Tk()
window.title('ToDo')
window.geometry('700x500')
window.resizable(width=False, height=False)
frame1 = Frame(window)
frame1.grid()

frame11 = Frame(window, background='', )
frame11.grid(row=0, column=1)
frame2 = Frame(frame11, padx=30, pady=20, background='')
frame2.grid(row=1, column=1)
Label(frame2, text='Добавить задания', font=16).pack()

frame3 = Frame(frame11, padx=30, pady=20, background='#D8D8D8')
frame3.grid(row=1, column=2)
Label(frame3, text='Задания на сегодня', background='#D8D8D8', font=16).pack()

frame4 = Frame(frame11, padx=54, pady=20, background='')
frame4.grid(row=1, column=3)
Label(frame4, text='Календарь', font=16).pack()



# frame1 = Frame(ws, padx=5, pady=5)
# frame1.grid(row=0, column=1)
#
# Label(frame1, text='Name', padx=5, pady=5).pack()
# Label(frame1, text='Email', padx=5, pady=5).pack()
# Label(frame1, text='Password', padx=5, pady=5).pack()
#
# frame2 = Frame(ws, padx=5, pady=5)
# frame2.grid(row=0, column=2)
#
# Entry(frame2).pack(padx=5, pady=5)
# Entry(frame2).pack(padx=5, pady=5)
# Entry(frame2).pack(padx=5, pady=5)
#
# Button(ws, text='Submit').grid(row=1, columnspan=2, pady=5, padx=10)
#
#
#


# frame_top_menu = Frame(window)
# frame_top_menu.grid(row=0, column=1)
#
# frame1 = frame_top_menu.Frame(width=1, height=100, bg="red")
# frame1.pack(fill=tk.X, side=tk.LEFT, expand=True)
#
# frame2 = tk.Frame(width=1, height=100, bg="yellow")
# frame2.pack(fill=tk.X, side=tk.LEFT, expand=True)
#
# frame3 = tk.Frame(width=1, height=100, bg="blue")
# frame3.pack(fill=tk.X, side=tk.LEFT, expand=True)
#
#


#
# frame_top_menu = Frame(root)
# frame_top_menu.pack(expand=False, fill=X)
#
# frame_top_menu_one_div = Frame(frame_top_menu)
# frame_top_menu.pack(expand=False, fill=Y)
# Label(frame_top_menu_one_div, text='Name', padx=5, pady=5).pack()
#
# frame_top_menu_two_div = Frame(frame_top_menu)
# frame_top_menu.pack(expand=False, fill=Y)
# Label(frame_top_menu_two_div, text='Email', padx=5, pady=5).pack()
#
# frame_top_menu_three_div = Frame(frame_top_menu)
# frame_top_menu.pack(expand=False, fill=Y)
# Label(frame_top_menu_three_div, text='Password', padx=5, pady=5).pack()

# ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
# ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)

# for j in range(3):
#     frame = tk.Frame(
#         master=window,
#         relief=tk.RAISED,
#         borderwidth=1
#     )
#     frame.grid(row=i, column=j)
#     label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
#     label.pack()

window.mainloop()
