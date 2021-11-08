from Particule import *
from ClassParticule.Component import Component
from ClassParticule.Vector2 import Vector2
from ClassParticule.Texture import Texture
from ClassParticule.Texture import Texture
import ClassParticule

class PlayerController(Component):
    def __init__(self,gameObject,**kwargs):
        Component.__init__(self,gameObject,__name__.split(".")[-1],**kwargs)
        self.Bas1= Texture(self.Particule,name="None")
        self.TypeVariables["Bas1"] = {"Type":Texture}
        self.Bas2= Texture(self.Particule,name="None")
        self.TypeVariables["Bas2"] = {"Type":Texture}
        self.Bas3= Texture(self.Particule,name="None")
        self.TypeVariables["Bas3"] = {"Type":Texture}
        self.Haut1= Texture(self.Particule,name="None")
        self.TypeVariables["Haut1"] = {"Type":Texture}
        self.Haut2= Texture(self.Particule,name="None")
        self.TypeVariables["Haut2"] = {"Type":Texture}
        self.Haut3= Texture(self.Particule,name="None")
        self.TypeVariables["Haut3"] = {"Type":Texture}
        self.Droite1= Texture(self.Particule,name="None")
        self.TypeVariables["Droite1"] = {"Type":Texture}
        self.Droite2= Texture(self.Particule,name="None")
        self.TypeVariables["Droite2"] = {"Type":Texture}
        self.Droite3= Texture(self.Particule,name="None")
        self.TypeVariables["Droite3"] = {"Type":Texture}
        self.Gauche1= Texture(self.Particule,name="None")
        self.TypeVariables["Gauche1"] = {"Type":Texture}
        self.Gauche2= Texture(self.Particule,name="None")
        self.TypeVariables["Gauche2"] = {"Type":Texture}
        self.Gauche3= Texture(self.Particule,name="None")
        self.TypeVariables["Gauche3"] = {"Type":Texture}
        self.Frame= 0
        self.TypeVariables["Frame"] = {"Type":int}
        self.Vitesse= 0
        self.TypeVariables["Vitesse"] = {"Type":int}
        

        self.AttributVisible=["Bas1","Bas2","Bas3","Haut1","Haut2","Haut3","Droite1","Droite2","Droite3","Gauche1","Gauche2","Gauche3","Vitesse",]

    def SaveDataDict(self):
        data = Component.SaveDataDict(self)
        
        data.update({
            "Bas1":self.Bas1.path,"Bas2":self.Bas2.path,"Bas3":self.Bas3.path,"Haut1":self.Haut1.path,"Haut2":self.Haut2.path,"Haut3":self.Haut3.path,"Droite1":self.Droite1.path,"Droite2":self.Droite2.path,"Droite3":self.Droite3.path,"Gauche1":self.Gauche1.path,"Gauche2":self.Gauche2.path,"Gauche3":self.Gauche3.path,"Vitesse":self.Vitesse,
        })
        return data

    def LoadDataDict(self,data,component,dataCompo,dicoGameObject,dicoComponent):
        Component.LoadDataDict(self,data,component,dataCompo,dicoGameObject,dicoComponent)
        self.Bas1= Texture(self.Particule,Path=dataCompo["Bas1"],name=os.path.basename(dataCompo["Bas1"]))
        self.Bas2= Texture(self.Particule,Path=dataCompo["Bas2"],name=os.path.basename(dataCompo["Bas2"]))
        self.Bas3= Texture(self.Particule,Path=dataCompo["Bas3"],name=os.path.basename(dataCompo["Bas3"]))
        self.Haut1= Texture(self.Particule,Path=dataCompo["Haut1"],name=os.path.basename(dataCompo["Haut1"]))
        self.Haut2= Texture(self.Particule,Path=dataCompo["Haut2"],name=os.path.basename(dataCompo["Haut2"]))
        self.Haut3= Texture(self.Particule,Path=dataCompo["Haut3"],name=os.path.basename(dataCompo["Haut3"]))
        self.Droite1= Texture(self.Particule,Path=dataCompo["Droite1"],name=os.path.basename(dataCompo["Droite1"]))
        self.Droite2= Texture(self.Particule,Path=dataCompo["Droite2"],name=os.path.basename(dataCompo["Droite2"]))
        self.Droite3= Texture(self.Particule,Path=dataCompo["Droite3"],name=os.path.basename(dataCompo["Droite3"]))
        self.Gauche1= Texture(self.Particule,Path=dataCompo["Gauche1"],name=os.path.basename(dataCompo["Gauche1"]))
        self.Gauche2= Texture(self.Particule,Path=dataCompo["Gauche2"],name=os.path.basename(dataCompo["Gauche2"]))
        self.Gauche3= Texture(self.Particule,Path=dataCompo["Gauche3"],name=os.path.basename(dataCompo["Gauche3"]))
        self.Vitesse= dataCompo["Vitesse"]
        
