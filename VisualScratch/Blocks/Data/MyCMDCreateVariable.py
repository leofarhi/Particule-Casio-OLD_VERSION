from ClassSystem.Scratch import *
from ClassSystem.Color import *
from ClassSystem.BlockSys import *
from ClassSystem.ScriptBlock import ScriptBlock
class ScriptBlockPython(ScriptBlock):
    def __init__(self, _Sys=None):
        ScriptBlock.__init__(self,_Sys)
        self.Onglet="Mes Blocs"
        self.TypeForme="Rectangle"
        self.Texte="Creer une variable personnalisé"
        self.Parametres=[['Label', 'Creer une variable'], ['TexteEtNombre', ''], ['Label', 'de type'], ['TexteEtNombre', ''],['Label', 'de façon priver']]
        self.Color=Couleurs.jaune
        self.Compile="MyCMDCreateVariable"
        self.Options = []
        self.SelfGetForme = None
        self.Image = None

        self.VariableName=""
        self.LastVariableName=""

    def WhenUpdate(self):
        try:
            self.VariableName = (self.SelfGetForme.Parametres[1])[1].get()
        except:
            return
        if self.VariableName!="":
            if self.VariableName!=self.LastVariableName:
                if self.LastVariableName in self._Sys.Scratch.ActuVarible:
                    self._Sys.Scratch.ActuVarible.remove(self.LastVariableName)
                self.LastVariableName=self.VariableName
                self._Sys.Scratch.ActuVarible.append(self.VariableName)


    #Pour Particule :
    def WhenCompileForPython(self,lst,base):
        TYPE=str(self.BlockSys.GetVariable(lst,1)[1])
        VarSetType = 'self.TypeVariables["'+str(self.BlockSys.GetVariable(lst,0)[1])+'"] = '+'{"Type":"'+TYPE+'"}'
        line = "self."+str(self.BlockSys.GetVariable(lst,0)[1])+"= None"+"""
        """+VarSetType+"""
        $$Attributs"""
        code = base.replace("$$Attributs",line)
        code = self.BlockSys.GetSuitePython(lst, code, 0)
        return code

    def WhenCompileForCasio(self, lst):
        TYPE = str(self.BlockSys.GetVariable(lst, 1)[1])
        code = "&&Private:" + str(self.BlockSys.GetVariable(lst, 0)[1]) +":Type:"+TYPE+ ":Private&&\n"
        code += self.BlockSys.GetSuite(lst,0)
        return code
    
