#p16.py
#Jose Melgar
#9/16/2024
#Python 3.12.5
#program used loop to display table(kg on the left and pounds on the right)

print("kilogramos     Pounds")

num = 0
while num<200:
    num+=1
    if num%2 != 0:
        print(num,"               {:.1f}".format(num*2.2))

"========== RESTART: C:\Users\janth\Desktop\phyton class\class4\p16.py =========="
"kilogramos     Pounds"
"1                2.2"
"3                6.6"
"5                11.0"
"7                15.4"
"9                19.8"
"11                24.2"
"13                28.6"

"CONTINUE"

"191                420.2"
"193                424.6"
"195                429.0"
"197                433.4"
"199                437.8"
