from tkinter import *
import tkinter
from tkinter.messagebox import *
from tkinter import messagebox
import tkinter.simpledialog
from tkinter.filedialog import *
from tkinter import ttk
import tkinter as tk
from tkinter.ttk import Notebook
from CppEditor.VisualScratchConverter import VisualScratch
import json
#import customtkinter as cstTk
from CppEditor.BaseBlockScript import BaseBlockScript

from functools import partial
def _from_rgb(r,g,b):
    return "#%02x%02x%02x" % (r,g,b)

class BoxScript(Frame):
    def __init__(self,root,particuleScript):
        Frame.__init__(self,root,height=15)
        if self in particuleScript.BoxScripts:
            self.index = particuleScript.BoxScripts.index(self)
        else:
            self.index = len(particuleScript.BoxScripts)
        self.particuleScript = particuleScript

        self.TextVar = StringVar()
        self.TextVar.set("▶◆")
        self.MainLabel = Label(self,textvariable=self.TextVar,font=("Consolas", 8))
        self.MainLabel.pack(side=TOP, anchor=NW)

        self.selected = False

        self.bind('<Double-Button-1>', self.OpenMenu)
        self.bind('<Button-1>', self.Button1)
        self.bind("<Button-3>", self.Button3)
        self.redirectionBox=None
        self.LastNodeBlock=self
        self.Data={"Affichage":["◆"],"Fonction":None}

        self.pack(fill=tkinter.X, expand=True,side=TOP, anchor=N)
        self.SetColor()
    def Button1(self,event):
        if not self.selected:
            self.DeselectAll()
            self.selected = True
            self.Update()

    def Button3(self, event):
        self.Button1(None)
        self.particuleScript.PopUpScript.popup(self,event)

    def OpenMenu(self,*args):
        print("ok")
        MenuSelection(self.particuleScript.Particule,self, self.particuleScript)

    def Update(self):
        if self in self.particuleScript.BoxScripts:
            self.index = self.particuleScript.BoxScripts.index(self)
        self.SetColor()
        if self.redirectionBox==None:
            Affichage = self.Data["Affichage"]
            if len(Affichage) >0:
                self.TextVar.set(Affichage[0])
        else:
            ind = self.redirectionBox.index - self.index
            Affichage = self.redirectionBox.Data["Affichage"]
            if len(Affichage)>ind:
                self.TextVar.set(Affichage[ind])
    def Delete(self):
        self.particuleScript.BoxScripts.remove(self)
        self.UpdateAll()
        self.destroy()
    def SetColor(self):
        if self.selected:
            self.config(bg=_from_rgb(2, 116, 230))
            self.MainLabel.config(bg=_from_rgb(2, 116, 230))
        elif self.index%2==0:
            self.config(bg="white")
            self.MainLabel.config(bg="white")
        else:
            self.config(bg=_from_rgb(228, 236, 242))
            self.MainLabel.config(bg=_from_rgb(228, 236, 242))
    def DeselectAll(self,*args):
        for i in self.particuleScript.BoxScripts:
            i.selected=False
            i.Update()

    def UpdateAll(self, *args):
        for i in self.particuleScript.BoxScripts:
            i.Update()


class PopUpScript:
    def __init__(self,Particule):
        self.Particule=Particule
        self.boxScript = None
        self.contextMenu = Menu(self.Particule.Mafenetre, tearoff=False)
        self.contextMenu.add_command(label="Nouveau")#, command=)
        self.contextMenu.add_command(label="Editer...")
        self.contextMenu.add_separator()
        self.contextMenu.add_command(label="Couper")
        self.contextMenu.add_command(label="Copier")
        self.contextMenu.add_command(label="Coller")
        self.contextMenu.add_command(label="Effacer")
        self.contextMenu.add_command(label="Tout sélectionner")
    def popup(self, boxScript,event):
        """action in event of button 3 on tree view"""
        self.boxScript=boxScript
        self.UpdateMenu()
        self.contextMenu.post(event.x_root, event.y_root)
    def UpdateMenu(self):
        self.contextMenu.entryconfig("Nouveau",command=self.boxScript.OpenMenu)
        self.contextMenu.entryconfig("Effacer", command=self.boxScript.Delete)
        self.contextMenu.entryconfig("Couper",state="disabled")
        self.contextMenu.entryconfig("Couper", state="normal")
