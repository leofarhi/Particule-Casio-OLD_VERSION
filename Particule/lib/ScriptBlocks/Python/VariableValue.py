class ScriptBlockPython:
    def __init__(self,SelfGetForme):#OnStart
        self.SelfGetForme=SelfGetForme
        self.WhenUpdate()
    def WhenAdded(self):
        pass
    def WhenUpdate(self):
        global Variables
        (self.SelfGetForme.Parametres[0])[1]=[i[0] for i in Variables]
    def WhenRemove(self):
        pass
    def WhenCompileForPython(self):
        pass
    def WhenCompileForCasio(self):
        pass