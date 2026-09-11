import tkinter as tk
from observers.observer import Observateur


class CompteurSessions(Observateur):

    def __init__(self, parent):
        self._label = tk.Label(
            parent,
            text="Sessions complétées : 0",
            font=("Arial", 12)
        )
        self._label.pack(pady=5)

    def actualiser(self, sujet) -> None:
        # met a jour label sessions selon nombre actuel
        donnees = sujet.get_donnees()
        sessions_completees = donnees["sessions_completees"]

        self._label.config(text=f"Sessions complétées : {sessions_completees}")

