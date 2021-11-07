from ClassSystem.Scratch import *
from ClassSystem.Color import *
from ClassSystem.BlockSys import *
from ClassSystem.ScriptBlock import ScriptBlock
class ScriptBlockPython(ScriptBlock):
    def __init__(self, _Sys=None):
        ScriptBlock.__init__(self,_Sys)
        self.Onglet="Opérateurs"
        self.TypeForme="Rectangle"
        self.Texte="Convertit Int/Float/string"
        self.Parametres=[['Label', 'Convertir '],['EmptyCercle'],['Label', 'qui est un '],
                         ["Liste",["int","float","string"] ],['Label', 'en '],
                         ["Liste",["int","float","string"] ],
                         ['Label', "d'une longueur de "],['TexteEtNombre', '80'],
                         ['Label', 'sauvegardé dans '],["Liste",[]]]
        self.Color=Couleurs.vert
        self.Compile="OperatorConvertType"
        self.Options = []
        self.SelfGetForme = None
        self.Image = None


    def WhenUpdate(self):
        (self.SelfGetForme.Parametres[9])[1]=self._Sys.Scratch.ActuVarible


    def WhenCompileForCasio(self,lst):
        val = self.BlockSys.GetParametre(lst,0)
        From = str(self.BlockSys.GetVariable(lst, 1)[2])
        To = str(self.BlockSys.GetVariable(lst, 2)[2])
        size = str(self.BlockSys.GetVariable(lst, 3)[1])
        var = str(self.BlockSys.GetVariable(lst, 4)[2])
        #print(val,From,To,size,var)
        if From=="int":
            if To=="int":
                code=""
            elif To=="float":
                code = var+" = (float)"+val+";\n"
            else :
                code = var + " = new unsigned char[" + str(size) + "];\n"
                code+='sprintf((char*)'+var+', "%d", '+val+');\n'
        elif From=="float":
            if To=="int":
                code= var+" = (int)"+val+";\n"
            elif To=="float":
                code = ""
            else :
                code = var + " = new unsigned char[" + str(size) + "];\n"
                code+='sprintf((char*)'+var+', "%f", '+val+');\n'
        else :
            if To=="int":
                code= 'sscanf((const char*)'+val+', "%d", &'+var+');\n'
            elif To=="float":
                code = 'sscanf((const char*)'+val+', "%f", &'+var+');\n'
            else :
                code=""

        code += self.BlockSys.GetSuite(lst, 0)
        return code