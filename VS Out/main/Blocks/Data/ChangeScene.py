from ClassSystem.Scratch import *
from ClassSystem.Color import *
from ClassSystem.BlockSys import *
from ClassSystem.ScriptBlock import ScriptBlock
class ScriptBlockPython(ScriptBlock):
    def __init__(self, _Sys=None):
        ScriptBlock.__init__(self,_Sys)
        self.Onglet="Capteurs"
        self.TypeForme="Rectangle"
        self.Texte="Changer la scene"
        self.Parametres=[["Label","Charger la scene"],["TexteEtNombre"]]
        self.Color=Couleurs.bleu_clair
        self.Compile="ChangeScene"
        self.Options = []
        self.SelfGetForme = None
        self.Image = None

    