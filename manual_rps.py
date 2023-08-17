
import random

#choice_list = ['rock', 'paper', 'scissors']
# comp_choice = random.choice(choice_list)
# user_choice = input("Please choose: rock, paper or scissors ")
# print(comp_choice)

def get_user_choice():   
    choice_list = ['rock', 'paper', 'scissors']                                                   #Function containing user input, while loop to ensure input is either rock/paper/scissors
    user_choice = input("Please choose: rock, paper or scissors ").lower()  #ensures capitlised input is not an issue
    print(f"You chose {user_choice}")
    while user_choice not in choice_list:                                   #while loop to ensure user choice is isnt ouside rock/paper/scissors, code is interrupted by repeating input
        print(f"Invalid input, please try again")
        user_choice = input("Please choose: rock, paper or scissors ")
    return user_choice

def get_computer_choice():
    choice_list = ['rock', 'paper', 'scissors']                             #While this code was working well when the choice_list was outside the function as a globla variable, based on feedback I placed it insie the function here and again in get_user_choice
    comp_choice = random.choice(choice_list)
    print(f'Computer choice is {comp_choice}')
    return comp_choice

def get_winner(comp_choice, user_choice):                                  #Function with rules of rock paper scissors
    if comp_choice == user_choice:
        print("It's a tie!")
    elif comp_choice == 'rock' and user_choice == 'scissors':
        print("You lost!")
    elif comp_choice == 'rock' and user_choice == 'paper':
        print("You win!")
    elif comp_choice == 'paper' and user_choice == 'scissors':
        print("You win!")   
    elif comp_choice == 'paper' and user_choice == 'rock':
        print("You lost!")
    elif comp_choice == 'scissors' and user_choice == 'rock':
        print("You win!")
    elif comp_choice == 'scissors' and user_choice == 'paper':
        print("You lost!")


def play():                                                                 #Final fucntion wrapping previous fucntions togther- functions are assigned the variables as per get_winner arguments
    user_choice = get_user_choice()
    comp_choice = get_computer_choice()
    winner = get_winner(comp_choice, user_choice)

play()


# ou received the following feedback for this task:
# Something went wrong when running the function `get_computer_choice`. Make sure you have defined the function correctly 
# in the manual_rps.py file and that it does not accept any parameter. Also, make sure that the list of options
# is defined inside the function.