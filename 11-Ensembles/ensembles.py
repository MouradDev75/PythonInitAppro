# set: est une collection non ordonnée sans doublons. De plus, le type set supporte les opérations sur
# les ensembles, telles que l'union, l'intersection, le différence et la différence symétrique

# set vide:

s = set()

panier = {'pomme', 'banane', 'pomme', 'poire', 'orange'}
print(panier)

a = set('abracadabra') # conversion d'une chaine en set
b = set('alacazam')

print(a)
print(b)

print(">>>>> Union:")
# lettres dans a ou dans b ou dans les deux
# 2 syntaxes:
print(a | b)
print(a.union(b))

print(">>>>> Différence:")

# lettres dans a mais pas dans b
# 2 syntaxes:
print(a - b)
print(a.difference(b))

print(">>>> différence symétrique:")
# lettres dans a ou dans b mais pas dans les 2
# 2 syntaxes:
print(a ^ b)
print(a.symmetric_difference(b))

print(">>>>> intersection:")
# lettres dans a et dans b
# 2 syntaxes
print(a & b)
print(a.intersection(b))
 
lst = [1,1,2,2,3,3]
# suppression des doublons dans une liste
lst = set(lst)
lst = list(lst)

print(lst)