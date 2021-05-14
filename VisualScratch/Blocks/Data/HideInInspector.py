from ClassSystem.Scratch import *
from ClassSystem.Color import *
from ClassSystem.BlockSys import *
from ClassSystem.ScriptBlock import ScriptBlock
class ScriptBlockPython(ScriptBlock):
    def __init__(self, _Sys=None):
        ScriptBlock.__init__(self,_Sys)
        self.Onglet="Editeur"
        self.TypeForme="Encadrement"
        self.Texte="Cacher dans l'editeur"
        self.Parametres=[["Label","Cacher dans l'editeur"]]
        self.Color=Couleurs.rose
        self.Compile="HideInInspector"
        self.Options = []
        self.SelfGetForme = None
        self.Image = None

    
