import random
'''
1 for snake
-1 for water
0 for gun
'''

computer = random.choice([-1, 0, 1])

youStr = input("Enter your choice:")
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

you = youDict[youStr]

# By now we have two numbers (variables), you and computers

print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

if (computer == you):
    print("Its Draw")
 
#less readable and understandable than the main one. 
else:
    if((computer - you) == 2 or (computer - you) == -1):
        print("You Win!")
    else:
        print("You Lose!")

    # the above logic is on the basis of the value(computer - you).