from ClassSystem.Scratch import *
from ClassSystem.Color import *
from ClassSystem.BlockSys import *
from ClassSystem.ScriptBlock import ScriptBlock
class ScriptBlockPython(ScriptBlock):
    def __init__(self, _Sys=None):
        ScriptBlock.__init__(self,_Sys)
        self.Onglet="Editeur"
        self.TypeForme="Rectangle"
        self.Texte="Creer une variable"
        self.Parametres=[['Label', 'Creer une variable'], ['TexteEtNombre', ''], ['Label', 'de type'], ["Liste",[] ],['Label', 'de façon'],["Liste",["public","priver"] ]]
        self.Color=Couleurs.rose
        self.Compile="CreateVariable"
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

    def WhenAdded(self):
        (self.SelfGetForme.Parametres[3])[1]=self.BlockSys.TypeAttributs

    #Pour Particule :
    def WhenCompileForPython(self,lst,base):
        line = "self."+str(self.BlockSys.GetVariable(lst,0)[1])+"= "+self.BlockSys.GetInitValueAttributPython(str(self.BlockSys.GetVariable(lst,1)[2]))+"""
        $$Attributs"""
        code = base.replace("$$Attributs",line)
        if self.BlockSys.GetVariable(lst,2)[2] == "public":
            code = code.replace("$$AttVisible", '"'+str(self.BlockSys.GetVariable(lst,0)[1])+'"'+",$$AttVisible")
            code = code.replace("$$DataSave", self.BlockSys.GetSaveValueAttributPython(str(self.BlockSys.GetVariable(lst,1)[2]),str(self.BlockSys.GetVariable(lst,0)[1])) + ",$$DataSave")
            line2=self.BlockSys.GetLoadValueAttributPython(str(self.BlockSys.GetVariable(lst,1)[2]),str(self.BlockSys.GetVariable(lst,0)[1]))+"""
        $$DataLoad"""
            code = code.replace("$$DataLoad",line2)
        code = self.BlockSys.GetSuitePython(lst, code, 0)
        return code

    def WhenCompileForCasio(self, lst):
        if self.BlockSys.GetVariable(lst,2)[2] == "public":
            code = "&&Public:"+str(self.BlockSys.GetVariable(lst,0)[1])+":Type:"+str(self.BlockSys.GetVariable(lst,1)[2])+":Public&&\n"
        else:
            code = "&&Private:" + str(self.BlockSys.GetVariable(lst, 0)[1]) +":Type:"+str(self.BlockSys.GetVariable(lst,1)[2])+ ":Private&&\n"
        code += self.BlockSys.GetSuite(lst,0)
        return code
    
