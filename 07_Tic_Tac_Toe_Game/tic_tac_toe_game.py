"""
Tic Tac Toe Game
Author: Satria Dwi Cahya
Purpose: Memahami cara membuat sebuah matriks 3x3 dengan list dan loop; menambah, menghapus, dan menampilkan item di sebuah list.
"""
# Modul untuk memberikan warna pada teks
import os
from termcolor import colored

# Nilai konstan untuk mempermudah
X = 'X'
O = 'O'

# Template untuk papan
board = [   
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

# Untuk memberishkan terminal dari teks sebelumnya
def clear_screen():
    os.system('cls')

# Memberikan warna merah untuk X dan warna hijau untuk O
def warna_teks(teks):
    if teks == X:
        color = 'red'
    else:
        color = 'green'

    return colored(teks, color)

# Menampilkan board 3x3 setelah diisi pengguna  
def print_board(board):

    lines = '---+---+---'
    print(lines)
    for row in board:
        print(f' {warna_teks(row[0])} | {warna_teks(row[1])} | {warna_teks(row[2])}')
        print(lines)

# Menentukan pemenang dengan memeriksa baris, kolom, dan diagonal dari board 3x3
def check_winner(board):

    # horizontal
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return True  

    # vertikal
    for column in range(3):
        if board[0][column] == board[1][column] == board[2][column] != ' ':
            return True

    # Diagonal
    if board[0][0] == board[1][1] == board[2][2] != ' ' or board[0][2] == board[1][1] == board[2][0] != ' ':
        return True
    
    return False

# Memberi tahu user bahwa papan sudah terisi penuh dan tidak bisa bermain lagi
def is_full(board):
    for row in board:
        if ' ' in row:
            return False    
        
    return True

# Mengambil masukan dari user dan mengatasi error ketika user memberikan nilai yang tidak sesuai
def get_position(promt):
    while True:
        try:
            position = int(input(promt))
            if position < 0 or position > 2:
                raise ValueError
            return position
        except ValueError:
            print('Invalid input!')

# Memberi tahu user bahwa posisi sudah di tempati
def get_move(current_player):
    print(f'Player {current_player} turn!')
    while True:
        row = get_position('Enter row (0-2): ')
        column = get_position('Enter Coloumn (0-2): ')

        if board[row][column] == ' ':
            board[row][column] = current_player
            break

        print('This spot is alrady taken!')


# orchestrator = hanya untuk pemanggilan fungsi dan mengatur alur
def main():
    clear_screen()
    current_player = X

    while True:
        get_move(current_player)
        print_board(board)
        
        if check_winner(board):
            print(f'Player {current_player} is wins!')
            break

        if is_full(board):
            print('Board is full!')
            break

        if current_player == X:
            current_player = O
        else:
            current_player = X


if __name__ == "__main__":
    main()