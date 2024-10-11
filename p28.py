#p28.py
#Jose Melgar
#10/11/2024
#Python 3.12.5
#program to Write a function which given two integer parameters Returns their sum...unless the two values are the same, then the function Returns their doubled sum


def sum_double(a,b):
    if a == b :
        print("Your values its same")
        return 2*(a+b)
    else :
        print("Your values its diferent")
        return a+b



def main():
    #input value 1
    a = int(input("input number 1: "))
    b = int(input("input number 2: "))
    #print result
    print(sum_double(a,b))

#call the function main()
if main() == "_main_":
    main()


"========== RESTART: C:/Users/janth/Desktop/phyton class/class6/p28.py =========="
"input number 1: 5"
"input number 2: 6"
"Your values its diferent"""
"11"

"========== RESTART: C:/Users/janth/Desktop/phyton class/class6/p28.py =========="
"input number 1: 5"
"input number 2: 5"
"Your values its same"
"20"
