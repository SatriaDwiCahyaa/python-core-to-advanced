# =================
#  LINEAR SEARCH
# =================

def linearSearch(sumber_data, target):
    for i in range(len(sumber_data)):
        if sumber_data[i] == target:
            return i
    return -1

def main():
    data = [3, 7, 2, 9, 5, 1, 8, 4, 6]
    target = 4

    hasil = linearSearch(data, target)

    if hasil != -1:
        print(f"{target} ditemukan pada indeks ke-{hasil}")
    else:
        print(f"{target} tidak ditemukan.")

if __name__ == "__main__":
   main()