nota = float(input("Introdueix la nota:"))
if nota < 5:
    print("Suspès")
elif nota < 7:
    print("Aprovat")
elif nota < 9:
    print("Notable")
else:
    print("Excel·lent")