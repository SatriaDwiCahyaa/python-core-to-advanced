import os
os.system('cls')
# ====================
#   TUGAS 1
# ====================
PRODUK = [
    'Jaguar', 'Lamborgini', 'Honda', 'Audi', 'Suzuki', 
    'Mazda', 'Daihatsu', 'Ford', 'Hyundai', 'Mitsubishi'
]

HARGA = [
    1_340_000_000,
    34_500_000_000,
    350_000_000,
    2_000_000_000,
    245_000_000,
    500_000_000,
    169_000_000,
    789_000_000,
    122_900_000,
    278_100_000,
]

def mencari_audi():
    
    target = 'Audi'
    ditemukan = False

    for i in range(len(PRODUK)):
        if PRODUK[i] == target:
            print(f' Produk {target} ditemukan!')
            print(f' Lokasi di array : indeks ke-{i} ')
            print(f' Harga           : {HARGA[i]:,.0f}')
            ditemukan = True
            break

    if not ditemukan:
        print(f'\n Produk {target} tidak ditemukan.')


def pengurutan_ascending_termurah():
    pasangan = list(zip(HARGA, PRODUK))
    pasangan.sort(key=lambda x: x[0])

    for rank, (h, p) in enumerate(pasangan, start=1):
        print(f"  {rank:<6} {p:<15} Rp {h:>20,.0f}")
    print()

pengurutan_ascending_termurah()
