from ClassSystem.Scratch import *
from ClassSystem.Color import *
from ClassSystem.BlockSys import *
from ClassSystem.ScriptBlock import ScriptBlock
class ScriptBlockPython(ScriptBlock):
    def __init__(self, _Sys=None):
        ScriptBlock.__init__(self,_Sys)
        self.Onglet="Capteurs"
        self.TypeForme="Losange"
        self.Texte="Touche L'element ?"
        self.Parametres=[["Label","touche le"],["Liste",["Sprite","Bord"]]]
        self.Color=Couleurs.bleu_clair
        self.Compile="TouchingElement"
        self.Options = []
        self.SelfGetForme = None
        self.Image = None


    