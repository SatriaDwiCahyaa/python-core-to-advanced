# =================
#  BINARY SEARCH
# =================

def binarySearch(sumber_data, target):
    kiri = 0
    kanan = len(sumber_data) - 1

    while kiri <= kanan:
        tengah = (kiri + kanan) // 2

        if sumber_data[tengah] == target:
            return tengah

        if sumber_data[tengah] < target:
            kiri = tengah + 1
        else:
            kanan = tengah - 1

    return -1

def main():
    # Data harus urut ascending/descending - binary search
    data = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19] 
    target = 8

    hasil = binarySearch(data, target)

    if hasil != -1:
        print(f"{target} ditemukan pada indeks ke-{hasil}")
    else:
        print(f"{target} tidak ditemukan.")

if __name__ == "__main__":
   main()