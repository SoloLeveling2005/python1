from tkinter import *
from tkinter import ttk

root = Tk()
frm = ttk.Frame(root, padding=10)
root.title("Заголовок окна программы")
root.geometry("500x250")

def start():
    print("Всё работает хорошо")

Button(text="Это кнопка",  # текст кнопки
       background="#c0c0c0",
       foreground="blue",
       # font="11",
       padx=100,
       pady=30,
       anchor=CENTER,
       command=start,
       ).pack()





root.mainloop()