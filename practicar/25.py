notes = [4, 8, 3, 10, 6, 2, 9]
i = 0
compt = 0
while i < len(notes):
    if notes[i] < 5:
        notes[i] = 0
    else:
        compt += 1
    i += 1
copia = notes.copy()
print(notes)
print(copia)
print(compt)