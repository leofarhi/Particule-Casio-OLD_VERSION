__author__ = 'Farhi'

from sys import platform as _platform
import sys,os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
#print(dname)

if _platform == "win32":
    Game_OS = "win"
elif _platform == "win64":
    Game_OS = "win"
elif _platform == "darwin":
    Game_OS = "Mac"
elif _platform == "linux":
    Game_OS = "linux"

import subprocess

if Game_OS == "win":
    from win32api import GetSystemMetrics
elif Game_OS == "Mac":
    from AppKit import NSScreen
    def GetSystemMetrics(nb):
        if nb == 0:
            return int(NSScreen.mainScreen().frame().size.width)
        elif nb == 1:
            return int(NSScreen.mainScreen().frame().size.height)
elif Game_OS == "linux":
    import subprocess


    def GetSystemMetrics(nb):
        output = \
        subprocess.Popen('xrandr | grep "\*" | cut -d" " -f4', shell=True, stdout=subprocess.PIPE).communicate()[0]
        resolution = output.split()[0].split(b'x')
        return int(resolution[nb])


from tkinter import *
import tkinter
from tkinter.messagebox import *
from  tkinter import messagebox
import tkinter.simpledialog
from tkinter.filedialog import *
from tkinter import ttk
import tkinter.simpledialog
from tkinter.filedialog import *
import ClassSystem.File_Folder as Fl
import ClassSystem.read_file as rf
from functools import partial

#import EditorComponent as InspectorCompo
from ClassSystem.Moteur import *
import ClassSystem.Moteur as M
from tkinter import *
from functools import partial
import _pickle as cPickle
import traceback
import os
import sys
import json
import ClassSystem.read_file
#sys.setrecursionlimit(10000)
from ClassSystem.ScreenOrganization import ScreenOrganization
from ClassSystem.MoveObject import MoveObject
from PIL import ImageTk,Image
from ClassSystem.BlockSys import *


class Loading:
    def __init__(self):
        self.Root = Tk()
        self.Root.resizable(False, False)
        self.Root.geometry("800x500")
        self.img = Image.open('lib/startup.png')
        self.Root.image = ImageTk.PhotoImage(self.img)
        self.label = Label(self.Root, image=self.Root.image, bg='white')
        self.Root.overrideredirect(True)
        self.Root.overrideredirect(True)
        #self.Root.geometry("+250+250")
        geom="+"+str((GetSystemMetrics(0)//2)-400)+"+"+str((GetSystemMetrics(1)//2)-250)
        self.Root.geometry(geom)
        self.Root.lift()
        self.Root.wm_attributes("-topmost", True)
        self.Root.wm_attributes("-disabled", True)
        #self.Root.wm_attributes("-transparentcolor", "white")
        self.label.pack()
        self.Root.after(1000, self.Root.destroy)
        self.label.mainloop()


class VisualScratch:
    def __init__(self,PathSLN = None,BuildMode=False):
        if PathSLN == None:
            self.SLN = {"PathParticule": "","Version": "2021.1.0","Files": []}
        else:
            with open(PathSLN,"r") as fic:
                dataSLN = fic.read()
            self.SLN = json.loads(dataSLN)
        self.LastTexte = [""] * 20
        self.Mafenetre = Tk()
        if BuildMode:
            self.Mafenetre.withdraw()
        self.Mafenetre.title('Visual Scratch')
        self.Mafenetre.grid_columnconfigure(0, weight=1)
        self.Mafenetre.grid_rowconfigure(0, weight=1)
        self.Mafenetre.Sys = self
        self.w = int(GetSystemMetrics(0) * 1)
        self.h = int(GetSystemMetrics(1) * 1)
        self.Mafenetre.geometry(str(self.w) + "x" + str(self.h))

        self.Mafenetre.attributes('-fullscreen', False)

        self.fullScreenState = False
        self.ScreenOrganization = ScreenOrganization(self)

        self.BlockSys = BlockSys(self)


        self.ScreenOrganization.ShowMenu()
        self.ScreenOrganization.CreateWindows()
        self.ScreenOrganization.SetWindows()
        self.ScreenOrganization.Bind_Setup()

        self.Mafenetre.protocol("WM_DELETE_WINDOW", self.on_closing)
        if BuildMode:
            code=(self.GetAllScriptPython(),self.GetAllScriptCasio())
            self.Mafenetre.destroy()
            print(code)
            sys.exit(code)
            return
        self.Mafenetre.mainloop()

    def OpenFile(self):
        #self.TextZone.OpenFile()
        pass

    def SaveFile(self, event=""):
        #self.TextZone.SaveFile()
        self.Scratch.SaveAllWidget()

    def SaveAsFile(self):
        self.TextZone.SaveAsFile()
        self.Scratch.SaveAllWidget()
    def CompileScript(self,*args):
        code = self.Scratch.GetCodeLst()
        PythonCode = self.GeneratePythonCode(code)
        self.TextZonePython.setTextInput(PythonCode)
        CasioCode = self.GenerateCasioCode(code)
        self.TextZone.setTextInput(CasioCode)


    def GenerateCasioCode(self, code):
        index = 0
        while (len(code)>index and (code[index])[0]!="InEditor"):
            index+=1
        if (len(code)>index):
            a=self.BlockSys.GetCode(code[index])
        else:
            return ""
        del code[index]
        Text=""
        for i in code:
            txt = self.BlockSys.GetCode(i)
            Text+=txt+"\n"
        a = a.replace("//&&Fonction",Text)
        return a
    def GeneratePythonCode(self,code):
        with open("lib/ComponentBase.py","r") as fic:
            base = fic.read()
        index = 0
        while (len(code)>index and (code[index])[0]!="InEditor"):
            index+=1
        if (len(code)>index):
            a=self.BlockSys.GetCodePython(code[index],base)
            return a
        else:
            return ""

    def GetAllScriptCasio(self):
        self.Scratch.SaveAllWidget()
        lst = []
        for i in self.Hierarchy.ALLfiles:
            name = os.path.basename(i)
            name = os.path.splitext(name)[0]
            self.Hierarchy.currentSelection = i
            self.Scratch.LoadAllWidget(i)
            code = self.Scratch.GetCodeLst()
            CasioCode = self.GenerateCasioCode(code)
            lst.append((i,CasioCode))
        return lst

    def GetAllScriptPython(self):
        self.Scratch.SaveAllWidget()
        lst = []
        for i in self.Hierarchy.ALLfiles:
            name = os.path.basename(i)
            name = os.path.splitext(name)[0]
            self.Hierarchy.currentSelection = i
            self.Scratch.LoadAllWidget(i)
            code = self.Scratch.GetCodeLst()
            PythonCode = self.GeneratePythonCode(code)
            lst.append((i,PythonCode))
        return lst


    def NewFile(self):
        self.TextZone.NewFile()

    def SaveAll(self, PathFile):
        self.TextZone.SaveAll()

    def on_closing(self):
        self.SaveFile()
        if messagebox.askokcancel("Quit", "Voulez-vous quitter ?"):
            self.Mafenetre.destroy()

    def toggleFullScreen(self, event):
        self.fullScreenState = not self.fullScreenState
        self.Mafenetre.attributes("-fullscreen", self.fullScreenState)

    def quitFullScreen(self, event):
        self.fullScreenState = False
        self.Mafenetre.attributes("-fullscreen", self.fullScreenState)


