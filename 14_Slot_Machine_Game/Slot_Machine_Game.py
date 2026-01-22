"""
Sloth Machine Game
Author: Satria Dwi Cahya
Purpose: 
"""
import os


def clear_screen():
    os.system('cls')


def get_starting_balance():
    while True:
        try:
            user_balance = int(input('Enter your starting balance: $').strip())
            if user_balance <= 0:
                print('Balance must a positive number.')
            else:
                return user_balance
        except ValueError:
            print('Please enter a valid number')


def get_bet_amount(user_balance):
    while True:
        try:
            bet = int(input('Enter your bet amount: $').strip())

            if bet > user_balance or bet <= 0:
                print(
                    f'Invalid bet amount. You can bet between $1 and ${user_balance}.')
            else:
                return bet
        except ValueError:
            print('')


def welcome_sign(user_balance):
    print('\nWelcome to the slot Machine Game!')
    print(f'You start with a balance of ${user_balance}')


# def slot_logic():


def main():
    clear_screen()

    balance = get_starting_balance()

    welcome_sign(balance)


if __name__ == '__main__':
    main()
