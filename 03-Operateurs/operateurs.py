print(">>>>>>>>>>>> Opérateurs arithmétiques:")

print("___Addition:")

a = 7
b = 3
c = a + b

c += 2 # syntaxe simplifiée de: c = c + 2
print(f"c = {c}")

print("___Soustraction:")

a = 7
b = 3
c = a - b

c -= 2 # syntaxe simplifiée de: c = c - 2
print(f"c = {c}")

print("___Multiplication:")

a = 7
b = 3
c = a * b

c *= 2 # syntaxe simplifiée de: c = c * 2
print(f"c = {c}")

print("___Division:")

a = 7
b = 3
c = a / b

c /= 2 # syntaxe simplifiée de: c = c / 2
print(f"c = {c}")

print("___Division entière:")

a = 7
b = 3
c = a // b

c //= 2 # syntaxe simplifiée de: c = c // 2
print(f"c = {c}")

print("___Modulo: reste de la division entière")

a = 7
b = 3
c = a % b

c %= 2 # syntaxe simplifiée de: c = c % 2
print(f"c = {c}")

print("___Puissance:")

a = 7
b = 3
c = a ** b

c **= 2 # syntaxe simplifiée de: c = c ** 2
print(f"c = {c}")

print(">>>>>>>>>>>>>>>>>> opérateurs de comparaison:")

# >, >=, <, <=, == (égalité), != (différent)
n1 = 5
n2 = 7

print(n1 == n2)
print(n1 != n2)
print(n1 > n2)
print(n1 >= n2)
print(n1 < n2)
print(n1 <= n2)

print(type(n1) == int)
print(type(n1) == float)
print(type(n1) == str)

print(">>>>>>>>>>>>>>> opérateurs logiques:")

# and, or et not
age = 17
derogation= True

print(age >= 18 or derogation == True)
# table logique
# A     B   A and B     A or B
# v     v      v          v
# v     f      f          v
# f     f      f          f
# f     v      f          v

n1 = 5
n2 = 7

print((n1 > 0) and (n1 > n2)) # False
print(not((n1 > 0) and (n1 > n2))) # True
print((n1 < 0) or (n2 > n1)) # True
print(not True)
print(not False)

print(">>>>>>>> Opérateurs: is et in")

# in permet de vérifier si un élément fait partie ou pas d'une collection

list1 = [1,2,3]

print(1 in list1) # true
print(5 in list1) # false

prenom = "sylvain" # une str est une collection de caractères

print('s' in prenom) # true
print('S' in prenom) # false: python est case sensitive
print('sv' in prenom) # false

list2 = [1,2,3]

print(list1 == list2) # True: car le mm contenu
print(list1 is list2) # False: car 2 objets différents en mémoire

print(id(list1))
print(id(list2))

list3 = list1
print(list1 is list3) # true: car le id en mémoire

x = 10

print(id(x))

y = x

print(id(y))

print(">>>>>>>>> Affectations multiples:")

# Si des variables qui sont du mm type et possèdent la mm valeur, on peut faire:

v1=v2=v3=10

# Si des variables ne sont pas du mm type, on peut faire: syntaxe non recommandée

val1,val2,val3 = 10,"test",False
print(val1)
print(val2)
print(val3)

# pour faire des calculs complèxes, on peut importer les 2 modules: math et statstics

import math,statistics

math.exp(2)
math.sqrt(25)
math.isinf(30)
math.pow(2,3) # 2 puissance 3

print(statistics.mean(list1))