'''
1 is for snake
-1 is for water
0 is for gun    
'''
import random
print("Your choice is 's' for snake, 'w' for water and 'g' for gun.")
computer = random.choice([1, -1, 0])
youstr = (input("Enter your choice: "))
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "snake", -1: "water", 0: "gun"}
you = youDict[youstr]   

print(f"Computer choose {reverseDict[computer]} \nAnd\nYour choice is {reverseDict[you]}")



if(computer == you):
    print("Match Draw")

else: 
    if(computer == -1 and you == 1 ):
        print("You win!") 

    elif(computer == -1 and you == 0 ):
        print("You lose!") 

    elif(computer == 1 and you == -1 ):
        print("You lose!")     

    elif(computer == 1 and you == 0 ):
        print("You win!")     

    elif(computer == 0 and you == -1 ):
        print("You win!")     

    elif(computer == 0 and you == 1 ):
        print("You lose!")      

    else: print("Something went wrong...")