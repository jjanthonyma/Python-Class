#p12.py
#Jose Melgar
#9/23/2024
#Python 3.12.5
#program to game generates two ramdon number 1 to 6 


from random import randint
while True:
    
    d1 = randint(1,6)
    d2 = randint(1,6)

    keep = input("you rolloed %i and %i  for a total of %i, keep y/n: "%(d1,d2,d1+d2))
    if keep == 'y':
        break


#check winner
pc1 = randint(1,6)
pc2 = randint(1,6)

if pc1 + pc2 > d1 + d2:
    print('computer winner')
elif pc1 + pc2 < d1 +d2:
    print('player wins')
else:
    print("tie")
