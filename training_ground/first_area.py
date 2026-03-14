import os
os.system('cls')


def binary_search(sumber_data, target):
    kiri = 0
    kanan = len(sumber_data) - 1

    ascending = sumber_data[kiri] < sumber_data[kanan]

    while kiri <= kanan:
        tengah = (kiri + kanan) // 2

        if sumber_data[tengah] == target:
            return tengah
        if ascending:
            if sumber_data[tengah] < target:
                kiri = tengah + 1
            else:
                kanan = tengah - 1
        else:
            if sumber_data[tengah] < target:
                kanan = tengah - 1
            else:
                kiri = tengah + 1
    return -1

def pemeriksa():
    # Data urut ascending/descending
    data = sorted([213, 34, 45, 423, 43, 54, 23, 45, 56, 78], reverse=True)
    target = 23

    # Binary
    hasil = binary_search(data, target)

    # Print Data
    print(f'Data: {data}')

    if hasil != -1:
        print(f'\n{target} ditemukan pada indeks ke-{hasil} atau urutan ke-{hasil + 1}')
    else:
        print(f'{target} tidak ditemukan.')

def main():
    pemeriksa()
    input()

if __name__ == "__main__":
    main()