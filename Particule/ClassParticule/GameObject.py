from ClassParticule.Object import Object
from ClassParticule.Components.Transform import Transform
from ClassParticule.Tag import Tag
from ClassParticule.Layer import Layer
from Particule import *
import os,sys
from Particule import *
class GameObject(Object):
    def __init__(self,Particule,name="",scene="",**kwargs):
        Object.__init__(self,Particule,name,**kwargs)
        self.activeInHierarchy = True
        self.activeSelf = True
        self.isStatic = False
        self.layer = Layer.Default
        self.scene = scene
        self.sceneCullingMask = ""
        self.tag = Tag.Untagged
        self.transform = Transform(self)
        self.ListOfComponent=[self.transform]

    def UpdateOnGUI(self):
        if self.transform.parent == None:
            self.activeInHierarchy = True
        else:
            parent = self.transform.parent.gameObject
            self.activeInHierarchy = (parent.activeSelf and parent.activeInHierarchy)
            if self.activeSelf and self.activeInHierarchy:
                tag = 'Active'
            else :
                tag = 'Desactive'
            try:
                self.Particule.Hierarchy.t.item(str(self.ID),  tags=(tag))
            except:
                pass
        for component in self.ListOfComponent:
            component.UpdateOnGUI()
    def AddComponent(self,ClassComponent):
        temp = ClassComponent(self)#getattr(sys.modules['Particule'], ClassComponent.__name__)(self)
        self.ListOfComponent.append(temp)
        self.Particule.Inspector.UpdateItemSelected()
        self.Particule.Inspector.focus_set()

    def AddComponentByName(self,name):
        for compo in self.Particule.AllComponent:
            if name == (compo.__name__).split(".")[-1]:
                self.AddComponent(compo)
    def Destroy(self):

        for i in range(len(self.ListOfComponent)):
            self.ListOfComponent[i].Destroy()
    def BroadcastMessage(self):
        pass
    def CompareTag(self):
        pass
    def GetComponent(self):
        pass
    def GetComponentInChildren(self):
        pass
    def GetComponentInParent(self):
        pass
    def GetComponents(self):
        pass
    def GetComponentsInChildren(self):
        pass
    def GetComponentsInParent(self):
        pass
    def SendMessage(self):
        pass
    def SendMessageUpwards(self):
        pass
    def SetActive(self):
        pass
    def TryGetComponent(self):
        pass
    def CreatePrimitive(self):
        pass
    def Find(self):
        pass
    def FindGameObjectsWithTag(self):
        pass
    def FindWithTag(self):
        pass