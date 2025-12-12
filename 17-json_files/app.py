import os, json

# contrairement à un fichier texte, un fichier json contient des données: texte, valeurs numériques......

# Etape1: construction du chemin du fichier

chemin_dossier = os.path.dirname(__file__) # dirname: directory name

chemin_json = os.path.join(chemin_dossier, 'users.json')

# Etape2: appelle de la fonction open

with open(chemin_json, 'r', encoding='utf-8') as flux:
    data = json.load(flux)

# print(data): il s'agit d'une liste de dict

for user in data:
    print(f"Name: {user.get('name')} - Latitude: {user.get('address').get('geo').get('lat')}")
    #print(user)

# Ecriture json:
chemin_sortie = os.path.join(chemin_dossier, 'sortie.json')

with open(chemin_sortie, 'w', encoding='utf-8') as stream:
    # les data à insérer sont: soit un dict - soit une liste de dict
    d = {
        'python': 'Langage de programmation',
        'version': 3.14
    }
    json.dump(d, stream, indent=4, ensure_ascii=False) 
    # ensure_ascii=True: tous les char non ASCII seront ignorés

# Exo: en utilisant le fichier users.json, construire un nouveau fichier json ne contenant que les clés:
# name, email et city

# 1- Constuire le contenu à insérer: une liste de dict

lst_dict = []

for u in data:
    d = {
        'nom': u.get('name'),
        'email': u.get('email'),
        'ville': u.get('address').get('city')
    }

    lst_dict.append(d)

# 2- Insérer la liste de dict dans un fichier json
chemin_resultat = os.path.join(chemin_dossier, 'resultat.json')

with open(chemin_resultat, 'w', encoding='utf-8') as flux:
    json.dump(lst_dict, flux, indent=4, ensure_ascii=False)


print(">>>>>>>>>>>>>>> Fonctions: loads() et dumps():")

# loads(): fonction de conversion d'une chaine json en objet (dict) - désérialiser - parser

chaine_json = '{"Nom": "FEDERER", "Prenom": "Roger", "Sport": "Football"}'

obj = json.loads(chaine_json)
print(type(obj))

# possibilité d'etraire des infos:
print(obj.get('Nom'))
print(obj.get('Prenom'))
print(obj.get('Sport'))

# possibilité d'ajouter des clés
obj['Age'] = 39

# possibilité de modifier des clés
obj['Sport'] = 'Tennis'

# possibilité de supprimer des clés:

obj.pop('Prenom')

print(obj)

# dumps(): conversion d'un dict en json str: sérialiser un objet

result = json.dumps(obj, indent=2)

print(result)