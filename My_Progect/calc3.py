# Готов!


import math

print("Знаки(+,-,/,*,**,%,//)")
input = str(input("Введите выражение:  "))
signs = ['+', '-', '/', '*']

print("-----------------------------")

line = []
past_number = ""

for i in input:
    if i in signs:
        line.append(past_number)  # Добавляем число
        line.append(i)  # Добавляем знак
        past_number = ""  # Чистим число
    else:
        past_number += i

line.append(past_number)


def calc(x):
    for x in line:
        if x == "*":
            index_sign = line.index(x)
            index_sign_past = index_sign - 1
            index_sign_future = index_sign + 1
            result = int(line[index_sign_past]) * int(line[index_sign_future])
            line[index_sign_past] = result
            line.pop(index_sign)
            line.pop(index_sign)
        elif x == "/":
            index_sign = line.index(x)
            index_sign_past = index_sign - 1
            index_sign_future = index_sign + 1
            result = int(line[index_sign_past]) / int(line[index_sign_future])
            line[index_sign_past] = int(result)
            line.pop(index_sign)
            line.pop(index_sign)
        elif x == "+":

            try:
                if "*" in line or "/" in line:
                    pass
                else:
                    # print(line)
                    index_sign = line.index(x)
                    index_sign_past = index_sign - 1
                    index_sign_future = index_sign + 1
                    result = int(line[index_sign_past]) + int(line[index_sign_future])
                    line[index_sign_past] = int(result)
                    line.pop(index_sign)
                    line.pop(index_sign)
            except:
                pass
        elif x == "-":

            try:
                if "*" in line or "/" in line:
                    pass
                else:
                    # print(line)
                    index_sign = line.index(x)
                    index_sign_past = index_sign - 1
                    index_sign_future = index_sign + 1
                    result = int(line[index_sign_past]) - int(line[index_sign_future])
                    line[index_sign_past] = int(result)
                    line.pop(index_sign)
                    line.pop(index_sign)
            except:
                pass


while True:
    if len(line) == 1:
        break
    else:
        calc(line)

print("Ответ:" + str(line[0]))
