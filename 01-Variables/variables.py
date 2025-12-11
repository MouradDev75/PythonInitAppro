# Variable: est une zone mémoire contenant une valeur typée
# Il à plusieurs types de données en Python:
# types numériques: int, float, complex
# type textuel: str
# type boolean: bool
# types collections: range, list, tuple, set, dict

# Python utilise le typage dynamique. nom_variable = valeur. L'interpréteur détermine le type de la variable
# selon la valeur qu'on lui a affecté.
# Java utilise le typage statique: int x = 10

my_int = 10
my_texte = "texte"
autre_texte = 'texte'

# 2 syntaxes pour le type texte en Python: " " ou ' '

my_reel = 10.55
my_bool = True
my_complex = 5 + 4j # j est le nombre imaginaire

print(my_int)
print(my_complex.real)
print(my_complex.imag)

# Conventions de nommage des variables:
# PascalCase: MyInt
# camelCase: myInt
# snake_case: my_int (convention utilisée par Python)

# Contante: est une variable dont le contenu n'est pas modifiable
# Convention: le nom d'une constante doit être en majuscule

MA_CONSTANTE = 15
MA_CONSTANTE = "texte"

# La notion de constante n'existe pas réellement en python, c'est plus une convention

# Variable nulle: None = null

x = None

print(x)

# Il est possible de rajouter le _ pour les entiers pour les rendre plus lisibles

i = 123_456_789
print(i)

# Pour les nombres réels, on peut faire:
a = 0.99
b = 00.99
c = .99

print(">>>>>>>>>>>>>>>>> type des variables:")

print(type(my_int))
print(type(my_reel))
print(type(my_texte))
print(type(my_bool))

print(">>>>>>>> Conversion de types:")

s = "10.5"
f = float(s)

print(f)

i = int(f)
print(i)

# int() - bool() - str()

nb1 = float(input('premier nombre: '))
nb2 = float(input('second nombre: '))

somme = nb1 + nb2

print(somme)

print(">>>>>>>>>> Nombres aléatoire:")

import random

e = random.randint(1,10)
print(e)



