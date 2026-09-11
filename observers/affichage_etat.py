import tkinter as tk
from observers.observer import Observateur


class AffichageEtat(Observateur):

    def __init__(self, parent):
        self._label = tk.Label(parent, text="Travail", font=("Arial", 16, "bold"))
        self._label.pack(pady=5)

    def actualiser(self, sujet) -> None:
        # À compléter :
        # Récupérez etat depuis sujet.get_donnees()
        # Mettez à jour le label
        # Couleur : noir pour "Travail", bleu pour "Pause"
        donnees = sujet.get_donnees() 
        etat = donnees["etat"]

        if etat == "Travail":
            self._label.config(text="Travail", fg="black")
        
        elif etat == "Pause":
            self._label.config(text="Pause", fg="blue")
