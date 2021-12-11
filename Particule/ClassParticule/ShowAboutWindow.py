from ClassSystem.EditorWindow import EditorWindow
from Particule import *


class ShowAboutWindow(EditorWindow):
    def __init__(self, RootWindow):
        EditorWindow.__init__(self, RootWindow,
                              ExternalWindow={"name":"A propos", "geometry": "350x250"},
                              Resize=False, ScrollbarShow=False)
        self.pack(fill=tkinter.BOTH, expand=True)
        Label(self, text="Version 2022.0b").pack(padx=5,pady=5)
        Label(self, text="Créé par Léo Farhi").pack(padx=5,pady=5)
        Label(self, text="Gestionnaire de fichier repris de RainingComputers").pack(padx=5,pady=5)

