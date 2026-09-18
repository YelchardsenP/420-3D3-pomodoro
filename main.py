from models.minuteur import Minuteur
from views.dashboard import Dashboard

minuteur = Minuteur()
app = Dashboard(minuteur)

app.mainloop()

