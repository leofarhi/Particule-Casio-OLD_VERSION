from Particule import *
from ClassParticule.Component import Component
from ClassParticule.Vector2 import Vector2
from ClassParticule.Texture import Texture
from ClassParticule.Texture import Texture
import ClassParticule

class BallGolem(Component):
    def __init__(self,gameObject,**kwargs):
        Component.__init__(self,gameObject,__name__.split(".")[-1],**kwargs)
        self.vitesse= 0
        self.TypeVariables["vitesse"] = {"Type":int}
        self.Xrestart= 0
        self.TypeVariables["Xrestart"] = {"Type":int}
        self.PlayerGm= None
        self.TypeVariables["PlayerGm"] = {"Type":GameObject}
        self.EpeeGm= None
        self.TypeVariables["EpeeGm"] = {"Type":GameObject}
        self.GolemGm= None
        self.TypeVariables["GolemGm"] = {"Type":GameObject}
        self.Direction= 0
        self.TypeVariables["Direction"] = {"Type":int}
        self.GameMg= None
        self.TypeVariables["GameMg"] = {"Type":AllFightGolem}
        

        self.AttributVisible=["vitesse","Xrestart",]

    def SaveDataDict(self):
        data = Component.SaveDataDict(self)
        
        data.update({
            "vitesse":self.vitesse,"Xrestart":self.Xrestart,
        })
        return data

    def LoadDataDict(self,data,component,dataCompo,dicoGameObject,dicoComponent):
        Component.LoadDataDict(self,data,component,dataCompo,dicoGameObject,dicoComponent)
        self.vitesse= dataCompo["vitesse"]
        self.Xrestart= dataCompo["Xrestart"]
        
