#p23.py
#Jose Melgar
#9/23/2024
#Python 3.12.5
#program to child practice arithmetic skills

from random import randint
while True:
    
    num1 = randint(0,9)
    num2 = randint(0,9)
    operation = input("would you like to add(+), sub(-) or mul(*)")
    #addition
    if operation == "+":
        answer = int (input("what id %i + %i = " %(num1,num2)))
    #ask the question again if the user is incorrect

        while answer != num1 + num2:
            answer = int(input("Incorrec, what is %i + %i = "%(num1,num2)))
    elif operation == "-":
        
        answer = int (input("what id %i - %i = " %(num1,num2)))
    #ask the question again if the user is incorrect

        while answer != num1 - num2:
            answer = int(input("Incorrec, what is %i - %i = "%(num1,num2)))
    elif operation == "*":
        
        answer = int (input("what id %i * %i = " %(num1,num2)))
    #ask the question again if the user is incorrect

        while answer != num1 * num2:
            answer = int(input("Incorrec, what is %i * %i = "%(num1,num2)))
    repeat =  input("would you like to try again (y/n)")
    if repeat != "y":
        break

    
"========== RESTART: C:/Users/janth/Desktop/phyton class/class5/p23.py =========="
"would you like to add(+), sub(-) or mul(*)"
"what id 0 + 4 = 0"
"Incorrec, what is 0 + 4 = 4"
"would you like to try again (y/n)y"
"would you like to add(+), sub(-) or mul(*)-"
"what id 2 - 0 = 0"
"Incorrec, what is 2 - 0 = 2v"
"would you like to try again (y/n)y"
"would you like to add(+), sub(-) or mul(*)*"
"what id 1 * 3 = 0"
"Incorrec, what is 1 * 3 = 3"
"would you like to try again (y/n)"
