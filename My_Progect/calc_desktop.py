from tkinter import *
from tkinter import ttk

root = Tk()
frm = ttk.Frame(root, padding=10)
root.title("Калькулятор")
root.geometry("300x450")

varInput = Entry(width=45, ).place(x=10, y=20)

Button(text="C",  # текст кнопки
       background="grey",  # фоновый цвет кнопки
       foreground="white",  # цвет текста
       font="12",  # высота шрифта
       padx=5,
       pady=5,
       height=2,
       width=3
       ).place(x=10, y=45)
#
# Button(text="<-",  # текст кнопки
#        background="#555",  # фоновый цвет кнопки
#        foreground="#ccc",  # цвет текста
#        font="12",  # высота шрифта
#        padx=5,
#        pady=5
#        ).grid(column=1, row=1)
# Button(text="%",  # текст кнопки
#        background="#555",  # фоновый цвет кнопки
#        foreground="#ccc",  # цвет текста
#        font="12",  # высота шрифта
#        padx=5,
#        pady=5
#        ).grid(column=2, row=1)
#
# Button(text="%",  # текст кнопки
#        background="#555",  # фоновый цвет кнопки
#        foreground="#ccc",  # цвет текста
#        font="12",  # высота шрифта
#        padx=5,
#        pady=5
#        ).grid(column=3, row=1)
# Button(text="7",  # текст кнопки
#        background="#555",  # фоновый цвет кнопки
#        foreground="#ccc",  # цвет текста
#        font="12",  # высота шрифта
#        padx=5,
#        pady=5
#        ).grid(column=0, row=2)
#
# Button(text="8",  # текст кнопки
#        background="#555",  # фоновый цвет кнопки
#        foreground="#ccc",  # цвет текста
#        font="12",  # высота шрифта
#        padx=5,
#        pady=5
#        ).grid(column=1, row=2)
# Button(text="9",  # текст кнопки
#        background="#555",  # фоновый цвет кнопки
#        foreground="#ccc",  # цвет текста
#        font="12",  # высота шрифта
#        padx=5,
#        pady=5
#        ).grid(column=2, row=2)
#
# Button(text="*",  # текст кнопки
#        background="#555",  # фоновый цвет кнопки
#        foreground="#ccc",  # цвет текста
#        font="12",  # высота шрифта
#        padx=5,
#        pady=5
#        ).grid(column=3, row=2)
# Button(text="4",  # текст кнопки
#        background="#555",  # фоновый цвет кнопки
#        foreground="#ccc",  # цвет текста
#        font="12",  # высота шрифта
#        padx=5,
#        pady=5
#        ).grid(column=0, row=3)
# Button(text="5",  # текст кнопки
#        background="#555",  # фоновый цвет кнопки
#        foreground="#ccc",  # цвет текста
#        font="12",  # высота шрифта
#        padx=5,
#        pady=5
#        ).grid(column=1, row=3)
#
# Button(text="6",  # текст кнопки
#        background="#555",  # фоновый цвет кнопки
#        foreground="#ccc",  # цвет текста
#        font="12",  # высота шрифта
#        padx=5,
#        pady=5
#        ).grid(column=2, row=3)
root.mainloop()
