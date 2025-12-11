# Un environnement virtuel est une copie de Python installé sur la machine

# Bonne pratique:

# Au début d'un projet Python, on crée un env. virtuel contenant les modules externes nécessaires au projet
# 
#  Pour créer des envi. virtuels, on utilise e module de base venv
# Etape1: Commande à exécuter dans le terminal:
# python -m venv nom_venv

# Etape2: activez l'env. virtuel
# commande à exécuter dans le terminal: .\_env\Scripts\activate

# Si PowerShell bloque l'exécution de scripts externes:
# Commande à exécuter dans powerShell:
# - Lancez powershell en tant qu'admin
# Set-ExecutionPolicy remoteSigned -> répondre par o (oui)

# Dans vs Code (en bas à droit): choisir l'interpréteur de l'env. virtuel

# Etape3: installez les modules externes nécessaires au projet

#### A la fin du projet, on génère un fichier contenant la liste des modules externes nécessaires
# au projet.

# Commande à exécuter: pip freeze --local > requirements.txt

# Pour installer les modules listés dans requirements.txt

# commande: pip install -r requirements.txt