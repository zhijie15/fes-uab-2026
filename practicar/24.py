nombres = [4, 7, 2, 9, 5, 8, 1]
print(nombres[1:5])
nombres[0] = 100
i = 0
while i < len(nombres):
    if nombres[i] > 7:
        print(nombres[i])
    i += 1
     