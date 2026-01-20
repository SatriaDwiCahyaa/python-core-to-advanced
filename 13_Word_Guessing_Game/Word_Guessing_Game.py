"""
Word Guessing Game
Author: Satria Dwi Cahya
Purpose: 
"""
import os 
import random

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

def secret_word():
    
    words = read_word()
    if not words:
        print('No words loaded.')
        return 
            
    secret_word = random.choice(words)
    return secret_word
    
def main():
    clear_screen()
    secret = secret_word()
    print(secret)

if __name__ == '__main__':
    main()