# Пример вывода:
# Anyone who
#  stops
#  learning
#  is old, whether at twenty or eighty.
#                          Henry Ford

import random

string = "Anyone who stops learning is old, whether at twenty or eighty. "

string = string.split()
i = 0
rand_late = ""
while i != 3:
    rand = random.randint(2, 7)
    if rand == rand_late:
        rand = random.randint(2, 7)
    if rand == rand_late:
        rand = random.randint(2, 7)
    rand_late = rand
    string.insert(rand, "\n")
    i += 1

myString = ' '.join(string)
myString = myString + "\n                               Henry Ford"
print(myString)
