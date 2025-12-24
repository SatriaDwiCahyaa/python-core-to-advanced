"""
Topic: Loops, If Statement
Project: Dice Game

"""

import random
import os
# ClearScreen
os.system('cls')
angka_acak = random.randint(0, 5)

user = 'y'

while user == 'y':
    user_input = input('Roll the dice? (y/n): ')

    if user_input != 'n':
        print(f'({random.randint(0, 5)}, {random.randint(0, 5)})')
    else:
        user = 'n'
        print('Permainan Selesai')