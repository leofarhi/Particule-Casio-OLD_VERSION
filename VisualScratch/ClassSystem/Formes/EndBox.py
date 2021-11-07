from ClassSystem.Forme import Forme
from VisualScratch import *
from ClassSystem.Scratch import *
from ClassSystem.Forme import *
class EndBox(Forme):
    def __init__(self, WindCanvas, x, y, Parametres, Color, Name, PythonScript, Options=[], Load=False):
        self.TypeForme = "EndBox"
        Forme.__init__(self,WindCanvas, x, y, Parametres, Color, Name, PythonScript, Options, Load)
        self.Init()
        self.StartType()

    def StartType(self):
        self.CanPutInBlock = True
        self.CanAddBlock = False
        MyGroupWidget = []
        r = 25
        r = self.espace(r)
        h = 15
        for i in self.Options:
            if i[0] == "AddSize":
                r += i[1]
        posi = (self.x, self.y, self.x + (5 * self.Zoom), self.y, self.x + (10 * self.Zoom), self.y + (5 * self.Zoom),
                self.x + (15 * self.Zoom), self.y + (5 * self.Zoom), self.x + (20 * self.Zoom), self.y,
                self.x + (r * self.Zoom), self.y, self.x + (r * self.Zoom), self.y + (h * self.Zoom), self.x,
                self.y + (h * self.Zoom))
        A = self.Canevas.create_polygon(posi, outline=color(Couleurs.gris), fill=self.Color)
        MyGroupWidget.append(A)
        self.BoxCollider.append([self.x, self.y, self.x + (r * self.Zoom), self.y + (h * self.Zoom)])

        MyGroupWidget = self.ShowParametre(20, h, MyGroupWidget, self.x, self.y + ((h / 2) * self.Zoom))
        self.GroupeWidget.append(MyGroupWidget)