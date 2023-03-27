nombres = []
for i in range(5):
    nombre = int(input("Entrez un nombre entier : "))
    nombres.append(nombre)

nombres.sort()
print("Voici les nombres triés par ordre croissant :")
for nombre in nombres:
    print(nombre)
