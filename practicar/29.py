num = int(input("Introuir un numero enter:"))
digit = 0
parell = 0
temp = 0
while num != 0:
    temp = num % 10
    num = num // 10
    digit += 1
    if temp % 2 == 0:
        parell += 1
print(f"Hi ha {digit} numero digit")
print(f"Hi ha {parell} numero parells")