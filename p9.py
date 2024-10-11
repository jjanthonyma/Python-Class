#p9.py
#Jose Melgar
#9/5/2024
#Python 3.12.5
#program to compute persons height and message

#ask the user for height, feet and inches
print('Enter your height')
feet = float(input('feet:'))
inches = float(input('inches:'))

#calculate the total inches
totalInches = feet*12 + inches

#show result

print('%.0f feet %.0f inch(es) = %.0f inches' % (feet,inches,totalInches))

if totalInches >= 72:
    print('you are tall')

if totalInches < 72 and totalInches > 60:
    print('you are average')
if totalInches < 60:
    print('you are short')

"= RESTART: C:/Users/janth/Desktop/phyton class/class2/p9.py"
"Enter your height"
"feet:6"
"inches:2"
"6 feet 2 inch(es) = 74 inches"
"you are tall"


"=========== RESTART: C:/Users/janth/Desktop/phyton class/class2/p9.py =========="
"Enter your height"
"feet:5"
"inches:1"
"5 feet 1 inch(es) = 61 inches"
"you are average"


"=========== RESTART: C:/Users/janth/Desktop/phyton class/class2/p9.py =========="
"Enter your height"
"feet:4"
"inches:7"
"4 feet 7 inch(es) = 55 inches"
"you are short"
