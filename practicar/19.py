matriu = [
    [4, 7, 2],
    [9, 3, 6],
    [5, 8, 1]
]
i = 0
num = 0
while i < len(matriu):
    if matriu[1][i] > num:
        num = matriu[1][i]
    i += 1
print(num)