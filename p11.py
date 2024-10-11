#p11.py
#Jose Melgar
#9/5/2024
#Python 3.12.5
#program rock, paper, scissors

#library
import random

#p1 input by user and random number for p2

p1 = int(input('p1 enter 1 for ROCK, 2 for PAPER, 3 for SCISSORS: '))
p2 = random.randint(1,3)



#show the generated values


if p1 < 1 or p1 >3:
    print ("error")

else:
    print('p1 = ', p1)
    print('p2 = ', p2)
    # make variables to store values for rock paper scissors

    rock = 1
    paper = 2
    scissors =3

    #cases when p1 wins
    if p1 == rock and p2 == scissors:
        print("p1 wins, rock breaks scissors")
    elif p1 == paper and p2 == rock:
        print("p1 wins, paper covers rock")
    elif p1 == scissors and p2 == paper:
        print ("p1 wins, scissors cut paper")

    #cases when p2 wins
    if p2 == rock and p1 == scissors:
        print("p2 wins, rock breaks scissors")
    elif p2 == paper and p1 == rock:
        print("p2 wins, paper covers rock")
    elif p2 == scissors and p1 == paper:
        print ("p2 wins, scissors cut paper")
    # you do the other 2

    #cases when p2 and p1 tie
    if p2 == rock and p1 == rock:
        print("tie")
    elif p2 == paper and p1 == paper:
        print("tie")
    elif p2 == scissors and p1 == scissors:
        print("tie")



"========== RESTART: C:/Users/janth/Desktop/phyton class/class2/p11.py =========="
"p1 enter 1 for ROCK, 2 for PAPER, 3 for SCISSORS: 2"
"p1 =  2"
"p2 =  1"
"p1 wins, paper covers rock"

"========== RESTART: C:/Users/janth/Desktop/phyton class/class2/p11.py =========="
"p1 enter 1 for ROCK, 2 for PAPER, 3 for SCISSORS: 3"
"p1 =  3"
"p2 =  1"
"p2 wins, rock breaks scissors"

"========== RESTART: C:/Users/janth/Desktop/phyton class/class2/p11.py =========="
"p1 enter 1 for ROCK, 2 for PAPER, 3 for SCISSORS: 1"
"p1 =  1"
"p2 =  3"
"p1 wins, rock breaks scissors"

"========== RESTART: C:/Users/janth/Desktop/phyton class/class2/p11.py =========="
"p1 enter 1 for ROCK, 2 for PAPER, 3 for SCISSORS: 2"
"p1 =  2"
"p2 =  1"
"p1 wins, paper covers rock"
"= RESTART: C:/Users/janth/Desktop/phyton class/class2/p11.py"
"p1 enter 1 for ROCK, 2 for PAPER, 3 for SCISSORS: 3"
"p1 =  3"
"p2 =  3"
"tie"
