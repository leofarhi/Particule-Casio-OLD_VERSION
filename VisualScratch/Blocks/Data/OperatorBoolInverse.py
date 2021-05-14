from ClassSystem.Scratch import *
from ClassSystem.Color import *
from ClassSystem.BlockSys import *
from ClassSystem.ScriptBlock import ScriptBlock
class ScriptBlockPython(ScriptBlock):
    def __init__(self, _Sys=None):
        ScriptBlock.__init__(self,_Sys)
        self.Onglet="Opérateurs"
        self.TypeForme="Losange"
        self.Texte="Non"
        self.Parametres=[['Label', 'non '],["Booleen"]]
        self.Color=Couleurs.vert
        self.Compile="OperatorBoolInverse"
        self.Options = []
        self.SelfGetForme = None
        self.Image = None



    def WhenCompileForCasio(self,lst):
        code = "!(" + self.BlockSys.GetParametre(lst,0) + ")"
        return code
    
