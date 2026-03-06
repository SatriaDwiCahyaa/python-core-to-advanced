import os
os.system('cls')


def linear_search(data, target):

    for indeks in range(len(data)):
        if data[indeks] == target:
            return indeks

    return -1

def pemeriksa():
    data = [12, 32, 34, 23, 43, 56, 76, 78, 87]
    target = 43

    hasil = linear_search(data, target)


    if hasil != -1:
        print(f'{target} ditemukan pada indkes: {hasil}')
    else:
        print(f'{target} tidak ditemukan')

def main():
    pemeriksa()

if __name__ == "__main__":
    main();