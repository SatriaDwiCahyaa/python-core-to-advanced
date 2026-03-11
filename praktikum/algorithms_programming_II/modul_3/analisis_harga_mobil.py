# ============================================================
#  MODUL 3 - SEARCHING
# ============================================================

# ─────────────────────────────────────────────
# TUGAS 1: DATA PRODUK & HARGA
# ─────────────────────────────────────────────
produk = [
    "Jaguar", "Lamborghini", "Honda", "Audi",      "Suzuki",
    "Mazda",  "Daihatsu",   "Ford",  "Hyundai",   "Mitsubishi"
]

harga = [
    1_340_000_000,
    34_500_000_000,
       350_000_000,
     2_000_000_000,
       245_000_000,
       500_000_000,
       169_000_000,
       789_000_000,
       122_900_000,
       278_100_000
]


# ─────────────────────────────────────────────
# Tampilkan seluruh data array
# ─────────────────────────────────────────────
def tugas1_tampil_data():
    print("=" * 55)
    print("  TUGAS 1 - DATA PRODUK & HARGA")
    print("=" * 55)
    print(f"  {'No':<4} {'Produk':<15} {'Harga (Rp)'}")
    print(f"  {'─'*4} {'─'*15} {'─'*20}")
    for i in range(len(produk)):
        print(f"  {i:<4} {produk[i]:<15} Rp {harga[i]:>20,.0f}")
    print()


# ─────────────────────────────────────────────
# TUGAS 2: Cari "Audi" dan tampilkan lokasinya
# ─────────────────────────────────────────────
def tugas2_cari_audi():
    print("=" * 55)
    print("  TUGAS 2 - PENCARIAN PRODUK 'AUDI'")
    print("=" * 55)

    target   = "Audi"
    ditemukan = False

    # Sequential Search
    for i in range(len(produk)):
        if produk[i] == target:
            print(f"\n  Produk '{target}' DITEMUKAN!")
            print(f"  Lokasi di array  : indeks ke-{i}")
            print(f"  Harga            : Rp {harga[i]:,.0f}")
            ditemukan = True
            break

    if not ditemukan:
        print(f"\n  Produk '{target}' tidak ditemukan.")
    print()


# ─────────────────────────────────────────────
# TUGAS 3: Urutkan harga dari termurah ke termahal
# ─────────────────────────────────────────────
def tugas3_urutkan_harga():
    print("=" * 55)
    print("  TUGAS 3 - PRODUK DIURUTKAN BERDASARKAN HARGA")
    print("        (Termurah → Termahal)")
    print("=" * 55)

    # Buat pasangan (harga, produk) lalu urutkan
    pasangan = list(zip(harga, produk))
    pasangan.sort(key=lambda x: x[0])   # Bubble sort menggunakan built-in sort

    print(f"\n  {'Rank':<6} {'Produk':<15} {'Harga (Rp)'}")
    print(f"  {'─'*6} {'─'*15} {'─'*20}")
    for rank, (h, p) in enumerate(pasangan, start=1):
        print(f"  {rank:<6} {p:<15} Rp {h:>20,.0f}")
    print()

    return pasangan  # Dikembalikan untuk dipakai Tugas 4


# ─────────────────────────────────────────────
# TUGAS 4: Harga produk termurah nomor ke-2
# ─────────────────────────────────────────────
def tugas4_termurah_kedua():
    print("=" * 55)
    print("  TUGAS 4 - PRODUK TERMURAH NOMOR KE-2")
    print("=" * 55)

    # Urutkan terlebih dahulu
    pasangan = list(zip(harga, produk))
    pasangan.sort(key=lambda x: x[0])

    h_termurah2, p_termurah2 = pasangan[1]  # indeks 1 = urutan ke-2

    print(f"\n  Produk Termurah #1 : {pasangan[0][1]:<15} Rp {pasangan[0][0]:,.0f}")
    print(f"  Produk Termurah #2 : {p_termurah2:<15} Rp {h_termurah2:,.0f}")
    print()


# ─────────────────────────────────────────────
# MENU UTAMA MODUL 3
# ─────────────────────────────────────────────
def main():
    while True:
        print("\n========================================")
        print("   MODUL 3 - SEARCHING")
        print("========================================")
        print("  [1] Tugas 1 - Tampilkan Semua Data")
        print("  [2] Tugas 2 - Cari Produk 'Audi'")
        print("  [3] Tugas 3 - Urutkan Harga")
        print("  [4] Tugas 4 - Produk Termurah ke-2")
        print("  [0] Keluar")
        print("========================================")
        pilih = input("Pilih menu: ")

        if pilih == "1":
            tugas1_tampil_data()
        elif pilih == "2":
            tugas2_cari_audi()
        elif pilih == "3":
            tugas3_urutkan_harga()
        elif pilih == "4":
            tugas4_termurah_kedua()
        elif pilih == "0":
            print("Keluar dari Modul 3. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")


if __name__ == "__main__":
    main()