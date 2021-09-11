from ClassSystem.Scratch import *
from ClassSystem.Color import *
from ClassSystem.BlockSys import *
from ClassSystem.ScriptBlock import ScriptBlock
class ScriptBlockPython(ScriptBlock):
    def __init__(self, _Sys=None):
        ScriptBlock.__init__(self,_Sys)
        self.Onglet="Opérateurs"
        self.TypeForme="Losange"
        self.Texte="Vrai ou Faux"
        self.Parametres=[["Liste",["Vrai","Faux"]]]
        self.Color=Couleurs.vert
        self.Compile="OperatorBool"
        self.Options = []
        self.SelfGetForme = None
        self.Image = None


    def WhenCompileForCasio(self,lst):
        if self.BlockSys.GetVariable(lst,0)[2] == "Vrai":
            code = "true"
        else:
            code = "false"
        return code
    
