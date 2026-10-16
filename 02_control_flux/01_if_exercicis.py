###
# EXERCICIS
###

# Exercici 1: Determinar el més gran de dos nombres
# Demana a l'usuari que introdueixi dos nombres i mostra un missatge
# que indiqui quin és més gran o si són iguals.

print("Introduir 2 numeros")
num1 = float(input("Numero 1: "))
num2 = float(input("Numero 2: "))
if num1 > num2:
    print(f"{num1} es mes gran")
elif num2 > num1:
    print(f"{num2} es mes gran")
else:
    print("Són iguals")
# Exercici 2: Calculadora senzilla
# Demana a l'usuari dos nombres i una operació (+, -, *, /).
# Fes l'operació i mostra'n el resultat (gestiona la divisió per zero).

operacio = input("Introdueix una operació (+, -, *, /): ")
if operacio in ['+', '-', '*', '/']:
    num1 = float(input("Numero 1: "))
    num2 = float(input("Numero 2: "))
    if operacio == '+':
        resultat = num1 + num2
    elif operacio == '-':
        resultat = num1 - num2
    elif operacio == '*':
        resultat = num1 * num2
    elif operacio == '/':
        if num2 != 0:
            resultat = num1 / num2
        else:
            print("Error: Divisió per zero")
            resultat = None
    if resultat is not None:
        print(f"Resultat: {resultat}")
else:
    print("Operació no vàlida")
# Exercici 3: Any de traspàs
# Demana a l'usuari que introdueixi un any i determina si és de traspàs.
# Un any és de traspàs si és divisible per 4, excepte si és divisible per 100
# però no per 400.

any = int(input("Introduir un any: "))
if (any % 4 == 0 and (any % 100 != 0 or any % 400 == 0)):
    print(f"{any} es un any de trspas")
else:
    print(f"{any} no es un any de trspas")
# Exercici 4: Classificar edats
# Demana a l'usuari que introdueixi una edat i classifica-la en:
# - Nadó (0-2 anys)
# - Infant (3-12 anys)
# - Adolescent (13-17 anys)
# - Adult (18-64 anys)
# - Persona gran (65 anys o més)

edat = int(input("Introduir edat: "))
if edat < 0:
    print("Edat no vàlida")
elif edat <= 2:
    print("Nadó")
elif edat <= 12:
    print("Infant")
elif edat <= 17:
    print("Adolescent")
elif edat <= 64:
    print("Adult")
else:
    print("Persona gran")
# Exercici 5: Qualitat del senyal Wi-Fi
# Demana el nivell de senyal rebut (RSSI) en dBm i classifica la cobertura:
# - -50 dBm o superior: excel·lent
# - Entre -67 dBm i menys de -50 dBm: bona
# - Entre -75 dBm i menys de -67 dBm: feble
# - Inferior a -75 dBm: molt feble

senyal = float(input("Introduir nuvell de senyal(dBm): "))
if senyal >= -50:
    print("Excel·lent")
elif senyal >= -67:
    print("Bona")
elif senyal >= -75:
    print("Feble")
else:
    print("Molt feble")
# Exercici 6: Nivell de recepció d'una connexió de fibra òptica
# Demana la potència òptica rebuda en dBm. Per a aquest exercici, considera
# acceptable un nivell entre -27 dBm i -8 dBm, ambdós inclosos.
# Indica si el nivell és massa baix, acceptable o massa alt.

potencia = float(input("Introduir potencia optica(dBm): "))
if potencia < -27:
    print("Massa baix")
elif potencia <= -8:
    print("Acceptable")
else:
    print("Massa alt")
# Exercici 7: Consum mensual de dades mòbils
# Demana el consum de dades en GB d'una línia mòbil. El pla inclou 20 GB.
# Indica si el consum és dins del límit o si l'ha superat; en aquest últim cas,
# calcula quants GB addicionals s'han consumit.

consum = float(input("Introduir consum de dades(GB): "))
if consum <= 20:
    print("Consum dins del límit")
else:
    addicional = consum - 20
    print(f"Consum superat en {addicional} GB")
# Exercici 8: Diagnòstic d'una connexió de fibra
# Demana si l'indicador LOS del terminal òptic està encès i si l'indicador
# d'Internet del router està encès. Segons aquestes dues dades, indica si cal
# revisar el cable de fibra, comprovar el servei del proveïdor o si la connexió
# sembla funcionar correctament.

los = input("Indicador LOS encès? (sí/no): ")
internet = input("Indicador Internet encès? (sí/no): ")
if los not in ["sí", "no"] or internet not in ["sí", "no"]:
    print("Entrada no vàlida. Si us plau, respon amb 'sí' o 'no'.")
else:
    if los == "sí" and internet == "sí":
        print("Connexió sembla funcionar correctament")
    elif los == "sí" and internet == "no":
        print("Cal comprovar el servei del proveïdor")
    elif los == "no" and internet == "sí":
        print("Cal revisar el cable de fibra")
    else:
        print("Cal revisar el cable de fibra i comprovar el servei del proveïdor")
