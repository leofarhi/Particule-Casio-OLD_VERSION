from tkinter import *
import tkinter
from tkinter.messagebox import *
from tkinter import messagebox
import tkinter.simpledialog
from tkinter.filedialog import *
from tkinter import ttk

class PFrame(Frame):
    def __init__(self,root,**kwargs):
        Frame.__init__(self,root,**kwargs)
        self.Particule = root.Particule
