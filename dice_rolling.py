import random
#add a function to role 2 dices
def roll_dice():
    dice1= random.randint(1,6)
    dice2 = random.randint(1,6)
    print(f"({dice1},{dice2})")
#run a loop
while True:
    #ask "Do u wanna role a dice?"
    choice = input("Do u wanna role a dice?(y/n)")
    #if yes call the funtion 
    if choice.lower() == "y":
        roll_dice()
    #if no then break
    elif choice.lower() == "n":
        break
    else:
        print("Invalid input!")

print("Thanks for playing!")