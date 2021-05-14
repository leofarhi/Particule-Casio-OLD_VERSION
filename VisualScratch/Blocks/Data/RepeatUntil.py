from ClassSystem.Scratch import *
from ClassSystem.Color import *
from ClassSystem.BlockSys import *
from ClassSystem.ScriptBlock import ScriptBlock
class ScriptBlockPython(ScriptBlock):
    def __init__(self, _Sys=None):
        ScriptBlock.__init__(self,_Sys)
        self.Onglet="Controle"
        self.TypeForme="Encadrement"
        self.Texte="repeter tant que ? est vrai"
        self.Parametres=[["Label","repeter tant que "],["Booleen"],["Label","est vrai"]]
        self.Color=Couleurs.orange
        self.Compile="RepeatUntil"
        self.Options = []
        self.SelfGetForme = None
        self.Image = None



    def WhenCompileForCasio(self,lst):
        code = "while (" + self.BlockSys.GetParametre(lst,0) + "){\n" + self.BlockSys.GetSuite(lst,0) + "\n}\n"
        code += self.BlockSys.GetSuite(lst,1)
        return code
    