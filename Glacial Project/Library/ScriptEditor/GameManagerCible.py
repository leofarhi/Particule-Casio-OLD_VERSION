from Particule import *
from ClassParticule.Component import Component
from ClassParticule.Vector2 import Vector2
from ClassParticule.Texture import Texture
from ClassParticule.Texture import Texture
import ClassParticule

class GameManagerCible(Component):
    def __init__(self,gameObject,**kwargs):
        Component.__init__(self,gameObject,__name__.split(".")[-1],**kwargs)
        self.points= 0
        self.TypeVariables["points"] = {"Type":int}
        self.StrPoints= ""
        self.TypeVariables["StrPoints"] = {"Type":str}
        self.M1= self.texture = self.Particule.FolderWindow.TextureVide
        self.TypeVariables["M1"] = {"Type":Texture}
        self.M2= self.texture = self.Particule.FolderWindow.TextureVide
        self.TypeVariables["M2"] = {"Type":Texture}
        self.V1= self.texture = self.Particule.FolderWindow.TextureVide
        self.TypeVariables["V1"] = {"Type":Texture}
        self.V2= self.texture = self.Particule.FolderWindow.TextureVide
        self.TypeVariables["V2"] = {"Type":Texture}
        

        self.AttributVisible=["points","M1","M2","V1","V2",]

    def SaveDataDict(self):
        data = Component.SaveDataDict(self)
        
        data.update({
            "points":self.points,"M1":self.M1.ID,"M2":self.M2.ID,"V1":self.V1.ID,"V2":self.V2.ID,
        })
        return data

    def LoadDataDict(self,data,component,dataCompo,dicoGameObject,dicoComponent):
        Component.LoadDataDict(self,data,component,dataCompo,dicoGameObject,dicoComponent)
        self.points= dataCompo["points"]
        self.M1= self.Particule.GetTextureUUID(dataCompo["M1"])
        self.M2= self.Particule.GetTextureUUID(dataCompo["M2"])
        self.V1= self.Particule.GetTextureUUID(dataCompo["V1"])
        self.V2= self.Particule.GetTextureUUID(dataCompo["V2"])
        
