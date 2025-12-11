print('>>>>>>>> __init__.py')

# permet d'initialiser le package: initialiser une connexion à une base données
from .module1 import init_database # . pointe vers la racine

init_database()


# permet la gestion des imports: limiter l'accès aux éléments du package
from .module2 import fct3

__all__ = ['module1', 'fct3'] # liste des modules et fonctions exportables