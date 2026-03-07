
meja = [["" for _ in range(3)] for _ in range(2)]

for bar in range(len(meja)):
    for kol in range(len(meja[bar])):
        meja [bar] [kol] = input(f"Yang akan duduk di meja ({bar}, {kol}): ")


print("----------")
for bar in meja:
    print(" | ".join(bar))
print("------------------------")