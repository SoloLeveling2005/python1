from tkinter import *
from tkinter import ttk

# from func import *

root = Tk()
frm = ttk.Frame(root, padding=10)
root.title("Калькулятор")
root.geometry("250x450")

first_value = ""
second_value = ""
sign = ""
signs = ""


def plus():
    global sign
    global first_value
    sign = "+"
    first_value = varInput["text"]
    varInput["text"] = ""
    # print(first_value)


def minus():
    global sign
    global first_value
    sign = "-"
    first_value = varInput["text"]
    varInput["text"] = ""
    # print(first_value)


def multiply():
    global sign
    global first_value
    sign = "*"
    first_value = varInput["text"]
    varInput["text"] = ""
    # print(first_value)


def divide():
    global sign
    global first_value
    sign = "/"
    first_value = varInput["text"]
    varInput["text"] = ""
    # print(first_value)


def degree():
    global sign
    global first_value
    sign = "**"
    first_value = varInput["text"]
    varInput["text"] = ""
    # print(first_value)


def delete():
    global sign
    global first_value
    global second_value
    del_var = varInput["text"]
    l = len(del_var)
    del_var = del_var[:l - 1]
    varInput["text"] = del_var


def clear():
    global sign
    global first_value
    global second_value
    sign = ""
    first_value = ""
    second_value = ""
    varInput["text"] = ""
    # print(first_value)


def calc():
    global first_value
    global second_value
    second_value = varInput["text"]
    if sign == "+":
        result = float(first_value) + float(second_value)
        first_value = result
        varInput["text"] = result
    elif sign == "-":
        result = float(first_value) - float(second_value)
        first_value = result
        varInput["text"] = result
    elif sign == "*":
        result = float(first_value) * float(second_value)
        first_value = result
        varInput["text"] = result
    elif sign == "/":
        result = float(first_value) / float(second_value)
        first_value = result
        varInput["text"] = result
    elif sign == "**":
        result = float(first_value) ** float(second_value)
        first_value = result
        varInput["text"] = result


def one():
    varInput["text"] = varInput["text"] + str("1")


def two():
    varInput["text"] = varInput["text"] + str("2")


def three():
    varInput["text"] = varInput["text"] + str("3")


def four():
    varInput["text"] = varInput["text"] + str("4")


def five():
    varInput["text"] = varInput["text"] + str("5")


def six():
    varInput["text"] = varInput["text"] + str("6")


def seven():
    varInput["text"] = varInput["text"] + str("7")


def eight():
    varInput["text"] = varInput["text"] + str("8")


def nine():
    varInput["text"] = varInput["text"] + str("9")


def zero():
    varInput["text"] = varInput["text"] + str("0")


def two_zero():
    varInput["text"] = varInput["text"] + str("00")


def point():
    varInput["text"] = varInput["text"] + str(".")


# Label(width=37, font="15", textvariable=varInput).place(x=10, y=20)
varInput = Label(text="", font="15", fg="black", bg="white")
varInput.place(x=10, y=20)
Button(text="C",  # текст кнопки
       background="grey",  # фоновый цвет кнопки
       foreground="white",  # цвет текста
       font="12",  # высота шрифта
       padx=5,
       pady=5,
       height=2,
       width=3,
       command=clear,
       ).place(x=10, y=55)
Button(text="⌫",  # текст кнопки
       background="grey",  # фоновый цвет кнопки
       foreground="white",  # цвет текста
       font="12",  # высота шрифта
       padx=5,
       pady=5,
       height=2,
       width=3,
       command=delete,
       ).place(x=70, y=55)
Button(text="**",  # текст кнопки
       background="grey",  # фоновый цвет кнопки
       foreground="white",  # цвет текста
       font="12",  # высота шрифта
       padx=5,
       pady=5,
       height=2,
       width=3,
       command=degree,
       ).place(x=130, y=55)
Button(text="/",  # текст кнопки
       background="grey",  # фоновый цвет кнопки
       foreground="white",  # цвет текста
       font="12",  # высота шрифта
       padx=5,
       pady=5,
       height=2,
       width=3,
       command=divide,
       ).place(x=190, y=55)
Button(text="7",  # текст кнопки
       background="grey",  # фоновый цвет кнопки
       foreground="white",  # цвет текста
       font="12",  # высота шрифта
       padx=5,
       pady=5,
       height=2,
       width=3,
       command=seven,
       ).place(x=10, y=130)
