from ClassSystem import read_file
from VisualScratch import *
from ClassSystem.MoveObject import MoveObject
import ClassSystem.Forme
import ClassSystem.Formes.Losange
import ClassSystem.Formes.Rectangle
import ClassSystem.Formes.Encadrement
import ClassSystem.Formes.EndBox
import ClassSystem.Formes.Vague
import ClassSystem.Formes.Cercle
from inspect import isclass
from pkgutil import iter_modules
import pkgutil
from pathlib import Path
from importlib import import_module
import importlib.util
from PIL import ImageTk,Image
from ClassSystem.Color import *



#PosX,PosY=0,0
#LastPosX,LastPosY=0,0

class Couleurs:
    bleu_fonce=(76,151,255)
    violet=(153,102,255)
    magenta=(207,99,207)
    jaune=(255,191,0)
    orange=(255,171,25)
    bleu_clair=(92,177,214)
    vert=(89,192,89)
    orange_fonce=(255,140,26)
    rose=(255,102,128)
    vert_fonce=(15,189,140)
    gris=(128,128,128)
    gris_clair=(208,208,208)
    noir=(0,0,0)

def color(colore):
    try:
        colore="#%02x%02x%02x" % colore
    except:
        pass
    return colore

class Scratch:
    def __init__(self, frame,_Sys):
        self.Sys = _Sys
        self.file = None
        #Constantes
        self.ScratchBlockIcon = []
        self.FolderProject = ""
        self.RepFolderSaveLoad = "__pycache__"
        self.RepFolderBlocks = "Blocks"
        self.RepFolderPython = "Python"
        self.TypeBox = ["Editeur", "Evenements", "Controle", "Variable", "Opérateurs", "Capteurs", "Mouvement", "Apparence",
                   "Stylo", "Mes Blocs"]
        self.OngletTypeTk = []
        self.Forme = ["Rectangle", "Cercle", "Losange", "Encadrement", "Vague", "EndBox"]
        self.ListFormeInFront = ["Cercle", "Losange"]  # ,"Encadrement"]
        self.FormeParametre = ["Cercle", "Losange"]

        self.Variables = []
        
        self.WindCanvas = self
        self.CamX = 0
        self.CamY = 0
        self.Zoom = 2
        self.MainCanvas = Canvas(frame, bg="white")

        self.ImgPoubelle = Image.open("lib/Poubelle.png")
        Cheight = 50
        Wimg, Himg = self.ImgPoubelle.size
        Wimg, Himg = int(Wimg * (Cheight / Himg)), int(Himg * (Cheight / Himg))
        self.ImgPoubelle = self.ImgPoubelle.resize((Wimg, Himg))  # , Image.ANTIALIAS)
        self.ImgPoubelle = ImageTk.PhotoImage(self.ImgPoubelle)
        self.MainCanvas.create_image(10, 10, anchor=NW, image=self.ImgPoubelle)

        self.ClassMoveObject = MoveObject(self.WindCanvas)
        self.MainCanvas.bind('<Button-1>', self.ClassMoveObject.Clic)  # evevement clic gauche (press)
        self.MainCanvas.bind('<B1-Motion>', self.ClassMoveObject.Drag)
        self.MainCanvas.bind('<ButtonRelease-1>', self.ClassMoveObject.Drop)
        self.MainCanvas.bind('<Button-2>', self.ClassMoveObject.ClicDuMilleu)
        self.MainCanvas.bind('<B2-Motion>', self.ClassMoveObject.ClicDuMilleuDrag)
        # self.CanvasScriptEditor.bind("<Key-Right>", keyRIGHT)
        # self.CanvasScriptEditor.bind("<Key-Left>", keyLEFT)
        # self.CanvasScriptEditor.bind("<Key-Up>", keyUP)
        # self.CanvasScriptEditor.bind("<Key-Down>", keyDOWN)

        self.MainCanvas.pack(fill=BOTH, expand=True)
        self.AllWidget = {}  # dictionnaire

    def AddCodeLst(self,Widget):
        Refuser = ["Label"]
        TypeParametre = ["Booleen", "EmptyCercle"]

        ActuLstNextBlock = []
        ActuLstParametre = []
        Parametres = Widget.SaveParametre(Widget.Parametres)
        for ind, i in enumerate(Widget.GroupeParametre):
            # print(i)
            if i[0] in TypeParametre:
                if i[1] != None:
                    ActuLstParametre.append(self.AddCodeLst(self.WindCanvas.AllWidget.get(i[1])))
                else:
                    ActuLstParametre.append(None)
            else:
                if not (Widget.Parametres[ind])[0] in Refuser:
                    ActuLstParametre.append(Parametres[ind])
        for i in Widget.NextBlockIn:
            if i != None:
                ActuLstNextBlock.append(self.AddCodeLst(self.WindCanvas.AllWidget.get(i)))
            else:
                ActuLstNextBlock.append([])
        return [Widget.Name, ActuLstParametre, ActuLstNextBlock]

    def GetCodeLst(self):
        self.SaveAllWidget()
        MyLst = []
        for i in list(self.WindCanvas.AllWidget.values()):
            if i == None: continue
            if i.TypeForme == "Vague":
                MyLst.append(i)
        CodeFinal = []
        for i in MyLst:
            CodeFinal.append(self.AddCodeLst(i))
        return CodeFinal

    def SaveAllWidget(self):
        if self.file==None:
            return
        if self.RepFolderSaveLoad == "": return
        Lst = []
        #read_file.save(self.RepFolderSaveLoad + "/settings.txt", "self.Variables", str(self.Variables))
        for forme in list(self.WindCanvas.AllWidget.values()):
            Lst.append(forme.SaveData())
        read_file.save(self.RepFolderSaveLoad + "/"+self.file, "AllWidget", str(Lst))
        for forme in list(self.WindCanvas.AllWidget.values()):
            if forme.ParentBlock == None:
                forme.update()

    def LoadAllWidget(self,file):
        global _iI
        self.file = file
        for forme in list(self.WindCanvas.AllWidget.values()):
            if forme.ParentBlock == None:
                forme.RemoveSelf()
        self.WindCanvas.CamX = 0
        self.WindCanvas.CamY = 0
        Lst = read_file.GetList(self.RepFolderSaveLoad + "/"+file, "AllWidget")
        if Lst == False: return
        LstWid = []
        for i in range(len(Lst)):
            LstWid.append(self.CreateWidget((Lst[i])[6].replace(".py", "")))
        self.WindCanvas.AllWidget = {}
        for ind, i in enumerate(LstWid):
            i.WidgetIndex = (Lst[ind])[2]
            self.WindCanvas.AllWidget.update({i.WidgetIndex: i})
        for ind, i in enumerate(LstWid):
            i.LoadData(Lst[ind])
        for forme in list(self.WindCanvas.AllWidget.values()):
            if forme.ParentBlock == None:
                forme.update()

    def CreateWidget(self,Block):
        file = self.RepFolderBlocks + "/Data/" + Block + ".py"
        spec = importlib.util.spec_from_file_location(Block, file)
        module = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = module
        spec.loader.exec_module(module)
        PythonScript = getattr(module,"ScriptBlockPython")(self.Sys)
        para = PythonScript.Parametres
        color = PythonScript.Color
        Options = PythonScript.Options

        nameClass = PythonScript.TypeForme
        #module = import_module(f"ClassParticule.Formes.{nameClass}")

        getattr(sys.modules["ClassSystem.Formes."+nameClass],nameClass)(self.WindCanvas,100,100,para,color,Block,PythonScript,Options=Options)
        return list(self.WindCanvas.AllWidget.values())[-1]

    def AddWidget(self,widget):
        
        self.WindCanvas.AllWidget.update({widget.WidgetIndex: widget})

    def GetNewIndexWidget(self):
        
        lst = list(self.WindCanvas.AllWidget.keys())
        count = 0
        while "Forme" + str(count) in lst: count += 1;
        return "Forme" + str(count)

    def MoveAll(self,x, y, x2, y2):
        for forme in list(self.WindCanvas.AllWidget.values()):
            if forme.ParentBlock == None:
                forme.SetXY(forme.x + (x2 - x), forme.y + (y2 - y))

    def MoveWidget(self,forme, x, y, x2, y2):
        forme.SetXY(forme.x + (x2 - x), forme.y + (y2 - y))