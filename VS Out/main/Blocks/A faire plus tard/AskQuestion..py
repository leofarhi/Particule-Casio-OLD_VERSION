from ClassSystem.Scratch import *
from ClassSystem.Color import *
from ClassSystem.BlockSys import *
from ClassSystem.ScriptBlock import ScriptBlock
class ScriptBlockPython(ScriptBlock):
    def __init__(self, _Sys=None):
        ScriptBlock.__init__(self,_Sys)
        self.Onglet="Capteurs"
        self.TypeForme="Cercle"
        self.Texte="Poser une question"
        self.Parametres=[["Label","Demander : "],['EmptyCercle'],["Label"," et attendre"]]
        self.Color=Couleurs.rose
        self.Compile="AskQuestion"
        self.Options = []
        self.SelfGetForme = None
        self.Image = None

    
