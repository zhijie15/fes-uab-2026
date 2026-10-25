contrasenya = "python123"
password = input("Introduir contrasenya: ")
while not (contrasenya == password):
    print("Contrasenya incorrecta")
    password = input("Introduir contrasenya: ")
print("Accés permès")