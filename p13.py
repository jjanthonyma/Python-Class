#p12.py
#Jose Melgar
#9/11/2024
#Python 3.12.5
#program to convert any number of total cents

#user enters number of change

totalCents = int(input('enter total of change: '))

#integer div to get whole number for quarters

quarters = int(totalCents/25)

#condition quarters

if quarters > 0:
    print('you have', quarters, ' Quarters | ',quarters*25,' cents total ')
    totalCents = totalCents - quarters*25

#integer div for dime

dime = int(totalCents/10)

if dime > 0: #condition dime
    print('you have', dime,' Dime | ',dime*10,' cents total ')
    totalCents = totalCents - dime*10 #new totalCent
    
#integer div for nickels
nickels = int(totalCents/5)
if nickels > 0: #conditions nickels
    print('you have ',nickels,' Nickels | ',nickels*5,' cents total ')
    totalCents = totalCents - nickels*5#new totalCents
    
#integer div for pennies
pennies = int(totalCents/1)
if pennies > 0:#conditions pennies
    print('you have', pennies, ' Pennies | ',pennies*1,' cents total ')

"= RESTART: C:/Users/janth/Desktop/phyton class/class3/p13.py"
"enter total of change: 99"
"you have 3  Quarters |  75  cents total "
"you have 2  Dime |  20  cents total "
"you have 4  Pennies |  4  cents total "

"========== RESTART: C:/Users/janth/Desktop/phyton class/class3/p13.py =========="
"enter total of change: 10"
"you have 1  Dime |  10  cents total "

"========== RESTART: C:/Users/janth/Desktop/phyton class/class3/p13.py =========="
"enter total of change: 39"
"you have 1  Quarters |  25  cents total "
"you have 1  Dime |  10  cents total "
"you have 4  Pennies |  4  cents total" 

"========== RESTART: C:/Users/janth/Desktop/phyton class/class3/p13.py =========="
"enter total of change: 25"
"you have 1  Quarters |  25  cents total "

"========== RESTART: C:/Users/janth/Desktop/phyton class/class3/p13.py =========="
"enter total of change: 24"
"you have 2  Dime |  20  cents total" 
"you have 4  Pennies |  4  cents total" 

"========== RESTART: C:/Users/janth/Desktop/phyton class/class3/p13.py =========="
"enter total of change: 4"
"you have 4  Pennies |  4  cents total "
