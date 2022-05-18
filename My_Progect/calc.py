import math

a = float(input("Введите число: "))
b = str(input("Введите знак(+,-,/,*,**,%,//,sqrt) : "))
if b == "sqrt":
    print(math.sqrt(a))
else:
    c = float(input("Введите число : "))

    def calc(a,b,c):

        if b == "+":
            print(a+b+c)
        elif b == "-":
            print(a-c)
        elif b == "/":
            if c == 0:
                print("На ноль делить нельзя")
            else:
                print("Результат деления:")
                print(a/c)
        elif b == "*":
            print("Результат умножения:")
            print(a*c)
        elif b == "**":
            print("Результат возведения в степень:")
            print(a**c)
        elif b == "%":
            print("Остаток от деления:")
            print(a % c)
        elif b == "//":
            print("Результат без остатка:")
            print(a // c)

        calc(a,b,c)



# .split (',')