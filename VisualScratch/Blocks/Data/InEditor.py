from ClassSystem.Scratch import *
from ClassSystem.Color import *
from ClassSystem.BlockSys import *
from ClassSystem.ScriptBlock import ScriptBlock
import os
class ScriptBlockPython(ScriptBlock):
    def __init__(self, _Sys=None):
        ScriptBlock.__init__(self,_Sys)
        self.Onglet="Editeur"
        self.TypeForme="Vague"
        self.Texte="Dans l'Editeur"
        self.Parametres=[['Label', "Dans l'Editeur"]]
        self.Color=Couleurs.rose
        self.Compile="InEditor"
        self.Options = []
        self.SelfGetForme = None
        self.Image = None

    #Pour Particule :
    def WhenCompileForPython(self,lst,base):
        code = self.BlockSys.GetSuitePython(lst,base,0)
        code = code.replace("$$Attributs","")
        #code = code.replace("$$ComponentName", "Error")
        code = code.replace("$$AttVisible", "")
        code = code.replace("$$DataSave", "")
        code = code.replace("$$DataLoad", "")
        if self.Sys.Hierarchy.currentSelection != None:
            name = self.Sys.Hierarchy.currentSelection
            name = os.path.basename(name)
            name = os.path.splitext(name)[0]
            code = code.replace("$$ComponentName", name)
        return code

    #Pour Casio
    def WhenCompileForCasio(self,lst):
        if self.Sys.Hierarchy.currentSelection == None:
            return ""
        name = self.Sys.Hierarchy.currentSelection
        name = os.path.basename(name)
        name = os.path.splitext(name)[0]

        suite = self.BlockSys.GetSuite(lst,0)
        GetPublic = []
        temp=suite.split("&&Public:")
        for i in temp:
            if ":Public&&" in i:
                GetPublic.append((i.split(":Public&&")[0]).split(":Type:"))
        GetPrivate = []
        temp = suite.split("&&Private:")
        for i in temp:
            if ":Private&&" in i:
                GetPrivate.append((i.split(":Private&&")[0]).split(":Type:"))


        etoile = self.BlockSys.Etoile

        public = ""
        for i in GetPublic:
            type = i[1]
            if not type in etoile:
                type+="*"
            public += type + " " + i[0]+";\n"
        private = ""
        for i in GetPrivate:
            type = i[1]
            if not type in etoile:
                type += "*"
            private += type + " " + i[0] + ";\n"

        listInit=","
        for i in GetPublic:
            type = i[1]
            if not type in etoile:
                type += "*"
            listInit += type + " " + i[0] + ","

        initPrivate=""
        for i in GetPrivate:
            initPrivate += "this->" + i[0] + "=" + self.BlockSys.GetInitValueAttributCasio(i[1]) + ";\n"

        initPublic=""
        for i in GetPublic:
            initPublic+="this->"+i[0]+"="+i[0]+";\n"

        initPublic+=initPrivate

        code = "class "+ name+""" : MonoBehaviour {
private:
    """+private+"""
public:
    """+public+"""
    """+name+'(GameObject* gameObject '+listInit+' int UUID = NULL) : MonoBehaviour("'+name+'''", gameObject, UUID) {
        '''+initPublic+'''
    };
    
    //&&Fonction
};'''
        return code

    