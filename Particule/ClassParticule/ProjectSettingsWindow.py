from ClassSystem.EditorWindow import EditorWindow
from Particule import *

class Vector2Show(Frame):
    def __init__(self,root,x=0,y=0):
        Frame.__init__(self, root)
        self.root = root
        self.var1 = DoubleVar()
        self.var2 = DoubleVar()
        self.var1.set(x)
        self.var2.set(y)
        Label(self, text="x :").grid(row=1, column=0)
        Label(self, text="y :").grid(row=1, column=2)
        self.entry1 = Entry(self, textvariable=self.var1)
        self.entry1.grid(row=1, column=1, sticky='EWNS')  # .pack(fill=tkinter.BOTH, expand=True)
        self.entry2 = Entry(self, textvariable=self.var2)
        self.entry2.grid(row=1, column=3, sticky='EWNS')  # .pack(fill=tkinter.BOTH, expand=True)
    def GetValue(self):
        return (self.var1.get(),self.var2.get())
    def SetValue(self,x,y):
        self.var1.set(x)
        self.var2.set(y)

class ProjectSettingsWindow(EditorWindow):
    def __init__(self, RootWindow,OnlyLoad=False):
        EditorWindow.__init__(self, RootWindow,
                              ExternalWindow={"name":"Project Settings", "geometry": "650x450"},
                              Resize=False, ScrollbarShow=False)
        if not OnlyLoad:
            self.pack(fill=tkinter.BOTH, expand=True)
        self.pathFile = self.Particule.FolderProject + "/ProjectSettings/ProjectSettings.txt"
        style = ttk.Style(self)
        style.configure('lefttab.TNotebook', tabposition='wn')

        self.NotebookOnglet = ttk.Notebook(self, style='lefttab.TNotebook')
        self.NotebookOnglet.pack(fill=BOTH, expand=True)

        buttonApply = tkinter.Button(self, text="Apply",command=self.SaveAllData)
        buttonApply.pack(anchor = "s", side = "right",padx=5,pady=5)

        self.EditorFrame = LabelFrame(self.NotebookOnglet)
        #self.EditorFrame.pack(fill=tkinter.BOTH, expand=True, anchor=N)

        self.GraphicsFrame = LabelFrame(self.NotebookOnglet)
        #self.GraphicsFrame.pack(fill=tkinter.BOTH, expand=True, anchor=N)

        #self.PhysicsFrame = LabelFrame(self.NotebookOnglet)
        #self.PhysicsFrame.pack(fill=tkinter.BOTH, expand=True, anchor=N)

        self.Physics2DFrame = LabelFrame(self.NotebookOnglet)
        self.Physics2DFrame.pack(fill=tkinter.BOTH, expand=True, anchor=N)

        self.PlayerFrame = LabelFrame(self.NotebookOnglet)
        self.PlayerFrame.pack(fill=tkinter.BOTH, expand=True, anchor=N)

        self.PresetManagerFrame = LabelFrame(self.NotebookOnglet)
        #self.PresetManagerFrame.pack(fill=tkinter.BOTH, expand=True, anchor=N)

        self.QualityFrame = LabelFrame(self.NotebookOnglet)
        #self.QualityFrame.pack(fill=tkinter.BOTH, expand=True, anchor=N)

        self.ScriptExecutionOrderFrame = LabelFrame(self.NotebookOnglet)
        #self.ScriptExecutionOrderFrame.pack(fill=tkinter.BOTH, expand=True, anchor=N)

        self.TagsAndLayersFrame = LabelFrame(self.NotebookOnglet)
        #self.TagsAndLayersFrame.pack(fill=tkinter.BOTH, expand=True, anchor=N)

        self.TimeFrame = LabelFrame(self.NotebookOnglet)
        #self.TimeFrame.pack(fill=tkinter.BOTH, expand=True, anchor=N)


        #self.NotebookOnglet.add(self.EditorFrame, text='Editor')
        #self.NotebookOnglet.add(self.GraphicsFrame, text='Graphics')
        self.NotebookOnglet.add(self.Physics2DFrame, text='Physics 2D')
        self.NotebookOnglet.add(self.PlayerFrame, text='Player')
        #self.NotebookOnglet.add(self.PresetManagerFrame, text='Preset Manager')
        #self.NotebookOnglet.add(self.QualityFrame, text='Quality')
        #self.NotebookOnglet.add(self.ScriptExecutionOrderFrame, text='Script Execution Order')
        #self.NotebookOnglet.add(self.TagsAndLayersFrame, text='Tags and Layers')
        #self.NotebookOnglet.add(self.TimeFrame, text='Time')


        ##############- Editor -##############

        #############- Graphics -#############

        ############- Physics 2D -############
        Label(self.Physics2DFrame,text="Gravity").grid(row=0, column=0)
        self.GravityValue = Vector2Show(self.Physics2DFrame)
        self.GravityValue.grid(row=0, column=1)

        ##############- Player -##############
        Label(self.PlayerFrame, text="Auteur").grid(row=0, column=0)
        self.AuteurValue = StringVar()
        self.AuteurEntry = Entry(self.PlayerFrame,textvariable=self.AuteurValue)
        self.AuteurEntry.grid(row=0, column=1)

        Label(self.PlayerFrame, text="Nom du jeu").grid(row=1, column=0)
        self.ProductNameValue = StringVar()
        self.ProductNameEntry = Entry(self.PlayerFrame, textvariable=self.ProductNameValue)
        self.ProductNameEntry.grid(row=1, column=1)

        Label(self.PlayerFrame, text="Version du jeu").grid(row=2, column=0)
        self.VersionGameValue = DoubleVar()
        self.VersionGameEntry = Entry(self.PlayerFrame, textvariable=self.VersionGameValue)
        self.VersionGameEntry.grid(row=2, column=1)

        Label(self.PlayerFrame, text="Screen Size").grid(row=3, column=0)
        self.ScreenSizeValue = Vector2Show(self.PlayerFrame)
        self.ScreenSizeValue.grid(row=3, column=1)


        ##########- Preset Manager -##########

        ##############- Quality -#############

        ######- Script Execution Order -######

        #########- Tags and Layers -##########

        ###############- Time -###############


        ###############- END -################
        self.LoadValue()
        if OnlyLoad:
            self.SaveAllData()
            self.RootWindow.quit()
            self.RootWindow.destroy()
            self.RootWindow.update()

    def SaveAllData(self,*args):
        rf.save(self.pathFile, "Physics2D&Gravity", self.GravityValue.GetValue())
        rf.save(self.pathFile, "Player&Auteur", self.AuteurValue.get())
        rf.save(self.pathFile, "Player&ProductName", self.ProductNameValue.get())
        rf.save(self.pathFile, "Player&VersionGame", self.VersionGameValue.get())
        rf.save(self.pathFile, "Player&ScreenSize", self.ScreenSizeValue.GetValue())

    def LoadValue(self):
        temp = rf.found(self.pathFile,"Physics2D&Gravity")
        if temp == False:self.GravityValue.SetValue(0,0)
        else:
            temp = eval(temp)
            self.GravityValue.SetValue(temp[0],temp[1])

        temp = rf.found(self.pathFile, "Player&Auteur")
        if temp == False:self.AuteurValue.set("")
        else:self.AuteurValue.set(temp)

        temp = rf.found(self.pathFile, "Player&ProductName")
        if temp == False:self.ProductNameValue.set("")
        else:self.ProductNameValue.set(temp)

        temp = rf.found(self.pathFile, "Player&VersionGame")
        if temp == False:self.VersionGameValue.set(0)
        else:self.VersionGameValue.set(temp)

        temp = rf.found(self.pathFile, "Player&ScreenSize")
        if temp == False:
            self.ScreenSizeValue.SetValue(127, 63)
        else:
            temp = eval(temp)
            self.ScreenSizeValue.SetValue(temp[0], temp[1])