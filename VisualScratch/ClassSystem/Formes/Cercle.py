from ClassSystem.Forme import Forme
from VisualScratch import *
from ClassSystem.Scratch import *
from ClassSystem.Forme import *
class Cercle(Forme):
    def __init__(self, WindCanvas, x, y, Parametres, Color, Name, PythonScript, Options=[], Load=False):
        self.TypeForme = "Cercle"
        Forme.__init__(self, WindCanvas, x, y, Parametres, Color, Name, PythonScript, Options, Load)
        self.Init()
        self.StartType()

    def StartType(self):
        self.TypeParametreSyc = "EmptyCercle"
        MyGroupWidget = []
        r = 0
        r = self.espace(r)
        h = 15
        for i in self.Options:
            if i[0] == "AddSize":
                r += i[1]
        A = self.Canevas.create_oval(self.x, self.y - ((h / 2) * self.Zoom), self.x + (h * self.Zoom),
                                     self.y + ((h / 2) * self.Zoom), outline=color(Couleurs.gris), fill=self.Color)
        MyGroupWidget.append(A)
        self.AddContextMenu(A)
        A = self.Canevas.create_oval(self.x + (r * self.Zoom), self.y - ((h / 2) * self.Zoom),
                                     self.x + (h * self.Zoom) + (r * self.Zoom), self.y + ((h / 2) * self.Zoom),
                                     outline=color(Couleurs.gris), fill=self.Color)
        MyGroupWidget.append(A)
        A = self.Canevas.create_rectangle(self.x + ((h / 2) * self.Zoom), self.y - ((h / 2) * self.Zoom),
                                          self.x + (r * self.Zoom) + ((h / 2) * self.Zoom),
                                          self.y + ((h / 2) * self.Zoom), outline=color(Couleurs.gris), fill=self.Color)
        MyGroupWidget.append(A)

        self.BoxCollider.append([self.x, self.y - ((h / 2) * self.Zoom), self.x + (h * self.Zoom) + (r * self.Zoom),
                                 self.y + ((h / 2) * self.Zoom)])

        MyGroupWidget = self.ShowParametre(0, h, MyGroupWidget, self.x + ((h / 2) * self.Zoom), self.y)
        self.GroupeWidget.append(MyGroupWidget)
        self.r = (h * self.Zoom) + (r * self.Zoom)