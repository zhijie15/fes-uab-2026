nombres = [8, 3, 12, 5, 2, 10, 7]
i = 0
compt = 0
while i < len(nombres):
    if nombres[i] < 5:
        nombres.pop(i)
    else:
        if nombres[i] % 2 == 0 and nombres[i] > 5:
            compt += 1
        i += 1
nombres.sort()
print(nombres)
print(compt)