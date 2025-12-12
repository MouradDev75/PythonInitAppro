# Pour se connecter à une base de données:
# 1- Installer le driver (connecter): module externe via le pip et l'importer
# 2- Se connecter à la bd en appelant la fct connect(params de connexion)
# 3- Récupérer le stream en appelant la fct cursor()
# 4- Exécution des commandes sql: cursor.execute(commande sql)

# python propose un type de BD à utiliser: SQlite avec le driver sqlite3 à importer

# pas besoin de l'installer, fait partie des modules de bases de Python
import sqlite3

cnx = sqlite3.connect('19-Database/db.sqlite3') # si la base n'existe: la fct connect() la génère

curseur = cnx.cursor()

# 2 types de commandes SQL:
# Commandes LDD: Langage de définition de données (concerne la structure de la bd): create - drop - alter
# Commandes LMD: Langage de manipulation de données: insert - delete- update - select

curseur.execute("""
CREATE TABLE IF NOT EXISTS personne(
  id integer PRIMARY KEY AUTOINCREMENT NOT NULL,
  nom varchar(30) NOT NULL,
  prenom varchar(30) NOT NULL,
  age int unsigned NOT NULL,  
  constraint unique_names UNIQUE (nom,prenom)           
)
""")

# insertion de données de test:
# Les opérations d'écriture en BD s'exécutent en mode transactionnel: c'est le principe de tout ou rien

try:
    curseur.execute("insert into personne(nom,prenom,age) values ('DUPONT', 'Jean', 60) ")
    # fct qui prend en param une cmd sql: faille 
    # Syntaxe déconseillée en pratique: injections sql
    # utilisez des cmds sql paramétrèes: sont des cmds précompilées, chargées en mémoire en attente de params

    curseur.execute('insert into personne values (NULL,?,?,?)', ("FEDERER", "Roger", 40))
    curseur.execute('insert into personne values (NULL,?,?,?)', ("NADAL", "Rafael", 37))

    cnx.commit() # le commit valide toutes les cmds sql

except Exception as e:
    cnx.rollback() # le rollback annule toutes les cmds sql
    print(e)

finally:
    curseur.close()
    cnx.close()

    # pour consulter une bD Sqlite:
    # 1- installer un client externe db browser
    # 2- Dans Vs Code: installer l'extenson sqlite viewer