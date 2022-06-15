# Обычные
# class Calc:
#     def __init__(self, first_value, second_value):
#         self.result_plus = float(first_value) + float(second_value)
#         self.result_minus = float(first_value) - float(second_value)
#         self.result_multiply = float(first_value) * float(second_value)
#         self.result_divide = float(first_value) / float(second_value)
#
# first_input_value = input("Введите число: ")
# sign = input("Введите знак: ")
# second_input_value = input("Введите число: ")
#
#
#
# results = Calc(first_input_value ,second_input_value)
# def calc():
#     if sign == "+":
#         print(results.result_plus)
#     elif sign == "-":
#         print(results.result_minus)
#     elif sign == "*":
#         print(results.result_multiply)
#     elif sign == "/":
#         print(results.result_divide)
#     else:
#         print("Ой что то не то")
#
# calc()

# статичные, вместо второго неизменимое число 10
class Calc:
    def __init__(self, first_value, second_value):
        self.result_plus = float(first_value) + float(second_value)
        self.result_minus = float(first_value) - float(second_value)
        self.result_multiply = float(first_value) * float(second_value)
        self.result_divide = float(first_value) / float(second_value)


first_input_value = input("Введите число: ")
sign = input("Введите знак: ")
second_input_value = 10

results = Calc(first_input_value, second_input_value)


def calc():
    if sign == "+":
        print(results.result_plus)
    elif sign == "-":
        print(results.result_minus)
    elif sign == "*":
        print(results.result_multiply)
    elif sign == "/":
        print(results.result_divide)
    else:
        print("Ой что то не то")


calc()
