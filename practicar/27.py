nombres = [8, 3, 12, 5, 2, 10, 7]
copia = nombres[1:5]
i = 0
while i < len(copia):
    if copia[i] < 5:
        copia.pop(i)
    else:
        i += 1
copia.sort()
print(copia)
print(copia.count(10))