nombres = [2, 5, 8, 11, 14, 17]
i = 0 
trobat = False
while i < len(nombres):
    if nombres[i] < 5 or (nombres[i] > 10 and nombres[i] % 2 == 0):
        print(nombres[i])
        trobat = True
    i += 1
if trobat:
    print("Trobat")
else:
    print("No trobat")