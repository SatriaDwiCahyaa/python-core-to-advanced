"""
Dice Game
Author: Satria Dwi Cahya
Purpose: Understand how use module from python library
"""
import os
import random


def ClearScreen():
    os.system('cls')


def RandomNumber():
    return random.randint(1, 6)


def LogicGame():
    variabel_control = 'y'

    while variabel_control == 'y':
        ClearScreen()
        print('Dice Game')
        print('---------')
        while True:
            try:
                amount_dice = int(
                    input('How many dice do you want to play: ').strip())
                if amount_dice < 1:
                    print('Amount must be greater than 0')
                    continue
                else:
                    break
            except ValueError:
                print('Please input right number!')

        while True:
            user_input = str(input('Roll the dice? (y/n): ').lower().strip())

            if user_input == 'y':
                for dice in range(1, amount_dice + 1):
                    FirstNumber = RandomNumber()
                    SecondNumber = RandomNumber()
                    print(f'Dice {dice}: ({FirstNumber}, {SecondNumber})')
                break
            elif user_input == 'n':
                print('Thank You!')
                break
            else:
                print('Wrong Input!')

        while True:
            user_continue = input('Continue rolling the dice? (y/n): ').lower()
            if user_continue == 'n':
                variabel_control = 'n'
                print('Thank You!')
                break
            elif user_continue == 'y':
                break
            else:
                print('Wrong Input!')


LogicGame()
