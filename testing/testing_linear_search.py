import os
os.system('cls')


def linear_search(sumber_data, target):

    for indeks in range(len(sumber_data)):
        if sumber_data[indeks] == target:
            return indeks
    return -1


# Tes penamaan
def area_pemeriksaan():    
    unorder_data = [66, 34, 67, 23, 96, 34, 12, 56]
    target = 12

    hasil = linear_search(unorder_data, target)

    if hasil != -1:
        print(f'Hasil ditemukan\nindeks\t: {hasil}\nData\t: {target}')
    else:
        print('Data tidak ditemukan:')


def main():
    area_pemeriksaan()


if __name__ == "__main__":
    main()