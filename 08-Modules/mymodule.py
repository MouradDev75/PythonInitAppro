# Syntaxes pour importer un module

import random

random.randint(1,10)

# On peut aussi modifier le nom du module importé on définissant un alias

import random as rd

rd.randint(1,10)

# On peut aussi importer des éléments spécifiques à partir d'un module

from math import sqrt
from statistics import mean,median

sqrt(25)

# On peut aussi modifiant le nom des éléments importés

from math import sqrt as racine_carree

racine_carree(25)

# On peut aussi importer tous les éléments d'un module: syntaxe non recommandée

from math import *


import math

math.sqrt(25)

# Un module Python est un fichier (.py) contenant généralement des fonctions, des classes et des constantes

# Un package Python est dossier contenant des modules

# Contrainte: le nom d'un module et d'un package doit être en miniscules, sans espaces ni underscore

# Pour convertir un répertoire en package Python, ce dernier doit contenir le fichier __init__.py
# qu'on peut laisser vide

# Pour Python < 3.3: __init__.py est obligatoire
# pour Python >= 3.3: __init__.py n'est plus obligatoire pour convertir un dossier en package, mais il
# est recommandée de le générer comme pour des questions de compatibilité

# Appeler la fonction fct1 définie dans le module mesfonctions.py

#import mypackage.mesfonctions # 1- importer tout le module

from mypackage.mesfonctions import fct1

# Un module importé est toujours exécuté
# Comment empêcher l'exécution d'un module importé?



# __name__ == '__main__' pour un module exécuté
# __name__ == 'nom du module' pour un module importé

# Lors d'un import, le __init__.py est exécuté en premier

# test du __all_ définit dans __init__.py
from mypackage import *
module1.init_database()
fct3()

# réferentiel des packages python: pypi
# pip: gestionnaire de modules externes

# commandes a exécuter dans le terminal

# pip install nom_module
# pip uninstall nom_module
# pip list

# Dans VS Code: si power shell empêche l'exécution de script externe :
# 1- Démarrez Powershell en tant qu'Admin
# 2- Exécutez la commande suivante:
# Set-ExecutionPolicy RemoteSigned -> répondre par o (pour oui)
