
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
    choice_list = ['rock', 'paper', 'scissors']                             #While this code was working well when the choice_list was outside the function as a globla variable, based on feedback I placed it insie the function here and again in get_user_choice which is not taking any parameters
    comp_choice = random.choice(choice_list)
    print(f'Computer choice is {comp_choice}')
    return comp_choice
                                #Function with rules of rock paper scissors
def get_winner(comp_choice, user_choice):                                  #Function with rules of rock paper scissors
    if comp_choice == user_choice =='rock':
        print("It's a tie!")
    elif (comp_choice == 'rock' and user_choice) == 'scissors' or (comp_choice == 'paper' and user_choice == 'rock') or (comp_choice == 'scissors' and user_choice == 'paper'):
        print("You lost!")
    elif (comp_choice == 'rock' and user_choice == 'paper') or (comp_choice == 'paper' and user_choice == 'scissors') or (comp_choice == 'scissors' and user_choice == 'rock'):
        print("You win!")


def play():                                                                 #Final fucntion wrapping previous fucntions togther- functions are assigned the variables as per get_winner arguments
    user_choice = get_user_choice()
    comp_choice = get_computer_choice()
    winner = get_winner(comp_choice, user_choice)

play()

