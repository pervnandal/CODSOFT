import random

def game(choice,radNo):
    if choice==radNo:
        return None
    
    #checking all passibilities of rock
    elif choice==1:
        if radNo==2:
            return False
        elif radNo==3:
            return True
    
    #checking all possibilites of paper
    elif choice==2:
        if radNo==3:
            return False
        elif radNo==1:
            return True
        
    # checking all possibilites of scissor    
    elif choice==3:
        if radNo==1:
            return False
        elif radNo==2:
            return True

# def rePlay():
#     re = print("Want to play again")

for i in range(1,101):
    # random number of computer choice
    radNo=random.randint(1,3)
    if radNo==1:
        comp="Rock"
    elif radNo==2:
        comp="Paper"
    else:
        comp="Scissors"

    #taking user inout choice
    choice=int(input("Enter your choice: \n"
                    +"1 --> Rock\n"
                    +"2 --> Paper\n"
                    +"3 --> Scissors\n"))

    win = game(choice,radNo)
    if choice==1:
        you="Rock"
    elif choice==2:
        you="Paper"
    else:
        you="Scissors"

    print(f"your choice is {you}")
    print(f"Computer choice is {comp}")

    if win==None:
        print("Game is a tie")
    elif win:
        print("You won!")
    else:
        print("You lost.")
    
    re = input("want to play again?(y/n): ")
    if re.lower()=='n':
        break
