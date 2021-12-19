from ClassParticule.Component import Component
from ClassParticule.Vector2 import Vector2
from ClassParticule.Scene import Arrow

from ClassParticule.Object import Object
import math
class Transform(Component):
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

        self.TypeVariables.update({"childCount": {"Type": int},
                                   "eulerAngles": {"Type": None},
                                   "forward": {"Type": None},
                                   "hasChanged": {"Type": None},
                                   "hierarchyCapacity": {"Type": None},
                                   "hierarchyCount": {"Type": None},
                                   "localEulerAngles": {"Type": None},
                                   "localPosition": {"Type": Vector2},
                                   "localRotation": {"Type": None},
                                   "localScale": {"Type": None},
                                   "localToWorldMatrix": {"Type": None},
                                   "lossyScale": {"Type": None},
                                   "parent": {"Type": Transform},
                                   "childs": {"Type":list,"LstValueType":{"Type":Transform},"LstType":"List"},
                                   "position": {"Type": Vector2},
                                   "right": {"Type": None},
                                   "root": {"Type": None},
                                   "rotation": {"Type": None},
                                   "up": {"Type": None},
                                   "worldToLocalMatrix": {"Type": None}
                                   })

        #Attributs privés
        self._localPosition = Vector2()
        self._position = Vector2()

        self.AttributVisible=["position","localPosition"]

        self.arrowX = Arrow(self.Particule.Scene.surface, 0, "blue")
        self.arrowY = Arrow(self.Particule.Scene.surface, math.pi / 2, "green")
        self.arrowX.Hide()
        self.arrowY.Hide()
        canvas = self.Particule.Scene.surface
        self.arrowMiddle = canvas.create_rectangle(0, 0, 0, 0, fill='red')
        canvas.tag_bind(self.arrowX.line, '<B1-Motion>', self.MoveOnX)
        canvas.tag_bind(self.arrowY.line, '<B1-Motion>', self.MoveOnY)
        canvas.tag_bind(self.arrowMiddle, '<B1-Motion>', self.Drag)
        self.Particule.Scene.surface.itemconfig(self.arrowMiddle, state='hidden')

        #print(self.GetAttribut())


    def MoveOnX(self, event):
        #event.x, event.y
        z = self.Particule.Scene.zoom
        self.gameObject.transform.position.set(( (event.x//z)+self.Particule.Scene.x, self.gameObject.transform.position.y))
        #self.Particule.Inspector.UpdateItemSelected()
        self.PrintOnGui()

    def MoveOnY(self, event):
        #event.x, event.y
        z = self.Particule.Scene.zoom
        self.gameObject.transform.position.set(( self.gameObject.transform.position.x, (event.y//z)-self.Particule.Scene.y))
        #self.Particule.Inspector.UpdateItemSelected()
        self.PrintOnGui()

    def Drag(self, event):
        #event.x, event.y
        z = self.Particule.Scene.zoom
        self.gameObject.transform.position.set(( (event.x//z)+self.Particule.Scene.x, (event.y//z)-self.Particule.Scene.y))
        #self.Particule.Inspector.UpdateItemSelected()
        self.PrintOnGui()


    def SetParent(self, Other):
        if self.parent!=None:
            self.parent.childs.remove(self)
            self.parent = None
        if not self in Other.childs:
            Other.childs.append(self)
        self.parent = Other
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
            "childs":[i.ID for i in self.childs]
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

    def WhenComponentIsShow(self):
        z = self.Particule.Scene.zoom
        x, y = self.gameObject.transform.position.get()
        coords = ((x - self.Particule.Scene.x) * z,(y + self.Particule.Scene.y) * z)
        self.arrowX.Move(*coords)
        self.arrowY.Move(*coords)
        size=3
        self.Particule.Scene.surface.coords(self.arrowMiddle,coords[0]-size,coords[1]-size ,coords[0]+size,coords[1]+size )
        self.Particule.Scene.surface.tag_raise(self.arrowMiddle)

    def WhenComponentIsShowSignal(self):
        z = self.Particule.Scene.zoom
        x, y = self.gameObject.transform.position.get()
        coords = ((x - self.Particule.Scene.x) * z, (y + self.Particule.Scene.y) * z)
        self.arrowX.Move(*coords)
        self.arrowY.Move(*coords)
        self.arrowX.Show()
        self.arrowY.Show()
        self.Particule.Scene.surface.itemconfig(self.arrowMiddle, state='normal')


    def WhenComponentIsHideSignal(self):
        self.arrowX.Hide()
        self.arrowY.Hide()
        self.Particule.Scene.surface.itemconfig(self.arrowMiddle, state='hidden')

    def Destroy(self):
        self.arrowX.Delete()
        self.arrowY.Delete()
        self.Particule.Scene.surface.delete(self.arrowMiddle)
        Component.Destroy(self)

    def AddContextMenu(self):
        return

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
