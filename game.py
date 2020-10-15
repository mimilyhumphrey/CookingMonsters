import os
import random


ALL_SKILLS = [
    "Asian Cooking",
    "French Baking",
    "Mediterranean cooking",
    "Latin American cooking"
]
class Player:
    def __init__(self, name):
        self.money = 500
        self.reputation = 2
        self.exp = 0
        self.name = name
        self.skills = {}

def main():
    new_name = input("What is your monster's name? ")
    new_name = new_name.capitalize()
    player = Player(new_name)
    
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
    #player.skills.append(new_skill)
    #check if player has new skill
    #if yes then increase level by 1
    #if no then add a new skill to key and value 1
    # { 'french_cooking': 1 }
    if new_skill in player.skills:
        player.skills[new_skill] += 1
    else:
        player.skills[new_skill] = 1
    increase = 10
    print('Yay you trained hard!  You gained {} exp points and learned {}'.format(increase, new_skill))
    return increase


def enter_contest(player):
    player.money -= 100

    """
pick a theme for the contest
use randomly choose a theme
check if the player has the skill in the theme
if yes give them extra 10 *10 (skill bonus = skill level *10)
add skill bonus to result 115
print (you receive extra bonus since you haave ..skill)
    """
    
    print("It costs 100 for entry fee")
    rand_theme = random.choice(ALL_SKILLS)
    if rand_theme in player.skills:
        skill_bonus = player.skills[rand_theme]*10
        print("You receive {} extra bonus since you have the {} skill".format(skill_bonus, rand_theme))   
    else:
        skill_bonus = 0
    rand = random.randint(0, 100)
    result = rand + player.exp + skill_bonus
    
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
    print_skills(player)

def show_emotions(emotion, player):
    if emotion == "happy":
        print("{} jumps up and down with glee!".format(player.name))
    if emotion == "sad":
        print("{} pouts and gazes down!".format(player.name))

def print_skills(player):
    for skill, level in player.skills.items():
        print("{}: {}".format(skill, level))

main()