class ParticuleScript(Toplevel):
    def __init__(self,Particule):#,VisualScratchFile):
        self.Particule = Particule
        Toplevel.__init__(self, Particule.Mafenetre)
        self.geometry("800x500")
        self.title("ParticuleScript")
        MainBg1=_from_rgb(226, 238, 253)

        #self.VisualScratchFile = VisualScratchFile
        with open(Particule.FolderProject + "/SLN/Solution.sls", "r") as fic:
            dataSLN = fic.read()
        files = json.loads(dataSLN)["Files"]
        self.VisualScratchFile = VisualScratch(files[0])
        #########################



        self.Top = Frame(self,background=MainBg1)
        self.Top.pack(fill=tkinter.X,side=TOP, anchor=NW)

        Label(self.Top,text="Nom du component :",
              font=("Consolas", 12),background=MainBg1).grid(row=0, column=0,padx=5,pady=5)
        txtvar = StringVar()
        txtvar.set(self.VisualScratchFile.component.NameComponent)
        Entry(self.Top, textvariable=txtvar,
              state=DISABLED,font=("Consolas", 12)).grid(row=0, column=1,padx=5,pady=5)
        self.MainFrame = Frame(self)
        self.MainFrame.pack(fill=tkinter.BOTH, expand=True)

        self.CanvasFrame = Frame(self.MainFrame)
        self.CanvasFrame.pack(fill=tkinter.BOTH, expand=True,side=TOP)

        self.CanvasScript = Canvas(self.CanvasFrame,background="white")
        self.CanvasScript.pack(side=LEFT, fill=tkinter.BOTH, expand=True, anchor=N)

        scrollbarScript = ttk.Scrollbar(self.CanvasFrame, orient="vertical", command=self.CanvasScript.yview)
        scrollbarScript.pack(side=RIGHT, fill=Y)
        self.CanvasScript.bind(
            "<Configure>",self.UpdateScrollBar
        )
        self.ScriptFrame = Frame(self.CanvasScript)

        self.CanvasScript.create_window((0, 0), window=self.ScriptFrame, anchor="nw",tags="self.ScriptFrame")

        self.CanvasScript.configure(yscrollcommand=scrollbarScript.set)

        self.PopUpScript = PopUpScript(self.Particule)
        self.BoxScripts = []

        for i in range(10):
            self.BoxScripts.append(BoxScript(self.ScriptFrame,self))

    def UpdateScrollBar(self,event):
        width = event.width - 4
        self.CanvasScript.itemconfigure("self.ScriptFrame", width=width)
        self.CanvasScript.configure(scrollregion=self.CanvasScript.bbox('all'))
    def Save(self):
        pass
    def Load(self):
        pass
from CppEditor.Blocks import While
class MenuSelection(Toplevel):
    def __init__(self, Particule,boxScript,particuleScript):
        self.Particule = Particule
        Toplevel.__init__(self, Particule.Mafenetre)
        self.particuleScript = particuleScript
        self.boxScript=boxScript
        self.geometry("400x700")
        self.title("Commandes d'évènements")
        self.bind("<FocusOut>", self.OnLostFocus)
        self.focus_set()
        MainBg1 = _from_rgb(226, 238, 253)
        MainBg2 = _from_rgb(194, 214, 235)

        self.MainNotebook = Notebook(self)
        self.MainNotebook.pack(fill=BOTH, expand=True)

        self.FramePage1 = Frame(self.MainNotebook,background=MainBg1)
        self.FramePage1.pack(fill=BOTH, expand=True)
        self.MainNotebook.add(self.FramePage1, text="|      1      |")

        self.FramePage2 = Frame(self.MainNotebook,background=MainBg1)
        self.FramePage2.pack(fill=BOTH, expand=True)
        self.MainNotebook.add(self.FramePage2, text="|      2      |")

        self.FramePage3 = Frame(self.MainNotebook,background=MainBg1)
        self.FramePage3.pack(fill=BOTH, expand=True)
        self.MainNotebook.add(self.FramePage3, text="|      3      |")

        PageF_Right = Frame(self.FramePage1,background=MainBg1)
        PageF_Right.pack(side=RIGHT,fill=BOTH, expand=True, anchor=NE,padx=5)
        PageF_Left = Frame(self.FramePage1,background=MainBg1)
        PageF_Left.pack(side=LEFT,fill=BOTH, expand=True, anchor=NW,padx=5)
        lbf = LabelFrame(PageF_Left,text = "Groupe1",background=MainBg2)
        lbf.pack(side=TOP,fill=X,pady=5)
        Button(lbf,text="While",command = partial(self.LoadBlockScript,While.While)).pack(fill=X,padx=5,pady=2)
        Button(lbf, text="Fonction2").pack(fill=X, padx=5, pady=2)
        Button(lbf, text="Fonction3").pack(fill=X, padx=5, pady=2)

        lbf = LabelFrame(PageF_Left, text="Groupe2",background=MainBg2)
        lbf.pack(side=TOP,fill=X,pady=5)
        Button(lbf, text="Fonction4").pack(fill=X,padx=5,pady=2)
        Button(lbf, text="Fonction5").pack(fill=X, padx=5, pady=2)

        lbf = LabelFrame(PageF_Right, text="Groupe3",background=MainBg2)
        lbf.pack(side=TOP,fill=X,pady=5)
        Button(lbf, text="Fonctio6").pack(fill=X,padx=5,pady=2)
        Button(lbf, text="Fonction7").pack(fill=X, padx=5, pady=2)
        Button(lbf, text="Fonction8").pack(fill=X, padx=5, pady=2)
        Button(lbf, text="Fonction9").pack(fill=X, padx=5, pady=2)

    def OnLostFocus(self,_=None):
        self.destroy()

    def LoadBlockScript(self,blockScriptFunct,*args):
        assert issubclass(blockScriptFunct,BaseBlockScript)
        BBS = blockScriptFunct(self.boxScript)
        BBS.GUI_Print()
        self.OnLostFocus()
