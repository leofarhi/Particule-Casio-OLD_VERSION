from Particule import *
from ClassParticule.Object import Object
from PIL import ImageFilter

class Texture(Object):
    def __init__(self, Particule,width=None,height=None,Path="Library/lib/vide.png", name="", scene="", **kwargs):
        Object.__init__(self, Particule, name, **kwargs)
        self.fileVariable = None
        self.path = Path
        self.ImgStd = None
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
            pathTmp = self.Particule.FolderProject + "/" + self.path
            if self.Particule.CalculatriceCouleur:
                name = os.path.basename(self.path)
                name = os.path.splitext(name)[0]
                obj = self.Particule.GetObjectWithUUID(name)
                if "FileVariable" in str(type(obj)):
                    pathTmp = obj.path
            #print(pathTmp)
            self.ImgStd = Image.open( pathTmp)
            self.Img = ImageTk.PhotoImage(self.ImgStd)
            #self.name = self.path.split("/")[1]
    def ToString(self):
        return self.name

