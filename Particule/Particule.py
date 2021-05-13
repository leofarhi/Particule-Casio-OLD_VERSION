__author__ = 'Farhi'

from sys import platform as _platform

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

from SystemExt.Moteur import *
from SystemExt import Moteur as M
import webbrowser
from math import *
from SystemExt import EditorComponent as InspectorCompo
import time
from SystemExt import Compile
from SystemExt import TransformImage
import subprocess
from tkinter import *
import tkinter
from tkinter.messagebox import *
from tkinter import messagebox
import tkinter.simpledialog
from tkinter.filedialog import *
from tkinter import ttk
from SystemExt import File_Folder as Fl
from PIL import Image
from PIL import ImageTk
import numpy as np
import pylab as pl
import matplotlib.cm as cm
import cv2
import sys, os
from SystemExt import Project as Pj
from SystemExt import read_file as rf
from functools import partial
from shutil import move
from glob import glob
from SystemExt import download as Dwn
from lib import AddBlockTk
import pygame
from inspect import isclass
from pkgutil import iter_modules
import pkgutil
from pathlib import Path
from importlib import import_module
from SystemExt import SpriteCoder
from ClassSystem.DragAndDropSys import DragAndDropSys

#Build :
from SystemExt import BuildSDKGraph


from ClassSystem.MenuItem import MenuItem
from ClassSystem.Notebook import Notebook
from ClassSystem.FrameDragAndDrop import FrameDragAndDrop
from ClassSystem.Editor import Editor
from ClassSystem.EditorWindow import EditorWindow
from ClassSystem.MonoBehaviour import MonoBehaviour
from ClassSystem.ScreenOrganization import ScreenOrganization
from ClassParticule.SaveData import *
import uuid
from ClassSystem.TypeGUI import TypeGUI
from ClassSystem.SLN_System import SLN_System
from ClassSystem.ProgressBarPopup import ProgressBarPopup

"""
from ClassParticule.Inspector import Inspector
from ClassSystem.WindowPanel import *
from ClassSystem.WinFrameBas import *
from ClassParticule.AssetStore import AssetStore
from ClassParticule.ClassImage import *
from ClassParticule.Component import *
from ClassParticule.Hierarchy import *
from ClassParticule.Inspector import *
from ClassParticule.LoadSystem import *
from ClassParticule.NewElement import *
from ClassParticule.ScratchEditor import *
from ClassParticule.WindowBuild import *
from ClassParticule.WindowFolder import *
from ClassParticule.WindowScene import *
"""


if rf.found("setup.txt","Langue")==False:rf.save("setup.txt","Langue",langue_sys)
else:
   langue_sys=rf.found("setup.txt","Langue")
   M.langue_sys=rf.found("setup.txt","Langue")



def ColorRGB(RGB):
    return "#%02x%02x%02x" % RGB


def show_about():
    about_window = Toplevel(self.Mafenetre)
    about_window.title(TradTxt("A propos"))
    lb1 = Label(about_window, text="Version 2.0 beta")
    lb1.pack()
    lb2 = Label(about_window, text=TradTxt("Fait par Farhi"))
    lb2.pack()
    # lb3=Label(about_window, text=TradTxt("Compilateur : Bide.jar fait par Zezombye"))
    # lb3.pack()
    lb3 = Label(about_window, text=TradTxt("Version incomplète"))
    lb3.pack()





