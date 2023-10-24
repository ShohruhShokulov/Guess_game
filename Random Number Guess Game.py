from random import randint
from time import sleep


while True:
    print("i have thought a number from 1 to 10 and try to find out the number i have thought.\n")
    com = randint(1,10)
    b =0
    while True:
        a = int(input("Enter a number: "))
        b = b+1
        if a== com:
            print(" you fond the number!! Congrotulations!!\n")
            break
        elif a >com:
            print("you entered bigger number than i thought. So, input smaller. ")
            continue
        else :
            print(" you entered smaller number than i thought. So, input larger. ")
            continue
    print(f"you have found the number i have thought in {b} tries")

    #computer  case
    print("Now, it is time for you to think a number and i will find it out.")
    sleep(11)

    y =0 # number of tries
    while True:
        y=y+1
        print (f"{com}\n Is it the number you thought. If yes input (T),otherwise (F). ")
        c = input()
        if c=="T":
            print(f"You thought {com} and i found it in {y} tries!!  ")
            break
        else:
            print("If number is smaller than yours (+), or greater (-)")
            n = input()
            if n =="+":
                com = randint(com,10)
            elif n =="-":
                com = randint(0,com)
            continue

    if b>y:
        print(f"I won: {b}-{y}")
    elif b<y:
        print(f"You won: {y}-{b}")
    else:
        print(f"Draw: {b}-{y}")
    
    
    v = input("Do you want to play the game again, Yes(Y),No(N). ")
    if v =="Y":
        continue
        sleep(10)
    else:
        break
    

        



