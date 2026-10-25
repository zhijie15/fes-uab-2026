nombres = [2, 5, 8, 3, 10, 1]
i = 0
dobles = []
while i <= len(nombres) - 1:
    if nombres[i] % 2 == 0:
        dobles.append(nombres[i] * 2)
    i += 1
print(dobles)