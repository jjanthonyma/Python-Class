#p14.py
#Jose Melgar
#9/11/2024
#Python 3.12.5
#program to tell you zodiac signs


#user input

day = int(input('Day of birth: '))
month = int(input('Month of birth: '))

if (month == 12 and day >= 22) or (month == 1 and day <=19): #condition capricorn
    print('You are Capricorn')

else:

    if (month == 1 and day >= 20) or (month == 2 and day <=18):#condition Aquarius
        print('You are Aquarius')
    if (month == 2 and day >= 19) or (month == 3 and day <=20):#condition Pisces
        print('You are Pisces')
    if (month == 3 and day >= 21) or (month == 4 and day <=19):#condition Aries
        print('You are Aries')
    if (month == 4 and day >= 20) or (month == 5 and day <=20):#condition Taurus
        print('You are Taurus')
    if (month == 5 and day >= 21) or (month == 6 and day <=21):#condition Gemini
        print('You are Gemini')
    if (month == 6 and day >= 22) or (month == 7 and day <=22):#condition Cancer
        print('You are Cancer')
    if (month == 7 and day >= 23) or (month == 8 and day <=22):#condition Leo
        print('You are Leo')
    if (month == 8 and day >= 23) or (month == 9 and day <=22):#condition Virgo
        print('You are Virgo')
    if (month == 9 and day >= 23) or (month == 10 and day <=23):#condition Libra
        print('You are Libra')
    if (month == 10 and day >= 24) or (month == 11 and day <=21):#condition Scorpio
        print('You are Scorpio')
    if (month == 11 and day >= 22) or (month == 12 and day <=21):#condition Sagitarius
        print('You are SAgitarius')

"========== RESTART: C:/Users/janth/Desktop/phyton class/class3/p14.py =========="
"Day of birth: 19"
"Month of birth: 8"
"You are Leo"

"========== RESTART: C:/Users/janth/Desktop/phyton class/class3/p14.py =========="
"Day of birth: 11"
"Month of birth: 2"
"You are Aquarius"

"========== RESTART: C:/Users/janth/Desktop/phyton class/class3/p14.py =========="
"Day of birth: 11"
"Month of birth: 7"
"You are Cancer"

"========== RESTART: C:/Users/janth/Desktop/phyton class/class3/p14.py =========="
"Day of birth: 28"
"Month of birth: 12"
"You are Capricorn"

"========== RESTART: C:/Users/janth/Desktop/phyton class/class3/p14.py =========="
"Day of birth: 9"
"Month of birth: 6"
"You are Gemini"
