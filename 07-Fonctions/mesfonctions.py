def convertir_heures_minutes():
     heures = int(input('Nombre heures: '))
     print(f"{heures}h = {heures * 60}m")


def convertir_minutes_heures():
    minutes = int(input('Nombre minutes: '))
    print(f"{minutes}m = {minutes // 60}h {minutes % 60}m")

def menu():
    choix = input("""
        1) Convertir heures en minutes
        2) Convertir minutes en heures
        3) Quitter
        """)
    return choix