from tkinter import *
import tkinter
from tkinter.messagebox import *
from tkinter import messagebox
import tkinter.simpledialog
from tkinter.filedialog import *
from tkinter import ttk
class MenuItem:
    def __init__(self,RootFrame):
        self.RootFrame = RootFrame
        self.mainMenu = Menu(self.RootFrame)
        self.dicoMenu = {}
        self.cascade = {}
    def Update(self):
        self.mainMenu.destroy()
        self.mainMenu = Menu(self.RootFrame)
        self.cascade = {}
        for index, val in self.dicoMenu.items():
            cascadeName = index.split("/")[-2]
            bouton = index.split("/")[-1]
            if not cascadeName in self.cascade:
                TempCascade = Menu(self.mainMenu,tearoff=0)
                self.cascade.update({cascadeName:TempCascade})
            if "#$#" in bouton:
                self.cascade[cascadeName].add_separator()
            else:
                self.cascade[cascadeName].add_command(label=bouton, command=val)
        for index,val in self.cascade.items():
            self.mainMenu.add_cascade(label=index, menu=val)
        self.RootFrame.config(menu=self.mainMenu)

    def AddItem(self,name,command=None):
        self.dicoMenu.update({name:command})
    def Add_separator(self,name):
        self.dicoMenu.update({name+"/#$#"+str(len(self.dicoMenu)): None})