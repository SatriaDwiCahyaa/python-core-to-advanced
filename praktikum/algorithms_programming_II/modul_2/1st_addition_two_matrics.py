# ─────────────────────────────────────────────
# TUGAS 1: Penjumlahan 2 Matriks 2x3
# ─────────────────────────────────────────────
def welcome_sign():
    print("=" * 50)
    print("  TUGAS 1 - PENJUMLAHAN MATRIKS A + B (2x3)")
    print("=" * 50)

BARIS, KOLOM = 2, 3

def input_matriks(nama):
    print(f"\n  Masukkan elemen Matriks {nama} ({BARIS}x{KOLOM}):")
    matriks = []
    for i in range(BARIS):
        baris = []
        for j in range(KOLOM):
            nilai = int(input(f"    {nama}[{i}][{j}]: "))
            baris.append(nilai)
        matriks.append(baris)
    return matriks

def tampil_matriks(nama, matriks):
    print(f"\n  Matriks {nama}:")
    for baris in matriks:
        print("   ", baris)

def jumlah_matriks(A, B):
    hasil = []
    for i in range(BARIS):
        baris = []
        for j in range(KOLOM):
            baris.append(A[i][j] + B[i][j])
        hasil.append(baris)
    return hasil

def main():
    A = input_matriks("A")
    B = input_matriks("B")

    tampil_matriks("A", A)
    tampil_matriks("B", B)

    C = jumlah_matriks(A, B)
    tampil_matriks("A + B", C)
    print()

if __name__ == "__main__":
    main()