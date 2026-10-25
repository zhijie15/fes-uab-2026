nombres = [3, 8, 2, 10, 5, 7]
i = 0 
trobat = False
while i < len(nombres):
    if nombres[i] == 3 or nombres[i] == 10:
        print(nombres[i])
        trobat = True
    i += 1
if trobat:
    print("Trobat")
else:
    print("No trobat")