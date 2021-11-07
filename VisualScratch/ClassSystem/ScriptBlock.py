from ClassSystem.Scratch import *
from ClassSystem.Color import *
from ClassSystem.BlockSys import *
class ScriptBlock:
    def __init__(self, _Sys=None):
        self.Sys = _Sys
        self.BlockSys = None
        if self.Sys != None:
            self.BlockSys = self.Sys.BlockSys
        self.Onglet=""
        self.TypeForme=""
        self.Texte=""
        self.Parametres=[]
        self.Color=Couleurs.orange
        self.Compile=""
        self.Options = []
        self.SelfGetForme = None
        self.Image = None


    def WhenAdded(self):
        pass

    def WhenUpdate(self):
        pass

    def AfterUpdate(self):
        pass

    def WhenRemove(self):
        pass

    def WhenCompile(self):
        self.WhenCompileForPython()
        self.WhenCompileForCasio()
    #Pour Particule :
    def WhenCompileForPython(self,lst,base):
        return base

    def WhenCompileForCasio(self,lst,base):
        return self.BlockSys.GetSuite(lst,0)