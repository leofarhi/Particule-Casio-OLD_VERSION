from ClassSystem.Scratch import *
from ClassSystem.Color import *
from ClassSystem.BlockSys import *
from ClassSystem.ScriptBlock import ScriptBlock
class ScriptBlockPython(ScriptBlock):
    def __init__(self, _Sys=None):
        ScriptBlock.__init__(self,_Sys)
        self.Onglet="Mes Blocs"
        self.TypeForme="Cercle"
        self.Texte="Récupérer le Component"
        self.Parametres=[['Label', 'Récupérer le Component :'],['TexteEtNombre', '']]
        self.Color=Couleurs.jaune
        self.Compile="MyCMDGetComponent"
        self.Options = []
        self.SelfGetForme = None
        self.Image = None



    def WhenCompileForCasio(self,lst):
        TYPE = str(self.BlockSys.GetVariable(lst, 0)[1])
        code='(('+TYPE+' *)this->gameObject->GetComponent("'+TYPE+'"))'
        return code
    
