nombres = [3, 8, 2, 10, 5, 7]
i = 0
trobat = False
while i < len(nombres):
    if nombres[i] > 5 and  nombres[i] % 2 == 0:
        print(nombres[i])
        trobat = True
    i += 1
if trobat:
    print("Trobat")
else:
    print("No trobat")