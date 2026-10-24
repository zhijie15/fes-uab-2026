secret = 7
numero = int(input("Introdueixi un número enter positiu: "))
while secret != numero:
    if numero > secret:
        print("Mes petit")
    else:
        print("Mes gran")
    numero = int(input("Introdueixi un número enter positiu: "))
print("Encertat")