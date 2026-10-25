num = int(input("Introdueix un nombre: "))
i = 0
while num != 0:
    if num > 0:
        i += 1
    num = int(input("Introdueix un nombre: "))
print(f"Has introduït {i} nombres positius")