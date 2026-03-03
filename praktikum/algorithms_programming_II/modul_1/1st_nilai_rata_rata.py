from colorama import Fore, Style
import os
os.system('cls')

# ─────────────────────────────────────────────
# TUGAS 1: Menghitung Nilai Rata-Rata
# ─────────────────────────────────────────────
def welcome_sign():
    print("=" * 45)
    print("   TUGAS 1 - MENGHITUNG NILAI RATA-RATA")
    print("=" * 45)


def get_valid_input(teks, tipe):
    while True:
        try:
            angka = tipe(input(teks))
            if angka < 1:
                print(Fore.RED + 'Angka tidak boleh sama dengan nol', Style.RESET_ALL)
                continue

            return angka
        except ValueError:
            print(Fore.RED + 'Masukkan nilai yang sesuai', Style.RESET_ALL)


def nilai_rata_rata():
    welcome_sign()

    jumlah_angka = get_valid_input(
        "Masukkan berapa angka yang ingin dihitung: ", int)
    total = 0

    for i in range(1, jumlah_angka + 1):
        angka = get_valid_input(f"  Masukkan angka ke-{i}: ", float)
        total += angka

    rata_rata = total / jumlah_angka

    print(f"\nJumlah angka  : {jumlah_angka}")
    print(f"Total         : {total}")
    print(f"Nilai Rata-rata: {rata_rata:.2f}")


def main():
    nilai_rata_rata()
    input()


if __name__ == "__main__":
    main()