"""
Mastermind
Generate a random four digit number. The player has to keep inputting four digit numbers until they guess the randomly generated number. After each unsuccessful try it should say
how many numbers they got correct, but not which position they got right. At the end of the game should congratulate the user and say how many tries it took.
"""

import random


def random_generator():
    num_random = random.randint(1000, 9999)
    print(num_random, type(num_random))
    return num_random


ranking = []


def menu():
    print(" 1 - guess a 04-digit number\n"
          " 2 - see highscore\n"
          " 3 - exit\n")

def start_game():
    choice_menu = input("Choose an option: ")
    if choice_menu in declarations_menu.keys():
        declarations_menu[choice_menu]()


def play_game(score=1,a=0):
    if score == 1:
        a = random_generator()
    num_guess = int(input("Insert your guess: \t"))
    if num_guess == a:
        print("you find it!")
        name = input("What's your name?")
        print(f"You find it at {score} chance")
        player_1 = {}
        player_1[name] = score
        ranking.append(player_1)
        menu()
        start_game()

    else:
        for i in str(num_guess):
            if i in str(a):
                print(f"number {i} is in the number")
        score += 1
        print(f"This is you {score} chance")
    play_game(score, a)


def see_highscore():
    print("highscore:")
    print(ranking)
    menu()
    start_game()


def exit_program():
    exit()


declarations_menu = {
    "1": play_game,
    "2": see_highscore,
    "3": exit_program,
}

while True:
    menu()
    start_game()

