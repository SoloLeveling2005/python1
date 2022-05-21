



import math
a = ""
d = ""
b = ""
input = str(input("Введите выражение, знаки(+,-,/,*,**,%,//,√): "))


if input.find("+") == 1:
    b = "+"
    input = input.split("+")
    d = input[1]
    a = input[0]

elif input.find("-") == 1:
    b = "-"
    input = input.split("-")
    a = input[0]
    d = input[1]

elif input.find("//") == 1:
    b = "//"
    input = input.split("//")
    a = input[0]
    d = input[1]
    print(input)

elif input.find("/") == 1:
    b = "/"
    input = input.split("/")
    a = input[0]
    d = input[1]

elif input.find("**") == 1:
    b = "**"
    input = input.split("**")
    a = input[0]
    d = input[1]


elif input.find("*") == 1:
    b = "*"
    input = input.split("*")
    a = input[0]
    d = input[1]


elif input.find("%") == 1:
    b = "%"
    input = input.split("%")
    a = input[0]
    d = input[1]


#
# elif input.find("√") == 1:
#     b = "sqrt"
#     input = input.split("sqrt")
#     a = float(input[0])
#     d = "1"
#



# print(a)
# print(d)
a = float(a)
d = float(d)
if b == "sqrt":
    print(math.sqrt(a))
else:
    def calc(a, b, d):
        if b == "+":
            print(a + d)
        elif b == "-":
            print(a - d)
        elif b == "/":
            if d == 0:
                print("На ноль делить нельзя")
            else:
                print("Результат деления:")
                print(a / d)
        elif b == "*":
            print("Результат умножения:")
            print(a * d)
        elif b == "**":
            print("Результат возведения в степень:")
            print(a ** d)
        elif b == "%":
            print("Остаток от деления:")
            print(a % d)
        elif b == "//":
            print("Результат без остатка:")
            print(a // d)
    calc(a, b, d)


