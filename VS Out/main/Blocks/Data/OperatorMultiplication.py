from ClassSystem.Scratch import *
from ClassSystem.Color import *
from ClassSystem.BlockSys import *
from ClassSystem.ScriptBlock import ScriptBlock
class ScriptBlockPython(ScriptBlock):
    def __init__(self, _Sys=None):
        ScriptBlock.__init__(self,_Sys)
        self.Onglet="Opérateurs"
        self.TypeForme="Cercle"
        self.Texte="Multiplication"
        self.Parametres=[['EmptyCercle'],['Label', ' * '],['EmptyCercle']]
        self.Color=Couleurs.vert
        self.Compile="OperatorMultiplication"
        self.Options = []
        self.SelfGetForme = None
        self.Image = None


    def WhenCompileForCasio(self,lst):
        code = "((" + self.BlockSys.GetParametre(lst,0) + ")*(" + self.BlockSys.GetParametre(lst,1) + "))"
        return code
    
