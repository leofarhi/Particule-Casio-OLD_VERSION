from Particule import *
from ClassParticule.Component import Component
from ClassParticule.Vector2 import Vector2
from ClassParticule.Texture import Texture
from ClassParticule.Texture import Texture
import ClassParticule

class Curseur(Component):
    def __init__(self,gameObject,**kwargs):
        Component.__init__(self,gameObject,__name__.split(".")[-1],**kwargs)
        

        self.AttributVisible=[]

    def SaveDataDict(self):
        data = Component.SaveDataDict(self)
        
        data.update({
            
        })
        return data

    def LoadDataDict(self,data,component,dataCompo,dicoGameObject,dicoComponent):
        Component.LoadDataDict(self,data,component,dataCompo,dicoGameObject,dicoComponent)
        
