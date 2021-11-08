from Particule import *
from ClassParticule.Object import Object
from ClassParticule.Texture import Texture
import os
class FileVariable(Object):
    def __init__(self, Particule,Path,UUID, **kwargs):
        name = os.path.basename(Path)
        Object.__init__(self, Particule, name, **kwargs)
        ext = os.path.splitext(Path)[1]
        if ext == ".meta":
            Path = os.path.splitext(Path)[0]
        self.path = Path
        self.pathMeta = Path+".meta"
        self.ID=UUID

        ext = os.path.splitext(self.path)[1]
        if ext in [".png",".bmp",".jpg"]:
            if UUID+".bmp" in os.listdir(self.Particule.FolderProject+"/Library/ImagesBmpCache") and UUID+".bmp"!=os.path.basename(self.path):
                texture = Texture(self.Particule, Path=self.path, name=os.path.basename(self.path))
                texture.name = os.path.basename(self.path)
                texture.fileVariable = self
                self.Particule.All_UUID[UUID] = texture


    def ToString(self):
        return self.path