import sqlite3

cnx = sqlite3.connect('19-Database/db.sqlite3') 

curseur = cnx.cursor()

sql = "delete from personne where id=?"
param = [1]

curseur.execute(sql, param)
cnx.commit()

# CRUD: Create Read Update Delete