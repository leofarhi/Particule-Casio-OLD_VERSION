from Particule import *
from ClassSystem.EditorWindow import EditorWindow
from ClassParticule.AddComponentFrame import AddComponentFrame

class WindowImage(EditorWindow):
    def __init__(self,RootWindow):
        EditorWindow.__init__(self,RootWindow,Resize=True,ScrollbarShow=False)
        self.mainFrame = Frame(self)
        self.mainFrame.pack(fill=tkinter.BOTH, expand=True)

        self.FrameComboboxTextureType = Frame(self.mainFrame)
        self.label_TextureType = Label(self.FrameComboboxTextureType, text="Texture Type: ")
        self.label_TextureType.grid(row=0, column=0)
        self.CurSelectTextureType = StringVar()
        self.LstAllSelectTextureType = ttk.Combobox(self.FrameComboboxTextureType, textvariable=self.CurSelectTextureType)
        self.LstAllSelectTextureType.grid(row=0, column=1)
        self.LstAllSelectTextureType["value"]=["Default","Sprite (2D and UI)","Cursor"]
        #self.LstAllSelectTextureType.bind('<<ComboboxSelected>>', self.updateDataGameObj)
        self.FrameComboboxTextureType.grid(row=0, column=0)

        self.varAlpha = IntVar()
        self.varAlpha.set(1)
        # self.varActive.trace("w", self.updateDataGameObj)
        self.CheckAlpha = Checkbutton(self.mainFrame,text="Alpha", variable=self.varAlpha, offvalue=0, onvalue=1)
        self.CheckAlpha.grid(row=1, column=0)

        self.boutonTransformeImg = Button(self.mainFrame,text= "Transformer l'image",command=self.CreateImage)
        self.boutonTransformeImg.grid(row=2,column=0, sticky='EWNS',padx=10,pady=10)

    def CreateImage(self,*args):
        if len(self.Particule.FolderWindow.selected_file_indices) > 0:
            if os.path.splitext(self.Particule.FolderWindow.detailed_file_list[list(self.Particule.FolderWindow.selected_file_indices)[0]])[1] in [".png", ".jpg", ".bmp"]:
                path = self.Particule.FolderWindow.detailed_file_list[list(self.Particule.FolderWindow.selected_file_indices)[0]]
                print(path)
                guid = rf.found(path+".meta","guid")
                TransformImage.ImportImage(path,self.Particule.FolderProject + "/Library/ImagesBmpCache/" +guid+'.bmp')