# bloc conditionnel: est une ensemble d'instructions qui ne s'exécute que si une condition
# est vérifiée

age = 26

if age < 18 :
    print("Majeur")
    print("Toujours majeur")

# les : représentent le début d'un bloc d'instructions. tant que les instructions sont indentées
# de la mm façon, on est dans le mm bloc

if age < 18 :
    print('Mineur')
elif age <= 25 :
    print('jeune adulte')
else :
    print('adulte')

# On peut aussi combiner des conditions, on utilisant les opérateurs logiques
# age compris entre 18 et 25
if age >= 18 and age <= 25:
    print('jeune adulte')

# Avoir 18 ans minimun, ou une dérogation
derogation = False

if age >= 18 or derogation == True:
    print('accès autorisé......')

# un bloc vide n'est pas valide syntaxiquement.
# pour pouvoir définir un bloc vide, on doit utiliser le mot clé pass 

if True:
    pass # à compléter

print('suite du script.....')

print(">>>>>>>>>>>>>>>>> match case:")

# Depuis python 3.10, ajout du match case: syntaxe simplifiée des elif qui s'imbriquent

note = 15

# if note == 1:
#     pass
# elif note == 2:
#     pass
# elif note == 3:
#     pass
# elif note == 4:
#     pass
# elif note == 5:
#     pass
# elif note == 6:
#     pass

# | pipe: équivalent de l'union

match note:

    case 0|1|2|3|4|5|6|7|8|9:
        print('en dessous de la moyenne......')
    case 10|11|12|13:
        print('Juste la moyenne....')

    # pour les autres case, 2 syntaxes:
    # case other: plus lisible
    # case _:

    # case other:
    #     print('Excellent.....')

    case _:
        print('Excellent.....')
