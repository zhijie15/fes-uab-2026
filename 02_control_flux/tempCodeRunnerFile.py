compte_actiu = True
contrasenya_correcta = True
codi_correcte = False
dispositiu_de_confiança = True
compte_bloquejat = False
accés_permes = compte_actiu and contrasenya_correcta and not compte_bloquejat and (codi_correcte or dispositiu_de_confiança)
print(accés_permes)