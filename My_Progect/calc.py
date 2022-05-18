a = int(input("Введите число: "))
b = str(input("Введите знак(+,-,/,*) : "))
c = int(input("Введите число : "))

def calc(a,b,c):
    if b == "+":
        print(a+c)
    elif b == "-":
        print(a-c)
    elif b == "/":
        print(a/c)
    elif b == "*":
        print(a*c)


calc(a,b,c)