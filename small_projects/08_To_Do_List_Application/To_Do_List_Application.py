"""
To-Do List Application
Author: Satria Dwi Cahya
Purpose: Memahami menambahkan, menampilkan, dan menghapus item di sebuah list.
"""
import os
from termcolor import colored


def clear_screen():
    os.system('cls')


def print_menu():
    print('\nTodo List Menu:')
    print('1. View Tasks')
    print('2. Add a Task')
    print('3. Remove a Task')
    print('4. Exit')


# Pilihan Pertama
def display_tasks(task):
    if len(task) == 0:
        print(colored('No tasks in the list.', 'red'))
    else:
        print(colored('Your task:', 'green'))
        for index, item in enumerate(task, 1):
            print(f'{index}. {item}')
        

# Pilihan Kedua
def add_task(task):
    while True:
        new_task = input('Enter a new task: ').strip()
        if len(new_task) != 0:
            task.append(new_task)
            break
        else:
            print(colored('Invalid Task!', 'red'))


# Pilihan Ketiga
def remove_task(task):
    display_tasks(task)

    while True:
        try:
            task_number = int(input('Enter the task number: ').strip())
            if 1 <= task_number <= len(task):
                task.pop(task_number - 1)
                break
            else:
                raise ValueError
        except ValueError:
            print(colored('Invalid Task!', 'red'))


# Meminta pengguna untuk memilih menu dengan sesuai.
def get_choice():
    valid_choice = ('1', '2', '3', '4')
    while True:
        choice = input('Enter you choice: ')
        if choice not in valid_choice:
            print(colored('Invalid Choice!', 'red'))
        else:
            return choice
        
# Orchestrator  
def main():
    clear_screen()
    task = []

    while True:
        print_menu()
        
        choice = get_choice()

        if choice == '1':
            display_tasks(task)
        elif choice == '2':
            add_task(task)
        elif choice == '3':
            remove_task(task)
        else:
            print(colored('Thank you, see u again!', 'blue'))
            break


if __name__ == '__main__':
    main()
