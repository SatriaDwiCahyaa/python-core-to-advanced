"""
Pig Dice Game
Author: Satria Dwi Cahya
Purpose: Memahami penggunaan modul random untuk random number dan list.
"""
import random
import os
from termcolor import colored

NILAI_MAKS = 100

def clear_screen():
    os.system('cls')


def welcome_sign():
    print(colored('\nPig Dice Game', 'green'))
    print('-------------')


def roll_dice():
    return random.randint(1, 6)


def play_turn(player_name):
    turn_score = 0

    print(f'\n{player_name} turn')
    
    while True:
        roll = roll_dice()
        print(f'You rolled a {colored(f'{roll}', 'red')}')

        if roll == 1:
            return 0

        turn_score += roll    
        while True:
            roll_again = input('Roll again? (y/n): ').lower().strip()

            if roll_again == 'y':
                break
            elif roll_again == 'n':  
                return turn_score
            else:
                print('Invalid input!')

def get_name():
    while True:
        player_1 = input("Enter player 1 name: ").strip()
        if len(player_1) < 1:
            print('Player 1 name cannot be empty!')
        else:
            break
    while True:
        player_2 = input("Enter player 2 name: ").strip()
        if len(player_2) < 1:
            print('Player 2 name cannot be empty!')
        else:
            break
    return player_1, player_2
    
    
def main():
    clear_screen()
    welcome_sign()

    scores = [0, 0]

    player_1, player_2 = get_name()
    print('-------------')
    current_player = player_1

    while True:
        turn_score = play_turn(current_player)
        if current_player == player_1:
            scores[0] += turn_score
        else:
            scores[1] += turn_score

        print(f'\nYou scored {turn_score} points this turn.')
        print(f'Current scores: {player_1}: {scores[0]}, {player_2}: {scores[1]}')

        if (current_player == player_1) and (scores[0] >= NILAI_MAKS):
            print(f'{current_player} wins!')
            break
        elif (current_player == player_2) and (scores[1] >= NILAI_MAKS):
            print(f'{current_player} wins!')
            break

        if current_player == player_1:
            current_player = player_2
        else:
            current_player = player_1

        
if __name__ == '__main__':
    main()