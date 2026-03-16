PERTEMUAN_UTS = 8

def get_nilai():
    keseluruhan = []
    
    print('\n===== NILAI TBO (8X Pertemuan) ======')
    
    for i in range(1, PERTEMUAN_UTS + 1):
        nilai = float(input(f'Masukkan nilai pertemuan Ke-{i}: '))
        keseluruhan.append(nilai)

    return keseluruhan


def rata_rata(*nilai):

    total_data = 0

    for n in nilai:
        total_data += n

    nilai_rata_rata = total_data / PERTEMUAN_UTS

    return nilai_rata_rata


def tampilkan_data(**data):
    print('======= INFORMASI MAHASISWA ======')

    print(f' Nama    : {data['nama']}')
    print(f' NIM     : {data['nim']}')
    print(f' Jurusan : {data['jurusan']}')


def main():
    tampilkan_data(nama = 'Adam Smith', nim = '123456789', jurusan = 'Artifical Intelligence')

    nilai_mahasiswa = get_nilai()
    hasil_rata_rata = rata_rata(*nilai_mahasiswa)

    print(f'\n Nilai Rata-rata  : {hasil_rata_rata:.2f}')


if __name__ == "__main__":
    main()