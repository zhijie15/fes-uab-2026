nombres = [3, 8, 2, 10, 5, 7]
i = 0
compt = 0
while i <= len(nombres) - 1:
    if nombres[i] > 5:
        compt += 1
    i += 1
print(f"Hi ha {compt} nombres més grans que 5")