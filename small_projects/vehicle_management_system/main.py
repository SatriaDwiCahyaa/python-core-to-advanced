import os
os.system('cls')


def menu():
    menu = ['1. Tambah Kendaraan', '2. Lihat Kendaraan', '3. Sorting', '4. Simpan']
    for promt in menu:
        print(promt)

def get_input():
    valid_input = [1, 2, 3, 4]

    while True:
        try:
            pilihan = int(input('Pilihan: '))
            if pilihan in valid_input:
                return pilihan
            else:
                print('Hanya ada 4 pilihan!')

        except ValueError:
            print('Masukkan input dengan benar!')

def main():
    menu()
    pilihan = get_input()



if __name__ == "__main__":
    main()