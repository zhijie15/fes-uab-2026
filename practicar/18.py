matriu = [
    [3, 8, 2],
    [10, 4, 7],
    [6, 1, 9]
]
i = 0
compt = 0
while i < len(matriu):
    j = 0
    while j < len(matriu):
        if matriu[i][j] > 5:
            compt += 1
        if i == 1:
            if matriu[i][j] < 5:
                matriu[i][j] = 0
        j += 1
    i += 1
print(compt)
print(matriu[1])