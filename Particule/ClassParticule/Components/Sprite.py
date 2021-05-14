from Particule import *
from ClassParticule.Component import Component
from ClassParticule.Texture import Texture
from PIL import ImageFilter
class Sprite(Component):
    def __init__(self,gameObject,texture=None,**kwargs):
        Component.__init__(self,gameObject,__name__.split(".")[-1],**kwargs)
        #Repertoir de l'image
        #repImg = "C:/Users/leofa/OneDrive/Documents/PycharmProjects/Particule/lib/logo.png"
        if texture==None:
            self.texture = Texture(self.Particule,name="None")
        else:
            self.texture = texture
        self._lastRepImg = self.texture.path
        #self._lastRepImg = texture.path
        self._lastZoom=1

        self.Img = self.texture.Img
        self.Mesh = self.Particule.Scene.surface.create_image(0, 0, anchor=tkinter.NW, image=self.Img)
        self.ReloadImg()

        self.Particule.Scene.surface.tag_bind(self.Mesh,'<Button-1>', self.Clic)  # evevement clic gauche (press)
        self.Particule.Scene.surface.tag_bind(self.Mesh,'<B1-Motion>', self.Drag)
        #self.Particule.Scene.surface.tag_bind(self.Mesh,'<ButtonRelease-1>', self.Drop)


        self.AttributVisible = ["texture"]
    def Clic(self, event):
        self.Particule.Hierarchy.t.focus(str(self.gameObject.ID))
        self.Particule.Hierarchy.t.selection_set(str(self.gameObject.ID))
        self.Particule.Hierarchy.SetItemSelect()
    def Drag(self, event):
        #event.x, event.y
        z = self.Particule.Scene.zoom
        self.gameObject.transform.position.set(( (event.x//z)+self.Particule.Scene.x, (event.y//z)-self.Particule.Scene.y))
        self.Particule.Inspector.UpdateItemSelected()

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

    def UpdateOnGUI(self):
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
        })
        return data

    def LoadDataDict(self,data,component,dataCompo,dicoGameObject,dicoComponent):
        Component.LoadDataDict(self,data,component,dataCompo,dicoGameObject,dicoComponent)
        self.texture = Texture(self.Particule,Path=dataCompo["repImg"],name=os.path.basename(dataCompo["repImg"]))
        self.ReloadImg()
