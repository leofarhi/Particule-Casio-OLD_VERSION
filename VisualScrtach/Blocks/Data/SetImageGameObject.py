from ClassSystem.Scratch import *
from ClassSystem.Color import *
from ClassSystem.BlockSys import *
from ClassSystem.ScriptBlock import ScriptBlock
class ScriptBlockPython(ScriptBlock):
    def __init__(self, _Sys=None):
        ScriptBlock.__init__(self,_Sys)
        self.Onglet="Apparence"
        self.TypeForme="Rectangle"
        self.Texte="basculer sur le costume"
        self.Parametres=[['Label', 'basculer sur le costume:'], ['EmptyCercle']]
        self.Color=Couleurs.violet
        self.Compile="SetImageGameObject"
        self.Options = []
        self.SelfGetForme = None
        self.Image = None

