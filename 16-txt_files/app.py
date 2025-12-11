
# Pour ouvrir un fichier on appelle la fonction open
# cette fonction prends plusieurs params:
# - le chemin du fichier
# - le mode d'accès au fichier: r: read - w: write - a: append
# - encoding: utf-8

# En mode écriture (w ou a) si le fichier n'existe pas, la fct open le crée

# Etape1: construire le chemin du fichier à manipuler:

# chemin = r'c:\test...........\16-txt_files\demo.txt'

import os # os: module facilitant la gestion des paths

print(__file__) # c:\.........\16-txt_files\app.py

chemin_dossier = os.path.dirname(__file__) # c:\.........\16-txt_files

chemin_fichier = os.path.join(chemin_dossier,"demo.txt") # join: génère un chemin valide selon l'os utilisé

# Etape2: appelle de la fct open

# stream (flux - zone mémoire): est une sorte de canal intermédiaire entre une source et destination

flux = open(chemin_fichier, 'a', encoding='utf-8')
flux.write("\nceci est le contenu du fichier.....")
flux.close()

# lecture :

stream = open(chemin_fichier, 'r', encoding='utf-8')
contenu = stream.read()
stream.close()

print(contenu)

print(">>>>>>>>>>>>>>>>>>>>> Context Manager >>>>>>>>>>>>>>>>>>>")

# Context Manager (with resource):  s'occupe de libérer la ressource à la fin de son utilisation

with open(chemin_fichier, 'r', encoding='utf-8') as flux:
    content = flux.read() # vous arrivez à la fin du fichier. La prochaine lecture, n'aura aucun char à lire
    #flux.close() -> non nécessaire
    flux.seek(0) # remettre le curseur de lecture au début du fichier
    # flux.seek(5): renvoie le 6ème char -> index commence à 0
    # whence = 0: partir du début du fichier
    # whence = 1: partir de la position actuelle du curseur
    # whence = 2: partir de la du fichier
    print(flux.read())


print(">>>>>>>>>>>>>>>>>> module OS:")

# get working directory: dossier principal (du projet)
print(os.getcwd())

# créer des réps:

chemin_rep = os.path.join(chemin_dossier, "rep1")

if os.path.exists(chemin_rep):
    print('Dossier existant....')
else:
    os.mkdir(chemin_rep) # pour 1 seul rep
    print('Dossier crée.....')

# os.makedirs("rep1/rep2") # pour 1 rep + sous reps

# lister le contenu d'un rép:

for f in os.listdir(chemin_dossier):
    print(f)


