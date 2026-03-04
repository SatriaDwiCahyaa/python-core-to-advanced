import os

# Membersihkan layar pada Windows
os.system("cls")

# Membersihkan layar pada Linux/Mac
os.system("clear")

# Pendekatan lintas platform
os.system("cls" if os.name == "nt" else "clear")