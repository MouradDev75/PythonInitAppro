#1)
def somme_liste(entiers):

    s = 0
    for e in entiers:
        s = s + e

    return s

print(somme_liste([2,7,3,5]))

#2)

def moyenne_liste(entiers):
    s = somme_liste(entiers)

    nb = 0
    for e in entiers:
         nb = nb + 1

    return s / nb

print(moyenne_liste([1,2]))

#3)
def table_multiplication(nombre, premier_multiple, dernier_multiple):
    if nombre < 0 or premier_multiple < 0 or dernier_multiple < 0 or premier_multiple > dernier_multiple:
        print("Params invalides.......")
    else:
        for i in range(premier_multiple, dernier_multiple + 1):
            print(f"{nombre} x {i} = {nombre * i}")

table_multiplication(11,1,10)

#4)

from mesfonctions import menu,convertir_heures_minutes,convertir_minutes_heures

while True:
 
    choix = menu()
    if choix == '3':
        break

    elif choix == '1':
        convertir_heures_minutes()

    elif choix == '2':
        convertir_minutes_heures()

    else:
        print('choix invalide.....')