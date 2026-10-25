num = int(input("Introdueix un nombre: "))
total = 0
i = 1
while i <= num:
    if i % 2 == 1:
        total += i
    i += 1
print(f"La suma dels nombres senars és {total}")