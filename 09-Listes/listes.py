# list: est une collection ordonnée avec doublons autorisés

# liste vide:

l = []
l1 = list()

# Aucune restriction sur le type des éléments d'une liste
lst = [10, "test", True, 10.5, [12,14]]

# Dans la pratique, on a pour habite de manipuler des listes cohérentes d'objets: liste de produits,....

notes = [2,6,7,9]

# Ajouts:
notes.append(2)
print(notes)

notes.insert(0,10)
print(notes)

# Modifications:
notes[0] = 15
print(notes)

# Suppressions:
notes.remove(2)
print(notes)

notes.pop() # supprime le dernier élément par défaut
print(notes)

print(notes.index(7)) # l'index commence à 0
print(notes.count(7))
print("test".count('t'))

print(">>>>>>> Atteindre un élément dans une liste:")

notes = [2,6,7,9]

print(f"Première note: {notes[0]}") # index 0
taille = len(notes)
print(f"Dernière note: {notes[taille - 1]}")

# Python autorise les indexs négatifs:
print(f"Dernière note: {notes[-1]}")

print(">>>>>>>> parcourir une liste:")

print('__FOR:')

for n in notes:
    print(n)

print('__WHILE:')

taille = len(notes)
index = 0

while index < taille:
    print(notes[index])
    index = index + 1

print(">>>>>>>>>> Slicing:")
# silicing: mécanisme permettant de créer des sous listes à partir de listes existantes

prenoms = ['Carine', 'Yoann', 'Mourad', 'Dawan']

list1 = prenoms[0:3] # de index 0 à 2 (n-1)
print(list1)

list2 = prenoms[:3] # du début jusqu'à n-1 (2)
print(list2)

list3 = prenoms[:] # du début jusqu'à la fin (une copie)
print(list3)

list4 = prenoms[::2] # du début jusqu'à la fin avec un pas de 2
print(list4)

print('>> affichez les 3 premiers prénoms:')

print(prenoms[:3])

print('>> affichez les 2 derniers prénoms:')
print(prenoms[-2:])

my_list = prenoms[2:] # éliminer des éléments dans une liste

# 3 syntaxes pour créer des copies
l1 = prenoms
l2 = prenoms.copy()
l3 = prenoms[:]

print(">>>>>>>>>>> Comprehension List:")
# Comprehension List: mécanisme permettant de créer de nouvelles listes à partir de listes existantes
# en modifiant les éléments des listes existantes

nombres = range(10)


# créez une nouvelle liste en doublant tous les nombres

# syntaxe classique:
nombres_doubles = []

for n in nombres:
    nombres_doubles.append(n * 2)

print(nombres_doubles)

# comprehension list: synatxe simplifiée

numbers_doubles = [e * 2 for e in nombres]
print(numbers_doubles)

nombres = range(10)

# nouvelle liste ne contenant que des nombres pairs

nombres_pairs = [e for e in nombres if e % 2 == 0]
print(nombres_pairs)

# comprehension list accèpte l'utilisation de fonctions
nombres = range(10)

def carre(e):
    return e ** 2


nombres_carres = [carre(x) for x in nombres]
print(nombres_carres)

print(">>>>>>>>> multiples conditions:")
nombres = range(10)

# nouvelle liste ne contenant que des nombres pairs supérieurs à 4

# sol1:

result = [e for e in nombres if e % 2 == 0 and e > 4]

# sol2: aucune limite sur le nombre de if

new_result = [e for e in nombres if e % 2 == 0 if e > 4 ]
print(result)
print(new_result)

print(">>>>>> random pour les listes:")
from random import choice, choices, sample, shuffle

cartes = [x for x in range(1, 11)]

print('choice: élément aléatoire')
print(choice(cartes))

print("choices: ensemble d'éléments aléatoire")

print(choices(cartes, k=5))

print("sample: ensemble d'éléments aléatoire")

print(sample(cartes,3))

print("shuffle: mélanger les éléments d'une liste")
shuffle(cartes)
print(cartes)