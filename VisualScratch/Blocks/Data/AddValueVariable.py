from ClassSystem.Scratch import *
from ClassSystem.Color import *
from ClassSystem.BlockSys import *
from ClassSystem.ScriptBlock import ScriptBlock
class ScriptBlockPython(ScriptBlock):
    def __init__(self, _Sys=None):
        ScriptBlock.__init__(self,_Sys)
        self.Onglet="Variable"
        self.TypeForme="Rectangle"
        self.Texte="ajouter une valeur à une variable"
        self.Parametres=[['Label', 'ajouter'],["Liste",[]],['Label', 'à'],['EmptyCercle']]
        self.Color=Couleurs.orange_fonce
        self.Compile="AddValueVariable"
        self.Options = []
        self.SelfGetForme = None
        self.Image = None

    
