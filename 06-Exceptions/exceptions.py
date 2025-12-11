# Il existe 3 types d'erreurs possibles dans un code:
# - Erreurs de compilation (de syntaxe): sont détectées automaliquement par l'IDE 
# - Exceptions: sont des erreurs qui provoquent l'arrêt de l'application
# - code fonctionnel qui renvoie un résultat inattendu -> faire du debuggage 

# Pour éviter l'arrêt de l'application, une exception doit être gérée
# Pour gérer une exception, on utilise le bloc try/except

# Il existe plusieurs types d'exceptions possibles, chacune d'elle porte le nom de l'erreur
# qu'elle génère. Il existe aussi un type anonyme (type générique) qui est Exception

# Obligation: une ressource (fichier, base de données) doit être libérer à la fin de son utilisation

# Bonne pratique: prévoir un try/except lors de manipulation de ressources

nb = 10

a = 5
b = "6"


try:
    c = a + 2
    print(nb / 2)
    # ouverture d'un fichier en lecture
    
    
    
    
# except ZeroDivisionError:
#     print('exception gérée.......')

# except TypeError:
#     print('Exception concaténation gérée........')

# except Exception as e:
#     print('Exception gérée...........')
#     print(e)

# syntaxe simplifiée du except Exception
except:
    print('Exception gérée...........')
    

finally:
    # bloc optionnel, qui s'exécute tout le temps: exception ou pas
    print('bloc finally.........')
    # fermeture du fichier
    # sert dans la pratique à libérer les ressources utilisées dans le try

print('suite du script.......')

# demandez la saisie d'un nombre
while True:
    nb = input('Votre nombre: ')

    try:
        nb = int(nb)
        break

    except:
        print('Nombre invalide.....')

print(nb)
