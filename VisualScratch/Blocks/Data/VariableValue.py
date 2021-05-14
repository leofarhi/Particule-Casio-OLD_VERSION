from ClassSystem.Scratch import *
from ClassSystem.Color import *
from ClassSystem.BlockSys import *
from ClassSystem.ScriptBlock import ScriptBlock
class ScriptBlockPython(ScriptBlock):
    def __init__(self, _Sys=None):
        ScriptBlock.__init__(self,_Sys)
        self.Onglet="Variable"
        self.TypeForme="Cercle"
        self.Texte="GetVariable"
        self.Parametres=[["Liste",[]]]
        self.Color=Couleurs.orange_fonce
        self.Compile="VariableValue"
        self.Options = []
        self.SelfGetForme = None
        self.Image = None


    