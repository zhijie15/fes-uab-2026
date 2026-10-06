###
# exercicis-basics.py
# Exercicis per practicar els conceptes apresos a les lliçons.
###
import math

print("\nExercici 1: Imprimir missatges")
print("Escriu un programa que imprimeixi el teu nom i la teva ciutat en línies separades.")

### Completa aquí

print("Zhijie", "Barcelona", sep="\t")

print("--------------")

print("\nExercici 2: Mostra els tipus de dades de les variables següents:")
print("Utilitza la comanda 'type()' per determinar el tipus de dades de cada variable.")
a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None

### Completa aquí
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

print("--------------")

print("\nExercici 3: Conversió de tipus")
print("Converteix la cadena \"12345\" a un enter i després a un float.")
print("Converteix el float 3.99 a un enter. Què passa?")

### Completa aquí
cadena = "12345"
enter = int(cadena)
float_cadena = float(cadena)
print(enter)
print(float_cadena)
float_num = 3.99
enter_num = int(float_num)
print(enter_num)

print("--------------")

print("\nExercici 4: Variables")
print("Crea variables per al teu nom, edat i alçada.")
print("Utilitza f-strings per imprimir una presentació.")

# "Hola! Em dic Marc, tinc 38 anys i faig 1.75 metres"
#name = "Marc"
#age = 38

### Completa aquí
name = "Zhijie"
age = 23
alcada = 1.75
print(f"Hola! Em dic {name}, tinc {age} anys i faig {alcada} metres")

print("--------------")

print("\nExercici 5: Nombres")
print("1. Crea una variable amb el nombre PI (sense assignar una variable)")
print("2. Arrodoneix el nombre amb round()")
print("3. Fes la divisió entera entre el nombre resultant i el nombre 2")
print("4. El resultat hauria de ser 1")

### Completa aquí
nombre = round(math.pi)
resultat = nombre // 2
print(resultat)

print("--------------")

print("\nExercici 6: Conversor de temperatura")
print("Demana a l'usuari una temperatura en graus Celsius.")
print("Converteix aquest valor a Fahrenheit amb la fórmula: F = (C * 9/5) + 32")
print("Mostra els dos valors amb un missatge clar.")

### Completa aquí
Celsius = float(input("Introdueix temperatura(Celsius): "))
Fahrenheit = (Celsius *9/5) + 32
print(f"{Celsius} celsius = {Fahrenheit} Fahrenheit")

print("--------------")

print("\nExercici 7: Calculadora de propina")
print("Demana el total d'un compte i el percentatge de propina.")
print("Calcula quant és la propina i el total final que s'ha de pagar.")
print("Mostra els resultats amb 2 decimals.")
total_compte = float(input("Introdueix el total del compte: "))
percentatge_propina = float(input("Introdueix el percentatge de propina: "))
propina = total_compte * (percentatge_propina / 100)
print("Propina: %.2f " %propina)
### Completa aquí

print("--------------")

print("\nExercici 8: Validador de contrasenya simple")
print("Demana una contrasenya a l'usuari.")
print("Comprova si té almenys 8 caràcters.")
print("Mostra 'Contrasenya vàlida' o 'Contrasenya no vàlida'.")
contrasenya = input("Introdueix una contrasenya: ")
if len(contrasenya) >= 8:
    print("Contrasenya vàlida")
else:
    print("Contrasenya no vàlida")
### Completa aquí