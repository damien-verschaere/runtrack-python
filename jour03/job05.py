import re
import matplotlib.pyplot as plt

filename = "data.txt"


with open(filename, 'r') as file:
    content = file.read()

content=content.lower()
lettres = re.findall(r'[a-zA-Z]', content)
comptageLettre = {}

for lettre in lettres:
    if lettre not in comptageLettre:
        comptageLettre[lettre] = 0
    comptageLettre[lettre] += 1


NbrTotal = len(lettres)
Pourcentages = {letter: count / NbrTotal * 100 for letter, count in comptageLettre.items()}


letters, percentages = zip(*Pourcentages.items())

fig, ax = plt.subplots()
ax.bar(letters, percentages)
ax.set_xlabel('Lettres')
ax.set_ylabel('Pourcentage d\'apparition (%)')
ax.set_title('Pourcentage d\'apparition de chaque lettre dans data.txt')

plt.show()
