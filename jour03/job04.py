import re 


chiffre=input("entrez un nombre:")
#print(chiffre)
try:
    chiffre=int(chiffre)
except ValueError:
    print("rentrez un nombre entier")
else:
    if chiffre < 0 :
        print("rentrez un nombre superieur a 0")
    else:
        filename = "data.txt"
        with open(filename,'r') as file:
            content = file.read()
        mots= re.findall(r'\b\w+\b', content)
        motsEgaux = [mot for mot in mots if len(mot) == chiffre]
        Comptage = len(motsEgaux)
        print("il y a",Comptage ,"mots qui ont",chiffre,"lettres")