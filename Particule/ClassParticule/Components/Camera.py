from Particule import *
from ClassParticule.Component import Component
class Camera(Component):
    def __init__(self,gameObject,**kwargs):
        Component.__init__(self, gameObject, __name__.split(".")[-1],**kwargs)
        self.canevas = self.Particule.Scene.surface
        self.Mesh = self.canevas.create_rectangle(0,0, 127, 63, fill="")

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
        self.Particule.Scene.surface.coords(self.Mesh,int((x-self.Particule.Scene.x)*z),int((y+self.Particule.Scene.y)*z),
                                            int((x-self.Particule.Scene.x+127)*z),int((y+self.Particule.Scene.y+63)*z))
    def Destroy(self):
        self.Particule.Scene.surface.delete(self.Mesh)