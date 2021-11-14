from ClassSystem.EditorWindow import EditorWindow
from Particule import *
class ProjectSettingsWindow(EditorWindow):
    def __init__(self, RootWindow):
        EditorWindow.__init__(self, RootWindow,
                              ExternalWindow={"name":"Project Settings"},
                              Resize=False, ScrollbarShow=False)
        self.pack(fill=tkinter.BOTH, expand=True)
        style = ttk.Style(self)
        style.configure('lefttab.TNotebook', tabposition='wn')

        self.NotebookOnglet = ttk.Notebook(self, style='lefttab.TNotebook')
        self.NotebookOnglet.pack(fill=BOTH, expand=True)

        self.EditorFrame = LabelFrame(self.NotebookOnglet)
        self.EditorFrame.pack(fill=tkinter.BOTH, expand=True, anchor=N)

        self.GraphicsFrame = LabelFrame(self.NotebookOnglet)
        self.GraphicsFrame.pack(fill=tkinter.BOTH, expand=True, anchor=N)

        #self.PhysicsFrame = LabelFrame(self.NotebookOnglet)
        #self.PhysicsFrame.pack(fill=tkinter.BOTH, expand=True, anchor=N)

        self.Physics2DFrame = LabelFrame(self.NotebookOnglet)
        self.Physics2DFrame.pack(fill=tkinter.BOTH, expand=True, anchor=N)

        self.PlayerFrame = LabelFrame(self.NotebookOnglet)
        self.PlayerFrame.pack(fill=tkinter.BOTH, expand=True, anchor=N)

        self.PresetManagerFrame = LabelFrame(self.NotebookOnglet)
        self.PresetManagerFrame.pack(fill=tkinter.BOTH, expand=True, anchor=N)

        self.QualityFrame = LabelFrame(self.NotebookOnglet)
        self.QualityFrame.pack(fill=tkinter.BOTH, expand=True, anchor=N)

        self.ScriptExecutionOrderFrame = LabelFrame(self.NotebookOnglet)
        self.ScriptExecutionOrderFrame.pack(fill=tkinter.BOTH, expand=True, anchor=N)

        self.TagsAndLayersFrame = LabelFrame(self.NotebookOnglet)
        self.TagsAndLayersFrame.pack(fill=tkinter.BOTH, expand=True, anchor=N)

        self.TimeFrame = LabelFrame(self.NotebookOnglet)
        self.TimeFrame.pack(fill=tkinter.BOTH, expand=True, anchor=N)


        self.NotebookOnglet.add(self.EditorFrame, text='Editor')
        self.NotebookOnglet.add(self.GraphicsFrame, text='Graphics')
        self.NotebookOnglet.add(self.Physics2DFrame, text='Physics 2D')
        self.NotebookOnglet.add(self.PlayerFrame, text='Player')
        self.NotebookOnglet.add(self.PresetManagerFrame, text='Preset Manager')
        self.NotebookOnglet.add(self.QualityFrame, text='Quality')
        self.NotebookOnglet.add(self.ScriptExecutionOrderFrame, text='Script Execution Order')
        self.NotebookOnglet.add(self.TagsAndLayersFrame, text='Tags and Layers')
        self.NotebookOnglet.add(self.TimeFrame, text='Time')


