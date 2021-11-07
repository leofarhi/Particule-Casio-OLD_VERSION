from ClassSystem.Scratch import *
from ClassSystem.Color import *
from ClassSystem.BlockSys import *
from ClassSystem.ScriptBlock import ScriptBlock
class ScriptBlockPython(ScriptBlock):
    def __init__(self, _Sys=None):
        ScriptBlock.__init__(self,_Sys)
        self.Onglet="Mouvement"
        self.TypeForme="Cercle"
        self.Texte="Position X de l'objet"
        self.Parametres=[['Label', "Position X de l'objet"]]
        self.Color=Couleurs.bleu_fonce
        self.Compile="CoordXObject"
        self.Options = []
        self.SelfGetForme = None
        self.Image = None


    def WhenCompileForCasio(self,lst):
        code = "this->gameObject->transform->position->x"
        return code
    
