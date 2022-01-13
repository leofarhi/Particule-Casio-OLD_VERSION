from CppEditor.BaseBlockScript import BaseBlockScript

class While(BaseBlockScript):
    def __init__(self,boxScript):
        BaseBlockScript.__init__(self,boxScript)

    def GUI_Print(self):
        self.boxScript.Data["Affichage"]=["while"]

        self.boxScript.UpdateAll()

    def GetDataDico(self):
        pass

    def GetCppScript(self):
        pass