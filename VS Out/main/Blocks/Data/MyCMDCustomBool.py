from ClassSystem.Scratch import *
from ClassSystem.Color import *
from ClassSystem.BlockSys import *
from ClassSystem.ScriptBlock import ScriptBlock
class ScriptBlockPython(ScriptBlock):
    def __init__(self, _Sys=None):
        ScriptBlock.__init__(self,_Sys)
        self.Onglet="Mes Blocs"
        self.TypeForme="Losange"
        self.Texte="CustomBool"
        self.Parametres=[['TexteEtNombre', '']]
        self.Color=Couleurs.jaune
        self.Compile="MyCMDCustomBool"
        self.Options = []
        self.SelfGetForme = None
        self.Image = None



    def WhenCompileForCasio(self,lst):
        code = "(" + str(self.BlockSys.GetVariable(lst,0)[1]) + ")"
        return code
    
