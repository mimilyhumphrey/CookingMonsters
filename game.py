import os
import random

ALL_SKILLS = [
    "Asian Cooking",
    "French Baking",
    "Mediteranian cooking",
    "Latin American cooking"
]

def main():
    new_name = input("What is your monster's name? ")
    player = {'reputation': 2,
    'exp': 0,
    'name': new_name,
    'skills': [],
    }

    
    os.system('clear')
    should_continue = True
    while should_continue:
        choices = [
            "Do some training",
            "Enter a cooking contest",
            "View profile",
            "Exit"
        ]
        print("Hello {}! What would you like to do today? ".format(player['name']))
        answer = choose(choices)
        if answer == 0:
            increase = perform_training()
            player['exp'] += increase
        if answer == 1:
            increase = enter_contest(player)
            player['reputation'] += increase
            if player['reputation'] == 0:
                print("Your reputation is 0. You lose the game!")
                break
        if answer == 2:
            print("Exp: {}".format(player['exp']))
            print("Reputation: {}".format(player['reputation']))
            print("Skills:")
            print_ordered_choices(player['skills'])
        if answer == 3:
            should_continue = False
            break
        input("Press enter to continue")
        os.system('clear')
    print("Bye")


def choose(valid_choices):
    print_ordered_choices(valid_choices)
    selection = get_valid_choice(valid_choices)
    return selection


def print_ordered_choices(choice_list):
    for index in range(len(choice_list)):
        element = choice_list[index]
        print("{}. {}".format(index + 1, element))


def get_valid_choice(choices):
    should_ask = True
    while should_ask:
        ask = input("Please enter your choice ")
        ask = int(ask)
        if ask in range(1, len(choices) + 1):
            index = ask - 1 
            return index
        print("Sorry, that is not a valid choice")


def perform_training():
    new_skill = random.choice(ALL_SKILLS)
    player['skills'].append(new_skill)
    increase = 10
    print('Yay you trained hard!  You gained {} exp points and learned {}'.format(increase, new_skill))
    return increase


def enter_contest(player):
    rand = random.randint(0, 100)
    result = rand + player['exp']
    if result > 50:
        print("You win!")
        return 1
    else:
        print("Loser!")
        return -1



main()
