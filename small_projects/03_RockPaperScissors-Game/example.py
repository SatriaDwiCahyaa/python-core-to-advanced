"""
Rock Paper Scissors Game
Author: Satria Dwi Cahya
Purpose: 
"""

import os
import random
os.system('cls')


emojis = {
    'r': '🪨',
    'p': '🧾',
    's': '✂️'
}
choices = ('r', 'p', 's')

while True:
    user = input('Rock, Paper, Scissors? (r/p/s): ').lower()
    if user not in choices:
        print('Invalid choice!')
        continue

    computer_choose = random.choice(choices)
    print(
        f'You chose: {emojis[user]}\nComputer chose: {emojis[computer_choose]}')

    if user == computer_choose:
        print('Tie!')
    elif (
        (user == 'r' and computer_choose == 's') or
        (user == 'p' and computer_choose == 'r') or
            (user == 's' and computer_choose == 'p')):
        print('You win')
    else:
        print('You lose')

    should_continue = input('Continue? (y/n): ').lower()
    if should_continue == 'n':
        break
