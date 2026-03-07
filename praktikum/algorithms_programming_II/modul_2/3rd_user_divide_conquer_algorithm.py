def welcome_sign():
    print("=" * 50)
    print("  TUGAS 3 - PENGURUTAN DENGAN DIVIDE AND CONQUER")
    print("          (Merge Sort)")
    print("=" * 50)

def merge_sort(arr):
    """
    Divide and Conquer - Merge Sort:
    1. DIVIDE  : Bagi array menjadi dua bagian (kiri & kanan).
    2. CONQUER : Urutkan masing-masing bagian secara rekursif.
    3. COMBINE : Gabungkan dua bagian yang sudah terurut.
    """
    if len(arr) <= 1:
        return arr

    # --- DIVIDE ---
    mid   = len(arr) // 2
    kiri  = merge_sort(arr[:mid])
    kanan = merge_sort(arr[mid:])

    # --- COMBINE ---
    return merge(kiri, kanan)

def merge(kiri, kanan):
    """Menggabungkan dua list terurut menjadi satu list terurut."""
    hasil = []
    i = j  = 0

    while i < len(kiri) and j < len(kanan):
        if kiri[i] <= kanan[j]:
            hasil.append(kiri[i])
            i += 1
        else:
            hasil.append(kanan[j])
            j += 1

    # Tambahkan sisa elemen
    hasil.extend(kiri[i:])
    hasil.extend(kanan[j:])
    return hasil

def main():    
    # Input dari user
    n = int(input("  Masukkan jumlah bilangan: "))
    bilangan = []
    for i in range(n):
        angka = int(input(f"    Bilangan ke-{i + 1}: "))
        bilangan.append(angka)

    print(f"\n  Data awal   : {bilangan}")
    hasil = merge_sort(bilangan)
    print(f"  Hasil Urut  : {hasil}\n")

if __name__ == "__main__":
    main()