# Exercici 9: Bateria d'un sistema d'alimentació ininterrompuda (SAI)
# Demana el percentatge de bateria disponible al SAI que alimenta un armari
# de comunicacions. Indica si el nivell és crític (menys del 20 %), baix
# (del 20 % al 49 %) o suficient (50 % o més). Rebutja valors fora del rang
# del 0 % al 100 %.

bateria = int(input("Introduir percentatge de bateria (%): "))
if bateria < 0 or bateria > 100:
    print("Fora del rang")
elif bateria < 20:
    print("Nivell crític")
elif bateria < 50:
    print("Nivell baix")
else:
    print("Nivell suficient")
# Exercici 10: Qualitat d'una connexió de xarxa
# Demana la latència en mil·lisegons i el percentatge de paquets perduts.
# Rebutja una latència negativa o una pèrdua fora del rang del 0 % al 100 %.
# Classifica la connexió com a excel·lent si la latència és de 30 ms o menys
# i la pèrdua és de l'1 % o menys; bona si és de 80 ms o menys i la pèrdua és
# del 3 % o menys; acceptable si és de 150 ms o menys i la pèrdua és del 5 %
# o menys; en qualsevol altre cas, deficient.

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
# Exercici 11: Cost mensual d'un pla de dades
# Demana el tipus de pla (bàsic o plus) i el consum mensual en GB.
# El pla bàsic costa 10 € i inclou 10 GB; cada GB addicional costa 1,50 €.
# El pla plus costa 20 € i inclou 30 GB; cada GB addicional costa 0,75 €.
# Rebutja un consum negatiu o un tipus de pla desconegut. Calcula i mostra el
# cost total, tenint en compte que no es cobra l'excés si no se supera el límit.

tipus_pla = input("Introdueix tipus de pla (bàsic/plus): ")
consum = float(input("Introdueix consum mensual (GB): "))
if consum < 0:
    print("Consum negatiu no vàlid")
elif tipus_pla == "bàsic":
    cost_base = 10
    limit = 10
    cost_exces = 1.50
elif tipus_pla == "plus":
    cost_base = 20
    limit = 30
    cost_exces = 0.75
else:
    print("Tipus de pla desconegut")
    cost_base = 0
    limit = 0
    cost_exces = 0
if cost_base > 0:
    if consum > limit:
        cost_total = cost_base + (consum - limit) * cost_exces
    else:
        cost_total = cost_base
    print(f"Cost total: {cost_total:.2f} €")
# Exercici 12: Accés a un compte de client
# Demana si el compte està actiu, si la contrasenya és correcta i si el codi
# de doble verificació és correcte. Demana el codi només si el compte és actiu
# i la contrasenya és correcta. Indica si l'accés es denega perquè el compte
# està desactivat, perquè la contrasenya és incorrecta o perquè falla el codi;
# si totes les comprovacions necessàries són correctes, permet l'accés.

actiu = input("Compte actiu? (sí/no): ")
if actiu == "sí":
    contrasenya = input("Contrasenya correcta? (sí/no): ")
    if contrasenya == "sí":
        codi = input("Codi de doble verificació correcte? (sí/no): ")
        if codi == "sí":
            print("Accés permès")
        else:
            print("Accés denegat: Codi incorrecte")
    else:
        print("Accés denegat: Contrasenya incorrecta")
else:
    print("Accés denegat: Compte desactivat")
# Exercici 13: Diagnòstic d'un router
# Demana si el router està encès, si l'indicador LOS del terminal òptic està
# encès i si l'indicador d'Internet del router està encès. Indica primer si
# cal encendre el router; si ja està encès, comprova si cal revisar el cable
# de fibra (LOS encès), si cal contactar amb el proveïdor (Internet apagat) o
# si la connexió funciona correctament. Considera els casos en aquest ordre.

router_encès = input("Router encès? (sí/no): ")
if router_encès == "no":
    print("Cal encendre el router")
else:
    los = input("Indicador LOS encès? (sí/no): ")
    internet = input("Indicador Internet encès? (sí/no): ")
    if los == "sí":
        print("Cal revisar el cable de fibra")
    elif internet == "no":
        print("Cal contactar amb el proveïdor")
    else:
        print("Connexió funciona correctament")
# Exercici 14: Prioritat d'una incidència de xarxa
# Demana si la incidència afecta un servei crític, el nombre d'usuaris afectats
# i si hi ha una alternativa de connexió disponible. Rebutja un nombre negatiu
# d'usuaris. Assigna prioritat crítica si afecta un servei crític i no hi ha
# alternativa, o si afecta almenys 50 usuaris i no hi ha alternativa; alta si
# afecta almenys 10 usuaris o un servei crític; en qualsevol altre cas, baixa.

incidencia_critica = input("Incidència afecta servei crític? (sí/no): ")
num_usuaris = int(input("Nombre d'usuaris afectats: "))
if num_usuaris < 0:
    print("Nombre d'usuaris negatiu no vàlid")
else:
    alternativa = input("Hi ha alternativa de connexió? (sí/no): ")
    if (incidencia_critica == "sí" and alternativa == "no") or (num_usuaris >= 50 and alternativa == "no"):
        print("Prioritat crítica")
    elif num_usuaris >= 10 or incidencia_critica == "sí":
        print("Prioritat alta")
    else:
        print("Prioritat baixa")