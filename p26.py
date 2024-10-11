#p26.py
#Jose Melgar
#9/26/2024
#Python 3.12.5
#program to ramdin list of number

import random

l = random.randint(15, 20)

# empty list 
num = []

# Fill list with random numbers between 2 and 5
for _ in range(l):
    num.append(random.randint(2, 5))

# print list
print("Generating a list of", l, "numbers:", num)

# counter
cont = 0
for num1 in num:
    if num1 == 3:
        cont += 1

# print result
print("The number 3 appears ", cont, "times")

"======== RESTART: C:/Users/janth/Desktop/phyton class/class5/p26.pyu.py ========"
"Generating a list of 17 numbers: [5, 4, 5, 2, 3, 3, 2, 4, 3, 4, 3, 5, 4, 3, 2, 2, 2]"
"The number 3 appears  5 times"
