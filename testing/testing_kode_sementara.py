from colorama import Fore, Back, Style
import colorama

# Mengubah warna teks menjadi merah
print(Fore.RED + "Ini teks berwarna merah")

# Mengubah warna teks menjadi hijau dengan latar kuning
print(Fore.GREEN + Back.YELLOW + "Teks hijau, latar kuning")

# Mereset semua pengaturan warna ke default
print(Style.RESET_ALL)

# Contoh penggunaan dalam validasi input
print(Fore.RED + "Error: Input tidak valid.", Style.RESET_ALL)