import sqlite3

cnx = sqlite3.connect('19-Database/db.sqlite3') 

curseur = cnx.cursor()

sql = "select * from personne"
curseur.execute(sql)

personnes = curseur.fetchall()

print(personnes) # il s'agit d'une liste de tuples

# Unpacking: déballer un tuple

for p in personnes:
    print(p) # p est un tuple

for id,nom,prenom,age in personnes:
    print(f"id: {id} - Nom: {nom} - Prénom: {prenom} - age: {age}")

print(curseur.fetchall()) 
# liste vide: une fois le contenu du curseur consommé (ligne 10), ce dernier est vidé en mémoire
# prévoir des variables pour conserver le contenu du curseur

sql = "select * from personne where id=?"
param = (1,)

curseur.execute(sql,param)

p = curseur.fetchone()

print(p)

print(curseur.fetchone()) # None car contenu consommé à la ligne 31
