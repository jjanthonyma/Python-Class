#p20.py
#Jose Melgar
#9/25/2024
#Python 3.12.5
#program  the sum of negative positive and all numbers


x = int(input("How many number would you like to enter "))
Sum = 0
sumNeg = 0
number = 0
sumPos = 0
for i in range(0,x,1):
    number = float(input("inter number %i: " %(i+1)))
    #sum + 
    Sum = Sum + number
    #sum negative
    if number < 0:
        sumNeg += number
    #sum positive
    elif number > 0:
        sumPos += number
print("sum = ", Sum)
print("sum Neg = ", sumNeg)
print("sum pos = ",sumPos)


"========== RESTART: C:/Users/janth/Desktop/phyton class/class4/p20.py =========="
"How many number would you like to enter 4"
"inter number 1: 5"
"inter number 2: -5"
"inter number 3: -5"
"inter number 4: 5"
"sum =  0.0"
"sum Neg =  -10.0"
"sum pos =  10.0"
