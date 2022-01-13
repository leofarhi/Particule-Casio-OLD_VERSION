from CppEditor.ParticuleScript import *
class BaseBlockScript:
    def __init__(self,boxScript):
        self.boxScript=boxScript

    def GUI_Print(self):
        pass

    def GetDataDico(self):
        pass

    def GetCppScript(self):
        pass

    def AddBoxScript(self):
        BoxScript(self.boxScript.particuleScript.ScriptFrame, self.boxScript.particuleScript)
        self.boxScript.particuleScript.BoxScripts