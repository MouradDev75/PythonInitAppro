import random

aleatoire = random.randint(1,100)

for i in range(6):
    try:
        print(f"Tentative {i+1}")
        nb = int(input('Votre nombre: '))
        if nb == aleatoire:
            print(f"Bravo! trouvé en {i+1} tentatives")
            break

        if aleatoire > nb:
            print("Supérieur")

        if aleatoire < nb:
            print('Inférieur')

        # dernière tentative
        if i == 5 and nb != aleatoire:
            print(f"Perdu! aléatoire = {aleatoire}")

    except:
        print('nombre invalide......')