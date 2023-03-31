# Ouvrir le fichier maze.mz
with open("maze.mz.txt", "r") as f:
    labyrinthe = [list(ligne.strip()) for ligne in f]

# Trouver la position de l'entrée et de la sortie
position_entree = (0, 0)
position_sortie = (len(labyrinthe)-1, len(labyrinthe[0])-1)

# Trouver le chemin de l'entrée à la sortie
def trouver_chemin(labyrinthe, pos_actuelle, pos_finale, visites, chemin_actuel):
    if pos_actuelle == pos_finale:
        return chemin_actuel

    visites.add(pos_actuelle)

    voisins = trouver_voisins(labyrinthe, pos_actuelle) - visites

    if not voisins:
        return None

    meilleur_chemin = None
    for voisin in voisins:
        chemin_voisin = trouver_chemin(labyrinthe, voisin, pos_finale, visites, chemin_actuel + [voisin])
        if chemin_voisin is not None:
            if meilleur_chemin is None or len(chemin_voisin) < len(meilleur_chemin):
                meilleur_chemin = chemin_voisin

    return meilleur_chemin

def trouver_voisins(labyrinthe, pos):
    row, col = pos

    voisins = set()

    if row > 0 and labyrinthe[row-1][col] != "#":
        voisins.add((row-1, col))
    if row < len(labyrinthe)-1 and labyrinthe[row+1][col] != "#":
        voisins.add((row+1, col))
    if col > 0 and labyrinthe[row][col-1] != "#":
        voisins.add((row, col-1))
    if col < len(labyrinthe[0])-1 and labyrinthe[row][col+1] != "#":
        voisins.add((row, col+1))

    return voisins

# Trouver le chemin de l'entrée à la sortie
visites = set()
chemin = trouver_chemin(labyrinthe, position_entree, position_sortie, visites, [position_entree])

# Marquer le chemin avec des 'X'
for pos in chemin:
    labyrinthe[pos[0]][pos[1]] = "X"

# Écrire le labyrinthe modifié dans un nouveau fichier 'maze-out.mz'
with open("maze-out.mz.txt", "w") as f:
    for ligne in labyrinthe:
        f.write("".join(ligne) + "\n")
