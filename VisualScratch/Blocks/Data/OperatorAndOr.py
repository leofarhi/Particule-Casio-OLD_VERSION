from ClassSystem.Scratch import *
from ClassSystem.Color import *
from ClassSystem.BlockSys import *
from ClassSystem.ScriptBlock import ScriptBlock
class ScriptBlockPython(ScriptBlock):
    def __init__(self, _Sys=None):
        ScriptBlock.__init__(self,_Sys)
        self.Onglet="Opérateurs"
        self.TypeForme="Losange"
        self.Texte="Et/Ou"
        self.Parametres=[["Booleen"],["Liste",["et","ou"]],["Booleen"]]
        self.Color=Couleurs.vert
        self.Compile="OperatorAndOr"
        self.Options = []
        self.SelfGetForme = None
        self.Image = None



    def WhenCompileForCasio(self,lst):
        if self.BlockSys.GetVariable(lst,1)[2] == "et":
            code = "((" + self.BlockSys.GetParametre(lst,0) + ")&&(" + self.BlockSys.GetParametre(lst,2) + "))"
        else:
            code = "((" + self.BlockSys.GetParametre(lst,0) + ")||(" + self.BlockSys.GetParametre(lst,2) + "))"
        return code
    
