nombres = [3, 8, 2, 10, 5, 7, 4]
i = 0
while i <= len(nombres) - 1:
    if nombres[i] < 5:
        nombres.pop(i)
    else:
        i += 1
print(nombres)