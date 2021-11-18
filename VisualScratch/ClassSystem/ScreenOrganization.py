from VisualScratch import *
from ClassSystem.Scratch import *
from ClassSystem.BlocksWindow import BlocksWindow
from ClassSystem.ZoneText import ZoneText
from ClassSystem.CustomNotebook import CustomNotebook
from ClassSystem.Hierarchy import Hierarchy
from ClassSystem.Console import Console
class ScreenOrganization:
    def __init__(self,_Sys):
        self.Sys = _Sys
        self.Mafenetre = self.Sys.Mafenetre

    def CreateWindows(self):
        self.PW = PanedWindow(self.Sys.Mafenetre, orient='vertical')
        self.GridTop = Frame(self.PW)
        self.GridTop.pack(fill=BOTH, expand=True)
        self.GridBottom = ttk.Notebook(self.PW)
        self.GridBottom.pack(fill=BOTH, expand=True)
        self.PW.add(self.GridTop)
        self.PW.add(self.GridBottom)

        self.PW.pack(fill=BOTH, expand=True)
        self.PW.configure(sashrelief=RAISED)

        self.pwTop = PanedWindow(self.GridTop, orient='horizontal')
        self.GridCenter = ttk.Notebook(self.pwTop, width=980, height=500)#CustomNotebook(self.pwTop, width=980, height=500)
        self.GridCenter.pack(fill=BOTH, expand=True)
        self.GridCenterLeft = ttk.Notebook(self.pwTop, width=230, height=500)
        self.GridCenterLeft.pack(fill=BOTH, expand=True)
        self.GridCenterRight = ttk.Notebook(self.pwTop, width=230, height=500)
        self.GridCenterRight.pack(fill=BOTH, expand=True)

        self.pwTop.add(self.GridCenterLeft)
        self.pwTop.add(self.GridCenter)
        self.pwTop.add(self.GridCenterRight)

        self.pwTop.pack(fill=BOTH, expand=True)
        self.pwTop.configure(sashrelief=RAISED)



    def SetWindows(self):
        self.ScratchZone = Frame(self.GridCenter)
        self.ScratchZone.pack(fill=BOTH, expand=True)
        self.GridCenter.add(self.ScratchZone, text='Scratch')
        self.Sys.Scratch = Scratch(self.ScratchZone,self.Sys)

        self.Sys.TextZonePython = ZoneText(self.GridCenter)
        self.Sys.TextZonePython.pack(side="left", fill=BOTH, expand=True)
        self.GridCenter.add(self.Sys.TextZonePython, text='Python')

        self.Sys.TextZone = ZoneText(self.GridCenter)
        self.Sys.TextZone.pack(side="left", fill=BOTH, expand=True)
        self.GridCenter.add(self.Sys.TextZone, text='Casio.hpp')

        self.Sys.TextZoneCpp = ZoneText(self.GridCenter)
        self.Sys.TextZoneCpp.pack(side="left", fill=BOTH, expand=True)
        self.GridCenter.add(self.Sys.TextZoneCpp, text='Casio.cpp')

        self.Sys.BlocksWindow = BlocksWindow(self.Sys,self.GridCenterRight)
        self.Sys.BlocksWindow.pack(fill=BOTH, expand=True)
        self.GridCenterRight.add(self.Sys.BlocksWindow, text='Blocks')

        self.GridCenterLeft.Sys = self.Sys
        self.Sys.Hierarchy = Hierarchy(self.GridCenterLeft)
        self.Sys.Hierarchy.pack(fill=BOTH, expand=True)
        self.GridCenterLeft.add(self.Sys.Hierarchy, text='Hierarchy')

        self.GridBottom.Sys = self.Sys
        self.Sys.Console = Console(self.GridBottom)
        self.Sys.Console.pack(fill=BOTH, expand=True)
        self.GridBottom.add(self.Sys.Console, text='Console')
    def Bind_Setup(self):
        #self.TextZone.bind("<F11>", self.Sys.toggleFullScreen)
        #self.TextZone.bind("<Control-s>", self.Sys.SaveFile)
        #self.TextZone.bind("<Escape>", self.Sys.quitFullScreen)

        self.Sys.Scratch.MainCanvas.bind("<FocusIn>", self.Sys.CompileScript)
        pass

    def ShowMenu(self):
        self.mainmenu = Menu(self.Mafenetre)
        self.Fichier = Menu(self.mainmenu, tearoff=0)
        self.Fichier.add_command(label="Nouveau", command=self.Sys.NewFile)
        self.Fichier.add_command(label="Ouvrir...", command=self.Sys.OpenFile)
        self.Fichier.add_command(label="Enregistrer", command=self.Sys.SaveFile)
        #self.Fichier.add_command(label="Enregistrer sous...", command=self.Sys.SaveAsFile)
        self.Fichier.add_separator()
        self.Fichier.add_command(label="Compile Script", command=self.Sys.CompileScript)
        self.Fichier.add_separator()
        self.Fichier.add_command(label="Quitter", command=self.Mafenetre.quit)


        self.Aide = Menu(self.mainmenu, tearoff=0)
        self.Aide.add_command(label="A propos")  # , command=show_about)

        self.mainmenu.add_cascade(label="Fichier", menu=self.Fichier)
        self.mainmenu.add_cascade(label="Aide", menu=self.Aide)
        self.Mafenetre.config(menu=self.mainmenu)