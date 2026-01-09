"""
Password Strength Checker
Author: Satria Dwi Cahya
Purpose: Memahami penggunaan modul re untuk mencari sebuah pola pada teks yang diberikan user.
"""
import os
import re

def clear_screen():
    os.system('cls')


def welcome_sign():
    print('Password Strength Checker')
    print('-------------------------')


def get_password():
    while True:
        password = input('Enter a password: ')
        
        if len(password) >= 1:
            print('Minimum password length is 1 letter')
        else: 
            return password


def password_criteria(criteria):
    rating = {
        1 : 'Very Weak',
        2 : 'Weak',
        3 : 'Medium',
        4 : 'Strong',
        5 : 'Very Strong'
    }

    return rating[criteria]    


def checker(password):
    strength = 0

    if len(password) >= 8:
        strength += 1
    if re.search('[a-z]', password):
        strength += 1
    if re.search('[A-Z]', password):
        strength += 1
    if re.search('[0-9]', password):
        strength += 1
    if re.search('[@#$%+=!]', password):
        strength += 1

    return strength    


def print_criteria(criteria):
    print(f'\nPassword strength: {password_criteria(criteria)}')


def main():
    control_variable = True
    while control_variable:
        clear_screen()
        welcome_sign()
             
        password = get_password()
        criteria = checker(password)
        print_criteria(criteria)

        
        while True:
            choice = input('\nCheck again? (y/n): ').lower().strip()
            if choice == 'y':
                break
            elif choice == 'n':
                control_variable = False
                break
            else:
                print('Invalid input!')


if __name__ == '__main__':
    main()