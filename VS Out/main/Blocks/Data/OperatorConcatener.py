from ClassSystem.Scratch import *
from ClassSystem.Color import *
from ClassSystem.BlockSys import *
from ClassSystem.ScriptBlock import ScriptBlock
class ScriptBlockPython(ScriptBlock):
    def __init__(self, _Sys=None):
        ScriptBlock.__init__(self,_Sys)
        self.Onglet="Opérateurs"
        self.TypeForme="Rectangle"
        self.Texte="Concatener deux string"
        self.Parametres=[['Label', 'regrouper '],['EmptyCercle'],['Label', 'et'],
                         ['EmptyCercle'],['Label', "d'une longueur de "],['TexteEtNombre', '80'],
                         ['Label', 'sauvegardé dans '],["Liste",[]]]
        self.Color=Couleurs.vert
        self.Compile="OperatorConcatener"
        self.Options = []
        self.SelfGetForme = None
        self.Image = None

    def WhenUpdate(self):
        (self.SelfGetForme.Parametres[7])[1]=self._Sys.Scratch.ActuVarible


    def WhenCompileForCasio(self,lst):

        var=str(self.BlockSys.GetVariable(lst, 3)[2])
        code=var+" = new unsigned char["+str(self.BlockSys.GetVariable(lst,2)[1])+"];\n"
        code +='strcpy((char*)'+var+',(const char*) '+self.BlockSys.GetParametre(lst,0)+');\n'
        code += 'strcat((char*)' + var + ',(const char*) ' + self.BlockSys.GetParametre(lst, 1) + ');\n'
        code += self.BlockSys.GetSuite(lst, 0)
        return code
