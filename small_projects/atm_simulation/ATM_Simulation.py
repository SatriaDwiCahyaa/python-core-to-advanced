"""
ATM Simulation
Author: Satria Dwi Cahya
Purpose: Memahami cara menggunakan class
"""
import os
from termcolor import colored

def clear_screen():
        os.system('cls')

class ATM:
    def __init__(self):
        self.balance = 0
    
    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError('Deposit amount must be positive.')

        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError('Withdraw amount must be positive')
        if amount > self.balance:
            raise ValueError('Insufficient funds.')

        self.balance -= amount


class ATMController:
    def __init__(self):
        self.atm = ATM()

    def display_menu(self):
        print('\nWelcome to the ATM!' \
        '\n1. Check Balance' \
        '\n2. Deposit' \
        '\n3. Withdraw' \
        '\n4. Exit')

    # Mendapatkan nilai float/pecahan dari perintah/fungsi yang sesuai
    def get_number(self, promt):
        while True:
            try:
                number = float(input(promt))
                return number
            except ValueError:
                print('Please enter a valid number!')


    def check_balance(self):
        balance = self.atm.check_balance()
        print(f'Your current balance is: ${balance}')


    def deposit(self):
        while True:
            try:
                amount = self.get_number('Enter the amount to deposit: ')
                self.atm.deposit(amount)
                print(colored('Successfully','green'), f'deposited ${amount}')
                break
            except ValueError as eror:
                print(eror)


    def withdraw(self):
        while True:
            try:
                amount = self.get_number('Enter the amount to withdraw: ')
                self.atm.withdraw(amount)
                print(colored('Successfully', 'green'), f'withdrew ${amount}')
                break
            except ValueError as eror:
                print(eror)


    def run(self):
        while True:
            self.display_menu()

            choice = input('Please choose an option: ')
            if choice == '1':
                self.check_balance()
            elif choice == '2':
                self.deposit()
            elif choice == '3':
                self.withdraw()
            elif choice == '4':
                print('Thank you for using the ATM.')
                break
            else:
                print('Invalid choice, please try again!')
        
def main():
    clear_screen()
    atm = ATMController()
    atm.run()


if __name__ == '__main__':
    main()