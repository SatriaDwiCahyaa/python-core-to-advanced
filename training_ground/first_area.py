import os
os.system('cls')


def linear_search(sumber_data, target):

    for data in range(len(sumber_data)):
        if sumber_data[data] == target:
            return data
        
    return -1      


def binary_search(sumber_data, target):
    
    kiri = 0
    kanan = len(sumber_data)

    while kiri <= kanan:
        tengah = (kiri + kanan) // 2

        if sumber_data[tengah] == target:
            return tengah
        elif sumber_data[tengah] < target:
            kiri = tengah + 1
        else:
            kanan = tengah - 1
    
    return -1


def pemeriksa(sumber_data, target):
    hasil = binary_search(sumber_data, target)

    if hasil != -1:
        print(f'{target} ditemukan pada indeks {hasil} atau urutan ke-{hasil+1}')
    else:
        print(f'{target} tidak ditemukan')

def main():
    data = [99, 20, 17, 8, 27, 5, 21, 10, 41, 11] 
    cari = 8

    pemeriksa(data, cari)


main()