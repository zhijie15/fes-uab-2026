preu = input("Introdueix el preu del producte: ")
print(f"Tipus inicial: {type(preu)}")
preu = float(preu)
print(f"Preu convertit:{type(preu)}")
unitat = int(input("Introdueix les unitats: "))
print(f"Tipus de les unitats:  {type(unitat)}")
total = preu * unitat
print(f"Preu total: {total}")
puc_comprar = 20 // preu
print(f"Unitats que puc comprar amb 20 euros: {puc_comprar}")
print(f"Preu arrodonit:{round(preu,1)}")
print(f"Preu final: {total:.2f} €")