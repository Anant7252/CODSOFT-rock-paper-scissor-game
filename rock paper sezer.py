import random

print("This is a rock paper scissor game where computer choice automatic and you have to choose one among the three option \n options are \n")

m=0
b = True
while (b):
    print(" 1.Rock \n 2.Paper \n 3.Scissor")
    n = int(input("enter the choice"))
    comp = random.randint(1, 3)
    if comp==1:
        print("computer choice is Rock")
    elif comp==2:
        print("computer choice is Paper")
    elif comp==3:
        print("computer choice is Scissor")
    if (n == 1):
        if (comp == 1):
            print("Match Draw")
        elif (comp == 2):
            print("YOU LOOSE ")
        elif (comp == 3):
            print("You win")
            m=m+1
    elif (n == 2):
        if (comp == 2):
            print("Match Draw")
        elif (comp == 3):
            print("YOU LOOSE ")
        elif (comp == 1):
            print("You win")
            m=m+1
    elif (n == 3):
        if (comp == 3):
            print("Match Draw")
        elif (comp == 1):
            print("YOU LOOSE ")
        elif (comp == 2):
            print("You win")
            m=m+1
    
    a=int(input("Do you want to play again press 1 for yes 2 for No:  "))
    if(a==1):
        b=True
    else:
        b=False
        print(f"Your Score :{m}")


