import os
os.system('cls')


# --- TUGAS 1 ---
produk = ['Jaguar', 'Lamborghini', 'Honda', 'Audi', 'Suzuki', 
          'Mazda', 'Daihatsu', 'Ford', 'Hyundai','Mitsubishi' 
          ]

harga = [ 1_340_000_000, 34_500_000_000, 350_000_000, 2_000_000_000, 
         245_000_000, 500_000_000, 169_000_000, 789_000_000, 122_900_000, 278_100_000
         ]     

# --- Tugas 2 ----
def tampilkan_audi():
    target = 'Audi'
    ditemukan = False
    print('=' * 45)
    print(f'{'':<15}Produk {target}')
    print('=' * 45)

    for indeks, data in enumerate(produk):
        if data == target:
            print(f'\n Produk {target} Ditemukan!')
            print(f' Lokasi di array  : indeks ke-{indeks}')
            print(f' Harga            : Rp{harga[indeks]:,.0f}')
            ditemukan = True
            break

    if not ditemukan:
        print(f'\nProduk {target} tidak ditemukan')

# --- Tugas 3 ---    
def sorting_cheap_expensive():
    print('=' * 45)
    print(f'{'':<7}Urutan Produk Termurah - Mahal')
    print('=' * 45)

    # Memasangkan nama produk dengan harga
    pasangan_data = list(zip(harga, produk))
    
    # Mengurutkan menggunakan bubble sort
    pasangan_data.sort(key=lambda x: x[0])

    for rank, (h, p) in enumerate(pasangan_data, start=1):
        print(f'{rank:<5} {p:<15} Rp {h:,.0f} ')

    return pasangan_data

# --- Tugas 4 ---
def second_cheap_produk(pasangan_data): 
    print('=' * 45)
    print(f'{'':<7}Produk Termurah Nomor 2')
    print('=' * 45)

    h_termurah_2 = pasangan_data[1]

    print(f'Produk Termurah ke-2 : {h_termurah_2[1]:<10} Rp {h_termurah_2[0]:,.0f}')

def main():
    tampilkan_audi()

    hasil = sorting_cheap_expensive()

    second_cheap_produk(hasil)

main()