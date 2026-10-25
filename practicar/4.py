num = int(input("Introdueix un nombre: "))
compt = 0
for i in range (1, num+1):
    if i % 2 == 0:
        compt += 1
print(f"Hi ha {compt} nombres parells")