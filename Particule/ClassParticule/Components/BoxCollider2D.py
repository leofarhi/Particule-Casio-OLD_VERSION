from Particule import *
from ClassParticule.Component import Component
from ClassParticule.Vector2 import Vector2
from ClassParticule.Components.Sprite import Sprite
class BoxCollider2D(Component):
    def __init__(self,gameObject,**kwargs):
        Component.__init__(self, gameObject, __name__.split(".")[-1],**kwargs)
        self.canevas = self.Particule.Scene.surface
        self.IsTrigger = False
        self.Center= Vector2()
        self.Size = Vector2(32,32)

        SpriteCompo = gameObject.GetComponent(Sprite)
        if SpriteCompo!=None:
            self.Size=Vector2(SpriteCompo.width,SpriteCompo.height)
            self.Center=Vector2(SpriteCompo.width//2,SpriteCompo.height//2)

        self.Mesh = self.canevas.create_rectangle(self.Center.x-(self.Size.x//2),self.Center.y-(self.Size.y//2),self.Center.x+(self.Size.x//2),self.Center.y+(self.Size.y//2), fill="", outline='green',width=3)
        self.TypeVariables.update({"Center": {"Type": Vector2},
                                   "Size": {"Type": Vector2},
                                   "IsTrigger": {"Type": bool},
                                   })
        self.AttributVisible = ["IsTrigger", "Center", "Size"]
        self.Particule.Scene.surface.tag_bind(self.Mesh, '<Button-1>', self.Clic)
        self.Particule.Scene.surface.tag_bind(self.Mesh, '<B1-Motion>', self.Drag)
    def Clic(self, event):
        self.Particule.Hierarchy.t.focus(str(self.gameObject.ID))
        self.Particule.Hierarchy.t.selection_set(str(self.gameObject.ID))
        self.Particule.Hierarchy.SetItemSelect()
    def Drag(self, event):
        #event.x, event.y
        z = self.Particule.Scene.zoom
        self.gameObject.transform.position.set(
            ((event.x // z) + self.Particule.Scene.x, (event.y // z) - self.Particule.Scene.y))
        self.Particule.Inspector.UpdateItemSelected()



    def UpdateOnGUI(self):
        z = self.Particule.Scene.zoom
        x,y = self.gameObject.transform.position.get()
        Start = Vector2(self.Center.x - (self.Size.x // 2), self.Center.y - (self.Size.y // 2))
        End = Vector2(self.Center.x + (self.Size.x // 2), self.Center.y + (self.Size.y // 2))

        self.Particule.Scene.surface.coords(
            self.Mesh,int((Start.x+x-self.Particule.Scene.x)*z),
            int((Start.y+y+self.Particule.Scene.y)*z),
            int((End.x+x-self.Particule.Scene.x)*z),
            int((End.y+y+self.Particule.Scene.y)*z))
        self.Particule.Scene.surface.tag_raise(self.Mesh)

    def SaveDataDict(self):
        data = Component.SaveDataDict(self)

        data.update({
            "IsTrigger":self.IsTrigger,
            "Center": self.Center.get(),
            "Size":self.Size.get()
        })
        return data

    def LoadDataDict(self, data, component, dataCompo, dicoGameObject, dicoComponent):
        Component.LoadDataDict(self, data, component, dataCompo, dicoGameObject, dicoComponent)
        self.IsTrigger = dataCompo["IsTrigger"]
        self.Center = Vector2.set(Vector2(), dataCompo["Center"])
        self.Size = Vector2.set(Vector2(), dataCompo["Size"])
    def Destroy(self):
        self.Particule.Scene.surface.delete(self.Mesh)
        Component.Destroy(self)