from tkinter import *
import tkinter
from tkinter.messagebox import *
from tkinter import messagebox
import tkinter.simpledialog
from tkinter.filedialog import *
from tkinter import ttk
from functools import partial
from inspect import isclass
from pkgutil import iter_modules
import pkgutil
from pathlib import Path
from importlib import import_module
import importlib.util
from PIL import ImageTk,Image
from VisualScratch import *
from ClassSystem.Color import *
from PIL import ImageTk,Image
class BlocksWindow(Frame):
    def __init__(self,_Sys,root,**kwargs):
        Frame.__init__(self,root,**kwargs)
        self.Sys = _Sys
        style = ttk.Style(self)#self.InspectorEditScriptOnglet)
        style.configure('lefttab.TNotebook', tabposition='wn')

        self.MiniOngletEditScript = ttk.Notebook(self, style='lefttab.TNotebook')
        self.MiniOngletEditScript.pack(fill=BOTH, expand=True)
        # Add Frame and Onglet
        for ind, i in enumerate(self.Sys.Scratch.TypeBox):
            TempFrame = ttk.Frame(self.MiniOngletEditScript)

            ScriptSlcBlock = Frame(TempFrame)  # ,width=50,height=100,bd=1)
            ScriptSlcBlock.pack(fill=BOTH, side=LEFT)
            # ScriptSlcBlock.update()
            ScriptSlcBlockCanvasScroll = Canvas(ScriptSlcBlock, width=300)  # int(ScriptSlcBlock.winfo_reqheight()))

            AllWinProjetframe = Frame(ScriptSlcBlockCanvasScroll)

            ScriptSlcBlockCScroll = Scrollbar(ScriptSlcBlock, orient="vertical",
                                              command=ScriptSlcBlockCanvasScroll.yview)
            ScriptSlcBlockCanvasScroll.configure(yscrollcommand=ScriptSlcBlockCScroll.set)

            ScriptSlcBlockCScroll.pack(side="right", fill="y")
            ScriptSlcBlockCanvasScroll.pack(side="left", fill="both", expand=True)

            ScriptSlcBlockCanvasScroll.create_window((0, 0), window=AllWinProjetframe,
                                                     anchor='nw')  # , width=int(w*0.75))
            AllWinProjetframe.bind("<Configure>", partial(self.ScriptSlcBlockframeconfig, ScriptSlcBlockCanvasScroll))
            TempData = [TempFrame, [], AllWinProjetframe]
            self.Sys.Scratch.OngletTypeTk.append(TempData)
            (self.Sys.Scratch.OngletTypeTk[-1])[0].pack(fill=BOTH, expand=True)
            self.MiniOngletEditScript.add((self.Sys.Scratch.OngletTypeTk[-1])[0], text=i)

        for i in os.listdir("Blocks/Data"):
            try:
                if i =="__pycache__":
                    continue
                file = "Blocks/Data/"+i
                spec = importlib.util.spec_from_file_location(i.replace(".py", ""), file)
                module = importlib.util.module_from_spec(spec)
                sys.modules[spec.name] = module
                spec.loader.exec_module(module)
                PythonScript = getattr(module, "ScriptBlockPython")()

                o = self.Sys.Scratch.OngletTypeTk[self.Sys.Scratch.TypeBox.index(PythonScript.Onglet)]
                tx = PythonScript.Texte
                colore = color(PythonScript.Color)
                if i.replace('.py', '.png') in os.listdir("Blocks/Images/"):
                    self.Sys.Scratch.ScratchBlockIcon.append(
                        ImageTk.PhotoImage(Image.open("Blocks/Images/" + i.replace('.py', '.png'))))
                    o[1].append(Button(o[2], text=tx, image=self.Sys.Scratch.ScratchBlockIcon[-1],
                                       command=partial(self.ButtonEditScript, "Blocks/Data/" + i)))
                else:
                    o[1].append(Button(o[2], text=tx, bg=colore,
                                       command=partial(self.ButtonEditScript, "Blocks/Data/" + i)))
                (o[1])[-1].pack()
            except Exception as e:
                print(e)

    def ScriptSlcBlockframeconfig(self, Canvas, event):
        Canvas.configure(scrollregion=Canvas.bbox("all"))  # ,width=200,height=200)

    def ButtonEditScript(self, file):
        global _i
        self.Sys.Scratch.CreateWidget((file.split("/")[-1]).replace(".py", ""))