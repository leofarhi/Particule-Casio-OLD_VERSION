from Particule import *
from ClassParticule.Component import Component
from ClassParticule.Vector2 import Vector2
from ClassParticule.Texture import Texture
from ClassParticule.Texture import Texture
import ClassParticule

class AllFightGolem(Component):
    def __init__(self,gameObject,**kwargs):
        Component.__init__(self,gameObject,__name__.split(".")[-1],**kwargs)
        self.TypeAttaque= 0
        self.TypeVariables["TypeAttaque"] = {"Type":int}
        self.Yplayer= 0
        self.TypeVariables["Yplayer"] = {"Type":int}
        self.PlayerGm= None
        self.TypeVariables["PlayerGm"] = {"Type":GameObject}
        self.EpeeGm= None
        self.TypeVariables["EpeeGm"] = {"Type":GameObject}
        self.PVplayer= 0
        self.TypeVariables["PVplayer"] = {"Type":int}
        self.PVGolem= 0
        self.TypeVariables["PVGolem"] = {"Type":int}
        self.StrPVplayer= ""
        self.TypeVariables["StrPVplayer"] = {"Type":str}
        self.StrPVGolem= ""
        self.TypeVariables["StrPVGolem"] = {"Type":str}
        

        self.AttributVisible=["PVplayer","PVGolem",]

    def SaveDataDict(self):
        data = Component.SaveDataDict(self)
        
        data.update({
            "PVplayer":self.PVplayer,"PVGolem":self.PVGolem,
        })
        return data

    def LoadDataDict(self,data,component,dataCompo,dicoGameObject,dicoComponent):
        Component.LoadDataDict(self,data,component,dataCompo,dicoGameObject,dicoComponent)
        self.PVplayer= dataCompo["PVplayer"]
        self.PVGolem= dataCompo["PVGolem"]
        
