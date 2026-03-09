# ─────────────────────────────────────────────
# TUGAS 2: Lengkapi Class MyInput
# ─────────────────────────────────────────────
def welcome_sign():
    print("=" * 50)
    print("  TUGAS 2 - CLASS MyInput")
    print("=" * 50)


def sebelum_perbaikan():
    class MyInput:
        def baca_string(self):
            return input()
        def baca_int(self):
            while True:
                try:
                    return int(self.baca_string())
                except ValueError:
                    print("Input harus berupa angka! Silakan coba lagi.")


def tugas2_validasi_input():
    class MyInput:
        """Class untuk membaca input dengan validasi tipe data."""

        def baca_string(self):
            """Membaca input sebagai string."""
            return input()

        def baca_int(self):
            """Membaca input sebagai integer dengan validasi loop."""
            while True:
                try:
                    return int(self.baca_string())
                except ValueError:
                    print("Input harus berupa angka! Silakan coba lagi.")

    # Contoh penggunaan
    mi = MyInput()
    print("  Masukkan nama Anda:")
    nama = mi.baca_string()
    print("  Masukkan usia Anda:")
    usia = mi.baca_int()
    print(f"\n  Halo, {nama}! Usia Anda adalah {usia} tahun.\n")


def main():
    tugas2_validasi_input()


if __name__ == "__main__": 
    main()