import os

import openpyxl
from openpyxl import Workbook

os.mkdir("new")

# получим объект файла
file = open("file.txt", "r")
i = 1
while True:
    # считываем строку
    line = file.readline()
    # прерываем цикл, если строка пустая
    if not line:
        break
    if line == '\n':
        continue

    # выводим строку

    file_name = "new/" + "Файл_" + str(i) + ".txt"

    my_file = open(file_name, "w+")
    my_file.write(str(line))
    my_file.close()

    print(line.strip())
    i += 1

# закрываем файл
file.close()

os.remove("file.txt")