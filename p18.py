#p18.py
#Jose Melgar
#9/22/2024
#Python 3.12.5
#program used loop to Print ASCII characters from ! until ~


num1 = 33  #ASCII !
num2 = 126    #ASCII ~

for i in range(num1, num2 + 1):
    print(chr(i), end=' ')
    
# Line break every 10 characters
    if (i - num1 + 1) % 10 == 0:
        print()


       " ============== RESTART: C:/Users/janth/Desktop/phyton class/class4/p18.py =============="
""! " # $ % & ' ( ) * "
"+ , - . / 0 1 2 3 4 "
"5 6 7 8 9 : ; < = > "
"? @ A B C D E F G H "
"I J K L M N O P Q R "
"S T U V W X Y Z [ \ "
"] ^ _ ` a b c d e f "
"g h i j k l m n o p "
"q r s t u v w x y z" 
"{ | } ~ "

