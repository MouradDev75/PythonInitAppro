# tuple: est une collection ordonnée avec doublons autorisés. Il s'agit d'une liste en lecture seule
# non modifiable

# tuple vide:
t1 = ()
t2 = tuple()

prenoms = ('Carine', 'Yoann', 'Mourad')
print(prenoms.count('Carine'))
print(prenoms.index('Carine'))

# Unpacking: déballage d'un tuple
p1,p2,p3 = prenoms
print(p1)
print(p2)
print(p3)

#modification d'un tuple:

# 1 - Converion en liste
prenoms = list(prenoms)
prenoms.append('Dawan')
prenoms.remove('Mourad')
# 2- Converion en tuple
prenoms = tuple(prenoms)

print(prenoms)