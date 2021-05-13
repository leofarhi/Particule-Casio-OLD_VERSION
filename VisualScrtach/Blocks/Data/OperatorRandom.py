from ClassSystem.Scratch import *
from ClassSystem.Color import *
from ClassSystem.BlockSys import *
from ClassSystem.ScriptBlock import ScriptBlock
class ScriptBlockPython(ScriptBlock):
    def __init__(self, _Sys=None):
        ScriptBlock.__init__(self,_Sys)
        self.Onglet="Opérateurs"
        self.TypeForme="Cercle"
        self.Texte="valeur aléatoire entre deux nombre"
        self.Parametres=[['Label', 'nombre aléatoire entre'],['EmptyCercle'],['Label', 'et'],['EmptyCercle'] ]
        self.Color=Couleurs.vert
        self.Compile="OperatorRandom"
        self.Options = []
        self.SelfGetForme = None
        self.Image = None


    
