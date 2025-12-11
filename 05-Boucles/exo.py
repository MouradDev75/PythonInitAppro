print("<<<<<<<<<<<<<< Exo1 >>>>>>>>>>>>>>>>>")
# Affichez tous les nombres de 1 (inclus) à 10 (inclus) -> utilisez la fonction range()

# sol1:
nombres = range(11)
for n in nombres:
    if n != 0:
        print(n)

# sol2:
nombres = range(10) # de 0 à 9
for n in nombres:
    print(n+1)


# sol3: on peut aussi modifier l'index de début de la fonction range
nombres = range(1,11)
for n in nombres:
    print(n)

print("<<<<<<<<<<<<<< Exo2 >>>>>>>>>>>>>>>>>")
# Affichez tous les nombres pairs de 1 (inclus) à 15 (inclus) -> utilisez la fonction range()
# sol1:
nombres = range(1,16)
for e in nombres:
    if e % 2 == 0:
        print(e, "pair")
    else:
        print(e, "impair")
    

# sol2: on a la possibilité de modifier le pas de la fonction range()
nombres = range(2,16,2)
for e in nombres:
    print(e)

print("<<<<<<<<<<<<<< Exo3 >>>>>>>>>>>>>>>>>")

while True:

    choix = input("""

        Choisir une opération:
        - Addition: tapez a
        - Soustraction: tapez s
        - Multiplication: tapez m
        - Division: tapez d
        - Quitter: tapez q
        
        """)
    # la fin du while
    if choix == "q":
        print('Fin du programmme.......')
        break

    # gestion d'un choix invalide
    if choix not in  'asmd': #['a','s','m','d']
        print('Choix invalide.....')
        continue

    # lire 2 nombres
    nb1 = float(input('Premier nombre: '))
    nb2 = float(input('Second nombre: '))

    # gestion de la division par 0

    if choix == 'd' and nb2 == 0:
        while True:
            print('Second nombre différent de 0')
            nb2 = float(input('Second nombre: '))
            if nb2 != 0:
                break

    # Afficher le résultat

    print('>>> Solution macth case:')
    # Solution avec match case:
    match choix:

        case 'a':
            print(f"{nb1} + {nb2} = {nb1 + nb2}")

        case 's':
            print(f"{nb1} - {nb2} = {nb1 - nb2}")

        case 'm':
            print(f"{nb1} x {nb2} = {nb1 * nb2}")

        case 'd':
            print(f"{nb1} / {nb2} = {nb1 / nb2}")


    print('>>> Solution if elif:')
    # Solution avec if elif else

    if choix == 'a':
        print(f"{nb1} + {nb2} = {nb1 + nb2}")
    elif choix == 's':
        print(f"{nb1} - {nb2} = {nb1 - nb2}")
    elif choix == 'm':
        print(f"{nb1} x {nb2} = {nb1 * nb2}")
    elif choix == 'd':
        print(f"{nb1} / {nb2} = {nb1 / nb2}")


