"""
Simple Text Editor
Author: Satria Dwi Cahya
Purpose: Memahami cara menggunakan modul sistem untuk membaca atau membuat file dan memasukkan teks ke dalam file tersebut.
"""

import os
from termcolor import colored

def clear_screen():
    os.system('cls')

def welcome_sign():
    print('Simple Text Editor')
    print('------------------')

def read_file(filename):
    with open(filename, 'r') as file:
        return file.read
    

def write_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)


def get_user_content():
    print(f'\nEnter your text (type {colored('SAVE', 'green')} on a new line to save and exist): ')

    contents = []
    while True:
        content = input()
        if content == 'SAVE':
            break
        else:
            contents.append(content)

    return '\n'.join(contents)


def main():
    clear_screen()
    welcome_sign()
    file_name = input('Enter the filename to open or create: ').strip()
    try:    
        if os.path.exists(file_name):
            print(read_file(file_name))
        else:
            write_file(file_name, '')


        content = get_user_content()
        write_file(file_name, content)
        print(f'{file_name} saved.')
    except OSError:
        print(f'{file_name} could not be opened.')


if __name__ == '__main__':
    main()