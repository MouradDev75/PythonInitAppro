prenom = "Maude"
age = 25

# chaine à afficher: Votre prénom est Maude et vous avez 25 ans

print(">>>>>>>> Concaténation:")

# Python ne permet que la concaténation des chaines

print("Votre prénom est "+prenom+" et vous avez "+str(age)+" ans")

print(">>>>>>> la fonction format:")

# A partir de python 3, ajout de la fonction format

print("Votre prénom est {} et vous avez {} ans".format(prenom,age))

print(">>>>>>>> fstring:")

# A partir de python >= 3.6: ajout de fstirng qui est une syntaxe simplifiée de la fonction format

print(f"Votre prénom est {prenom} et vous avez {age} ans")

print(f"{5 * 3}") # exemple d'une expression dans fstring

# Avec fstring, on peut soit utiliser des variables ou des expressions entre accolades

print(f"{int(11.5)}") # autre expression

print(">>>>>>>> Utiliser la virgule comme séparateur")
# ne fonctionne qu'avec a fonction print

print("Votre prénom est",prenom,"et vous avez",age)

# pas besoin de faire des conversions en str, de plus la virgule génère un espace

print(">>>>>>>>>>>>>> les caractères d'échappements:")

# \n: new line - retour à la ligne
# \t: tabulation
# \s: space
# \b: backspace  

print("\tCeci est une\nchaine sur\nplusieurs lignes")

print('ceci est une "phrase" complèxe')
print("ceci est une \"phrase\" complèxe")

# raccourcis claviers: ctr + c -- ctr + v: copier/coller
# commenter et décommenter des lignes sélectionnées: ctr + /

chemin_fichier = "c:\\test\\notes.txt"

print(chemin_fichier)

print(">>>>>>>>>>>>>< DocString:")

# pratique pour définir des chaines multilignes :  chaine verbatime

print("""
    ceci est une
chaine sur plusieurs
lignes.
""")