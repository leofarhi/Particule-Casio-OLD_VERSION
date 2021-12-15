from ClassSystem.EditorWindow import EditorWindow
from Particule import *


class ShowAboutWindow(EditorWindow):
    def __init__(self, RootWindow):
        EditorWindow.__init__(self, RootWindow,
                              ExternalWindow={"name":TradTxt("A propos"), "geometry": "350x250"},
                              Resize=False, ScrollbarShow=False)
        self.pack(fill=tkinter.BOTH, expand=True)
        Label(self, text=TradTxt("Version ")+str(self.Particule.version)).pack(padx=5,pady=5)
        Label(self, text=TradTxt("Créé par Léo Farhi")).pack(padx=5,pady=5)
        Label(self, text=TradTxt("Gestionnaire de fichier repris de RainingComputers")).pack(padx=5,pady=5)

