from Particule import *
from ClassParticule.Component import Component
from ClassParticule.Vector2 import Vector2
from ClassParticule.Texture import Texture
from ClassParticule.Texture import Texture
import ClassParticule

class RoomCible(Component):
    def __init__(self,gameObject,**kwargs):
        Component.__init__(self,gameObject,__name__.split(".")[-1],**kwargs)
        self.GameMg= None
        self.TypeVariables["GameMg"] = {"Type":GameManagerCible}
        self.IsMonster= False
        self.TypeVariables["IsMonster"] = {"Type":bool}
        self.MySprite= None
        self.TypeVariables["MySprite"] = {"Type":Sprite}
        self.WaitTime= 0
        self.TypeVariables["WaitTime"] = {"Type":int}
        self.NextSprite= 0
        self.TypeVariables["NextSprite"] = {"Type":int}
        

        self.AttributVisible=["WaitTime",]

    def SaveDataDict(self):
        data = Component.SaveDataDict(self)
        
        data.update({
            "WaitTime":self.WaitTime,
        })
        return data

    def LoadDataDict(self,data,component,dataCompo,dicoGameObject,dicoComponent):
        Component.LoadDataDict(self,data,component,dataCompo,dicoGameObject,dicoComponent)
        self.WaitTime= dataCompo["WaitTime"]
        
