import os
os.system('cls')


# --- TUGAS 1 ---
PRODUK = ['Jaguar', 'Lamborghini', 'Honda', 'Audi', 'Suzuki', 
          'Mazda', 'Daihatsu', 'Ford', 'Hyundai','Mitsubishi' 
          ]

HARGA = [ 1_340_000_000, 34_500_000_000, 350_000_000, 2_000_000_000, 
         245_000_000, 500_000_000, 169_000_000, 789_000_000, 122_900_000, 278_100_000
         ]     


def display_audi():
    target = 'Audi'
    founded = False

    for indeks, product in enumerate(PRODUK):
        if product == target:
    
            print(f'Produk {target} ditemukan!')
            print(f'\nProduk {target} pada indeks ke-{indeks} atau urutan ke-{indeks + 1}')
            print(f'\nHarga produk Rp{HARGA[indeks]:,.0f}')
            founded = True

    if not founded:
        print(f'Produk {target} tidak ditemukan pada data.')


def pengurutan_ascending():
    pasangan = list(zip(HARGA, PRODUK))
    pasangan.sort(key=lambda x: x[0])

    print(f'Rank{'':<2} Produk {'':<10} Harga')
    print(f'{'-'*4} {'-'*14} {'-'*20}')
    
    for indeks, (h, p) in enumerate(pasangan, start=1):
        print(f'{indeks:<6} {p:<13} Rp {h:,.0f}')

    return pasangan

def request_display(pasangan_data):
    target = 2
    
    for indeks, (h, p) in enumerate(pasangan_data, start=1):
        if indeks == target:
            print('=' * 45)
            print(f'{'':<10} Harga Produk Termurah')
            print('=' * 45)
            print(f'{indeks:<3} {p:<13} Rp {h:,.0f}')

def main():
    hasil = pengurutan_ascending()
    request_display(hasil)
    input()

if __name__ == "__main__":
    main()