class Particule:
    def __init__(self,FolderProject=os.getcwd()+"/ProjectFolder"):
        self.Process = []
        self.version = "2021.1.0"
        self.rep_sys = os.getcwd()
        self.FolderProject = FolderProject
        self.All_UUID = []
        self.DragAndDropSys = DragAndDropSys(self)

        self.SLN_System = SLN_System(self)

        path = os.path.dirname(os.path.abspath(__file__))
        path += "/ClassParticule/Components/"
        #print(path)

        #search_path = [path]  # set to None to see all modules importable from sys.path
        # self.all_modules = [x[1] for x in pkgutil.iter_modules(path=search_path)]

        # print(self.all_modules)
        # package_dir = Path(__file__).resolve().parent+"/Components/"
        # print(package_dir)
        self.AllComponent = []
        for (_, module_name, _) in iter_modules([path]):

            # import the module and iterate through its attributes
            module = import_module(f"ClassParticule.Components.{module_name}")
            for attribute_name in dir(module):
                attribute = getattr(module, attribute_name)

                if isclass(attribute):
                    # Add the class to this package's variables
                    globals()[attribute_name] = attribute
                #print(attribute_name)
                if attribute_name+".py" in os.listdir(path) and (not attribute in self.AllComponent):
                    self.AllComponent.append(attribute)
        #print(self.AllComponent)
        # print(getattr(sys.modules[__name__], "Camera"))
        # getattr(module, class_name)
        # print(getattr(self.module, "Transform")(gameObject))
        # return

        """
        self.LoadSystem = LoadSystem(self)
        self.LoadSystem.All_load_on_start(True)
        self.FolderSystem = Folder(self)
        self.Component = Component(self)
        """

        self.Mafenetre = Tk()
        self.Mafenetre.Particule = self
        self.Mafenetre.title('Particule - Editeur de jeu pour casio')
        self.Mafenetre.attributes('-fullscreen', False)
        self.Mafenetre.grid_columnconfigure(0, weight=1)
        self.Mafenetre.grid_rowconfigure(0, weight=1)

        self.AllEditorWindow=[]


        self.fullScreenState = False
        self.Mafenetre.bind("<F11>", self.toggleFullScreen)
        self.Mafenetre.bind("<Escape>", self.quitFullScreen)

        if Game_OS == "linux":
            try:
                self.Mafenetre.iconbitmap('@lib/logo.xbm')
            except:
                pass
            try:
                tempimg = tkinter.PhotoImage(file='lib/logo.png')
                self.Mafenetre.tk.call('wm', 'iconphoto', self.Mafenetre._w, tempimg)
            except:
                pass
        else:
            try:
                self.Mafenetre.iconbitmap('lib/logo.ico')
            except:
                pass

        self.Mafenetre.geometry(str(GetSystemMetrics(0)) + "x" + str(GetSystemMetrics(1)))
        self.Mafenetre.configure(bg=ColorRGB((162, 162, 162)))

        self.ScreenOrganization = ScreenOrganization(self)

        """
        self.Onglets()
        self.Scene = Scene(self)
        self.Inspector = Inspector(self)
        self.ScratchEditor = ScratchEditor(self)
        self.Hierarchy = Hierarchy(self)
        self.ScalePrefab = (self.Mafenetre.winfo_screenheight() - int(self.Scene.surface.config("height")[-1]))

        self.FrameBasWObject = WinFrameBas(self.FolderOnglet, self.FolderSystem.FolderShowPrefabs)
        self.FrameBasWObject.WObject()

        self.ScenesFrameBasWObject = WinFrameBas(self.FolderScenesBOnglet, self.FolderSystem.FolderShowScenes)
        self.ScenesFrameBasWObject.WObject()

        self.ImagesFrameBasWObject = WinFrameBas(self.FolderImagesBOnglet, self.FolderSystem.FolderShowImages)
        self.ImagesFrameBasWObject.WObject()
        """

        # self.Inspector.EditElement()

        self.MainLoop()
        #self.Inspector.LoopEdit()
        #self.LoadSystem.All_load_Element_Start(True)

        #self.CanevasAsset.UpdateScreen()
        self.Mafenetre.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.Mafenetre.mainloop()
    def on_closing(self):
        if messagebox.askokcancel("Quit", TradTxt("Voulez-vous quitter ?")):
            self.Mafenetre.destroy()

    def toggleFullScreen(self, event):
        self.fullScreenState = not self.fullScreenState
        self.Mafenetre.attributes("-fullscreen", self.fullScreenState)

    def quitFullScreen(self, event):
        self.fullScreenState = False
        self.Mafenetre.attributes("-fullscreen", self.fullScreenState)

    def CreateUUID(self,UUID = False):
        if UUID == False:
            UUID = str(uuid.uuid4())
            while UUID in self.All_UUID:
                UUID= str(uuid.uuid4())
            self.All_UUID.append(UUID)
        else:
            if UUID not in self.All_UUID:
                self.All_UUID.append(UUID)
        return UUID
    def VerifFocusSet(self):
        self.Scene.surface.focus_set()

    def UpdateOnFocus(self,event,*args):
        if str(event.widget)!=".":
            return
        print("FocusMainWindow")
        if self.UpdateOnFocus in self.Process:
            return
        self.Process.append(self.UpdateOnFocus)
        progress = ProgressBarPopup(self.Mafenetre)
        self.FolderWindow.CreateMetaFile()
        progress.SetValue(30)
        self.FolderWindow.GetAll_UUID()
        progress.SetValue(70)
        self.FolderWindow.update_search_files()
        progress.SetValue(100)
        progress.destroy()
        self.Process.remove(self.UpdateOnFocus)

    def MainLoop(self):
        for EditorWindow in self.AllEditorWindow:
            EditorWindow.Update()
        dt_ms = 50
        self.Mafenetre.after(dt_ms, self.MainLoop)

#######################################








Pj.selected = None






