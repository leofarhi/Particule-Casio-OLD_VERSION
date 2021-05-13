from tkinter import *
import tkinter
from tkinter.messagebox import *
import tkinter.simpledialog
from tkinter.filedialog import *
from tkinter import ttk
from ClassSystem.MenuItem import MenuItem
from ClassSystem.PFrame import PFrame
from ClassSystem.Toolbar import Toolbar

class FrameDragAndDrop(PFrame):
    def __init__(self,RootWindow, **kw):
        PFrame.__init__(self,RootWindow, relief='raised',borderwidth = 5, **kw)
        self.IsWindowed = False
        # EditorWindow qui a actuellement le focus clavier. (Lecture seulement)
        self.focusedWindow = None
        # EditorWindow actuellement sous le curseur de la souris. (Lecture seulement)
        self.mouseOverWindow = None
        # Apparait dans le menu en haut à gauche
        self.MenuItem = None
        # Fenetre principale
        # Fenetre parent hiérachique
        self.RootWindow = RootWindow
        # Nom de la fenetre
        self.name = ""
        #self.MakeMenu()
        #self.MenuItem.Update()

        self.toolbar = Toolbar(self)

        self.Init()
    def Init(self):
        pass

    def MakeMenu(self):
        self.MenuItem = MenuItem(self)
        self.MenuItem.AddItem("Settings/Windowed")


    def destroy(self):
        self.toolbar.destroy()
        PFrame.destroy(self)



