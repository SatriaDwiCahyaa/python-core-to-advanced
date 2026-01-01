"""
Number Guessing Game
Author: Satria Dwi Cahya
Purpose: Practice basic Python Logic
"""

import os
import random

def clear_screen():
    os.system('cls')

def welcome_sign():
    clear_screen()
    print('Welcome to the Number Guessing Game!')
    print('------------------------------------')

def right_number(angka_awal, angka_akhir):
    return random.randint(angka_awal, angka_akhir)

def specific_value():
    attempt = 0

    while True:
        try:
            print('Select range of value for the number')
            minimum_number = int(input('Minimum Number: '))
            maximum_number = int(input('Maximum Number: '))

            if minimum_number > maximum_number:
                print('Minimum number must less than maximum number!')
            elif (minimum_number < 1) or (maximum_number < 1):
                print('Number must be greater than 0')
            elif (maximum_number > 9999) or (minimum_number > 9999):
                print('Maximum number is 9999!')
            else:
                break
        except ValueError:
            print('Please input right number!') 

    right_answer = random.randint(int(minimum_number), int(maximum_number))
    
    while True:
        try:
            user = int(input(f'Guess the number (between {minimum_number} and {maximum_number}): '))

            if user > right_answer:
                print('Too high! Try again.')
                attempt += 1
            elif user < right_answer:
                print('Too low! Try again.')
                attempt += 1
            else:
                attempt += 1
                print('Congratulations! You guessed the number in ', attempt, ' attempts')
                break
        except ValueError:
            print('Please input right number!')

def DefaultGame():
    attempt = 0
    angka_awal = random.randint(1, 500)
    angka_akhir = random.randint(501, 999)
    right_answer = right_number(angka_awal, angka_akhir)

    while True:
        try:
            user = int(input(f'Guess the number (between {angka_awal} and {angka_akhir}): '))


            if user > right_answer:
                print('Too high! Try again.')
                attempt += 1
            elif user < right_answer:
                print('Too low! Try again.')
                attempt += 1
            else:
                attempt += 1
                print()
                print('Congratulations! You guessed the number in ', attempt, ' attempts')
        except ValueError:
            print('Please input number!')


welcome_sign()
while True:
    choice_mode = input('Do you want a specific value? (Y/N): ').lower().strip()

    if choice_mode == 'y':
        specific_value()    
        break
    elif choice_mode == 'n':
        DefaultGame()
        break
    else:
        print('Wrong Input!')  