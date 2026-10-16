latencia = int(input("Introduir latència (ms): "))
perdua = float(input("Introduir pèrdua de paquets (%): "))
if latencia < 0 or perdua < 0 or perdua > 100:
    print("Entrada no vàlida")
elif latencia <= 30 and perdua <= 1:
    print("Connexió excel·lent")
elif latencia <= 80 and perdua <= 3:
    print("Connexió bona")
elif latencia <= 150 and perdua <= 5:
    print("Connexió acceptable")
else:
    print("Connexió deficient")