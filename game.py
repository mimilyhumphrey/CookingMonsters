import os
import random


def main():
    player_reputation = 2
    player_skill = 0 
    player_name = input("What is your monster's name? ")
    os.system('clear')
    should_continue = True
    while should_continue:
        choices = [
            "Do some training",
            "Enter a cooking contest",
            "View profile",
            "Exit"
        ]
        print("Hello {}! What would you like to do today? ".format(player_name))
        answer = choose(choices)
        if answer == 0:
            increase = perform_training()
            player_skill += increase
        if answer == 1:
            increase = enter_contest(player_skill)
            player_reputation += increase
            if player_reputation == 0:
                print("Your reputation is 0. You lose the game!")
                break
        if answer == 2:
            print("Skill: {}".format(player_skill))
            print("Reputation: {}".format(player_reputation))
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
    increase = 10
    print('Yay you trained hard!  You gained {} skill points'.format(increase))
    return increase


def enter_contest(skill):
    rand = random.randint(0, 100)
    result = rand + skill
    if result > 50:
        print("You win!")
        return 1
    else:
        print("Loser!")
        return -1



main()
