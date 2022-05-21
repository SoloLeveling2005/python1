#  Еще разбираюсь
#  Еще разбираюсь
#  Еще разбираюсь
#  Еще разбираюсь
#  Еще разбираюсь
#  Еще разбираюсь




from random import randint

string = "Nothing will work unless you do"
string = string.split()
list_words = []

while True:
    for i in string:
        random = randint(0, 2)
        if random == 0:
            list_words.append(i)
            print(list_words)
            list_words = []
            break
        elif random == 1:
            list_words.append(i)
            random -= 1
        elif random == 2:
            list_words.append(i)
            random -= 1

