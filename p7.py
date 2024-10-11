#p7.py
#Jose Melgar
#9/5/2024
#Python 3.12.5
#program to calculate circumference and area of a circle

#define PI
PI = 3.1415

#ask for radius
radius = float(input('enter radius:'))

#validate radius

if radius < 0:
    print('error, radius cannot be negative')
else:
    #calculate area
    area = PI*radius*radius
    #calculate circunference
    circunference = 2*PI*radius
    #show result
    print('a circle with radius %.1f inches has ' %radius)
    print('area: %.1f square inches' %area)
    print('circunference: %.1f inches' %circunference)
   

"=========== RESTART: C:/Users/janth/Desktop/phyton class/class2/p7.py =========="
"enter radius:5"
"a circle with radius 5.0 inches has" 
"area: 78.5 square inches"
"circunference: 31.4 inches"
