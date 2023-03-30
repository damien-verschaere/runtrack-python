import re 

filename = "data.txt"
with open(filename,'r') as file:
    content = file.read()

mots=re.findall(r'\b\w+\b',content)
comptemots=len(mots)

print("nombre de mots dans ce texte a rallonge est de",comptemots)