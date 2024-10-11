#p25.py
#Jose Melgar
#9/25/2024
#Python 3.12.5
#program to find letters


sentence = input("pleaes enter sentence: ")
count1 = 0
count2 = 0
letter1 = input("Inser the letter you want to find: ")
letter2 = input("Inser the letter 2 you want to find: ")
for i in range(0,len(sentence), 1):
    if sentence[i] == letter1:
        count1 += 1
    if sentence[i] == letter2:
        count2 += 1
print("The letter: ",letter1,"Occurs: ",count1,"time")
print("The letter: ",letter2,"Occurs: ",count2,"time")


"========== RESTART: C:/Users/janth/Desktop/phyton class/class5/p25.py =========="
"pleaes enter sentence: hello world"
"Inser the letter you want to find: l"
"Inser the letter 2 you want to find: o"
"The letter:  l Occurs:  3 time"
"The letter:  o Occurs:  2 time"

