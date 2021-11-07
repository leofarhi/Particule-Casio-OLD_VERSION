from Particule import *
from ClassParticule.Object import Object
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

    def ToString(self):
        return self.path