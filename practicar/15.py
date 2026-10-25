nombres = [4, 9, 2, 7, 6, 3]
i = 0
suma = 0
while i < len(nombres):
    if nombres[i] % 2 == 0:
        suma += nombres[i]
    i += 1
print(f"La suma dels nombres parells és {suma}")