#output.py
#Jose Melgar
#8/29/2024
#Python 3.12.5
#program to show output in python

print('hello world') #single quote
print("hello world") #double quote
print("he\nllo") #\n insert a new liine like press enter

#VARIABLE are named storage locations for numbers, string, lists
#STRING is anything enclosed in quotes "hello world", that's a string
#NUMBER can be either a float (Ex: 2.5) or an INTEGER (3.0)
#LISTS are things like [1,2,3] or ["jose","melgar"]

myName = "Jose" #declare/initialize string variable myName
myWeight = 275.35453 #declare/initialize float varible myWeight
myAge = 29 #declare int variable myAge
myGrade = [90,77,"hola"]
nameZ = ["Gabriela","melgar"]

print ('hello' , myName)
print ('Your weight is ', myWeight, ' and your age is: ',myAge)
print ('Your weight is %.3f and your age is %i: ' %(myWeight,myAge))
print ("Lists : grades =", myGrade, "nameZ ",nameZ)
print ("This is how you print", end= ' ')
print ("on the same line")


"================ RESTART: C:/Users/janth/Desktop/phyton class/output.py ================"
"hello world"
"hello world"
"he"
"llo"
"hello Jose"
"Your weight is  275.35453  and your age is:  29"
"Your weight is 275.355 and your age is 29: "
"Lists : grades = [90, 77, 'hola'] nameZ  ['Gabriela', 'melgar']"
"This is how you print on the same line"

