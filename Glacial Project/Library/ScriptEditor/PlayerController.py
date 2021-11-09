from Particule import *
from ClassParticule.Component import Component
from ClassParticule.Vector2 import Vector2
from ClassParticule.Texture import Texture
from ClassParticule.Texture import Texture
import ClassParticule

class PlayerController(Component):
    def __init__(self,gameObject,**kwargs):
        Component.__init__(self,gameObject,__name__.split(".")[-1],**kwargs)
        self.Bas1= self.texture = self.Particule.FolderWindow.TextureVide
        self.TypeVariables["Bas1"] = {"Type":Texture}
        self.Bas2= self.texture = self.Particule.FolderWindow.TextureVide
        self.TypeVariables["Bas2"] = {"Type":Texture}
        self.Bas3= self.texture = self.Particule.FolderWindow.TextureVide
        self.TypeVariables["Bas3"] = {"Type":Texture}
        self.Haut1= self.texture = self.Particule.FolderWindow.TextureVide
        self.TypeVariables["Haut1"] = {"Type":Texture}
        self.Haut2= self.texture = self.Particule.FolderWindow.TextureVide
        self.TypeVariables["Haut2"] = {"Type":Texture}
        self.Haut3= self.texture = self.Particule.FolderWindow.TextureVide
        self.TypeVariables["Haut3"] = {"Type":Texture}
        self.Droite1= self.texture = self.Particule.FolderWindow.TextureVide
        self.TypeVariables["Droite1"] = {"Type":Texture}
        self.Droite2= self.texture = self.Particule.FolderWindow.TextureVide
        self.TypeVariables["Droite2"] = {"Type":Texture}
        self.Droite3= self.texture = self.Particule.FolderWindow.TextureVide
        self.TypeVariables["Droite3"] = {"Type":Texture}
        self.Gauche1= self.texture = self.Particule.FolderWindow.TextureVide
        self.TypeVariables["Gauche1"] = {"Type":Texture}
        self.Gauche2= self.texture = self.Particule.FolderWindow.TextureVide
        self.TypeVariables["Gauche2"] = {"Type":Texture}
        self.Gauche3= self.texture = self.Particule.FolderWindow.TextureVide
        self.TypeVariables["Gauche3"] = {"Type":Texture}
        self.Frame= 0
        self.TypeVariables["Frame"] = {"Type":int}
        self.Vitesse= 0
        self.TypeVariables["Vitesse"] = {"Type":int}
        

        self.AttributVisible=["Bas1","Bas2","Bas3","Haut1","Haut2","Haut3","Droite1","Droite2","Droite3","Gauche1","Gauche2","Gauche3","Vitesse",]

    def SaveDataDict(self):
        data = Component.SaveDataDict(self)
        
        data.update({
            "Bas1":self.Bas1.ID,"Bas2":self.Bas2.ID,"Bas3":self.Bas3.ID,"Haut1":self.Haut1.ID,"Haut2":self.Haut2.ID,"Haut3":self.Haut3.ID,"Droite1":self.Droite1.ID,"Droite2":self.Droite2.ID,"Droite3":self.Droite3.ID,"Gauche1":self.Gauche1.ID,"Gauche2":self.Gauche2.ID,"Gauche3":self.Gauche3.ID,"Vitesse":self.Vitesse,
        })
        return data

    def LoadDataDict(self,data,component,dataCompo,dicoGameObject,dicoComponent):
        Component.LoadDataDict(self,data,component,dataCompo,dicoGameObject,dicoComponent)
        self.Bas1= self.Particule.GetTextureUUID(dataCompo["Bas1"])
        self.Bas2= self.Particule.GetTextureUUID(dataCompo["Bas2"])
        self.Bas3= self.Particule.GetTextureUUID(dataCompo["Bas3"])
        self.Haut1= self.Particule.GetTextureUUID(dataCompo["Haut1"])
        self.Haut2= self.Particule.GetTextureUUID(dataCompo["Haut2"])
        self.Haut3= self.Particule.GetTextureUUID(dataCompo["Haut3"])
        self.Droite1= self.Particule.GetTextureUUID(dataCompo["Droite1"])
        self.Droite2= self.Particule.GetTextureUUID(dataCompo["Droite2"])
        self.Droite3= self.Particule.GetTextureUUID(dataCompo["Droite3"])
        self.Gauche1= self.Particule.GetTextureUUID(dataCompo["Gauche1"])
        self.Gauche2= self.Particule.GetTextureUUID(dataCompo["Gauche2"])
        self.Gauche3= self.Particule.GetTextureUUID(dataCompo["Gauche3"])
        self.Vitesse= dataCompo["Vitesse"]
        
