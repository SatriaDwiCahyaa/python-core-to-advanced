import os
os.system('cls')


def linear_search(data_sumber, target_nilai):
    for indeks in range(len(data_sumber)):

        if data_sumber[indeks] == target_nilai:
        
            return indeks
    
    return -1


def pemeriksa():    
    data = [3, 7, 2, 9, 5, 1, 8, 4, 6]
    target = 4

    hasil = linear_search(data, target)

    if hasil != -1:
        print(f"{target} Ditemukan pada indeks: {hasil}")
    else:
        print(f"{target} Tidak ditemukan")


def main():
    pemeriksa()
    input()


if __name__ == "__main__":
    main()