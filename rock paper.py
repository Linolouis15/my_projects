import random
print("welocme to the Game \n 1:rock 2: paper 3 : scissor")
def rpc(choice):
    cpu_choice=random.randint(1,3)
    print(f"CPU choice is {cpu_choice}")
    if choice == 1 and cpu_choice ==2 :
        print("CPU wins")
    elif choice ==1 and cpu_choice == 3:
        print("user wins")
    elif choice ==2 and cpu_choice == 1:
        print("YOU wins")
    elif choice==2 and cpu_choice == 3:
        print("CPU wins")
    elif choice == 3 and cpu_choice==1 :
        print("CPU wins")
    elif choice==3 and cpu_choice==2:
        print("you wins")
    else :
        print("TIE")
    return " "
Choice1=input("enter your choice :")
choice2=int(Choice1)
print(rpc(choice2))