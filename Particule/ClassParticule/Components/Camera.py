from Particule import *
from ClassParticule.Component import Component
class Camera(Component):
    def __init__(self,gameObject,**kwargs):
        Component.__init__(self, gameObject, __name__.split(".")[-1],**kwargs)
        self.canevas = self.Particule.Scene.surface
        self.pathProjectSettings = self.Particule.FolderProject + "/ProjectSettings/ProjectSettings.txt"
        self.w,self.h=self.ReloadSize()
        self.Mesh = self.canevas.create_rectangle(0,0, self.w,self.h, fill="")

        self.Particule.Scene.surface.tag_bind(self.Mesh, '<Button-1>', self.Clic)
        #self.Particule.Scene.surface.tag_bind(self.Mesh, '<B1-Motion>', self.Drag)
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
                                            int((x-self.Particule.Scene.x+self.w)*z),int((y+self.Particule.Scene.y+self.h)*z))

    def WhenComponentIsShowSignal(self):
        self.Particule.Scene.surface.tag_raise(self.Mesh)
    def Destroy(self):
        self.Particule.Scene.surface.delete(self.Mesh)
        Component.Destroy(self)

    def ReloadSize(self):
        temp = eval(rf.found(self.pathProjectSettings, "Player&ScreenSize"))
        return temp