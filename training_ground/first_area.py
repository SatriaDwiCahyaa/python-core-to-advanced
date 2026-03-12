import os
os.system('cls')


def linear_search(data, target):

    for i, data in enumerate(data):
        if data == target:
            return i

    return -1
        
def binary_search(data, target):
    kiri = 0
    kanan = len(data)

    while kiri <= kanan:
        tengah = (kiri + kanan) // 2

        if data[tengah] == target:
            return tengah
        elif data[tengah] < target:
            kiri = tengah + 1
        else:
            kanan = tengah - 1

    return -1

def pemeriksa(data, target):
    hasil = binary_search(data, target)
    
    if hasil != -1:
        print(f'{target} ditemukan pada indeks ke-{hasil} atau urutan ke-{hasil + 1}')
    else:
        print(f'{target} tidak ditemukan.')


def main():
    data = sorted([10, 23, 34, 12, 34, 56, 87, 54, 32, 545, 67, 54, 43], reverse=False)

    print(data)
    target = 43

    pemeriksa(data, target)

main()