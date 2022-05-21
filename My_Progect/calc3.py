# НЕ РАБОЧАЯ
# НЕ РАБОЧАЯ
# НЕ РАБОЧАЯ
# НЕ РАБОЧАЯ
# НЕ РАБОЧАЯ
# НЕ РАБОЧАЯ
# НЕ РАБОЧАЯ
# НЕ РАБОЧАЯ
# НЕ РАБОЧАЯ
# НЕ РАБОЧАЯ
# НЕ РАБОЧАЯ




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
print('line')
print(line)

multiplier = []
in_brackets = "false"
x = 0

# 22*22*22


# if past_number == "":
#     past_number = meaning
#     zero += 1
#     print(meaning)
#     break
# else:
#     meaning = str(past_number) + str(meaning)
#     input.pop(zero - 1)
#     print("zero:")
#
#     print(zero - 1)
#     zero -= 1
#     # print(input)
#     # print("=")
#     # print(meaning)
#     past_number = ""
#
#     break

# while y < x:
#    try:
#       for i in signs:
#
#            if input[y] == i:
#                input[y] = i
#                print(input[y])
#                print(i)
#                print("Все норм")
#                sign = i;
#
#        if sign == "":
#            input[y] = input[y] + input[y+1]
#            input.pop(y+1)
#            print(input)
#            y -= 1
#        else:
#            y +=1
#        y += 1
#        sign = ""
#
#        print(input)
#    except:
#        continue
