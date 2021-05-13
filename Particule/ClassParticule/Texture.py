from Particule import *
from ClassParticule.Object import Object
from ClassParticule.Component import Component
from PIL import ImageFilter
class Texture(Object):
    def __init__(self, Particule,width=None,height=None,Path="Library/lib/vide.png", name="", scene="", **kwargs):
        Object.__init__(self, Particule, name, **kwargs)
        self.path = Path
        self.Img = None
        #print(self.path)
        self.ReloadImg()
        if width==None:
            self.width = self.Img.width()
            self.height = self.Img.height()
        else:
            self.width = width
            self.height = height

    def ReloadImg(self):
        if self.path !=None:
            self.path = self.path.replace(self.Particule.FolderProject, "").replace("\\", "/")
            self.Img = Image.open(self.Particule.FolderProject + "/" + self.path)
            self.Img = ImageTk.PhotoImage(self.Img)
            self.name = self.path.split("/")[1]
    def ToString(self):
        return self.path