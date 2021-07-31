# Stage 5
import random


def rating_txt(name1):
    with open('rating.txt', 'r') as file_r:
        for line in file_r:
            if name1 == (line.split())[0]:
                score1 = (line.split())[1]
                break

        else:
            score1 = 0

    return int(score1)


def rpc_game(answer1, score2, list_of_options_1):
    winning_cases = {
        'water': ['scissors', 'fire', 'rock', 'gun', 'lightning', 'devil', 'dragon'],
        'dragon': ['snake', 'scissors', 'fire', 'rock', 'gun', 'lightning', 'devil'],
        'devil': ['tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun'],
        'gun': ['wolf', 'tree', 'human', 'snake', 'scissors', 'fire', 'rock'],
        'rock': ['sponge', 'wolf', 'tree', 'human', 'snake', 'scissors', 'fire'],
        'fire': ['paper', 'sponge', 'wolf', 'tree', 'human', 'snake', 'scissors'],
        'scissors': ['air', 'paper', 'sponge', 'wolf', 'tree', 'human', 'snake'],
        'snake': ['water', 'air', 'paper', 'sponge', 'wolf', 'tree', 'human'],
        'human': ['dragon', 'water', 'air', 'paper', 'sponge', 'wolf', 'tree'],
        'tree': ['devil', 'dragon', 'water', 'air', 'paper', 'sponge', 'wolf'],
        'wolf': ['lightning', 'devil', 'dragon', 'water', 'air', 'paper', 'sponge'],
        'sponge': ['gun', 'lightning', 'devil', 'dragon', 'water', 'air', 'paper'],
        'paper': ['rock', 'gun', 'lightning', 'devil', 'dragon', 'water', 'air'],
        'air': ['fire', 'rock', 'gun', 'lightning', 'devil', 'dragon', 'water'],
        'lightning': ['tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun']
    }
    selected_winning_cases = {}
    for item in list_of_options_1:
        selected_winning_cases[item] = winning_cases[item]

    choice1 = random.choice(list(selected_winning_cases.keys()))

    if choice1 in selected_winning_cases[answer1]:
        print(f"Well done. The computer chose {choice1} and failed")
        score2 = score2 + 100
    elif choice1 == answer1:
        print(f"There is a draw ({choice1})")
        score2 = score2 + 50
    else:
        print(f"Sorry, but the computer chose {choice1}")

    return score2


name = input("Enter your name:")
print(f"Hello, {name}")
score = rating_txt(name)
list_of_options = input().split(sep=',')
print("Okay, let's start")

if len(list_of_options) == 1:
    list_of_options = ['rock', 'paper', 'scissors']

while True:
    answer = input().strip()
    if answer == '!exit':
        print("Bye!")
        break
    elif answer == '!rating':
        print(f"Your rating: {score}")

    elif answer in list_of_options:
        score = rpc_game(answer, score, list_of_options)

    elif answer not in list_of_options:
        print("Invalid input")
        continue

#
# #alternate solution
# choices = ['rock', 'fire', 'scissors', 'snake', 'human', 'tree', 'wolf', 'sponge', 'paper', 'air', 'water', 'dragon',
#            'devil', 'lightning', 'gun'] * 2
#
# choice1 = 'gun'
# random_choice =  random.choice(choices)
# print(f"random : {random_choice}, user: {choice1}")
#
# #list of items that will get defeated by the choice1
# # Last item is not included
# weaker_options_list = choices[choices.index(choice1) + 1:choices.index(choice1) + 8]
# print(f"weaker_options_list: {weaker_options_list}")
#
# if random_choice in weaker_options_list:
#     print('user wins')
# elif random_choice == choice1:
#     print('draw')
# else:
#     print('computer wins')
