#p24.py
#Jose Melgar
#9/23/2024
#Python 3.12.5
#program to child practice arithmetic skills

from random import randint

x = randint(10,15)
print("x= ",x)
sum = 0

for i in range (0,x,1):
    print (i)
    y = randint(20,50)
    sum += y
    print(y, end=',')
    if i == 0:
        smallest = y
    elif i == 1:
        larges = y
    else:
        if y < smallest:
            smallest = y
        elif y > larges:
            larges = y
print('\nsmallest = ', smallest)
print('\nlarges = ', larges)
print('\nsum = ', sum)
print('\nAverage', (sum)/x)

"============== RESTART: C:\Users\janth\Desktop\phyton class\class5\p24."py ==============
"x=  10"
"0"
"23,"
"31,"
"28,"
"38,"
"37,"
"26,"
"48,"
"42,"
"37,"
"26,"
"smallest =  23"

"larges =  48"

"sum =  336"

"Average 33.6"
