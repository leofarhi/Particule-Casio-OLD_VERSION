from ClassSystem.Scratch import *
from ClassSystem.Color import *
from ClassSystem.BlockSys import *
from ClassSystem.ScriptBlock import ScriptBlock
class ScriptBlockPython(ScriptBlock):
    def __init__(self, _Sys=None):
        ScriptBlock.__init__(self,_Sys)
        self.Onglet="Editeur"
        self.TypeForme="Rectangle"
        self.Texte="Utiliser une Image"
        self.Parametres=[['Label', "J'utilise l'image :"], ["Liste",[] ]]
        self.Color=Couleurs.rose
        self.Compile="UseImage"
        self.Options = []
        self.SelfGetForme = None
        self.Image = None


    