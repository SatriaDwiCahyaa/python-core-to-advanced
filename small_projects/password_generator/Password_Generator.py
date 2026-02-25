"""
Password Generator
Author: Satria Dwi Cahya
Purpose: Memahami penggunaan modul string dan number untuk membuat sebuah password dengan mengacak karakter yang sudah ditambahkan oleh modul yang sudah ditetapkan.
"""
import os
import string
import random


def clear_screen():
    os.system('cls')


def welcome_sign():
    print('Password generator')
    print('------------------')


def validation_input(promt):
    instruction = promt

    if instruction == 'Enter password length: ':
        while True:
            try:
                promt = int(input(instruction).strip())
                return promt
            except ValueError:
                print('Must enter a number')


def get_password_criteria():
    length_pass = validation_input('Enter password length: ') 
    uppercase_pass = input('Include uppercase letters? (y/n): ').lower() == 'y'
    number_pass = input('Include number? (y/n): ').lower() == 'y'
    special_pass = input('Include special characters? (y/n): ').lower() == 'y'

    return length_pass, uppercase_pass, number_pass, special_pass


def generate_password():
    length, uppercase, numbers, special = get_password_criteria()

    if length < (uppercase + numbers + special):
        raise ValueError('Password length is too short for the specified criteria.')
  
    password = ''

    if uppercase:
        password += random.choice(string.ascii_uppercase)
    if numbers:
        password += random.choice(string.digits)
    if special:
        password += random.choice(string.punctuation)

    # Fill the remaining length with any allowed characters
    characters = string.ascii_lowercase
    if uppercase:
        characters += string.ascii_uppercase
    if numbers:
        characters += string.digits
    if special:
        characters += string.punctuation

    for _ in range(length - len(password)):
        password += random.choice(characters)

    password_list = list(password)
    random.shuffle(password_list)
    return ''.join(password_list)


def main():
    clear_screen()
    welcome_sign()
    
    try:
        password = generate_password()
        print(f'Generated password: {password}')
    except ValueError as e:
        print(e)
    
    
if __name__ == '__main__':
    main()