Button(text="8",  # текст кнопки
       background="grey",  # фоновый цвет кнопки
       foreground="white",  # цвет текста
       font="12",  # высота шрифта
       padx=5,
       pady=5,
       height=2,
       width=3,
       command=eight,
       ).place(x=70, y=130)
Button(text="9",  # текст кнопки
       background="grey",  # фоновый цвет кнопки
       foreground="white",  # цвет текста
       font="12",  # высота шрифта
       padx=5,
       pady=5,
       height=2,
       width=3,
       command=nine,
       ).place(x=130, y=130)
Button(text="*",  # текст кнопки
       background="grey",  # фоновый цвет кнопки
       foreground="white",  # цвет текста
       font="12",  # высота шрифта
       padx=5,
       pady=5,
       height=2,
       width=3,
       command=multiply,
       ).place(x=190, y=130)
Button(text="4",  # текст кнопки
       background="grey",  # фоновый цвет кнопки
       foreground="white",  # цвет текста
       font="12",  # высота шрифта
       padx=5,
       pady=5,
       height=2,
       width=3,
       command=four,
       ).place(x=10, y=205)
Button(text="5",  # текст кнопки
       background="grey",  # фоновый цвет кнопки
       foreground="white",  # цвет текста
       font="12",  # высота шрифта
       padx=5,
       pady=5,
       height=2,
       width=3,
       command=five,
       ).place(x=70, y=205)
Button(text="6",  # текст кнопки
       background="grey",  # фоновый цвет кнопки
       foreground="white",  # цвет текста
       font="12",  # высота шрифта
       padx=5,
       pady=5,
       height=2,
       width=3,
       command=six,
       ).place(x=130, y=205)
Button(text="-",  # текст кнопки
       background="grey",  # фоновый цвет кнопки
       foreground="white",  # цвет текста
       font="12",  # высота шрифта
       padx=5,
       pady=5,
       height=2,
       width=3,
       command=minus,
       ).place(x=190, y=205)
Button(text="1",  # текст кнопки
       background="grey",  # фоновый цвет кнопки
       foreground="white",  # цвет текста
       font="12",  # высота шрифта
       padx=5,
       pady=5,
       height=2,
       width=3,
       command=one,
       ).place(x=10, y=280)
Button(text="2",  # текст кнопки
       background="grey",  # фоновый цвет кнопки
       foreground="white",  # цвет текста
       font="12",  # высота шрифта
       padx=5,
       pady=5,
       height=2,
       width=3,
       command=two,
       ).place(x=70, y=280)
Button(text="3",  # текст кнопки
       background="grey",  # фоновый цвет кнопки
       foreground="white",  # цвет текста
       font="12",  # высота шрифта
       padx=5,
       pady=5,
       height=2,
       width=3,
       command=three,
       ).place(x=130, y=280)
Button(text="+",  # текст кнопки
       background="grey",  # фоновый цвет кнопки
       foreground="white",  # цвет текста
       font="12",  # высота шрифта
       padx=5,
       pady=5,
       height=2,
       width=3,
       command=plus,
       ).place(x=190, y=280)
Button(text="00",  # текст кнопки
       background="grey",  # фоновый цвет кнопки
       foreground="white",  # цвет текста
       font="12",  # высота шрифта
       padx=5,
       pady=5,
       height=2,
       width=3,
       command=two_zero,
       ).place(x=10, y=355)
Button(text="0",  # текст кнопки
       background="grey",  # фоновый цвет кнопки
       foreground="white",  # цвет текста
       font="12",  # высота шрифта
       padx=5,
       pady=5,
       height=2,
       width=3,
       command=zero,
       ).place(x=70, y=355)
Button(text=".",  # текст кнопки
       background="grey",  # фоновый цвет кнопки
       foreground="white",  # цвет текста
       font="12",  # высота шрифта
       padx=5,
       pady=5,
       height=2,
       width=3,
       command=point,
       ).place(x=130, y=355)
Button(text="=",  # текст кнопки
       background="grey",  # фоновый цвет кнопки
       foreground="white",  # цвет текста
       font="12",  # высота шрифта
       padx=5,
       pady=5,
       height=2,
       width=3,
       command=calc,
       ).place(x=190, y=355)
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
