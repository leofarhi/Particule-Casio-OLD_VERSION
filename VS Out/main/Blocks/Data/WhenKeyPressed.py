from ClassSystem.Scratch import *
from ClassSystem.Color import *
from ClassSystem.BlockSys import *
from ClassSystem.ScriptBlock import ScriptBlock
class ScriptBlockPython(ScriptBlock):
    def __init__(self, _Sys=None):
        ScriptBlock.__init__(self,_Sys)
        self.Onglet="Capteurs"
        self.TypeForme="Losange"
        self.Texte="Quand la touche ? est presse"
        self.Parametres=[["Label","Quand la touche "],["Liste",["CHAR_0","CHAR_1","CHAR_2","CHAR_3","CHAR_4","CHAR_5","CHAR_6","CHAR_7","CHAR_8","CHAR_9","CHAR_DP","CHAR_EXP","CHAR_PMINUS","CHAR_PLUS","CHAR_MINUS","CHAR_MULT","CHAR_DIV","CHAR_FRAC","CHAR_LPAR","CHAR_RPAR","CHAR_COMMA","CHAR_STORE","CHAR_LOG","CHAR_LN","CHAR_SIN","CHAR_COS","CHAR_TAN","CHAR_SQUARE","CHAR_POW","CTRL_EXE","CTRL_DEL","CTRL_AC","CTRL_FD","CTRL_EXIT","CTRL_SHIFT","CTRL_ALPHA","CTRL_OPTN","CTRL_VARS","CTRL_UP","CTRL_DOWN","CTRL_LEFT","CTRL_RIGHT","CTRL_F1","CTRL_F2","CTRL_F3","CTRL_F4","CTRL_F5","CTRL_F6","CTRL_MENU"] ],["Label","est presse"]]
        self.Color=Couleurs.bleu_clair
        self.Compile="WhenKeyPressed"
        self.Options = []
        self.SelfGetForme = None
        self.Image = None


    def WhenCompileForCasio(self,lst):
        code = "IsKeyDown(KEY_" + self.BlockSys.GetVariable(lst,0)[2] + ")"
        return code
    