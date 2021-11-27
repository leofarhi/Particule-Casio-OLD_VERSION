from VisualScratch import *
from ClassSystem.Scratch import *
from ClassSystem.Color import *
import unicodedata
import platform


def CorrectString(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s)
                   if unicodedata.category(c) != 'Mn')
class Forme:
    def __init__(self,WindCanvas, x, y, Parametres, Color, Name, PythonScript, Options=[], Load=False):
        self.WindCanvas = WindCanvas
        self.WidgetIndex = self.WindCanvas.GetNewIndexWidget()
        self.Options = Options
        self.Parametres = Parametres
        self.Canevas = WindCanvas.MainCanvas
        self.Color = "#%02x%02x%02x" % Color
        self.x = x
        self.y = y
        self.Zoom = WindCanvas.Zoom
        self.Name = Name
        self.NextBlockPosY = [15 * 2]
        self.NextBlockIn = [None]
        self.ParentBlock = None

        # ---------
        self.PythonScript = PythonScript
        self.PythonScript._Sys = self.WindCanvas._Sys
        self.PythonScript.SelfGetForme = self
        #self.PythonScript.WhenAdded()
        # ------------

        self.GroupeParametre = []
        for i in self.Parametres:
            self.GroupeParametre.append([i[0], None])

        self.WindCanvas.AddWidget(self)
        if Load != False: self.LoadData(Load)

        self.PythonScript.WhenAdded()

    def Init(self):
        self.h = 15
        self.h_add = 0
        self.x_add = [0]
        self.r = 0
        self.GroupeWidget = []
        self.BoxCollider = []
        self.CanAddBlock = False
        self.CanPutInBlock = False
        self.TypeParametreSyc = None

        self.ParametrePosi = []
        self.BoxColiParametre = []

    def SaveParametre(self, Para):
        Parametre = []
        for ind, i in enumerate(Para):
            if i[0] == "TexteEtNombre":
                if type(i[1]) == tkinter.StringVar:
                    Parametre.append([i[0], None])
                    (Parametre[ind])[1] = str(i[1].get())
            elif i[0] == "Liste":
                if type(i[2]) == tkinter.StringVar:
                    Parametre.append([i[0], i[1], None])
                    (Parametre[ind])[2] = str(i[2].get())
            else:
                Parametre.append(i)
        return Parametre

    def SaveData(self):
        Parametre = self.SaveParametre(self.Parametres)
        Option = []
        for ind, i in enumerate(self.Options):
            Option.append(i)
            if i[0] == "Parametres":
                (Option[ind])[1] = self.SaveParametre(i[1])
        X = self.x - self.WindCanvas.CamX
        Y = self.y - self.WindCanvas.CamY
        return [X, Y, self.WidgetIndex, self.NextBlockIn, self.ParentBlock, self.GroupeParametre, self.Name, Parametre, Option]

    def LoadData(self, Data):
        self.x, self.y, self.WidgetIndex, self.NextBlockIn, self.ParentBlock, self.GroupeParametre, self.Name, self.Parametres, self.Options = Data
        # print(self.GroupeParametre,self.Parametres,self.Options)

    def RemoveSelf(self):
        self.PythonScript.WhenRemove()
        for ind, i in enumerate(self.GroupeParametre):
            if i[1] != None: (self.WindCanvas.AllWidget.get(i[1])).RemoveSelf()
        for i in self.NextBlockIn:
            if i != None:
                (self.WindCanvas.AllWidget.get(i)).RemoveSelf()
        for A in self.GroupeWidget:
            for i in A:
                try:
                    self.Canevas.delete(i)
                except:
                    i.destroy()
        del self.WindCanvas.AllWidget[self.WidgetIndex]
        del self
        return

    def lenBlock(self, Widget, e):
        e += Widget.h + Widget.h_add
        for i in Widget.NextBlockIn:
            if i != None:
                e = self.lenBlock(self.WindCanvas.AllWidget.get(i), e)
        return e

    def espace(self, r):
        for ind, i in enumerate(self.Parametres):
            try:
                # print(self.GroupeParametre[ind])
                if i[0] == "Label":
                    tempV = 0
                    if platform.system()!='Windows': tempV = 0.5
                    r += len(i[1]) * (3 + tempV)
                if i[0] == "EmptyCercle":
                    h = 10
                    r += 2
                    d = 5
                    if (self.GroupeParametre[ind])[1] != None:
                        r += self.WindCanvas.AllWidget.get((self.GroupeParametre[ind])[1]).r / self.Zoom
                    else:
                        r += d + h + 4
                if i[0] == "TexteEtNombre":
                    h = 10
                    r += 3
                    if platform.system() != 'Windows': r += 8
                    d = 5
                    r += d + h + 25
                if i[0] == "Liste":
                    h = 10
                    r += 3
                    if platform.system() != 'Windows': r += 15
                    d = 5
                    r += d + h + 45
                if i[0] == "Booleen":
                    r += 2
                    h = 10
                    d = 5
                    if (self.GroupeParametre[ind])[1] != None:
                        r += self.WindCanvas.AllWidget.get((self.GroupeParametre[ind])[1]).r / self.Zoom
                    else:
                        r += d + h + h + 4
            except:
                pass
        return r

    def ShowParametre(self, r, h, MyGroupWidget, x, y, opts=None):
        A = None
        Autorise = ["Label", "TexteEtNombre", "Liste"]
        for ind, i in enumerate(self.Parametres):
            if True:#try:
                # if (self.GroupeParametre[ind])[0] in Autorise or (self.GroupeParametre[ind])[1]==None
                if i[0] == "Label":
                    i[1]=CorrectString(i[1])
                    A = self.Canevas.create_text(x + (r * self.Zoom), y, text=i[1], anchor='w', fill="white",
                                                 font=("TkDefaultFont", int(10 * (self.Zoom / 2))))
                    tempV = 0
                    if platform.system()!='Windows': tempV = 0.5
                    r += len(i[1]) * (3 + tempV)
                    MyGroupWidget.append(A)
                    self.BoxColiParametre.append([0, 0, 0, 0])
                    self.ParametrePosi.append([0, 0])
                if i[0] == "EmptyCercle":
                    h = 10
                    r += 2
                    o = (r * self.Zoom)
                    d = 5
                    self.ParametrePosi.append([x + o, y])
                    self.BoxColiParametre.append(
                        [x + o, y - ((h / 2) * self.Zoom), x + (h * self.Zoom) + (d * self.Zoom) + o,
                         y + ((h / 2) * self.Zoom)])
                    if (self.GroupeParametre[ind])[1] == None:

                        A = self.Canevas.create_oval(x + o, y - ((h / 2) * self.Zoom), x + (h * self.Zoom) + o,
                                                     y + ((h / 2) * self.Zoom), outline=color(Couleurs.gris),
                                                     fill=color(Couleurs.gris))
                        MyGroupWidget.append(A)
                        A = self.Canevas.create_oval(x + (d * self.Zoom) + o, y - ((h / 2) * self.Zoom),
                                                     x + (h * self.Zoom) + (d * self.Zoom) + o,
                                                     y + ((h / 2) * self.Zoom), outline=color(Couleurs.gris),
                                                     fill=color(Couleurs.gris))
                        MyGroupWidget.append(A)
                        A = self.Canevas.create_rectangle(x + ((h / 2) * self.Zoom) + o, y - ((h / 2) * self.Zoom),
                                                          x + (d * self.Zoom) + o + ((h / 2) * self.Zoom),
                                                          y + ((h / 2) * self.Zoom), outline=color(Couleurs.gris),
                                                          fill=color(Couleurs.gris))
                        MyGroupWidget.append(A)
                        r += d + h + 4

                    else:
                        r += self.WindCanvas.AllWidget.get((self.GroupeParametre[ind])[1]).r / self.Zoom
                if i[0] == "TexteEtNombre":
                    h = 15
                    r += 3
                    if len(i) < 2:
                        tx = StringVar()
                        self.Parametres[ind].append(tx)
                    else:
                        if type(i[1]) == tkinter.StringVar:
                            tx = i[1]
                        else:
                            tx = StringVar()
                            tx.set(str(i[1]))
                            (self.Parametres[ind])[1] = tx
                    tempWidth = int(10 * (self.Zoom / 2))
                    if platform.system() == 'Mac': tempWidth = 6
                    A = Entry(self.Canevas, textvariable=tx, width=tempWidth)
                    A.bind("<FocusOut>", partial(CorrigeBind, tx))
                    tempMacAddY = 0
                    if Game_OS == "Mac": tempMacAddY = int(h / 2)
                    A.place(x=x + (r * self.Zoom), y=y - int(int(h / 2) + tempMacAddY))
                    # self.Parametres[ind].append(A)
                    MyGroupWidget.append(A)
                    d = 5
                    r += d + 10 + 25
                    if platform.system() != 'Windows': r += 8
                    self.BoxColiParametre.append([0, 0, 0, 0])
                    self.ParametrePosi.append([0, 0])
                if i[0] == "Liste":
                    h = 15
                    r += 3
                    if platform.system() != 'Windows': r += 1
                    if len(i) < 3:
                        tx = StringVar()
                        self.Parametres[ind].append(tx)
                    else:
                        if type(i[2]) == tkinter.StringVar:
                            tx = i[2]
                        else:
                            tx = StringVar()
                            tx.set(str(i[2]))
                            (self.Parametres[ind])[2] = tx
                    tempWidth = int(15 * (self.Zoom / 2))
                    if platform.system() == 'Mac': tempWidth = 9
                    A = ttk.Combobox(self.Canevas, textvariable=tx, width=tempWidth)
                    A['values'] = tuple(i[1])
                    tempMacAddY = 0
                    if Game_OS == "Mac": tempMacAddY = int(h / 4)
                    A.place(x=x + (r * self.Zoom), y=y - int(int(h / 2) + tempMacAddY))
                    # self.Parametres[ind].append(A)
                    MyGroupWidget.append(A)
                    d = 5
                    r += d + 10 + 45
                    if platform.system() != 'Windows': r += 14
                    self.BoxColiParametre.append([0, 0, 0, 0])
                    self.ParametrePosi.append([0, 0])
                if i[0] == "Booleen":
                    r += 2
                    o = (r * self.Zoom)
                    h = 10
                    d = 5
                    self.ParametrePosi.append([x + o, y - (h * self.Zoom)])
                    self.BoxColiParametre.append(
                        [x + o, y - ((h / 2) * self.Zoom), x + (d * self.Zoom) + o + ((h * 2) * self.Zoom),
                         y + (h * self.Zoom - ((h / 2) * self.Zoom))])
                    # print(self.GroupeParametre[ind])
                    if (self.GroupeParametre[ind])[1] == None:

                        # print(r,self.Parametres)
                        posi = (x + (h * self.Zoom) + o, y - ((h / 2) * self.Zoom),
                                x + (d * self.Zoom) + o + (h * self.Zoom), y - ((h / 2) * self.Zoom),
                                x + (d * self.Zoom) + o + ((h * self.Zoom) * 2), y,
                                x + (d * self.Zoom) + o + (h * self.Zoom), y + (h * self.Zoom - ((h / 2) * self.Zoom)),
                                x + (h * self.Zoom) + o, y + (h * self.Zoom) - ((h / 2) * self.Zoom),
                                x + o, y)

                        A = self.Canevas.create_polygon(posi, outline=color(Couleurs.gris), fill=color(Couleurs.gris))
                        MyGroupWidget.append(A)
                        r += d + h + h + 4
                    else:
                        r += self.WindCanvas.AllWidget.get((self.GroupeParametre[ind])[1]).r / self.Zoom
                    # self.BoxColiParametre.append([x+o,0,0,0])
            #except:
                #pass
            if opts != None:
                if opts == "NotBoxColi":
                    del self.BoxColiParametre[-1]
        return MyGroupWidget

    def SetXY(self, x, y):
        if self.WindCanvas.ClassMoveObject.WidgetIsDrabed == self:
            if x - self.WindCanvas.CamX < 0:
                x = self.WindCanvas.CamX
            if y - self.WindCanvas.CamY < 0:
                y = self.WindCanvas.CamY
        for A in self.GroupeWidget:
            for i in A:
                try:
                    LstCoo = []
                    lst = self.Canevas.coords(i)
                    for ind, o in enumerate(lst):
                        if ind % 2 == 0:
                            LstCoo.append((o - (self.x - x)))
                        else:
                            LstCoo.append((o + ((-self.y) + y)))
                    self.Canevas.coords(i, tuple(LstCoo))
                    try:
                        self.Canevas.tag_raise(i)
                    except:
                        pass
                except:
                    try:
                        i.place(x=(int(i.place_info().get("x")) - (self.x - x)),
                                y=(int(i.place_info().get("y")) + ((-self.y) + y)))
                    except:
                        pass
        for ind2 in range(len(self.BoxCollider)):
            LstCoo = []
            for ind, o in enumerate(self.BoxCollider[ind2]):
                if ind % 2 == 0:
                    LstCoo.append((o - (self.x - x)))
                else:
                    LstCoo.append((o + ((-self.y) + y)))
            self.BoxCollider[ind2] = LstCoo
        for i in self.NextBlockIn:
            if i != None:
                TempWidget = self.WindCanvas.AllWidget.get(i)
                TempWidget.SetXY(TempWidget.x - (self.x - x), TempWidget.y + ((-self.y) + y))
        for ind, i in enumerate(self.GroupeParametre):
            if i[1] != None:
                TempWidget = self.WindCanvas.AllWidget.get(i[1])
                TempWidget.SetXY(TempWidget.x - (self.x - x), TempWidget.y + ((-self.y) + y))
        self.x = x
        self.y = y

    def childUpdate(self):
        for ind, i in enumerate(self.GroupeParametre):
            if i[1] != None: (self.WindCanvas.AllWidget.get(i[1])).Refresh()
        for i in self.NextBlockIn:
            if i != None:
                (self.WindCanvas.AllWidget.get(i)).Refresh()

    def Refresh(self):
        if self.PythonScript != None: self.PythonScript.WhenUpdate()

        for A in self.GroupeWidget:
            for i in A:
                try:
                    self.Canevas.delete(i)
                except:
                    i.destroy()

        self.Init()
        if self.ParentBlock != None and (not self.TypeForme in self.WindCanvas.FormeParametre):
            tempB = self.WindCanvas.AllWidget.get(self.ParentBlock)
            o = tempB.NextBlockPosY[tempB.NextBlockIn.index(self.WidgetIndex)]
            ind = tempB.NextBlockIn.index(self.WidgetIndex)
            self.WindCanvas.MoveWidget(self, self.x, self.y,
                       tempB.x + tempB.x_add[ind], tempB.y + o)
        elif self.ParentBlock != None and self.TypeForme in self.WindCanvas.FormeParametre:
            tempB = self.WindCanvas.AllWidget.get(self.ParentBlock)
            for ind, i in enumerate(tempB.GroupeParametre):
                if i[1] == self.WidgetIndex:
                    A = ind
                    break
            x_add, y_add = tempB.ParametrePosi[A]
            self.WindCanvas.MoveWidget(self, self.x, self.y,
                       x_add, y_add)
        self.StartType()
        if self.PythonScript != None: self.PythonScript.AfterUpdate()
        self.childUpdate()

    def update(self):
        if self.ParentBlock == None:
            self.Refresh()
        else:
            TempWidget = self.WindCanvas.AllWidget.get(self.ParentBlock)
            TempWidget.update()

