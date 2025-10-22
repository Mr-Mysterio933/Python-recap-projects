import random
#add a function to role 2 dices
def roll_dice(num_of_dice):
    dices = []
    for i in range(num_of_dice):
        dice = random.randint(1,6)
        dices.append(dice)
    iteration = 0
    for j in dices:
        if iteration == 0:
            print("("+str(j),end=", ")
        elif iteration == num_of_dice - 1:
            print(str(j)+")")
        else:
            print(str(j),end=", ")
        
        iteration +=1
        
    
#run a loop
times = 0
while True:
    #ask "Do u wanna role a dice?"
    choice = input("Do u wanna role a dice?(y/n)")
    #if yes call the funtion 
    if choice.lower() == "y":
        num_of_dice = int(input("Enter the number of dices u wanna role: "))
        roll_dice(num_of_dice)
        times +=1
    #if no then break
    elif choice.lower() == "n":
        break
    else:
        print("Invalid input!")

print(f"You rolled {times} times")
print("Thanks for playing!")