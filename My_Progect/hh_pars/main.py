# -*- coding: utf8 -*-
from tkinter import *
from tkinter import ttk
import requests
import json
import re
import threading, time

root = Tk()
frm = ttk.Frame(root, padding=10)
root.title("Find work (hh)")
root.geometry("850x650")
root.resizable(width=False, height=False)


# scroll = Scrollbar(command=root.yview)


def write_file():
    with open("file_name.json", 'w', encoding="utf-8") as file:
        json.dump(json_data, file)


def read_file():
    with open('file_name.json', 'r', encoding='utf-8') as file:
        global json_data1
        json_data1 = json.loads(file.read())
        json_data1 = json.loads(json_data1)
        print(json_data1)
        conclusion()


def find():
    global url
    global response
    global json_data
    varInput1 = varInput.get()
    url = "https://api.hh.ru/vacancies?text=" + str(varInput1) + "&area=40"
    response = requests.get(url)
    json_data = response.content.decode('utf-8')
    write_file()
    read_file()


i_name_vac = ""
i_name_city = ""
page = 0
Lab1 = Label(font="10", text="")
Lab2 = Label(font="10", text="")
Lab3 = Label(font="10", text="")
Lab4 = Label(font="10", text="")
Lab5 = Label(font="10", text="", justify=LEFT)
Lab6 = Label(font="10", text="", justify=LEFT)
Lab1.place(x=10, y=90)
Lab2.place(x=10, y=120)
Lab3.place(x=10, y=150)
Lab4.place(x=10, y=180)
Lab5.place(x=10, y=210)
Lab6.place(x=10, y=350)
two = 1


def conclusion():
    global page
    while True:
        try:

            print(json_data1['items'][page])
            name_vac = "Название вакансии: " + json_data1['items'][page]['name']
            # if (json_data1['items'][0]['address']['city'] == "")
            try:
                name_city = "Город: " + json_data1['items'][page]['address']['city']
            except:
                name_city = "Адрес не указан"
            try:
                name_street = "Адрес: " + json_data1['items'][page]['address']['street']
            except:
                name_street = "Адрес не указан"

            name_url_vac = "Cсылка: " + json_data1['items'][page]['alternate_url']
            name_snippet = json_data1['items'][page]['snippet']['requirement']
            name_responsibility = json_data1['items'][page]['snippet']['responsibility']
            try:
                name_snippet_responsibility = "Комментариий: " + name_snippet + " " + name_responsibility
            except:
                name_snippet_responsibility = "Комментариий: комментариев нет"
            try:
                currency = json_data1['items'][page]['salary']['currency']
                currency_from = json_data1['items'][page]['salary']['from']
                currency_to = json_data1['items'][page]['salary']['to']
                currency_from_to = str(currency) + ": " + "от" + str(currency_from) + " до" + str(currency_to)
            except:
                currency_from_to = "что то не то"
            # Label(font="10", text="-------------------------------------------------").place(x=10, y=80)

            name_snippet_responsibility = re.sub(r'<.*?>', '', name_snippet_responsibility)
            name_snippet_responsibility = name_snippet_responsibility.split(" ")
            y = 0
            v = []
            for i in name_snippet_responsibility:
                y += len(i)
                # print(y)
                if y > 55:
                    i = "\n" + i
                    y = 0
                v.append(i)

            z = " ".join(v)
            name_snippet_responsibility = z
            Lab1['text'] = name_vac
            Lab2['text'] = name_city
            Lab3['text'] = name_street
            Lab4['text'] = name_url_vac
            Lab5['text'] = name_snippet_responsibility
            Lab6['text'] = currency_from_to
        except:
            Lab1['text'] = "Вакансии закончились"
            Lab2['text'] = "Вакансии закончились"
            Lab3['text'] = "Вакансии закончились"
            Lab4['text'] = "Вакансии закончились"
            Lab5['text'] = "Вакансии закончились"
            Lab6['text'] = "Вакансии закончились"

        # Label(font="10", text="-------------------------------------------------").place(x=10, y=270)
        global two
        if two == 2:
            two = 1
            break
        else:
            two = two + 1


def next_page():
    global page
    page = page + 2
    conclusion()


def past_page():
    global page
    page = page - 2
    conclusion()


varInput = StringVar()
lab = Label(font="10", text="Введите интересующую вас вакансию:")
lab.place(x=10, y=10)
Entry(width=30, font="10", textvariable=varInput).place(x=10, y=40)
find = Button(font="Times 13", height=1, text="Поиск", command=find)
find.place(x=350, y=35)
Button_next = Button(font="Times 13", height=1, text="Прошлая страница", command=past_page)
Button_next.place(x=500, y=600)
Button_next = Button(font="Times 13", height=1, text="Следующая страница", command=next_page)
Button_next.place(x=650, y=600)

root.mainloop()
