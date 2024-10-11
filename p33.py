#p33.py
#Jose Melgar
#10/11/2024
#Python 3.12.5
#If you are given three sticks, you may or may not be able to arrange them in a triangle. For example, if one of the sticks is 12 inches long and the other two are one inch long, you will not be able to get the short sticks to meet in the middle.



def isTriangle(a,b,c):
    return a + b > c and b + c > a and c + a > b

def main():
    a = int(input("input number one of the triangle: "))
    b = int(input("input number two of the triangle: "))
    c = int(input("input number three of the triangle: "))
    print("the side of the triangle are (",a,") (",b,") (",c,") Can a triangle be formed? ", isTriangle(a,b,c))



#call the function main()
if main() == "_main_":
    main()

"========== RESTART: C:/Users/janth/Desktop/phyton class/class6/p33.py =========="
"input number one of the triangle: 5"
"input number two of the triangle: 1"
"input number three of the triangle: 2"
"the side of the triangle are ( 5 ) ( 1 ) ( 2 ) Can a triangle be formed?  False"

"========== RESTART: C:/Users/janth/Desktop/phyton class/class6/p33.py =========="
"input number one of the triangle: 1"
"input number two of the triangle: 2"
"input number three of the triangle: 6"
"the side of the triangle are ( 1 ) ( 2 ) ( 6 ) Can a triangle be formed?  False"

"========== RESTART: C:/Users/janth/Desktop/phyton class/class6/p33.py =========="
"input number one of the triangle: 3"
"input number two of the triangle: 4"
"input number three of the triangle: 5"
"the side of the triangle are ( 3 ) ( 4 ) ( 5 ) Can a triangle be formed?  True"
