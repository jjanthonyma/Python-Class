#p17.py
#Jose Melgar
#9/22/2024
#Python 3.12.5
#program used loop to display year and increases university tuition

year = 0
tuition = 9524

while year < 10:
    year+=1
    tuition+=tuition*0.05

    print("Year: ",year,"                       Tuition:{:.0f}".format(tuition))
    

"========== RESTART: C:\Users\janth\Desktop\phyton class\class4\p17.py =========="
"Year:  1                        Tuition:10000"
"Year:  2                        Tuition:10500"
"Year:  3                        Tuition:11025"
"Year:  4                        Tuition:11576"
"Year:  5                        Tuition:12155"
"Year:  6                        Tuition:12763"
"Year:  7                        Tuition:13401"
"Year:  8                        Tuition:14071"
"Year:  9                        Tuition:14775"
"Year:  10                        Tuition:15514"
