import Project as Pj
class ScriptBlockPython:
    def __init__(self,SelfGetForme):#OnStart
        self.SelfGetForme=SelfGetForme
        self.WhenUpdate()
    def WhenAdded(self):
        pass
    def WhenUpdate(self):
        global Variables
        (self.SelfGetForme.Parametres[0])[1]=[(Img[1])[2] for Img in Pj.ImageLoad]
    def WhenRemove(self):
        pass
    def WhenCompileForPython(self):
        pass
    def WhenCompileForCasio(self):
        pass
