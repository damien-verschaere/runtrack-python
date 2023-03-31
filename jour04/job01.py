def puissance(base, exposant):
    if exposant == 0:
        return 1
    elif exposant < 0:
        return 1 / puissance(base, -exposant)
    else:
        return base * puissance(base, exposant - 1)

nombre_base = int(input("Entrez un nombre entier pour la base: "))
nombre_exposant = int(input("Entrez un nombre entier pour l'exposant: "))

resultat = puissance(nombre_base, nombre_exposant)
print(f"{nombre_base}^{nombre_exposant} = {resultat}")
