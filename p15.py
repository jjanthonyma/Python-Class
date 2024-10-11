#p15.py
#Jose Melgar
#9/11/2024
#Python 3.12.5
#program to enter 4 number +/- and show all sum, sum +, sum-

num1 = float(input('Enter num1: '))
num2 = float(input('Enter num2: '))
num3 = float(input('Enter num3: '))
num4 = float(input('Enter num4: '))

sumAll = 0

sumAll = num1+num2+num3+num4

print('the sum of all number is: ', sumAll)

sumNeg = 0
sumPos = 0

if num1 < 0:
    sumNeg += num1 #num1 is negative ADD to sumNeg

if num2 < 0:
        sumNeg +=  num2 #num2 is negative ADD to sumNeg
if num3 < 0 :
        sumNeg += num3#num3 is negative ADD to sumNeg
if num4 < 0:
        sumNeg += num4#num4 is negative ADD to sumNeg
if num1 > 0:
        sumPos += num1 #num1 is positive ADD to sumPos
if num2 > 0:
        sumPos +=  num2#num2 is positive ADD to sumPos
if num3 > 0 :
        sumPos += num3#num3 is positive ADD to sumPos
if num4 > 0:
        sumPos += num4 #num4 is positive ADD to sumPos

print('Negative sum total is: ', sumNeg)
print('Positive sum total is: ', sumPos)


"= RESTART: C:/Users/janth/Desktop/phyton class/class3/p15.py"
"Enter num1: -5"
"Enter num2: 8"
"Enter num3: 10"
"Enter num4: -5"
"the sum of all number is:  8.0"
"Negative sum total is:  -10.0"
"Positive sum total is:  18.0"

"========== RESTART: C:/Users/janth/Desktop/phyton class/class3/p15.py =========="
"Enter num1: -5"
"Enter num2: 6"
"Enter num3: 6"
"Enter num4: -9"
"the sum of all number is:  -2.0"
"Negative sum total is:  -14.0"
"Positive sum total is:  12.0"

"========== RESTART: C:/Users/janth/Desktop/phyton class/class3/p15.py =========="
"Enter num1: 258"
"Enter num2: -85"
"Enter num3: 698"
"Enter num4: -698"
"the sum of all number is:  173.0"
"Negative sum total is:  -783.0"
"Positive sum total is:  956.0"
