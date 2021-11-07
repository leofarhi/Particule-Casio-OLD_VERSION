from ClassSystem.Scratch import *
from ClassSystem.Color import *
from ClassSystem.BlockSys import *
from ClassSystem.ScriptBlock import ScriptBlock
class ScriptBlockPython(ScriptBlock):
    def __init__(self, _Sys=None):
        ScriptBlock.__init__(self,_Sys)
        self.Onglet="Evenements"
        self.TypeForme="Vague"
        self.Texte="Update"
        self.Parametres=[["Label","A chaque rafraichissement"]]
        self.Color=Couleurs.jaune
        self.Compile="OnUpdate"
        self.Options = []
        self.SelfGetForme = None
        self.Image = None



    def WhenCompileForCasio(self,lst):
        code = "void Update(){\n" + self.BlockSys.GetSuite(lst,0) + "\n}"
        return code
    