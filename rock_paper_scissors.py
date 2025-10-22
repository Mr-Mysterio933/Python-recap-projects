import random


choices = ['r','p','s']
#add a function that generates computer choice
def computer_choice():
    computer_response = random.choice(choices)
    return computer_response
#add a function that decides the winner
def winner(user, computer):
    if computer == user:
        print("Its a Tie")
    else:
        if user.lower() == 'r':
            if computer == 'p':
                print('You Lose!')
            else:
                print('You Win!')
        elif user.lower() == 'p':
            if computer == 's':
                print('You Lose!')
            else:
                print('You Win!')
        elif user.lower() == 's':
            if computer == 'r':
                print('You Lose!')
            else:
                print('You Win!')

#emojis dictionary
emojis = {'r':'🪨', 'p':'📄','s':'✂️'}
#loop
while True:
    #user choice
    user_choice = input("Rock, paper or scissors(r/p/s)? ")
    try:
        print(f"You chose {emojis[user_choice.lower()]}")
        computer_response = computer_choice()
        print(f"Computer chose {emojis[computer_response]}")
        winner(user_choice,computer_response)

        wanna_continue = input("U wanna continue(y/n)?")
        if wanna_continue.lower()== 'y':
            continue
        else:
            break
    except KeyError:
        print("Invalid choice!")

print("Thanks for playing!")