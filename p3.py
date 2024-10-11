#p3.py
#Jose Melgar
#8/30/2024
#python 3.12.5
#Program to take input in python

myName = input("Please enter your name: ") #this is a string
myWeight = float(input("please enter your weight in lbs: ")) # is float
myAge = int(input("please enter your age: ")) #integer
weightKg = myWeight*0.453592
title = "human"

print ("hello ", title, myName," your weight is" )
print (myWeight, "lbs")
print ("Which equals = %.2f" %weightKg, end= ' ') #end=' ' prevent new line
print ("Kilograms ")




"================== RESTART: C:/Users/janth/Desktop/phyton class/p3.py =================="
"Please enter your name: Jose Melgar"
"please enter your weight in lbs: 275.386"
"please enter your age: 29"
"hello  human Jose Melgar  your weight is"
"275.386 lbs"
"Which equals = 124.91 Kilograms" 
