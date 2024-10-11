#p27.py
#Jose Melgar
#9/29/2024
#Python 3.12.5
#program to ramdon letter

import random

# Generate random list length between 50 and 75
l = random.randint(50, 75)

#Create empty list
letters = []

#Fill list with random letters between A and F
for _ in range(l):
    ascii_number = random.randint(65, 70)  #ASCII of A to F
    letter = chr(ascii_number)
    letters.append(letter)

#Print generated list
print("Lift of ", l, "letter :", letters)

#Counting occurrences of the letter B
cont = 0
for letter in letters:
    if letter == 'B':
        cont += 1

#Print result 
print("the letter  'B' appears", cont, "times")


"============================================================== RESTART: C:/Users/janth/Desktop/phyton class/class5/p27.py =============================================================="
"Lift of  74 letter : ['F', 'E', 'A', 'B', 'D', 'F', 'A', 'F', 'A', 'F', 'E', 'B', 'C', 'C', 'C', 'B', 'D', 'E', 'A', 'A', 'B', 'F', 'C', 'A', 'E', 'C', 'B', 'F', 'A', 'B', 'E', 'C', 'A', 'E', 'E', 'F', 'D', 'A', 'A', 'E', 'F', 'B', 'F', 'F', 'F', 'D', 'A', 'C', 'C', 'D', 'C', 'E', 'A', 'D', 'E', 'A', 'A', 'B', 'B', 'E', 'F', 'E', 'C', 'E', 'B', 'C', 'F', 'C', 'A', 'C', 'A', 'D', 'C', 'B']"
"the letter  'B' appears 11 times"
