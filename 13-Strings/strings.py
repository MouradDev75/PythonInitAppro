# Un objet de type str est une collection ordonnée de caractères

texte = " ceci est une chaine "
r = texte.upper()

print(r)

# le type str par définition est immuable (quelque soit le langage de programmation utilisé)

print(texte.count("c"))
print(texte.index('c'))
print(len(texte))
print(texte.upper())
print(texte.lower())
print(texte.startswith("ceci")) # False
print(texte.endswith("chaine ")) # True
print(texte.strip()) # élimine les espaces en début et en fin de chaine
print(texte.rstrip()) # élimine les espaces en fin de chaine
print(texte.lstrip()) # élimine les espaces en début de chaine 
print('ceci' in texte)
print(texte.replace('e', 'a'))
print(texte.replace('e', 'a', count=1))
print('Premeir caractère:',texte[1])

print(">>>>>>> split:")

tab = texte.split()
print(tab)

chaine = "mot1,mot2,mot3,mot4"
print(chaine.split(','))
print(chaine.split(',', maxsplit=2))

fichier = "notes.2015.pdf"

# récupérer l'extension d'un fichier
print(fichier.rsplit('.', maxsplit=1)[1])

# fonction join: permet de construire une chaine

print(" ".join(['il','est','12',':','00']))

print(">>>>> chaines brutes:")

chemin = 'c:\test\notes.pdf'

# sol1: échapper les \

chemin = 'c:\\test\\notes.pdf'

# sol2: utiliser une chaine brute (chaine verbatime)

chemin_brute = r'c:\test\notes.pdf'
print(chemin_brute)

print(">>>>> chaine en octets (bytes)")

my_string = "hello, world!"
my_byte = my_string.encode(encoding='utf-8')

print(my_byte)

# la méthode .encode() renvoie un nouvel objet bytes représentant la version codée de la chaine originale

# le type str et les octets (byte) sont des séquences de caractères immuables
# byte est une séquence d'entiers compris entre 0 et 255 (entiers représentés sur 8 bits, 1 otects)

# ASCII est un codage de caractères qui ne contient que 128 caractères. par conséquence, tout char ASCII
#est représenté par 7 bits, ce qui inférieur à 1 octet

print(">>>> ASCII")
str_byte = b'Python'

print(str_byte)
print(type(str_byte))
print(str_byte[0])
print(list(str_byte))

print(chr(80)) #caractère associé au code ASCII 80

print(">>>>>>>>>>>>UTF-8")

# UTF-8 codage de char le pus courant qui est un codage unicode sur 8 bits
# Les 128 char ASCII possède le code numérique dans UTF-8 et les autres sont codés sur 2 octets

chaine_byte = bytes("café", 'utf-8')
print(chaine_byte)

# le é n'est pas un char ASCII, il est représenté sur 2 octets xc3 et xa9

# la conversion de chaines octets est une opération qui trouve des applications:
# - le traitement du langage naturel: NPL
# - Nettoyage des données
# - Scraping : extraction de données sur le web
# - Compression des données