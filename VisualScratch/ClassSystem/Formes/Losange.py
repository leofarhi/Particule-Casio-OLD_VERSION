from ClassSystem.Forme import Forme
from VisualScratch import *
from ClassSystem.Scratch import *
from ClassSystem.Forme import *
class Losange(Forme):
    def __init__(self, WindCanvas, x, y, Parametres, Color, Name, PythonScript, Options=[], Load=False):
        self.TypeForme = "Losange"
        Forme.__init__(self,WindCanvas, x, y, Parametres, Color, Name, PythonScript, Options, Load)
        self.Init()
        self.StartType()

    def StartType(self):
        self.TypeParametreSyc = "Booleen"
        MyGroupWidget = []
        r = 5
        r = self.espace(r)
        h = 15
        for i in self.Options:
            if i[0] == "AddSize":
                r += i[1]
        # print(r,self.Parametres)
        posi = (self.x + (h * self.Zoom), self.y,
                self.x + (r * self.Zoom) + (h * self.Zoom), self.y,
                self.x + (r * self.Zoom) + ((h * self.Zoom) * 2), self.y + ((h / 2) * self.Zoom),
                self.x + (r * self.Zoom) + (h * self.Zoom), self.y + (h * self.Zoom),
                self.x + (h * self.Zoom), self.y + (h * self.Zoom),
                self.x, self.y + ((h / 2) * self.Zoom))

        A = self.Canevas.create_polygon(posi, outline=color(Couleurs.gris), fill=self.Color)
        MyGroupWidget.append(A)
        self.BoxCollider.append(
            [self.x, self.y, self.x + (r * self.Zoom) + ((h * self.Zoom) * 2), self.y + (h * self.Zoom)])

        MyGroupWidget = self.ShowParametre(0, h, MyGroupWidget, self.x + (h * self.Zoom),
                                           self.y + ((h / 2) * self.Zoom))
        self.GroupeWidget.append(MyGroupWidget)
        self.r = (r * self.Zoom) + ((h * self.Zoom) * 2)