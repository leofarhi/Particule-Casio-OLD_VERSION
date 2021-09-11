from ClassSystem.Forme import Forme
from VisualScratch import *
from ClassSystem.Scratch import *
from ClassSystem.Forme import *
class Encadrement(Forme):
    def __init__(self, WindCanvas, x, y, Parametres, Color, Name, PythonScript, Options=[], Load=False):
        self.TypeForme = "Encadrement"
        Forme.__init__(self,WindCanvas, x, y, Parametres, Color, Name, PythonScript, Options, Load)
        self.Init()
        self.StartType()

    def StartType(self):
        self.CanPutInBlock = True
        self.CanAddBlock = True
        Encoche = 1
        End = False
        Parametre = [self.Parametres]
        for i in self.Options:
            if i[0] == "Encoche":
                Encoche = i[1]
            if i[0] == "End":
                End = i[1]
            if i[0] == "Parametres":
                Parametre.append(i[1])
        h = 15
        d = 0
        e = 0
        PosYpara = []
        h_add = 0
        if len(self.NextBlockIn) < 2:
            for i in range(Encoche + 2):
                self.NextBlockIn.append(None)
                self.NextBlockPosY.append(0)
        for i in range(Encoche):
            MyGroupWidget = []
            try:
                self.Parametres = Parametre[i]
            except:
                self.Parametres = []
            d += e
            r = 30
            r = self.espace(r)
            e = 0
            if i == 0:
                posi = (self.x, self.y,
                        self.x + (5 * self.Zoom), self.y, self.x + (10 * self.Zoom), self.y + (5 * self.Zoom),
                        self.x + (15 * self.Zoom), self.y + (5 * self.Zoom), self.x + (20 * self.Zoom), self.y,
                        self.x + (r * self.Zoom), self.y, self.x + (r * self.Zoom), self.y + (h * self.Zoom))

                self.BoxCollider.append([self.x, self.y, self.x + (r * self.Zoom), self.y + (h * self.Zoom)])
                self.NextBlockPosY[0] = (((h) * self.Zoom))
                self.x_add[0] = (3 * self.Zoom)
            else:
                self.NextBlockPosY[i] = (((h) * self.Zoom) + (d * self.Zoom))

            if i == 0:
                PosYpara.append(self.y + ((h / 2) * self.Zoom) + (d * self.Zoom))
            else:
                PosYpara.append(self.y + (int(h / 1.5) * self.Zoom) + (d * self.Zoom))

            if self.NextBlockIn[i] != None:
                self.h_add = (h / 2)
                try:
                    e = self.lenBlock(self.WindCanvas.AllWidget.get(self.NextBlockIn[i]), e)
                except:
                    pass
            else:
                e = h
                h_add += h

            posi += (self.x + (3 * self.Zoom) + (20 * self.Zoom), self.y + (h * self.Zoom) + (d * self.Zoom),
                     self.x + (3 * self.Zoom) + (15 * self.Zoom),
                     self.y + (h * self.Zoom) + (5 * self.Zoom) + (d * self.Zoom),
                     self.x + (3 * self.Zoom) + (10 * self.Zoom),
                     self.y + (h * self.Zoom) + (5 * self.Zoom) + (d * self.Zoom),
                     self.x + (3 * self.Zoom) + (5 * self.Zoom), self.y + (h * self.Zoom) + (d * self.Zoom))

            posi += (self.x + (3 * self.Zoom), self.y + (h * self.Zoom) + (d * self.Zoom),

                     self.x + (3 * self.Zoom), self.y + ((h) * self.Zoom) + (e * self.Zoom) + (d * self.Zoom),
                     self.x + (3 * self.Zoom) + (5 * self.Zoom),
                     self.y + ((h) * self.Zoom) + (e * self.Zoom) + (d * self.Zoom),
                     self.x + (3 * self.Zoom) + (10 * self.Zoom),
                     self.y + ((h) * self.Zoom) + (e * self.Zoom) + (5 * self.Zoom) + (d * self.Zoom),
                     self.x + (3 * self.Zoom) + (15 * self.Zoom),
                     self.y + ((h) * self.Zoom) + (e * self.Zoom) + (5 * self.Zoom) + (d * self.Zoom),
                     self.x + (3 * self.Zoom) + (20 * self.Zoom),
                     self.y + ((h) * self.Zoom) + (e * self.Zoom) + (d * self.Zoom),
                     self.x + (r * self.Zoom), self.y + ((h) * self.Zoom) + (e * self.Zoom) + (d * self.Zoom),
                     self.x + (r * self.Zoom),
                     self.y + ((h) * self.Zoom) + (e * self.Zoom) + ((h / 2) * self.Zoom) + (d * self.Zoom))

            if i + 1 == Encoche:
                if End:
                    posi += (
                    self.x, self.y + ((h) * self.Zoom) + (e * self.Zoom) + ((h / 2) * self.Zoom) + (d * self.Zoom))
                else:
                    posi += (self.x + (20 * self.Zoom),
                             self.y + ((h) * self.Zoom) + (e * self.Zoom) + ((h / 2) * self.Zoom) + (d * self.Zoom),
                             self.x + (15 * self.Zoom),
                             self.y + ((h) * self.Zoom) + (e * self.Zoom) + ((h / 2) * self.Zoom) + (d * self.Zoom) + (
                                         5 * self.Zoom),
                             self.x + (10 * self.Zoom),
                             self.y + ((h) * self.Zoom) + (e * self.Zoom) + ((h / 2) * self.Zoom) + (d * self.Zoom) + (
                                         5 * self.Zoom),
                             self.x + (5 * self.Zoom),
                             self.y + ((h) * self.Zoom) + (e * self.Zoom) + ((h / 2) * self.Zoom) + (d * self.Zoom),
                             self.x,
                             self.y + ((h) * self.Zoom) + (e * self.Zoom) + ((h / 2) * self.Zoom) + (d * self.Zoom))

                    self.NextBlockPosY[i + 1] = (
                                ((h) * self.Zoom) + ((h / 2) * self.Zoom) + (e * self.Zoom) + (d * self.Zoom))
                    self.BoxCollider.append([self.x, self.y + ((h) * self.Zoom) + (e * self.Zoom) + (d * self.Zoom),
                                             self.x + (r * self.Zoom),
                                             self.y + (h * self.Zoom) + ((h) * self.Zoom) + (e * self.Zoom) + (
                                                         d * self.Zoom)])
                    try:
                        self.x_add[i + 1] = 0
                    except:
                        self.x_add.append(0)
            else:
                self.NextBlockPosY[i + 1] = (((h * 2) * self.Zoom) + (e * self.Zoom) + (d * self.Zoom))
                self.BoxCollider.append([self.x, self.y + ((h) * self.Zoom) + (e * self.Zoom) + (d * self.Zoom),
                                         self.x + (r * self.Zoom),
                                         self.y + (h * self.Zoom) + ((h) * self.Zoom) + (e * self.Zoom) + (
                                                     d * self.Zoom)])
                try:
                    self.x_add[i + 1] = (3 * self.Zoom)
                except:
                    self.x_add.append((3 * self.Zoom))
            e += (h / 2)

        A = self.Canevas.create_polygon(posi, outline=color(Couleurs.gris), fill=self.Color)
        for i in range(Encoche):
            MyGroupWidget = []
            try:
                self.Parametres = Parametre[i]
            except:
                self.Parametres = []
            opts = None
            if i != 0:
                opts = "NotBoxColi"
            MyGroupWidget = self.ShowParametre(20 + 3, h, MyGroupWidget, self.x, PosYpara[i], opts=opts)
            self.GroupeWidget.append(MyGroupWidget)
        self.GroupeWidget[0].insert(0, A)
        self.Parametres = Parametre[0]
        self.h_add = (h / 2) * Encoche + h_add