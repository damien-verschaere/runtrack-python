import re
import matplotlib.pyplot as plt

filename = "data.txt"

with open(filename,'r') as file:
    content = file.read()
    mots = re.findall(r'\b\w+\b', content)

LongueurMots = [len(mot) for mot in mots]
comptageLongueur = {}

for longueur in LongueurMots:
    if longueur not in comptageLongueur:
        comptageLongueur[longueur] = 0
    comptageLongueur[longueur] += 1

NbrTotal = len(mots)
Pourcentages = {longueur: (count / NbrTotal) * 100 for longueur, count in comptageLongueur.items()}

longueurs, pourcentages_valeurs = zip(*Pourcentages.items())

fig, ax = plt.subplots()
ax.bar(longueurs, pourcentages_valeurs)
ax.set_xlabel('Longueur des mots')
ax.set_ylabel('Pourcentage d\'apparition (%)')
ax.set_title('Pourcentage d\'apparition de chaque longueur de mot dans data.txt')

plt.show()
