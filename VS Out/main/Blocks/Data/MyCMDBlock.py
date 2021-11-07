from ClassSystem.Scratch import *
from ClassSystem.Color import *
from ClassSystem.BlockSys import *
from ClassSystem.ScriptBlock import ScriptBlock
class ScriptBlockPython(ScriptBlock):
    def __init__(self, _Sys=None):
        ScriptBlock.__init__(self,_Sys)
        self.Onglet="Mes Blocs"
        self.TypeForme="Rectangle"
        self.Texte="Ma Commande"
        self.Parametres=[['Label','CMD :'], ['TexteEtNombre', '']]
        self.Color=Couleurs.jaune
        self.Compile="MyCMDBlock"
        self.Options = [["AddSize",120]]
        self.SelfGetForme = None
        self.Image = None

    def AfterUpdate(self):
        (self.SelfGetForme.GroupeWidget[0])[2].configure(width=50)

    def WhenCompileForCasio(self,lst):
        code=str(self.BlockSys.GetVariable(lst,0)[1])+ "\n"
        code += self.BlockSys.GetSuite(lst, 0)
        return code
    
