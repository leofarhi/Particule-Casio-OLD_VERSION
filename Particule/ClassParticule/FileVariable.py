from Particule import *
from ClassParticule.Object import Object
from ClassParticule.Texture import Texture
import os
class FileVariable(Object):
    def __init__(self, Particule,Path,UUID, **kwargs):
        name = os.path.basename(Path)
        Object.__init__(self, Particule, name, UUID = UUID)
        ext = os.path.splitext(Path)[1]
        if ext == ".meta":
            Path = os.path.splitext(Path)[0]
        self.path = Path
        self.pathMeta = Path+".meta"
        self.IsHide = rf.found(self.pathMeta, "IsHide")
        if UUID!=False:
            self.ID=UUID

    def UpdateCheck(self):
        ext = os.path.splitext(self.path)[1]
        if ext in [".png",".bmp",".jpg"]:
            if os.path.abspath(self.Particule.FolderProject+"/Library/ImagesBmpCache") in os.path.abspath(self.path):
                MpathFile = os.path.abspath(rf.found(self.pathMeta, "pathFile"))
                MainUUID = os.path.splitext(os.path.basename(MpathFile))[0]
                texture = Texture(self.Particule, Path=self.path, name=os.path.basename(self.Particule.All_UUID[MainUUID].path),UUID = self.ID)
                texture.name = os.path.basename(self.Particule.All_UUID[MainUUID].path)
                texture.fileVariable = self
                self.Particule.All_UUID[self.ID] = texture
        self.IsHide = rf.found(self.pathMeta, "IsHide")


    def ToString(self):
        return self.path