from ClassSystem.Scratch import *
from ClassSystem.Color import *
from ClassSystem.BlockSys import *
from ClassSystem.ScriptBlock import ScriptBlock
class ScriptBlockPython(ScriptBlock):
    def __init__(self, _Sys=None):
        ScriptBlock.__init__(self,_Sys)
        self.Onglet="Mes Blocs"
        self.TypeForme="Vague"
        self.Texte="Ma Fonction"
        self.Parametres=[["Label","void"],['TexteEtNombre', ''],["Label","("],['TexteEtNombre', ''],["Label",")"]]
        self.Color=Couleurs.jaune
        self.Compile="MyCMDFunction"
        self.Options = []
        self.SelfGetForme = None
        self.Image = None



    def WhenCompileForCasio(self,lst):
        code = "void "+str(self.BlockSys.GetVariable(lst,0)[1])+"("+str(self.BlockSys.GetVariable(lst,1)[1])+"){\n" + self.BlockSys.GetSuite(lst,0) + "\n}"
        return code
    