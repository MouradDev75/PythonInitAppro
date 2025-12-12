# tkinter: Tool Kit INTERface

import tkinter

def open_window():
    w = tkinter.Toplevel(fenetre)
    w.title("New Window")
    w.geometry("200x100")

# créer une fenêtre
fenetre = tkinter.Tk()

fenetre.title("Fenêtre principale")
fenetre.geometry("400x600")

tkinter.Label(fenetre, text="New window").pack()
tkinter.Button(fenetre, text='Open new window', command=open_window).pack()
tkinter.Button(fenetre, text='Quitter', command=fenetre.destroy).pack()


# afficher la fenêtre
fenetre.mainloop()

# Documentation : https://docs.python.org/3/library/tkinter.html

# Pour les applications client/serveur (web): modules (Djongo - Flask - Fast API (plus récent))
