line = input("Введите ширину и высоту прямоугольника: ")


line = line.split()

width = line[0]
height = line[1]

S = int(width) * int(height)
print("Площадь прямоугольника равно: " + str(S))
