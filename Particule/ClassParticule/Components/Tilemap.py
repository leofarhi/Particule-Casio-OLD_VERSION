from Particule import *
from ClassParticule.Component import Component
from ClassParticule.Texture import Texture
from ClassParticule.Vector2 import Vector2
import numpy
import PIL
import SystemExt.ImageFunctions as ImageFunctions
from PIL import ImageFilter, ImageOps
from ClassParticule.Components.BoxCollider2D import BoxCollider2D
class Tilemap(Component):
    def __init__(self,gameObject,**kwargs):
        Component.__init__(self,gameObject,__name__.split(".")[-1],**kwargs)
        #Repertoir de l'image
        #repImg = "C:/Users/leofa/OneDrive/Documents/PycharmProjects/Particule/lib/logo.png"

        self.canvas = self.Particule.Scene.surface
        self.IsHide = True
        self.gameObject.isStatic = True

        self._lastZoom=1

        self.SizeTilemap=Vector2(10,10)
        self.SizeCase = Vector2(16, 16)
        self.Textures = [self.Particule.FolderWindow.TextureVide]
        self.DataTilemap=[]
        self.TypeVariables.update({"SizeTilemap": {"Type": Vector2},
                                   "SizeCase": {"Type": Vector2},
                                   "Textures": {"Type":list,"LstValueType":{"Type":Texture},"LstType":"Array"},
                                   })
        self._lastRepImgs = str([o.path for o in self.Textures])
        self.Meshs=[]
        self.Imgs=[]
        self.grille = []
        self.LoadMap()
        self.PaintPen = 1




        self.AttributVisible = ["SizeTilemap","SizeCase"]

    def SetPen(self,index,*args):
        self.PaintPen =index
    def UpdatePalette(self,*args):
        self.FramePaletteButton.destroy()
        self.RefeshPalette()
    def RefeshPalette(self):
        self.FramePaletteButton = Frame(self.FramePalette)
        self.FramePaletteButton.pack(fill=tkinter.BOTH, expand=True)
        Button(self.FramePaletteButton, text="Mise à Jour de la Palette",command=self.UpdatePalette).pack(side=TOP,padx=10,pady=10)
        Button(self.FramePaletteButton, text="TextureVide",command=partial(self.SetPen,0)).pack(side=TOP)
        for ind,photo in enumerate(self.Textures):
            if (ind==0):continue
            Button(self.FramePaletteButton, image=photo.Img,command=partial(self.SetPen,ind)).pack(side=TOP)
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

        self.FrameSettingsCollider = Frame(self.FrameSettings)
        self.FrameSettingsCollider.pack(fill=X, expand=True)

        self.FrameSettingsTypeGUI = Frame(self.FrameSettings)
        self.FrameSettingsTypeGUI.pack(fill=BOTH, expand=True)

        self.ButtonCollision = Button(self.FrameSettingsCollider,text="Add/Update Collider",command=self.AddCollider)
        self.ButtonCollision.grid(row=0, column=0)

        self.ButtonCollision = Button(self.FrameSettingsCollider, text="Remove Collider", command=self.RemoveCollider)
        self.ButtonCollision.grid(row=0, column=1)

        self.FrameSettings.Particule = self.Particule
        self.FrameSettingsTypeGUI.Particule = self.Particule
        self.FramePalette.Particule = self.Particule

        self.RefeshPalette()

        # self.myFrame.pack(fill=tkinter.BOTH, expand=True)
        self.AddContextMenu()
        one = False
        count = 0
        for i in self.GetAttribut():
            if i[0] in ["Textures"]+self.AttributVisible:
                # print(i[0],getattr(self,i[0]))
                one = True
                tempUI = TypeGUI(self.FrameSettingsTypeGUI, self, i[0],self.TypeVariables[i[0]])
                tempUI.grid(row=count, column=0, sticky='EWNS')
                self._valueGUI.append(tempUI)
                count += 1
                # Button(self.myFrame,text=self.gameObject.name+i[0]+" : "+str(i[1].get())).pack()
        if not one:
            Label(self.FrameSettingsTypeGUI, text="Pas de paramètres").pack()

    def RemoveCollider(self):
        i=0
        while i <len(self.gameObject.ListOfComponent):
            if type(self.gameObject.ListOfComponent[i]) == BoxCollider2D:
                self.gameObject.ListOfComponent[i].Destroy()
            else:
                i+=1

    def AddCollider(self):
        self.RemoveCollider()
        DataTemp = eval(str(self.DataTilemap))
        for y,i in enumerate(DataTemp):
            for x,o in enumerate(i):
                if ((DataTemp[y])[x]!=0):
                    temp = self.gameObject.AddComponent(BoxCollider2D)

                    if x+1< len(i) and (DataTemp[y])[x+1]!=0:
                        j=0
                        while x+j< len(i) and (DataTemp[y])[x+j]!=0:
                            (DataTemp[y])[x + j]=0
                            j+=1
                        H=1
                        while y+H< len(DataTemp):
                            somme=True
                            for k in range(j):
                                somme=((DataTemp[y+H])[x + k]!=0) and somme
                            if not somme:
                                break
                            H+=1
                        for m in range(H):
                            for k in range(j):
                                (DataTemp[y + m])[x + k]=0
                        temp.Center = Vector2((self.SizeCase.x * x) + ((self.SizeCase.x* j) / 2),
                                              (self.SizeCase.y * y) + (self.SizeCase.y*H / 2))
                        temp.Size = Vector2(self.SizeCase.x*j,self.SizeCase.y*H)
                    elif y+1< len(DataTemp) and (DataTemp[y+1])[x]!=0:
                        j = 0
                        while y + j < len(DataTemp) and (DataTemp[y+j])[x] != 0:
                            (DataTemp[y+j])[x] = 0
                            j += 1
                        temp.Center = Vector2((self.SizeCase.x * x) + (self.SizeCase.x / 2),
                                              (self.SizeCase.y * y) + ((self.SizeCase.y* j) / 2))
                        temp.Size = Vector2(self.SizeCase.x, self.SizeCase.y* j)
                    else:
                        (DataTemp[y])[x] = 0
                        temp.Center = Vector2((self.SizeCase.x * x) + (self.SizeCase.x / 2),
                                              (self.SizeCase.y * y) + (self.SizeCase.y / 2))
                        temp.Size = self.SizeCase+Vector2()



    def Clic(self, event):
        if self.myFrame!=None:
            if self.myFrame.winfo_ismapped()==1:
                w = event.widget
                x = w.canvasx(event.x)
                y = w.canvasy(event.y)
                item = w.find_closest(x, y)
                for y2,i in enumerate(self.Meshs):
                    for x2,o in enumerate(i):
                        if item[0]==o:
                            (self.DataTilemap[y2])[x2] = self.PaintPen
                            self.LoadMap()
                            return

    def LoadMap(self):
        self.Imgs = []
        for i in self.Meshs:
            for o in i:
                self.canvas.delete(o)
        for i in self.grille:
            self.canvas.delete(i)
        self.Meshs=[]
        for y,i in enumerate(self.DataTilemap):
            tempM=[]
            for x, o in enumerate(i):
                if not o<len(self.Textures):
                    o=0
                if o==0:
                    img = Image.new('RGB', [self.SizeCase.x,self.SizeCase.y], (255,255,255))
                    color = "black"
                    # top, right, bottom, left
                    border = (1, 1, 1, 1)
                    img = ImageOps.expand(img, border=border, fill=color)
                else:
                    try:
                        img = self.Textures[o].ImgStd
                    except:
                        self.Textures[o] = self.Particule.FolderWindow.TextureVide
                        img = self.Textures[o].ImgStd
                img = img.resize(
                    (int(img.width * self._lastZoom), int(img.height * self._lastZoom)),
                    resample=Image.NEAREST)
                img = ImageFunctions.WhiteToTransparent(img)
                img = ImageTk.PhotoImage(img)
                self.Imgs.append(img)
                ImgCan = self.canvas.create_image(x*self.SizeCase.x, y*self.SizeCase.y, anchor=tkinter.NW, image=self.Imgs[-1])
                self.canvas.tag_bind(ImgCan, '<Button-1>', self.Clic)
                for i in range(100):
                    self.canvas.tag_lower(ImgCan)
                #gr = self.canvas.create_rectangle(x*self.SizeCase.x, y*self.SizeCase.y, self.SizeCase.x, self.SizeCase.y, fill="")
                #self.grille.append(gr)
                tempM.append(ImgCan)
            self.Meshs.append(tempM)
        if self.IsHide:
            self.WhenComponentIsHideSignal()
    def UpdateLst(self):
        self.SizeTilemap.y = abs(self.SizeTilemap.y)
        self.SizeTilemap.x = abs(self.SizeTilemap.x)
        modif = False
        if len(self.DataTilemap)>self.SizeTilemap.y:
            for i in range(len(self.DataTilemap)-self.SizeTilemap.y):
                del self.DataTilemap[-1]
            modif = True
        elif len(self.DataTilemap)<self.SizeTilemap.y:
            for i in range(len(self.DataTilemap),self.SizeTilemap.y):
                self.DataTilemap.append([0 for i in range(self.SizeTilemap.x)])
            modif = True
        if len(self.DataTilemap)>0:
            if len(self.DataTilemap[0]) > self.SizeTilemap.x:
                for o in range(len(self.DataTilemap)):
                    for i in range(len(self.DataTilemap[o]) - self.SizeTilemap.x):
                        del (self.DataTilemap[o])[-1]
                modif = True
            elif len(self.DataTilemap[0]) < self.SizeTilemap.x:
                for o in range(len(self.DataTilemap)):
                    for i in range(len(self.DataTilemap[o]), self.SizeTilemap.x):
                        self.DataTilemap[o].append(0)
                modif = True
        return modif

    def WhenComponentIsShowSignal(self):
        self.IsHide = False
        for i in self.Meshs:
            for o in i:
                self.canvas.itemconfig(o, state='normal')
                self.Particule.Scene.surface.tag_raise(o)

    def WhenComponentIsHideSignal(self):
        self.IsHide=True
        for y, i in enumerate(self.DataTilemap):
            for x, o in enumerate(i):
                if o == 0:
                    self.canvas.itemconfig((self.Meshs[y])[x], state='hidden')

    def AddScriptAfterInitCasio(self):
        lst = []
        for i in self.DataTilemap:
            for o in i:
                lst.append(o)
        code = "static int "+str(self.ID)+"_TilemapDatas[] = "+str(lst).replace("[","{").replace("]","}")+";\n"
        code += str(self.ID)+"->Datas = "+str(self.ID)+"_TilemapDatas;\n"
        code += str(self.ID) + "->images = new Texture * ["+str(len(self.Textures))+"];\n"
        for ind,i in enumerate(self.Textures):
            path = os.path.basename(i.path)
            path = os.path.splitext(path)[0]
            if (i.path == "Library/lib/vide.png"):
                valT = "new Texture()"
            else:
                valT = "Texture_" + path
            code += str(self.ID) + "->images["+str(ind)+"] = "+valT+";\n"
        return code

    def UpdateOnGUI(self):
        if len(self.Textures)==0:
            self.Textures=[self.Particule.FolderWindow.TextureVide]
        else:
            self.Textures[0]=self.Particule.FolderWindow.TextureVide
        modif = self.UpdateLst()
        pathT=str([o.path for o in self.Textures])
        if self._lastRepImgs != pathT or self._lastZoom != self.Particule.Scene.zoom or modif:
            self._lastRepImgs = pathT
            self._lastZoom = self.Particule.Scene.zoom
            self.LoadMap()
        z = self.Particule.Scene.zoom
        x,y = self.gameObject.transform.position.get()
        index = 0
        for y2,i in enumerate(self.Meshs):
            for x2,o in enumerate(i):
                self.canvas.coords(o,((x+x2*self.SizeCase.x)-self.Particule.Scene.x)*z,((y+y2*self.SizeCase.y)+self.Particule.Scene.y)*z)
                #self.canvas.coords(self.grille[index], int(((x+x2*self.SizeCase.x)-self.Particule.Scene.x)*z),int(((y+y2*self.SizeCase.y)+self.Particule.Scene.y)*z),
                #                int(((x+(x2+1)*self.SizeCase.x)-self.Particule.Scene.x)*z),int(((y+(y2+1)*self.SizeCase.y)+self.Particule.Scene.y)*z)*z)

                index+=1


    def Destroy(self):
        for i in self.Meshs:
            for o in i:
                self.canvas.delete(o)
        for i in self.grille:
            self.canvas.delete(i)
        Component.Destroy(self)

    def SaveDataDict(self):
        data = Component.SaveDataDict(self)
        data.update({
            "SizeTilemap":self.SizeTilemap.get(),
            "SizeCase": self.SizeCase.get(),
            "DataTilemap":self.DataTilemap,
            "Textures":[i.ID for i in self.Textures]
        })
        return data

    def LoadDataDict(self,data,component,dataCompo,dicoGameObject,dicoComponent):
        Component.LoadDataDict(self,data,component,dataCompo,dicoGameObject,dicoComponent)
        #self.texture = Texture(self.Particule,Path=dataCompo["repImg"],name=os.path.basename(dataCompo["repImg"]))
        self.Textures = [self.Particule.GetTextureUUID(o) for o in dataCompo["Textures"]]
        self.SizeTilemap = Vector2.set(Vector2(), dataCompo["SizeTilemap"])
        self.SizeCase = Vector2.set(Vector2(), dataCompo["SizeCase"])
        self.DataTilemap = dataCompo["DataTilemap"]
        self.LoadMap()

