with open('text.txt', 'r') as f:
    text = f.read()
    text_lower = text.lower()
    print("\n","Скопированный текст:", text_lower,"\n")

count = text_lower.count("etiam")
print("Элементов соответствующих строке 'etiam':",count,"\n")
# text_lower = text_lower.split("")

string = list(map(ord,text_lower))
# Первый вариант
print("Первый вариант:", string)



# Второй вариант
text_char = ""
for i in text_lower:
    text_char = text_char + " " + str(ord(i))
print("Второй вариант:",text_char,"\n")


# Выводим список в обратную сторону
print("список в обратную сторону:", string[::-1],"\n")