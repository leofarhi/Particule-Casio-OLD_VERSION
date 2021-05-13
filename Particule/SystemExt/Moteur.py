#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Farhi'

from sys import platform as _platform
if _platform == "win32":
   Game_OS="win"
elif _platform == "win64":
    Game_OS="win"
elif _platform == "darwin":
    Game_OS="Mac"
elif _platform == "linux":
    Game_OS="linux"

if Game_OS=="win":
    from win32api import GetSystemMetrics
elif Game_OS=="Mac":
    from AppKit import NSScreen
    def GetSystemMetrics(nb):
        if nb==0:
            return int(NSScreen.mainScreen().frame().size.width)
        elif nb==1:
            return int(NSScreen.mainScreen().frame().size.height)
elif Game_OS=="linux":
    import subprocess
    def GetSystemMetrics(nb):
        output = subprocess.Popen('xrandr | grep "\*" | cut -d" " -f4',shell=True, stdout=subprocess.PIPE).communicate()[0]
        resolution = output.split()[0].split(b'x')
        return int(resolution[nb])
    
import time
import os
import tkinter
from tkinter.messagebox import *
from tkinter import ttk
import tkinter as tk
import sys
from functools import partial
import locale
import shutil
import random
from SystemExt import read_file as rf

import hashlib
from getpass import getpass
from threading import Thread
import threading
from googletrans import Translator
try:
    # Python2
    from urllib2 import urlopen
except ImportError:
    # Python3
    from urllib.request import urlopen
#locale.getdefaultlocale()#langue OS système
rep=os.getcwd()+"/lib"
sys.path.insert(0, rep)
rep_sys=os.getcwd()
def cherchefichier(fichier, rep_dico):
         
    # recherche du contenu du répertoire rep (fichiers et sous-répertoires)
    entrees = os.listdir(rep_dico)
             
    # traitement des fichiers du répertoire
    for entree in entrees:
        if (not os.path.isdir(os.path.join(rep_dico, entree))) and (entree==fichier):
            return True
             
    # traitement récursif des sous-répertoires de rep
    for entree in entrees:
        rep2 = os.path.join(rep_dico, entree)
        if os.path.isdir(rep2):
            chemin = cherchefichier(fichier, rep2)
            if chemin!="":
                return chemin
    return False
bleu_clair = (114, 186, 245)
bleu = (0, 0, 255)
blanc = (255, 255, 255)
noir = (0, 0, 0)
rouge= (255, 0, 0)
langue_sys=((locale.getdefaultlocale())[0])[0:2]
#pygame.init()
#mixer.init()

def create_rep(rep):
    os.makedirs(rep, exist_ok=True)
def del_rep(rep):
    shutil.rmtree(rep)
def rep_AppData():
    if Game_OS=="win":
        rep_AppData=str(os.getenv('APPDATA'))+'\\.venicarix'
    elif Game_OS=="Mac":
        rep_AppData=rep_sys+'/AppData/'
    return rep_AppData




#https://stackoverflow.com/questions/56494188/create-a-simple-function-for-combobox-dialog-in-tkinter
class SimpleChoiceBox:
    def __init__(self,title,text,choices,command=None):
        self.t = tk.Toplevel()
        self.t.title(title if title else "")
        self.selection = None
        self.command=command
        tk.Label(self.t, text=text if text else "").grid(row=0, column=0)
        self.c = ttk.Combobox(self.t, value=choices if choices else [], state="readonly")
        self.c.grid(row=1, column=0)
        self.but=tk.Button(self.t,text="Valider",command=self.ValideChoix)
        self.but.grid(row=2, column=0)
        #self.c.bind("<<ComboboxSelected>>", self.combobox_select)
    def ValideChoix(self):
        self.combobox_select("")
        if self.command!=None:
           self.command(self.selection)
           
    def combobox_select(self,event):
        self.selection = self.c.get()
        self.t.destroy()

        
#https://stackoverflow.com/questions/50398649/python-tkinter-tk-support-checklist-box
class ChecklistBox(tk.Frame):
    def __init__(self, parent, choices,command,prefix, **kwargs):
        self.fram=tk.Frame(parent, **kwargs)
        self.fram.pack(fill = tk.BOTH, expand = True)
        Etat=[i[1] for i in choices]
        self.choices=[i[0] for i in choices]
        self.vars = []
        self.command=command
        bg = self.fram.cget("background")
        for ind,choice in enumerate(self.choices):
            chkValue = tk.BooleanVar() 
            chkValue.set(Etat[ind])
            cb = tk.Checkbutton(self.fram, text=prefix+choice,var=chkValue,command=self.ExeCommandChangeValue,
                                onvalue=True, offvalue=False,
                                anchor="w", width=20, background=bg,
                                relief="flat", highlightthickness=0)
            self.vars.append(chkValue)
            cb.pack(side="top", fill="x", anchor="w")
            """
            if Etat[ind]==0:cb.deselect()
            elif Etat[ind]==1:cb.select()
            """
    def ExeCommandChangeValue(self):
        self.command(self.getCheckedItems())
    def getCheckedItems(self):
        values = []
        for ind,var in enumerate(self.vars):
            value =  var.get()
            if True:#value:
                values.append([self.choices[ind],value])
        return values
vide=None
try:
   translator = Translator()
except:
   langue_sys="fr"
def TradTxt(fr):
    name=langue_sys
    if name=="fr":return fr
    else:
       c=None
       if cherchefichier(name+".txt", "lib/Langues"):
          c=rf.found("lib/Langues/"+name+".txt",fr)
          if c!=False:return c
    
    translations = translator.translate(fr, dest=name)
    b=translations.text
                
    b=b.replace("&#39;","'")
    b=b.replace("&quot;",'"')
    b=b.replace("&",'')
    try:
       rf.save("lib/Langues/"+name+".txt",fr,b)
    except:
       pass
    return b

