"""
Word Guessing Game
Author: Satria Dwi Cahya
Purpose: Memahami cara membaca sebuah file dan cara penggunaan list append.
"""
import os 
import random
import re
from termcolor import colored


def clear_screen():
    os.system('cls')


def read_word():
    try:
        with open('words.txt', 'r') as file:
            words = file.read().splitlines()
            return words
    except FileNotFoundError:
        print('words.txt does not exist.')
        return []


def secret_words():
    words = read_word()
    if not words:
        print('No words loaded.')
        return 
            
    secret_word = random.choice(words)
    return secret_word


def display_words(secret_word, guessed_letters):
    word_to_display = ''
    
    for letter in secret_word:
        if letter in guessed_letters:
            word_to_display += letter
        else:
            word_to_display += '_'

    print(f'\n{word_to_display}')


def get_guess(guessed_letters):
    while True:
        guess = input('Enter a letter: ').strip()
        if len(guess) != 1:
            print('Enter only one letter.')
        elif not re.search('[a-z]', guess):
            print('Enter only letters from a to z.')
        elif guess in guessed_letters:
            print('You already guessed that letter.')
        else: 
            return guess


def is_word_guessed(secret_word, guessed_letters):
    for letter in secret_word:
        if letter not in guessed_letters:
            return False
    return True


def main():
    clear_screen()
    secret_word = secret_words()
    print(secret_word)

    attempt = 6
    guessed_letters = []

    while attempt > 0:
        try:
            display_words(secret_word, guessed_letters)
        except TypeError:
            print(colored('Make sure the terminal path is correct', 'red'))    
            break

        guess = get_guess(guessed_letters)
        guessed_letters.append(guess)

        if guess in secret_word:
            print('Good guess')
            if is_word_guessed(secret_word, guessed_letters):
                print(colored('Congratulations! you guessed the word.', 'green'))
                break
        else:
            print('Wrong guess')
            attempt -= 1
            print(f'Your attempt: {attempt}')
            if attempt == 0:
                print(colored(f'Game over! the word was {secret_word}.', 'red'))

                
if __name__ == '__main__':
    main()