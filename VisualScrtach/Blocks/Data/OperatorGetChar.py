from ClassSystem.Scratch import *
from ClassSystem.Color import *
from ClassSystem.BlockSys import *
from ClassSystem.ScriptBlock import ScriptBlock
class ScriptBlockPython(ScriptBlock):
    def __init__(self, _Sys=None):
        ScriptBlock.__init__(self,_Sys)
        self.Onglet="Opérateurs"
        self.TypeForme="Cercle"
        self.Texte="Récuperer une lettre"
        self.Parametres=[['Label', 'lettre '],['EmptyCercle'],['Label', 'de'],['EmptyCercle']]
        self.Color=Couleurs.vert
        self.Compile="OperatorGetChar"
        self.Options = []
        self.SelfGetForme = None
        self.Image = None


    
