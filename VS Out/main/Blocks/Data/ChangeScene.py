from ClassSystem.Scratch import *
from ClassSystem.Color import *
from ClassSystem.BlockSys import *
from ClassSystem.ScriptBlock import ScriptBlock
class ScriptBlockPython(ScriptBlock):
    def __init__(self, _Sys=None):
        ScriptBlock.__init__(self,_Sys)
        self.Onglet="Controle"
        self.TypeForme="Rectangle"
        self.Texte="Changer la scene"
        self.Parametres=[["Label","Charger la scene"],['EmptyCercle']]
        self.Color=Couleurs.orange
        self.Compile="ChangeScene"
        self.Options = []
        self.SelfGetForme = None
        self.Image = None

    def WhenCompileForCasio(self,lst):
        code = "LoadScene(this->gameObject->scene," + self.BlockSys.GetParametre(lst,0) + ");\n"
        code +="return;\n"
        code += self.BlockSys.GetSuite(lst, 0)
        return code