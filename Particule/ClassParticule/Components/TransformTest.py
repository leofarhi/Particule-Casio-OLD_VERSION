from ClassParticule.Component import Component
from ClassParticule.Vector2 import Vector2
class TransformTest(Component):
    def __init__(self,gameObject,**kwargs):
        Component.__init__(self,gameObject,__name__.split(".")[-1],**kwargs)
        self.childCount = 0
        self.eulerAngles = None
        self.forward = None
        self.hasChanged = None
        self.hierarchyCapacity = None
        self.hierarchyCount = None
        self.localEulerAngles = None
        self.localPosition = Vector2()
        self.localRotation = None
        self.localScale = None
        self.localToWorldMatrix = None
        self.lossyScale = None
        self.parent = None
        self.childs = []
        self.position = Vector2()
        self.right = None
        self.root = None
        self.rotation = None
        self.up = None
        self.worldToLocalMatrix = None
        self.TestLst = [0,4]

        #Attributs privés
        self._localPosition = Vector2()
        self._position = Vector2()

        self.AttributVisible=["position","localPosition","TestLst"]

        #print(self.GetAttribut())
    def UpdateOnGUI(self):
        self.childCount = len(self.childs)
        if self.parent == None:
            if self.localPosition != self._localPosition:
                self.position.set(self.localPosition.get())
            self.localPosition.set(self.position.get())
        else:
            if self.localPosition != self._localPosition:
                self.position.set((self.localPosition+self.parent.position).get())
            else:
                if self.position != self._position:
                    self.localPosition.set((self.position - self.parent.position).get())
            #self.localPosition.set((self.parent.position-self.position).get())
            self.position.set((self.localPosition+self.parent.position).get())
        self._localPosition.set(self.localPosition.get())
        self._position.set(self.position.get())
        #print(self.gameObject.name)

    def SaveDataDict(self):
        data = Component.SaveDataDict(self)
        if self.parent == None:
            parent=None
        else:
            parent = self.parent.ID
        data.update({
            "childCount":self.childCount,
            "localPosition":self.localPosition.get(),
            "position":self.position.get(),
            "parent":parent,
            "childs":[i.ID for i in self.childs],
            "TestLst":self.TestLst
        })
        return data

    def LoadDataDict(self,data,component,dataCompo,dicoGameObject,dicoComponent):
        Component.LoadDataDict(self,data,component,dataCompo,dicoGameObject,dicoComponent)
        self.childCount = dataCompo["childCount"]
        self.localPosition = Vector2.set(Vector2(),dataCompo["localPosition"])
        self.position = Vector2.set(Vector2(),dataCompo["position"])
        parent = dataCompo["parent"]
        if parent != None:
            parent = dicoComponent[parent]
        self.parent = parent
        self.childs = [dicoComponent[o] for o in dataCompo["childs"]]
        self.TestLst=dataCompo["TestLst"]
    def DetachChildren(self):
        pass
    def Find(self):
        pass
    def GetChild(self):
        pass
    def GetSiblingIndex(self):
        pass
    def InverseTransformDirection(self):
        pass
    def InverseTransformPoint(self):
        pass
    def InverseTransformVector(self):
        pass
    def IsChildOf(self):
        pass
    def LookAt(self):
        pass
    def Rotate(self):
        pass
    def RotateAround(self):
        pass
    def SetAsFirstSibling(self):
        pass
    def SetAsLastSibling(self):
        pass
    def SetParent(self):
        pass
    def SetPositionAndRotation(self):
        pass
    def SetSiblingIndex(self):
        pass
    def TransformDirection(self):
        pass
    def TransformPoint(self):
        pass
    def TransformVector(self):
        pass
    def Translate(self):
        pass