num1 = int(input("Introdueix el primer nombre: "))
num2 = int(input("Introdueix el segon nombre: "))
if num1 > num2:
    print(f"El nombre més gran és {num1}")
elif num2 > num1:
    print(f"El nombre més gran és {num2}")
else:
    print("Els dos nombres són iguals")

