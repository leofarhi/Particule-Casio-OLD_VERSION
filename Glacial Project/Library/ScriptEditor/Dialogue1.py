from Particule import *
from ClassParticule.Component import Component
from ClassParticule.Vector2 import Vector2
from ClassParticule.Texture import Texture
from ClassParticule.Texture import Texture
import ClassParticule

class Dialogue1(Component):
    def __init__(self,gameObject,**kwargs):
        Component.__init__(self,gameObject,__name__.split(".")[-1],**kwargs)
        self.MySprite= None
        self.TypeVariables["MySprite"] = {"Type":Sprite}
        self.longueur= 0
        self.TypeVariables["longueur"] = {"Type":int}
        self.loadD= 0
        self.TypeVariables["loadD"] = {"Type":int}
        self.NextScene= 0
        self.TypeVariables["NextScene"] = {"Type":int}
        self.TextureV= self.texture = self.Particule.FolderWindow.TextureVide
        self.TypeVariables["TextureV"] = {"Type":Texture}
        self.Snowman= self.texture = self.Particule.FolderWindow.TextureVide
        self.TypeVariables["Snowman"] = {"Type":Texture}
        self.Jessy= self.texture = self.Particule.FolderWindow.TextureVide
        self.TypeVariables["Jessy"] = {"Type":Texture}
        self.Petra= self.texture = self.Particule.FolderWindow.TextureVide
        self.TypeVariables["Petra"] = {"Type":Texture}
        

        self.AttributVisible=["loadD","NextScene","TextureV","Snowman","Jessy","Petra",]

    def SaveDataDict(self):
        data = Component.SaveDataDict(self)
        
        data.update({
            "loadD":self.loadD,"NextScene":self.NextScene,"TextureV":self.TextureV.ID,"Snowman":self.Snowman.ID,"Jessy":self.Jessy.ID,"Petra":self.Petra.ID,
        })
        return data

    def LoadDataDict(self,data,component,dataCompo,dicoGameObject,dicoComponent):
        Component.LoadDataDict(self,data,component,dataCompo,dicoGameObject,dicoComponent)
        self.loadD= dataCompo["loadD"]
        self.NextScene= dataCompo["NextScene"]
        self.TextureV= self.Particule.GetTextureUUID(dataCompo["TextureV"])
        self.Snowman= self.Particule.GetTextureUUID(dataCompo["Snowman"])
        self.Jessy= self.Particule.GetTextureUUID(dataCompo["Jessy"])
        self.Petra= self.Particule.GetTextureUUID(dataCompo["Petra"])
        
