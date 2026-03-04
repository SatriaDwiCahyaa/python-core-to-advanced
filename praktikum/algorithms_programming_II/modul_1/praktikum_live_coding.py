import os
os.system('cls')


def main():

    banyak_data = int(input('Masukkan berapa angka yang ingin dihitung: '))

    total = 0

    for x in range(1, banyak_data + 1):
        nilai = float(input(f'Masukkan Angka ke-{x}: '))
        total += nilai

    rata_rata = total / banyak_data


    print(f'\nNilai rata-rata: {rata_rata:.2f}')

if __name__ == '__main__':
    main()