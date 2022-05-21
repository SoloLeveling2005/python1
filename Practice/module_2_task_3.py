line = input("Введите два числа: ")

numbers = []
line = line.split()

for x in line:
    x = int(x)
    print(x)
    numbers.append(x)
    numbers.sort()

summa = numbers[1] + numbers[0]

difference = numbers[1] - numbers[0]
composition = numbers[1] * numbers[0]

print(summa)
print(difference)
print(composition)
