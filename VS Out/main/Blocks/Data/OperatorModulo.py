from ClassSystem.Scratch import *
from ClassSystem.Color import *
from ClassSystem.BlockSys import *
from ClassSystem.ScriptBlock import ScriptBlock
class ScriptBlockPython(ScriptBlock):
    def __init__(self, _Sys=None):
        ScriptBlock.__init__(self,_Sys)
        self.Onglet="Opérateurs"
        self.TypeForme="Cercle"
        self.Texte="Modulo"
        self.Parametres=[['EmptyCercle'],['Label', ' modulo '],['EmptyCercle']]
        self.Color=Couleurs.vert
        self.Compile="OperatorModulo"
        self.Options = []
        self.SelfGetForme = None
        self.Image = None


    def WhenCompileForCasio(self,lst):
        code = "mod((int)" + self.BlockSys.GetParametre(lst,0) + ",(int)" + self.BlockSys.GetParametre(lst,1) + ")"
        return code
