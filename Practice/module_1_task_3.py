numbers = input("Введите два числа: ")

numbers = numbers.split()
summa = ""
for i in numbers:
    summa += str(i)
print(summa)