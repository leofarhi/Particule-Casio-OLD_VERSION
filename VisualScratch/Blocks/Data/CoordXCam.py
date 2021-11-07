from ClassSystem.Scratch import *
from ClassSystem.Color import *
from ClassSystem.BlockSys import *
from ClassSystem.ScriptBlock import ScriptBlock
class ScriptBlockPython(ScriptBlock):
    def __init__(self, _Sys=None):
        ScriptBlock.__init__(self,_Sys)
        self.Onglet="Capteurs"
        self.TypeForme="Cercle"
        self.Texte="Position X de la Camera"
        self.Parametres=[['Label', 'Position X de la Camera']]
        self.Color=Couleurs.bleu_clair
        self.Compile="CoordXCam"
        self.Options = []
        self.SelfGetForme = None
        self.Image = None


    def WhenCompileForCasio(self,lst):
        code = "gameObject->scene->AllCameras[0]->gameObject->transform->localPosition->x"
        return code
    
