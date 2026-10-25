matriu = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matriu[1][1])
print(matriu[2][2])
i = 0
sum = 0
while i < len(matriu):
    sum += matriu[1][i]
    i += 1
print(sum)