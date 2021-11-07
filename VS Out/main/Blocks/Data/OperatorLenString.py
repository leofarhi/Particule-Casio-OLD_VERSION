from ClassSystem.Scratch import *
from ClassSystem.Color import *
from ClassSystem.BlockSys import *
from ClassSystem.ScriptBlock import ScriptBlock
class ScriptBlockPython(ScriptBlock):
    def __init__(self, _Sys=None):
        ScriptBlock.__init__(self,_Sys)
        self.Onglet="Opérateurs"
        self.TypeForme="Cercle"
        self.Texte="Longueur d'un string"
        self.Parametres=[['Label', 'longueur '],['EmptyCercle']]
        self.Color=Couleurs.vert
        self.Compile="OperatorLenString"
        self.Options = []
        self.SelfGetForme = None
        self.Image = None

    def WhenCompileForCasio(self,lst):
        code = "LenChar((char*)" + self.BlockSys.GetParametre(lst,0) + ")"
        return code
