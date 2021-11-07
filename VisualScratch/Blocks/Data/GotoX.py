from ClassSystem.Scratch import *
from ClassSystem.Color import *
from ClassSystem.BlockSys import *
from ClassSystem.ScriptBlock import ScriptBlock
class ScriptBlockPython(ScriptBlock):
    def __init__(self, _Sys=None):
        ScriptBlock.__init__(self,_Sys)
        self.Onglet="Mouvement"
        self.TypeForme="Rectangle"
        self.Texte="Aller aux coordonnées X"
        self.Parametres=[['Label', 'aller a x:'], ['EmptyCercle']]
        self.Color=Couleurs.bleu_fonce
        self.Compile="GotoX"
        self.Options = []
        self.SelfGetForme = None
        self.Image = None

    def WhenCompileForCasio(self,lst):
        code = "this->gameObject->transform->position->x = " + self.BlockSys.GetParametre(lst,0) + ";\n"
        code += self.BlockSys.GetSuite(lst, 0)
        return code
    
