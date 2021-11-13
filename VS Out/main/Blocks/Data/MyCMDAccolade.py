from ClassSystem.Scratch import *
from ClassSystem.Color import *
from ClassSystem.BlockSys import *
from ClassSystem.ScriptBlock import ScriptBlock
class ScriptBlockPython(ScriptBlock):
    def __init__(self, _Sys=None):
        ScriptBlock.__init__(self,_Sys)
        self.Onglet="Mes Blocs"
        self.TypeForme="Encadrement"
        self.Texte="Creer une Accolade"
        self.Parametres=[['TexteEtNombre', ''],["Label"," alors"]]
        self.Color=Couleurs.jaune
        self.Compile="MyCMDAccolade"
        self.Options = []
        self.SelfGetForme = None
        self.Image = None


    def WhenCompileForCasio(self,lst):
        code = str(self.BlockSys.GetVariable(lst,0)[1])+"{\n" + self.BlockSys.GetSuite(lst,0) + "\n}\n"
        code += self.BlockSys.GetSuite(lst,1)
        return code
    