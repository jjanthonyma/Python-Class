#p10.py
#Jose Melgar
#9/5/2024
#Python 3.12.5
#program to letter grades with input vaidation

#ask the user to enter grade as percent
percent = float(input('Please enter grade as percent: '))

#validate input
if percent < 0 or percent > 100:
    print('Error, percent must be between 0 to 100')
    percent = float(input('enter value between 0 to 100: '))

#show the correct letter grade based on the percent

if percent >= 90 and percent <= 100:
    print('the grade is "A"')

if percent >= 80 and percent <=90:
    print('the grade is "B"')
if percent >= 70 and percent < 80:
    print('the grade is "C"')
if percent >=60 and percent <70:
    print('the grade is "D"')
if percent < 60:
    print ('the grade is "F"')


"= RESTART: C:/Users/janth/Desktop/phyton class/class2/p10.py"
"Please enter grade as percent: 96"
"the grade is 'A'"

"========== RESTART: C:/Users/janth/Desktop/phyton class/class2/p10.py =========="
"Please enter grade as percent: 80"
"the grade is 'B'"

"========== RESTART: C:/Users/janth/Desktop/phyton class/class2/p10.py =========="
"Please enter grade as percent: 70"
"the grade is 'C'"

"========== RESTART: C:/Users/janth/Desktop/phyton class/class2/p10.py =========="
"Please enter grade as percent: 60"
"the grade is 'D'"

"========== RESTART: C:/Users/janth/Desktop/phyton class/class2/p10.py =========="
"Please enter grade as percent: 55"
"the grade is 'F'"
