from ClassSystem.Scratch import *
from ClassSystem.Color import *
from ClassSystem.BlockSys import *
from ClassSystem.ScriptBlock import ScriptBlock
class ScriptBlockPython(ScriptBlock):
    def __init__(self, _Sys=None):
        ScriptBlock.__init__(self,_Sys)
        self.Onglet="Controle"
        self.TypeForme="EndBox"
        self.Texte="Stoper ce script ou tout"
        self.Parametres=[["Label","Stoper "],["Liste",["Ce script","Tout"] ]]
        self.Color=Couleurs.orange
        self.Compile="Stop"
        self.Options = []
        self.SelfGetForme = None
        self.Image = None


    