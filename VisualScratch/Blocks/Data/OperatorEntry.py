from ClassSystem.Scratch import *
from ClassSystem.Color import *
from ClassSystem.BlockSys import *
from ClassSystem.ScriptBlock import ScriptBlock
class ScriptBlockPython(ScriptBlock):
    def __init__(self, _Sys=None):
        ScriptBlock.__init__(self,_Sys)
        self.Onglet="Opérateurs"
        self.TypeForme="Cercle"
        self.Texte="Zone de texte"
        self.Parametres=[['TexteEtNombre', '']]
        self.Color=Couleurs.vert
        self.Compile="OperatorEntry"
        self.Options = []
        self.SelfGetForme = None
        self.Image = None



    def WhenCompileForCasio(self,lst):
        code = ""
        temp = str(self.BlockSys.GetVariable(lst,0)[1])
        if temp[0]=='"' or temp[-1]=='"':
            code += "(unsigned char*)"+str(temp)
            return code
        try:
            temp_ = int(temp)
            code += str(temp_)
        except:
            try:
                temp_ = float(temp.replace(",", "."))
                code += str(temp_)
            except:
                code += "(unsigned char*)"+'"' + temp + '"'
        return code
    
