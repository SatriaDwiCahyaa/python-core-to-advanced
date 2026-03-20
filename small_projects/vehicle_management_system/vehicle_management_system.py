class Kendaraan:
    def __init__(self, nama, kecepatan, **kwargs):
        self.nama = nama
        self.__kecepatan = kecepatan
        self.properti = kwargs

    def get_kecepatan(self):
        return self.__kecepatan
    

    def info(self):
        print(f'Kendaraan: {self.nama}')


    def set_kecepatan(self, kecepatan_baru):
        if kecepatan_baru < 0:
            print('Kecepatan tidak boleh negatif')
        else:
            self.__kecepatan = kecepatan_baru

class Mobil(Kendaraan):
    def info(self):
        return f'Mobil: {self.nama}, Kecepatan: {self.get_kecepatan()} km/jam, Warna: {self.properti.get('warna', '-')} '

class Motor(Kendaraan):
    def info(self):
        return f'Motor: {self.nama}, kecepatan: {self.get_kecepatan()} km/jam, Warna: {self.properti.get('warna', '-')} '

class Truk(Kendaraan):
    def info(self):
        return f'Truk: {self.nama}, kecepatan: {self.get_kecepatan()} km/jam, Warna: {self.properti.get('warna', '-')} '


def tambah_kendaraan(*args):
    return [kendaraan for kendaraan in args]


def cetak_objek(nama_variabel):
    for item in nama_variabel:
        print(item.info())

k1 = Mobil('Avanza', 120, warna='Merah')
k2 = Motor('Suzuki', 100, warna='Dark Blue')
k3 = Mobil('Alphard', 160, warna='White')
k4 = Truk('Volvo', 276, warna='Black')

daftar_kendaraan = tambah_kendaraan(k1,k2, k3, k4)

print('=== DAFTAR KENDARAAN ===')
cetak_objek(daftar_kendaraan)
Kendaraan_cepat = [k for k in daftar_kendaraan if k.get_kecepatan() > 110]

print('\n=== KECEPATAN KENDARAAN URUT ASCENDING ===')
kendaraan_sorted = sorted(daftar_kendaraan,key=lambda k: k.get_kecepatan())
cetak_objek(kendaraan_sorted)