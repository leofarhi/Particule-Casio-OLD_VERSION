from ClassSystem.Scratch import *
from ClassSystem.Color import *
from ClassSystem.BlockSys import *
from ClassSystem.ScriptBlock import ScriptBlock
class ScriptBlockPython(ScriptBlock):
    def __init__(self, _Sys=None):
        ScriptBlock.__init__(self,_Sys)
        self.Onglet="Evenements"
        self.TypeForme="Vague"
        self.Texte="Quand je recois le message"
        self.Parametres=[["Label","Quand je recois"],["TexteEtNombre"]]
        self.Color=Couleurs.jaune
        self.Compile="WhenReceiveMessage"
        self.Options = []
        self.SelfGetForme = None
        self.Image = None
