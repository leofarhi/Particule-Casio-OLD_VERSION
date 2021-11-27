from Particule import *
from ClassParticule.Component import Component
from ClassParticule.Vector2 import Vector2

class Text(Component):
    def __init__(self,gameObject,**kwargs):
        Component.__init__(self,gameObject,__name__.split(".")[-1],**kwargs)
        self.text= ""
        self.font = "Consolas"
        self.TypeVariables.update({"text": {"Type": str}})

        self.Mesh = self.Particule.Scene.surface.create_text(0, 0, fill="black",font=(self.font, 5),anchor="nw",
                               text=self.text)
        

        self.AttributVisible=["text",]

        self.Particule.Scene.surface.tag_bind(self.Mesh, '<Button-1>', self.Clic)  # evevement clic gauche (press)
        self.Particule.Scene.surface.tag_bind(self.Mesh, '<B1-Motion>', self.Drag)
        # self.Particule.Scene.surface.tag_bind(self.Mesh,'<ButtonRelease-1>', self.Drop)

    def Clic(self, event):
        self.Particule.Hierarchy.t.focus(str(self.gameObject.ID))
        self.Particule.Hierarchy.t.selection_set(str(self.gameObject.ID))
        self.Particule.Hierarchy.SetItemSelect()

    def Drag(self, event):
        # event.x, event.y
        z = self.Particule.Scene.zoom
        self.gameObject.transform.position.set(
            ((event.x // z) + self.Particule.Scene.x, (event.y // z) - self.Particule.Scene.y))
        self.Particule.Inspector.UpdateItemSelected()

    def UpdateOnGUI(self):
        z = self.Particule.Scene.zoom
        self.Particule.Scene.surface.itemconfig(self.Mesh, text=self.text, font=(self.font, int(5 * z)))
        x,y = self.gameObject.transform.position.get()
        self.Particule.Scene.surface.coords(self.Mesh,(x-self.Particule.Scene.x)*z,(y+self.Particule.Scene.y)*z)
        if self.gameObject.activeInHierarchy and self.gameObject.activeSelf:
            self.Particule.Scene.surface.itemconfig(self.Mesh, state='normal')
        else:
            self.Particule.Scene.surface.itemconfig(self.Mesh, state='hidden')

    def SaveDataDict(self):
        data = Component.SaveDataDict(self)
        
        data.update({
            "text":self.text,
        })
        return data

    def LoadDataDict(self,data,component,dataCompo,dicoGameObject,dicoComponent):
        Component.LoadDataDict(self,data,component,dataCompo,dicoGameObject,dicoComponent)
        self.text= dataCompo["text"]

    def Destroy(self):
        self.Particule.Scene.surface.delete(self.Mesh)
        Component.Destroy(self)
