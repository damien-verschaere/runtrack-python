def CaluclFactoriel(x):
    return 1 if x == 0 else x * CaluclFactoriel(x-1)

nombre = int(input("Entrez un nombre entier : "))

print("La factorielle de", nombre, "est", CaluclFactoriel(nombre))