# dict: est une collection non ordonnée qui fonctionne par association clé:valeur.
# Dans un dictionnaire physique, le mot est la clé, la valeur est sa définition
# Dans un dict, les clés sont uniques

# dict vide:

d1 = {}
d2 = dict()

# Le type dict sert généralement à regrouper les caractéristiques d'un objet

user = {
    'nom' : 'DUPONT',
    'prenom' : 'Jean',
    'age': 60
}

#Afficher le nom:

print(user['nom'])
#print(user['Nom']) -> si clé introuvable -> Exception

print(user.get('nom'))
print(user.get('Nom')) # si clé inexistante -> renvoie None

# Ajouter de nouvelles clés:
user['contrat'] = 'CDD'
print(user)

user['contrat'] = 'CDI'
print(user)

# On peut avoir aussi des dicts complèxes:

utilisateur = {
    'nom' : 'DUPONT',
    'prenom' : 'Jean',
    'age': 60,
    'telephones': ['060606060', '070707070'],
    'adresse': {
        'rue': '10 rue Machin',
        'code_postal': 75015
    }
}

# affichez chaque num. de tél.:
for t in utilisateur.get('telephones'):
    print(t)

# affichez le nom de la rue:
print(utilisateur.get('adresse').get('rue'))

print('>>>>>> parcourir un dictionnaire:')

d = {
    'a': 1,
    'b': 2
}

print('>>> for:') # renvoie dyniquement les clés

for e in d:
    print(e)

print(">>>> for sur les clés:")

for k in d.keys():
    print(f"Clé: {k} - valeur: {d.get(k)}")

print(">>>> for sur les valeurs:")

for v in d.values():
    print(v)

print(">>>> for sur les items:")

for i in d.items():
    print(i) # i est tuple (clé, valeur)


# Unpacking d'un tuple:

for k,v in d.items():
    print(k,v)

print(">>>>>>>>>>>>>>>>>> API rest")

# web Service REST ou API Rest: est une application web qui renvoie du contenu JSON.
# il s'agit d'un ensemble de ressources (images, article d'un journal....) o* chaque ressource un ID
# (URI: Uniform Resource Identifier - end point), une méthode d'accès (GET-POST-PUT-DELETE) et elle 
# publique ou privée.

# Une API Rest n'est pas lmitée au format JSON: elle peut renvoyée du texte, du XmL, du binaire

# Toutes ces infos sont fournies dans la doc de l'api

# Pour consommer une API Rest à partir d'un script python, il faut utiliser le module requests
# pip install requests

import requests

URI = 'https://api.restful-api.dev/objects'

reponse = requests.get(URI).json()
#print(reponse) # liste de dict

for o in reponse:
    print(f"ID: {o.get('id')} - Name: {o.get('name')}")

# Analyse de données:

# Jupyter Notebook: IDE utilisé dans l'analyse de données (installer anaconda pour l'avoir)
# Dans Vs code: installez l'extension Jupyter
# ctr + shift + p: tapez jupyter -> choisir create Jupyter notebook
# jupyter notebook utilise des cellules et dans une cellule on peut soit insérer du code Python ou
# du markdown (langage de formattage de texte)