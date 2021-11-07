from ClassSystem.Scratch import *
from ClassSystem.Color import *
from ClassSystem.BlockSys import *
from ClassSystem.ScriptBlock import ScriptBlock
class ScriptBlockPython(ScriptBlock):
    def __init__(self, _Sys=None):
        ScriptBlock.__init__(self,_Sys)
        self.Onglet="Mouvement"
        self.TypeForme="Rectangle"
        self.Texte="Ajouter aux coordonnées Y"
        self.Parametres=[['Label', 'Ajouter a y:'], ['EmptyCercle']]
        self.Color=Couleurs.bleu_fonce
        self.Compile="GotoY"
        self.Options = []
        self.SelfGetForme = None
        self.Image = None

    def WhenCompileForCasio(self,lst):
        code = "this->gameObject->transform->position->y += " + self.BlockSys.GetParametre(lst, 0) + ";\n"
        code += self.BlockSys.GetSuite(lst, 0)
        return code
    
