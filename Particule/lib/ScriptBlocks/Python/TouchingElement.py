import Project as Pj
class ScriptBlockPython:
    def __init__(self,SelfGetForme):#OnStart
        self.SelfGetForme=SelfGetForme
        self.WhenUpdate()
    def WhenAdded(self):
        pass
    def WhenUpdate(self):
        global Variables
        (self.SelfGetForme.Parametres[1])[1]=[i.name for i in Pj.Elements]
    def WhenRemove(self):
        pass
    def WhenCompileForPython(self):
        pass
    def WhenCompileForCasio(self):
        pass
