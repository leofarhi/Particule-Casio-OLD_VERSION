from ClassSystem.Scratch import *
from ClassSystem.Color import *
from ClassSystem.BlockSys import *
from ClassSystem.ScriptBlock import ScriptBlock
class ScriptBlockPython(ScriptBlock):
    def __init__(self, _Sys=None):
        ScriptBlock.__init__(self,_Sys)
        self.Onglet="Controle"
        self.TypeForme="Encadrement"
        self.Texte="Repeter un certains nombre de fois"
        self.Parametres=[["Label","repeter "],["TexteEtNombre"],["Label","fois avec la variable :"],["TexteEtNombre"]]
        self.Color=Couleurs.orange
        self.Compile="RepeatNb"
        self.Options = []
        self.SelfGetForme = None
        self.Image = None

    def WhenCompileForCasio(self,lst):
        var = self.BlockSys.GetVariable(lst,1)[1]
        code = "for (int "+var+" = 0;"+var+"<" + self.BlockSys.GetVariable(lst,0)[1]+"; "+var+ "++){\n" + self.BlockSys.GetSuite(lst,0) + "\n}\n"
        code += self.BlockSys.GetSuite(lst,1)
        return code
    