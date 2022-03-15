import random

def game(a,b):
    if (a==1 and b==2):
        print("computer won")
    if (a==2 and b==3):
        print("computer won")
    if (a==3 and b==1):
        print("compuetr won")
    if a==b:
        print("its a tie")
    if (a==1 and b==3):
        print("you win")  
    if (a==2 and b==1):
        print("you win")
    if (a==3 and b==2):
        print("you win")     

randNo=random.randint(1,3)
a=int(input("your turn: \nSnake(1)\nWater(2)\nGun(3)\n"))
game(randNo,a)
print("computer chose",randNo)


