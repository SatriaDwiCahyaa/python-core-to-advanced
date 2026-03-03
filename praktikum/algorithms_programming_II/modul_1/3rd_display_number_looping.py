import os
os.system('cls')

# ─────────────────────────────────────────────
# TUGAS 3: Pengulangan Angka 1–15 & Total
# ─────────────────────────────────────────────


def welcome_sign():
    print("=" * 45)
    print("  TUGAS 3 - PENGULANGAN ANGKA 1 - 15")
    print("=" * 45)

# FOR LOOP 
def pengulangan_for():
    print("\nFOR loop:")
    
    total_for = 0
    for x in range(1, 16):
        print(f"  Angka ke-{x}: {x}")
        total_for += x
    print(f"  Total (for) = {total_for}")

# WHILE LOOP
def pengulangan_while():
    print("\nWHILE loop:")

    x = 1
    total_while = 0
    while x <= 15:
        print(f"  Angka ke-{x}: {x}")
        total_while += x
        x += 1
    print(f"  Total (while) = {total_while}")

# DO-WHILE (simulasi dengan while True + break) 
def pengulangan_do_while():
    print("\nDO-WHILE (while True + break):")
    
    x = 1
    total_dowhile = 0
    while True:
        print(f"  Angka ke-{x}: {x}")
        total_dowhile += x
        x += 1
        if x > 15:
            break
    print(f"  Total (do-while) = {total_dowhile}\n")


def main():
    welcome_sign()
    pengulangan_for()
    pengulangan_while()
    pengulangan_do_while()
    input()


if __name__ == "__main__":
    main()