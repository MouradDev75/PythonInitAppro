# for:
# 1- permet de parcourir tous les éléments d'une collection: chaine, liste, dict......
# 2- pour un traitement répététif dont le nombre d'itérations est connu d'avance


# while: boucle conditionnelle
# permet de gérer les traitements répététifs dont le nombre d'itérations n'est pas connu d'avance
# mais qui dépendent d'une condition


print(">>>>>>>>>>>> For:")

my_liste = [10, "test", 10.4, True]

for element in my_liste :
    print(element)

prenom = "carine"

for lettre in prenom:
    # if lettre en cours dans le for égale i -> quitter la boucle
    if lettre == "i":
        break
    print(lettre)

# affichez hello 5 fois: print('hello')

for x in [1,1,1,1,1]:
    print('hello')

# Pour générer des collections en python, on peut utiliser la fonction range

nombres = range(10) # de 0 à  9 -> s'arrête à n-1

for n in nombres:
    
    print(n)

# affichez bonjour 8 fois
for i in range(8):
    print('bonjour')

print(">>>>>>>>>>>>> While:")

# demandez la saisie d'un nombre compris entre 1 et 10. Tant que le nombre saisi n'est pas valide
# redemandez la saisie d'un autre


print('<<<< boucle infinie:')
# boucle infinie: on doit gérer la sortie (break)
while True:
    nb = int(input('nombre entre 1 et 10: '))
    if nb >= 1 and nb <= 10:
        break


print('<<<< boucle finie:')
# boucle finie

n = 0
while not(n >= 1 and n <= 10):
    n = int(input('nombre entre 1 et 10: '))

print(">>>>>>>>>>>>> break et continue:")

prenom = "sylvain"

for lettre in prenom:

    if lettre == 'y':
        continue # force le passage à l'itération suivante - la suite de la boucle n'est pas exécutée

    if lettre == 'i':
        break

    print(lettre) #slva


prime = 150
absence = True # False

if absence:
    print('pas de prime')
else:
    print('Salaire', prime)

