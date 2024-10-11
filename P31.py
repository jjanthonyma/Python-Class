#p31.py
#Jose Melgar
#10/11/2024
#Python 3.12.5
#Write a function that has an integer N as parameter and returns true if N is even.

#function to verify its or nor even
def isEven(a):
    return a%2==0
#function to input value 
def main():
    a = int(input("input number : "))
    print("is even: ",isEven(a))

#call the function main()
if main() == "_main_":
    main()


"============== RESTART: C:/Users/janth/Desktop/phyton class/class6/P31.PY =============="
"input number : 5"
"is even:  False"

"============== RESTART: C:/Users/janth/Desktop/phyton class/class6/P31.PY =============="
"input number : 4"
"is even:  True"
