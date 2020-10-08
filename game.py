import os
import random


ALL_SKILLS = [
    "Asian Cooking",
    "French Baking",
    "Mediteranian cooking",
    "Latin American cooking"
]
class Player:
    def __init__(self, money, reputation, exp, name, skills):
        self.money = money
        self.reputation = reputation
        self.exp = exp
        self.name = name
        self.skills = skills

def main():
    new_name = input("What is your monster's name? ")
    new_name = new_name.capitalize()
    player = Player(500, 2, 0, new_name, [])
    
    os.system('clear')
    should_continue = True
    while should_continue:
        choices = [
            "Do some training",
            "Enter a cooking contest",
            "View profile",
            "Exit"
        ]
        print("Hello {}! What would you like to do today? ".format(player.name))
        answer = choose(choices)
        if answer == 0:
            increase = perform_training(player)
            player.exp += increase
            if player.money <= 0:
                print("You broke. You lose the game!")
                break
    
        if answer == 1:
            increase = enter_contest(player)
            player.reputation += increase
            if player.reputation == 0:
                print("Your reputation is 0. You lose the game!")
                break
            if player.money <= 0:
                print("You broke. You lose the game!")
                break
        if answer == 2:
            show_profile(player)
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


def perform_training(player):
    player.money -= 50 
    print('It costs 50 for training')
    new_skill = random.choice(ALL_SKILLS)
    player.skills.append(new_skill)
    increase = 10
    print('Yay you trained hard!  You gained {} exp points and learned {}'.format(increase, new_skill))
    return increase


def enter_contest(player):
    player.money -= 100
    print("It costs 100 for entry fee")
    rand = random.randint(0, 100)
    result = rand + player.exp
    if result > 50:
        player.money += 200
        print("You win! Congrats you got 200!")
        show_emotions("happy", player)
        return 1
    else:
        print("Loser!")
        show_emotions("sad", player)
        return -1
    
def show_profile(player):
    print("Money: {}".format(player.money))
    print("Exp: {}".format(player.exp))
    print("Reputation: {}".format(player.reputation))
    print("Skills:")
    print_ordered_choices(player.skills)

def show_emotions(emotion, player):
    if emotion == "happy":
        print("{} jumps up and down with glee!".format(player.name))
    if emotion == "sad":
        print("{} pouts and gazes down!".format(player.name))



main()
