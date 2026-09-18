from datetime import datetime
from observers.observer import Observateur


class LoggerSession(Observateur):

    def __init__(self, chemin_fichier: str = "pomodoro.log"):
        self._chemin = chemin_fichier
        self._derniere_session = 0

    def actualiser(self, sujet) -> None:
        # Récupérez sessions_completees depuis sujet.get_donnees()
        # Écrivez dans le fichier SEULEMENT si une nouvelle session est complétée
        # (comparez avec self._derniere_session)
        # Mettez à jour self._derniere_session

        donnees = sujet.get_donnees()
        sessions_completees = donnees["sessions_completees"]

        if sessions_completees > self._derniere_session:
            horodatage = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            with open(self._chemin, "a") as f:
                f.write(
                    f"{horodatage} | Session {sessions_completees} "
                    f"completee\n"
                )

            self._derniere_session = sessions_completees

