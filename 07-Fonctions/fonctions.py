# Fonction: est un bloc d'instructions réutilisable

# 2 types de fonctions:
# fonction qui renvoie un résultat: input()
# fonction qui ne renvoie aucun résultat: print()

# Syntaxe pour créer une fonction: def nom_fonction(paramètres): instructions

# Exemple d'une fonction sans paramètres:

def my_fonction():
    print('texte...........')

# Appelle de my_function:

my_fonction()

# Sans les 2 parenthèses, il s'agit d'une variable contenant l'id de la fonction en mémoire
my_fonction

# Exemple d'une fonction avec des paramètres

def repeter(texte, nombre_de_fois):
    # for i in range(nombre_de_fois):
    #     print(texte)

    compteur = 0
    while True:
        print(texte)
        compteur += 1
        if compteur == nombre_de_fois:
            break

repeter('hello', 4)

# exemple d'une fonction qui renvoie un résultat

def somme(x, y):
    return x + y

r = somme(10,15)

print(f"somme = {r}")

# Annotation de types de puis python 3.5: 
# mécanisme permettant de spécifier le type de params attendus par une fonction

s:str = 'test'
i:int = 10
b:bool = False

s = 15.6

print(s)

# le fait de pratiquer les annotations de types, ne change pas le caractère dynamique du langage Python
# Intérêt: rendre la documentation technique des fonctions plus lisible

def addition(a:int, b:int) -> int:
    return a+b

print(">>>>>>>>>>>>> Fonction avec des params optionnels:")

def fct(x, alpha=10, beta=11):
    print(x,alpha,beta)

fct(99)
fct(55,66,77) # on a la possibilité de modifier les valeurs initiales des différents params

# Les params optionnels dans une fonctions, possèdent une valeur initiales et sont définis à la suite
# des params obligatoires

# en python, on peut appeler une fonction avec des params nommés sans tenir compte de leur position
# dans la fonction

fct(beta=42,x=2)

def prix_ttc(prix_ht:float, tva:float=0.2) -> float:
    return prix_ht * (1 + tva)

prix_ttc(50)
prix_ttc(50)
prix_ttc(60)

prix_ttc(99, tva=0.35)

# Intérêt: les params optionnels permettent d'obtenir un code facile à étendre, qui ne nécessite
# pas des modifications à mettre en place

print(10, end=" ")
print(20)

print(10,11,12, sep=":")

print(">>>>>>>>>>>>> fonction qui renvoie plusieurs résultats:")

def calculs(a:int, b:int):
    somme = a+b
    produit = a*b
    return somme,produit

resultat = calculs(10,5)
print(resultat)
print(type(resultat)) # il s'agit d'un tuple (c'est liste non modifiable)

# Unpacking: eclater un tuple
 
s,p = resultat

print("Somme =", s)
print("Produit =", p)

print(">>>>>>>>>> Fonction avec un nombre variable de params en entrée:")

def add(*entiers:int):
    #print(type(entiers))

    s = 0
    for e in entiers:
        s = s + e

    return s


print(10, "test", True, 10.5, "😄")

print(add(10,15))
print(add(10,15,20))
print(add(10,15,30,40))
print(add(10,15, 20,25,42))

print(">>>>>>>>>>>>>>> Variable locale - variable globale")

# b et c sont des variables globales: visiblent dans tout le script
b = 10
c = 10

def ma_fct():
    global b,c
    b = 15
    c = 15
    v = 12
    print("==============================================")
    print(locals())
    print("==============================================")
    # v est une variable locale: visible uniquement dans la fonction

ma_fct()

print(f"b = {b}")
print(f"c = {c}")


print(globals())

chemin_fichier = "c:\\notes.txt"

def f1():
    # lire le fichier
    global chemin_fichier
    pass

def f2():
    # modifier le fichier
    global chemin_fichier
    pass

def f3():
    # sauvegarder le fichier
    global chemin_fichier
    pass



print(">>>>>>>>>>>>>>>> Quelques fonctions natives de python:")

l = [1,2,3]

print(sum(l))
print(min(l))
print(max(l))
print(len(l)) # taille ou nombre d'éléments dans une collection
print(len('test'))

print(round(2.4589,ndigits=2))

# print()
# input()
# quit() - exit()

print(">>>>>>>>> le mot clé yield:")

# le mot clé yield est un outil puissant qui permet de créer des générateurs de valeurs
# facilitant la gestion de grandes quantités de données sans surcharger la mémoire

# Contrairement à un return, le yield ne termine pas la fonction
# Il suspend son exécution et reprend là où elle s'était arrêtée

def return_salaries():
    return ["premier_salarie", "deuxieme_salarie", "troisieme_salarie"]

def simple_generateur():
    yield "premier_salarie"
    yield "deuxieme_salarie"
    yield "troisieme_salarie"

    

gen = simple_generateur()

print(next(gen))
print(next(gen))
print(next(gen))

print("******************************************************")


def traitement_sequentiel_des_salaries():
    lst = ["premier_salarie", "deuxieme_salarie", "troisieme_salarie"]
    # return lst  -> charger tous les salariés en mémoire
    for s in lst:
        yield s

t = traitement_sequentiel_des_salaries()

salarie_en_cours = next(t)
if salarie_en_cours == 'premier_salarie':
    print('salarié traité...')
print(next(t))
print(next(t))


# yield est utile pour l'analyse de données (big data):

# si vous traitez de grandes quantités de données
# si vous voulez économiser de la mémoire en générant des données au fur et à mesure plutôt que
# de charger tout d'un coup

# cas pratique:
# charger le contenu d'une collection élément par élément
# lecture d'un fichier volumineux ligne par ligne

def generateur_nombres_pairs():
    entiers = [1,2,4,5,7,8,15,10,12,56,99,120]
    for e in entiers:
        if e % 2 == 0:
            yield e

gen_pair = generateur_nombres_pairs()

value = next(gen_pair)

try:
    while value != None:
        print(value)
        value = next(gen_pair)

except:
    pass
