import re

filename = "domains.xml"

# Lecture du fichier XML
with open(filename, 'r') as file:
    content = file.read()

# Recherche des noms de domaine
domain_names = re.findall(r'\b(\w+\.\w+)\b', content)

# Affichage des noms de domaine
print("Noms de domaine trouvés :")
for domain_name in domain_names:
    print(domain_name)

# Recherche des extensions de domaine
domain_extensions = re.findall(r'\.(\w+)', content)

# Comptage des extensions de domaine
domain_extensions_count = {}
for extension in domain_extensions:
    if extension in domain_extensions_count:
        domain_extensions_count[extension] += 1
    else:
        domain_extensions_count[extension] = 1

# Affichage du nombre d'extensions de domaine
print("\nNombre d'extensions de domaine :")
for extension, count in domain_extensions_count.items():
    print(f"{extension}: {count}")
