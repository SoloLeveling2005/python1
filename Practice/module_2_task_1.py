import random

string = "Nothing will work unless you do"

string = string.split()
i = 0
while i != 2:
    rand = random.randint(0, 5)
    string.insert(rand, "\n")
    i += 1

myString = ' '.join(string)
print(myString)
