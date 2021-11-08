from Particule import *
from ClassParticule.Component import Component
from ClassParticule.Texture import Texture
from ClassParticule.Vector2 import Vector2
from PIL import ImageFilter
class Tilemap(Component):
    def __init__(self,gameObject,texture=None,**kwargs):
        Component.__init__(self,gameObject,__name__.split(".")[-1],**kwargs)
        #Repertoir de l'image
        #repImg = "C:/Users/leofa/OneDrive/Documents/PycharmProjects/Particule/lib/logo.png"
        if texture==None:
            self.texture = self.Particule.FolderWindow.TextureVide
        else:
            self.texture = texture


        self._lastRepImg = self.texture.path
        #self._lastRepImg = texture.path
        self._lastZoom=1

        self.SizeTilemap=Vector2(10,10)
        self.SizeCase = Vector2(16, 16)
        self.Textures = [Texture(self.Particule,name="None")]
        self.DataTilemap=[]
        self.TypeVariables.update({"texture": {"Type": Texture},
                                   "SizeTilemap": {"Type": Vector2},
                                   "SizeCase": {"Type": Vector2},
                                   "Textures": {"Type":list,"LstValueType":{"Type":Texture},"LstType":"Array"},
                                   })

        self.Img = self.texture.Img
        self.Mesh = self.Particule.Scene.surface.create_image(0, 0, anchor=tkinter.NW, image=self.Img)
        self.ReloadImg()

        self.Particule.Scene.surface.tag_bind(self.Mesh,'<Button-1>', self.Clic)  # evevement clic gauche (press)
        #self.Particule.Scene.surface.tag_bind(self.Mesh,'<ButtonRelease-1>', self.Drop)


        self.AttributVisible = ["texture","SizeTilemap","SizeCase"]
    def RefreshGUI(self):
        if self.myFrame != None:
            self.myFrame.destroy()
        self.myFrame = LabelFrame(self.Particule.Inspector.mainComponentsFrame, text=self.name)
        self.myFrame.Particule = self.Particule
        self.NotebookTilemap = ttk.Notebook(self.myFrame)
        self.NotebookTilemap.pack(fill=BOTH, expand=True)
        self.FrameSettings = ttk.Frame(self.NotebookTilemap)
        self.FramePalette = ttk.Frame(self.NotebookTilemap)

        self.FrameSettings.pack(fill=tkinter.BOTH, expand=True)
        self.FramePalette.pack(fill=tkinter.BOTH, expand=True)

        self.NotebookTilemap.add(self.FrameSettings, text='Settings')
        self.NotebookTilemap.add(self.FramePalette, text='Palette')

        self.FrameSettings.Particule = self.Particule
        self.FramePalette.Particule = self.Particule
        # self.myFrame.pack(fill=tkinter.BOTH, expand=True)
        self.AddContextMenu()
        one = False
        count = 0
        for i in self.GetAttribut():
            if i[0] in self.AttributVisible:
                # print(i[0],getattr(self,i[0]))
                one = True
                tempUI = TypeGUI(self.FrameSettings, self, i[0])
                tempUI.grid(row=count, column=0, sticky='EWNS')
                self._valueGUI.append(tempUI)
                count += 1
                # Button(self.myFrame,text=self.gameObject.name+i[0]+" : "+str(i[1].get())).pack()
        if not one:
            Label(self.FrameSettings, text="Pas de paramètres").pack()


    def Clic(self, event):
        self.Particule.Hierarchy.t.focus(str(self.gameObject.ID))
        self.Particule.Hierarchy.t.selection_set(str(self.gameObject.ID))
        self.Particule.Hierarchy.SetItemSelect()

    def ReloadImg(self):
        try:
            self.repImg = self.texture.path.replace(self.Particule.FolderProject,"")
            self.Img = ImageTk.Image.open(self.Particule.FolderProject+"/"+self.repImg)
            self.width = self.Img.width
            self.height = self.Img.height
            self.Img = self.Img.resize((int(self.Img.width*self._lastZoom), int(self.Img.height*self._lastZoom)),resample=Image.NEAREST)
            self.Img = ImageTk.PhotoImage(self.Img)
        except:
            self.Img = Image.open("lib/vide.png")
            self.Img = ImageTk.PhotoImage(self.Img)
            self.width = self.Img.width()
            self.height = self.Img.height()
        self.Particule.Scene.surface.itemconfig(self.Mesh,image = self.Img)

    def UpdateLst(self):
        self.SizeTilemap.y = abs(self.SizeTilemap.y)
        self.SizeTilemap.x = abs(self.SizeTilemap.x)
        if len(self.DataTilemap)>self.SizeTilemap.y:
            for i in range(len(self.DataTilemap)-self.SizeTilemap.y):
                del self.DataTilemap[-1]
        elif len(self.DataTilemap)<self.SizeTilemap.y:
            for i in range(len(self.DataTilemap),self.SizeTilemap.y):
                self.DataTilemap.append([0 for i in range(self.SizeTilemap.x)])
        if len(self.DataTilemap)>0:
            if len(self.DataTilemap[0]) > self.SizeTilemap.x:
                for o in range(len(self.DataTilemap)):
                    for i in range(len(self.DataTilemap[o]) - self.SizeTilemap.x):
                        del (self.DataTilemap[o])[-1]
            elif len(self.DataTilemap[0]) < self.SizeTilemap.x:
                for o in range(len(self.DataTilemap)):
                    for i in range(len(self.DataTilemap[o]), self.SizeTilemap.x):
                        self.DataTilemap[o].append(0)


    def AddScriptAfterInitCasio(self):
        lst = []
        for i in self.DataTilemap:
            for o in i:
                lst.append(o)
        code = "static int "+str(self.ID)+"_TilemapDatas[] = "+str(lst).replace("[","{").replace("]","}")+";\n"
        code += str(self.ID)+"->Datas = "+str(self.ID)+"_TilemapDatas;\n"
        code += str(self.ID) + "->images = new Texture * ["+str(len(self.Textures))+"];\n"
        for ind,i in enumerate(self.Textures):
            code += str(self.ID) + "->images["+str(ind)+"] = !!!;\n"
            raise Exception("à coder")
        return code

    def UpdateOnGUI(self):
        self.UpdateLst()
        if self._lastRepImg != self.texture.path or self._lastZoom != self.Particule.Scene.zoom:
            self._lastRepImg = self.texture.path
            self._lastZoom = self.Particule.Scene.zoom
            self.ReloadImg()
        z = self.Particule.Scene.zoom
        x,y = self.gameObject.transform.position.get()
        self.Particule.Scene.surface.coords(self.Mesh,(x-self.Particule.Scene.x)*z,(y+self.Particule.Scene.y)*z)


    def Destroy(self):
        self.Particule.Scene.surface.delete(self.Mesh)
        Component.Destroy(self)

    def SaveDataDict(self):
        data = Component.SaveDataDict(self)
        data.update({
            "repImg":self.texture.path,
            "SizeTilemap":self.SizeTilemap.get(),
            "SizeCase": self.SizeCase.get(),
            "DataTilemap":self.DataTilemap
        })
        return data

    def LoadDataDict(self,data,component,dataCompo,dicoGameObject,dicoComponent):
        Component.LoadDataDict(self,data,component,dataCompo,dicoGameObject,dicoComponent)
        self.texture = Texture(self.Particule,Path=dataCompo["repImg"],name=os.path.basename(dataCompo["repImg"]))
        self.ReloadImg()
        self.SizeTilemap = Vector2.set(Vector2(), dataCompo["SizeTilemap"])
        self.SizeCase = Vector2.set(Vector2(), dataCompo["SizeCase"])
        self.DataTilemap = dataCompo["DataTilemap"]
