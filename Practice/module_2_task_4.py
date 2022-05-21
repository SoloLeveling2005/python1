line = input("Введите число и процент: ")


line = line.split()

integer = line[0]
percent = line[1]
anser = (int(integer) * int(percent)) / 100
print(anser)