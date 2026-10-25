nombres = [3, 8, -2, 6, 0, 10, 4]
i = 0
compt = 0
while i < len(nombres):
    if nombres[i] < 0:
        i += 1
        continue
    elif nombres[i] == 0:
        break
    elif nombres[i] % 2 == 0:
        print(nombres[i])
        compt += 1
    i += 1
print(compt)