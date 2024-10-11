#p32.py
#Jose Melgar
#10/11/2024
#Python 3.12.5
#Write a function multAdd(a,b,c)  that Returns a*b+c.

def multAdd(a,b,c):
    return a*b+c

def main():
    a = int(input("input the number 1: "))
    b = int(input("input the number 2: "))
    c = int(input("input the number 3: "))

    print("the result (",a,") * (",b,") + (",c,") = ", multAdd(a,b,c))

#call the function main()
if main() == "_main_":
    main()


"============== RESTART: C:/Users/janth/Desktop/phyton class/class6/p32.py =============="
"input the number 1: 1"
"input the number 2: 2"
"input the number 3: 3"
"the result ( 1 ) * ( 2 ) + ( 3 ) =  5"

"============== RESTART: C:/Users/janth/Desktop/phyton class/class6/p32.py =============="
"input the number 1: 5"
"input the number 2: 8"
"input the number 3: 6"
"the result ( 5 ) * ( 8 ) + ( 6 ) =  46"
