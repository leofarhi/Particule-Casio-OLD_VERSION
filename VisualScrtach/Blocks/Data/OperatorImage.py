from ClassSystem.Scratch import *
from ClassSystem.Color import *
from ClassSystem.BlockSys import *
from ClassSystem.ScriptBlock import ScriptBlock
class ScriptBlockPython(ScriptBlock):
    def __init__(self, _Sys=None):
        ScriptBlock.__init__(self,_Sys)
        self.Onglet="Opérateurs"
        self.TypeForme="Cercle"
        self.Texte="Selection d'images"
        self.Parametres=[["Liste",[]]]
        self.Color=Couleurs.vert
        self.Compile="OperatorImage"
        self.Options = []
        self.SelfGetForme = None
        self.Image = None


