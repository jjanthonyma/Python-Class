#p30.py
#Jose Melgar
#10/11/2024
#Python 3.12.5
#Write a function which has two parameters, N and M.

def isDivisible(a,b):
    if a % b == 0:
        print(a, "is evenly divisible by ",b)
    if a % b != 0:
        print(a, "is not evenly divisible by ", b)

def main():
    a = int(input("inout number 1: "))
    b = int(input("input number 2: "))

    isDivisible(a,b)

#call the function main()
if main() == "_main_":
    main()


"============== RESTART: C:/Users/janth/Desktop/phyton class/class6/p30.py =============="
"inout number 1: 5"
"input number 2: 8"
"5 is not evenly divisible by  8"

"============== RESTART: C:/Users/janth/Desktop/phyton class/class6/p30.py =============="
"inout number 1: 5"
"input number 2: 5"
"5 is evenly divisible by  5"
