from tkinter import *
import tkinter
from tkinter.messagebox import *
import tkinter.simpledialog
from tkinter.filedialog import *
from tkinter import ttk
import tkinter as tk
import time
from ClassSystem.EditorWindow import EditorWindow

class Hierarchy(EditorWindow):
    def __init__(self,RootWindow):
        EditorWindow.__init__(self,RootWindow)
        self.currentSelection=None
        self.listBox = Listbox(self)
        self.ALLfiles=[]
        self.listBox.pack(side="left",fill=BOTH, expand=True)
        self.reloadFiles()
        self.listBox.bind("<<ListboxSelect>>", self.callback)

    def reloadFiles(self):
        self.listBox.delete(0, tk.END)
        self.ALLfiles = self.Sys.SLN["Files"]
        for i in self.ALLfiles:
            self.listBox.insert('end',i.split("/")[-1])

    def callback(self,event):
        selection = event.widget.curselection()
        if (len(selection)>0):
            self.currentSelection = self.listBox.get(selection)
            self.Sys.Scratch.SaveAllWidget()
            self.Sys.Scratch.LoadAllWidget(self.ALLfiles[selection[0]])#self.listBox.get(selection))

    def RecursionFoundFile(self):
        pass