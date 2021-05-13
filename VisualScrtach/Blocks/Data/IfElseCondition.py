from ClassSystem.Scratch import *
from ClassSystem.Color import *
from ClassSystem.BlockSys import *
from ClassSystem.ScriptBlock import ScriptBlock
class ScriptBlockPython(ScriptBlock):
    def __init__(self, _Sys=None):
        ScriptBlock.__init__(self,_Sys)
        self.Onglet="Controle"
        self.TypeForme="Encadrement"
        self.Texte="Si ? est vrai alors, Sinon ..."
        self.Parametres=[["Label","Si "],["Booleen"],["Label"," alors"]]
        self.Color=Couleurs.orange
        self.Compile="IfElseCondition"
        self.Options = [["Encoche",2],["Parametres",[["Label","Sinon"]]]]
        self.SelfGetForme = None
        self.Image = None




    def WhenCompileForCasio(self,lst):
        code = "if (" + self.BlockSys.GetParametre(lst,0) + "){\n" + self.BlockSys.GetSuite(lst,0) + "\n}"
        code += "else {\n" + self.BlockSys.GetSuite(lst,1) + "\n}\n"
        code += self.BlockSys.GetSuite(lst,2)
        return code
    