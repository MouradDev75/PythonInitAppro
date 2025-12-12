import sqlite3

cnx = sqlite3.connect('19-Database/db.sqlite3') 

curseur = cnx.cursor()

# cmd sql avec des params nommés
sql = "update personne set nom=:last_name,prenom=:first_name,age=:age where id=:id"

# tuple pour les params anonymes: ?
# dict pour les params nommés

params = {
    'last_name': 'NOVAK',
    'first_name': "Djokovic",
    'age': 35,
    'id': 1
}

curseur.execute(sql, params)
cnx.commit()