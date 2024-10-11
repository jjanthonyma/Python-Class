#p29.py
#Jose Melgar
#10/11/2024
#Python 3.12.5
#Write a function that calculates the absolute value and returns the absolute value of a number.

#create the function to absolute number
def absolute(a):
    if a >= 0:
        return a
    if a<0:
        return a*(-1)
    
#main function to input the number of evaluate
def main():
    a = float(input("Enter a positive or negative value: "))
    print("the absolute value of",a," is ",absolute(a));


#call the function main()
if main() == "_main_":
    main()
    
"= RESTART: C:/Users/janth/Desktop/phyton class/class6/p29.py"
"Enter a positive or negative value: -5"
"the absolute value of -5.0  is  5.0"

"========== RESTART: C:/Users/janth/Desktop/phyton class/class6/p29.py =========="
"Enter a positive or negative value: 5"
"the absolute value of 5.0  is  5.0"
