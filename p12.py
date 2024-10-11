#p12.py
#Jose Melgar
#9/11/2024
#Python 3.12.5
#program to voters

#Ask for input user

age = int(input('please enter age: '))
citizen = input('are you citizen? (y/n):')
registered = input('are you registered? (y/n): ')

#check if they can vote

if age >=18 and citizen == 'y' and registered =='y':
    print('Congratulations, you can vote! ')
else:
    if age <18: #condition age
        print('Sorry, you cannot vote. you are not old enough')
    if citizen != 'y': #condition citizen
        print('Sorry, you cannot vote. you are not citizen')
    if registered != 'y': #condition registered
        print('Sorry, you cannot vote. you are not registered')


"========== RESTART: C:/Users/janth/Desktop/phyton class/class3/p12.py =========="
"please enter age: 29"
"are you citizen? (y/n):y"
"are you registered? (y/n): n"
"Sorry, you cannot vote. you are not registered"

"========== RESTART: C:/Users/janth/Desktop/phyton class/class3/p12.py =========="
"please enter age: 20"
"are you citizen? (y/n):n"
"are you registered? (y/n): n"
"Sorry, you cannot vote. you are not citizen"
"Sorry, you cannot vote. you are not registered"

"========== RESTART: C:/Users/janth/Desktop/phyton class/class3/p12.py =========="
"please enter age: 17"
"are you citizen? (y/n):n"
"are you registered? (y/n): n"
"Sorry, you cannot vote. you are not old enough"
"Sorry, you cannot vote. you are not citizen"
"Sorry, you cannot vote. you are not registered"

"========== RESTART: C:/Users/janth/Desktop/phyton class/class3/p12.py =========="
"please enter age: 29"
"are you citizen? (y/n):y"
"are you registered? (y/n): y"
"Congratulations, you can vote! "
