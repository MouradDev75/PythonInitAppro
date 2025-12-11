#1)nouvelle liste ne contenant que des nombres positifs
nombres = range(-10,10)

nombres_positifs = [n for n in nombres if n >= 0]

#2)nouvelle liste en inversant uniquement les nombres impairs
nombres = range(10)
nombres_inverse = [n if n % 2 == 0 else -n for n in nombres]

#3)Affichez le nombre d'éléments supérieurs à 3 dans lst
lst = [1,5,2,3,7,9]
print(len([n for n in lst if n > 3]))

#4)
listA = [1,2,3,4]
listB = [1,2]

liste_difference = [e for e in listA if e not in listB]

#5)
def somme_pairs_distincts(entiers:list[int]) -> int:
    # construire une liste ne contenant que des nombres pairs distincts
    lst = []
    for e in entiers:
        if e % 2 == 0 and e not in lst:
            lst.append(e)

    return sum(lst)