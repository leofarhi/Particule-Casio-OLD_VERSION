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
import importlib
from pkgutil import iter_modules
import pkgutil
from pathlib import Path
from importlib import import_module
from SystemExt import SpriteCoder

#Build :
from SystemExt import BuildSDKGraph


from ClassSystem.MenuItem import MenuItem
from ClassSystem.Notebook import Notebook
from ClassSystem.Editor import Editor
from ClassSystem.EditorWindow import EditorWindow
from ClassSystem.MonoBehaviour import MonoBehaviour
from ClassSystem.ScreenOrganization import ScreenOrganization
from ClassParticule.SaveData import *
import uuid
from ClassSystem.TypeGUI import TypeGUI
from ClassSystem.SLN_System import SLN_System
from ClassSystem.ProgressBarPopup import ProgressBarPopup
import ClassParticule.Component
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
        self.Process = ["Starting"]
        self.version = "2021.1.0"
        self.VisualScratchPath="C:\\Users\\leofa\\OneDrive\\Documents\\PycharmProjects\\Particule-Casio\\VS Out\\main\\main.exe"

        self.rep_sys = os.getcwd()
        self.FolderProject = FolderProject
        self.All_UUID = {}

        self.SLN_System = SLN_System(self)


        #print(path)

        #search_path = [path]  # set to None to see all modules importable from sys.path
        # self.all_modules = [x[1] for x in pkgutil.iter_modules(path=search_path)]

        # print(self.all_modules)
        # package_dir = Path(__file__).resolve().parent+"/Components/"
        # print(package_dir)
        self.AllComponent = []
        self.PersonnalModule = []
        self.GetCodeFromVisualScratch()
        sys.path.append(self.FolderProject+ "/Library/ScriptEditor")
        self.LoadComponents()
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

        self.Process.remove("Starting")
        self.Mafenetre.mainloop()

    def GetCodeFromVisualScratch(self):

        process = subprocess.Popen([self.VisualScratchPath,self.FolderProject + '/SLN/Solution.sls',"True"], stdout=subprocess.PIPE)
        #print(eval(process.stdout.readlines()[-1]))
        code=eval(process.stdout.readlines()[-1].decode('latin-1'))
        PythonCode=code[0]
        try:
            for i in os.listdir(self.FolderProject + "/Library/ScriptEditor/"):
                if ".py" in i:
                    os.remove(self.FolderProject + "/Library/ScriptEditor/" + i)
            for i in PythonCode:
                name = os.path.basename(i[0])
                name = os.path.splitext(name)[0]
                with open(self.FolderProject+ "/Library/ScriptEditor/"+name+".py","w",encoding="ascii") as fic:
                    fic.write(i[1])
        except:
            return




    def on_closing(self):
        if messagebox.askokcancel("Quit", TradTxt("Voulez-vous quitter ?")):
            self.Mafenetre.destroy()

    def toggleFullScreen(self, event):
        self.fullScreenState = not self.fullScreenState
        self.Mafenetre.attributes("-fullscreen", self.fullScreenState)

    def quitFullScreen(self, event):
        self.fullScreenState = False
        self.Mafenetre.attributes("-fullscreen", self.fullScreenState)

    def LoadComponents(self):
        path = os.path.dirname(os.path.abspath(__file__))
        path += "/ClassParticule/Components/"
        path2 = self.FolderProject+ "/Library/ScriptEditor"
        for (_, module_name, _) in iter_modules([path]):

            # import the module and iterate through its attributes
            module = import_module(f"ClassParticule.Components.{module_name}")
            for attribute_name in dir(module):
                attribute = getattr(module, attribute_name)

                if isclass(attribute):
                    # Add the class to this package's variables
                    globals()[attribute_name] = attribute
                # print(attribute_name)
                if attribute_name + ".py" in os.listdir(path) \
                        and (not attribute in self.AllComponent) \
                        and "ClassParticule.Components" in str(attribute):
                    self.AllComponent.append(attribute)
        for i in self.PersonnalModule:
            self.AllComponent.remove(i)
        self.PersonnalModule=[]
        PersonnalModuleName=[]
        for (_, module_name, _) in iter_modules([path2]):

            # import the module and iterate through its attributes

            module = import_module(module_name)
            #print(module, module_name)
            #getattr(module, module_name)
            for attribute_name in dir(module):
                attribute = getattr(module, attribute_name)

                if isclass(attribute):
                    # Add the class to this package's variables
                    globals()[attribute_name] = attribute
                # print(attribute_name)
                if attribute_name + ".py" in os.listdir(path2):
                    importlib.reload(module)
                if attribute_name + ".py" in os.listdir(path2) and (not str(attribute) in PersonnalModuleName):
                    PersonnalModuleName.append(str(attribute))
                    self.PersonnalModule.append(attribute)
                    self.AllComponent.append(attribute)

    def CreateUUID(self,TypeObject,UUID = False):
        if UUID == False or str(UUID).lower() =="false":
            UUID = "UUID_"+(str(uuid.uuid4()).replace("-","_"))
            while UUID in self.All_UUID:
                UUID = "UUID_"+(str(uuid.uuid4()).replace("-","_"))
            self.All_UUID.update({UUID:TypeObject})
        else:
            #if not UUID in [i[0] for i in self.All_UUID]:
            self.All_UUID.update({UUID:TypeObject})
        return UUID
    def GetObjectWithUUID(self,UUID):
        if UUID in self.All_UUID:
            return self.All_UUID[UUID]
        else:
            return None

    def GetTextureUUID(self, UUID):
        txt = self.GetObjectWithUUID(UUID)
        if txt == None:
            txt = self.GetObjectWithUUID("TextureVide")
        return txt

    def VerifFocusSet(self):
        self.Scene.surface.focus_set()

    def UpdateOnFocus(self,event=None,*args):
        if event!=None:
            if str(event.widget)!=".":
                return
        print("FocusMainWindow")
        if self.UpdateOnFocus in self.Process:
            return
        if "Starting" in self.Process:return
        self.Process.append(self.UpdateOnFocus)
        progress = ProgressBarPopup(self.Mafenetre)

        self.GetCodeFromVisualScratch()
        self.LoadComponents()
        self.LoadComponents()
        progress.SetValue(30)
        self.FolderWindow.CreateMetaFile()
        progress.SetValue(50)
        self.FolderWindow.GetAll_UUID()
        progress.SetValue(70)
        self.SLN_System.UpdateSLN()
        progress.SetValue(90)
        self.FolderWindow.update_search_files()
        progress.SetValue(95)
        ItemSelected = None
        if self.Hierarchy.ItemSelected!=None:
            ItemSelected = self.Hierarchy.ItemSelected.ID
        tempSlc = self.Hierarchy.t.selection()
        self.SaveData.SaveScene()
        if self.SaveData.PathScene!=None:
            self.SaveData.LoadScene(self.SaveData.PathScene)
            time.sleep(0.02)
            self.ScreenOrganization.ChangeInspector("Inspector")
            self.Hierarchy.t.selection_set(tempSlc)
            if ItemSelected != None:
                try:
                    ItemSelected=self.Hierarchy.allGameObjectOnScene[self.Hierarchy.t.item(ItemSelected)['values'][0]]
                except:
                    ItemSelected=None
                self.Hierarchy.ItemSelected = ItemSelected
                self.Inspector.UpdateItemSelected()
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






