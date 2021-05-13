from ClassSystem.Scratch import *
from ClassSystem.Color import *
from ClassSystem.BlockSys import *
from ClassSystem.ScriptBlock import ScriptBlock
class ScriptBlockPython(ScriptBlock):
    def __init__(self, _Sys=None):
        ScriptBlock.__init__(self,_Sys)
        self.Onglet="Evenements"
        self.TypeForme="Rectangle"
        self.Texte="envoyer a tous message"
        self.Parametres=[["Label","envoyer a tous "],["TexteEtNombre","message1"]]
        self.Color=Couleurs.jaune
        self.Compile="BroadcastMessage"
        self.Options = []
        self.SelfGetForme = None
        self.Image = None

    