import os,csv

# Etape1: construction du chemin

chemin_dossier = os.path.dirname(__file__)
chemin_csv = os.path.join(chemin_dossier, 'demo_file.csv')

# Etape2: appelle de la fonction open

contenu = []

with open(chemin_csv, 'r', encoding='utf-8') as flux:
    curseur = csv.reader(flux, delimiter=',')
    for ligne in curseur:
        contenu.append(ligne)

#print(contenu): il s'agit d'une liste de listes, où chaque liste contient les détails de chaque ligne
# du fichier csv

# Ecriture dans un csv:

chemin_sortie = os.path.join(chemin_dossier, 'copie.csv')

with open(chemin_sortie, 'w', encoding='utf-8') as stream:
    # le contenu est soit une liste (1 seule ligne) soit une liste de listes
    curseur = csv.writer(stream, delimiter=';', lineterminator='\n')

    for ligne in contenu:
        curseur.writerow(ligne)

    # ou bien insérer toutes les lignes en une seule opération:
    # curseur.writerows(contenu)