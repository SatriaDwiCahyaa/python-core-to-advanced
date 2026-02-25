"""
Sloth Machine Game
Author: Satria Dwi Cahya
Purpose: Memahami cara slot bekerja, yaitu dengan modul random.
"""
import os
import random

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
            print('Please enter a valid number for the bet emount.')

def spin_reels():
    symbols = ['🍒', '🍋', '🔔', '⭐️', '🍉']    
    return [random.choice(symbols) for _ in range(3)]

def display_reels(reels):
    print(f'{reels[0]} | {reels[1]} | {reels[2]}')

def welcome_sign(user_balance):
    print('\nWelcome to the slot Machine Game!')
    print(f'You start with a balance of ${user_balance}')

def calculate_payout(reels, bet):
    if reels[0] == reels[1] == reels [2]:
        return bet * 10
    if reels[0] == reels[1] or reels[0] == reels[2] or reels[1] == reels[2]:
        return bet * 2
    return 0

def main():
    clear_screen()
    
    balance = get_starting_balance()

    welcome_sign(balance)

    while balance > 0:
        print(f'\nCurrent balance: ${balance}')

        bet = get_bet_amount(balance)
        reels = spin_reels()
        display_reels(reels)
        payout = calculate_payout(reels, bet)

        if payout > 0:
            print(f'You won ${payout}!')
        else:
            print('You lost!')

        balance += payout - bet

        if balance <= 0:
            print('\nYou are out of money! Game over.')
            break
        
        variable_control = True
        
        while variable_control:
            play_again = input('Do you want to play again? (y/n): ').strip().lower()
            if play_again == 'n':
                print(f'\nYou walk away with ${balance}')
                variable_control = False
                break
            elif play_again == 'y':
                break
            else:
                print('Enter a right value!')

        if variable_control == False:
            break


if __name__ == '__main__':
    main()