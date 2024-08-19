'''

-1 = water
0 = gun
1 = snack

'''
import random

system = random.choice([-1,0,1])
print("W = Water","S = Snack","G = Gun")
userstr = input("Enter your Choice :")
userDict = {"S" : 1, "W" : -1, "G" : 0}
reverseDict = {1: "Snack", -1 : "Water", 0 : "Gun"}

user = userDict[userstr]

print(f"You choose {reverseDict[user]}\nSystem choose {reverseDict[system]}")

if(system == user):
    print("Its a Draw")

else:
    # if(system == -1 and user == 1): (system - user = -2)
    #     print("You Win..!")               
    # elif(system == -1 and user == 0): (system - user = -1)
    #     print("You lose..!")              loss
    # elif(system == 1 and user == -1): (system - user = 2)
    #     print("You lose..!")              loss
    # elif(system == 1 and user == 0): (system - user = 1)
    #     print("You Win..!")
    # elif(system == 0 and user == 1): (system - user = -1)
    #     print("You Win..!")               loss
    # elif(system == 0 and user == -1): (system - user = 1)
    #     print("You lose..!")
    if((system - user) == -1 or (system - user) == 2): 
        print("You lose")
    else:
        print("You Win")