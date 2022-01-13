import os,sys
from CppEditor.ParseHpp import CasioComponent
import json

class VisualScratch:
    def __init__(self,pathFile):
        self.pathFile = pathFile
        self.component = CasioComponent()
        self.component.Load(pathFile)

    def CompileScript(self, *args):
        return (self.GeneratePythonCode(),self.GenerateCasioCode())

    def GeneratePythonCode(self):
        with open("lib/ComponentBase.py", "r") as fic:
            base = fic.read()
        base = self.CplPythonInEditor(base)
        return base

    def GenerateCasioCode(self):
        return self.component.SaveHppCpp()

    def CplPythonInEditor(self,code):
        for i in self.component.Variables:
            if i["IsArray"] or i["IsList"]:
                code = self.CplPythonCreateVariableList(i,code)
            else:
                code = self.CplPythonCreateVariable(i,code)
        code = code.replace("$$Attributs","")
        #code = code.replace("$$ComponentName", "Error")
        code = code.replace("$$AttVisible", "")
        code = code.replace("$$DataSave", "")
        code = code.replace("$$DataLoad", "")
        code = code.replace("$$ComponentName", self.component.NameComponent)
        return code

    def CplPythonCreateVariable(self,lst,base):
        VarSetType = 'self.TypeVariables["'+str(lst["Name"])+'"] = '+self.GetSetTypeDicoPython(str(lst["Type"]))
        line = "self."+str(lst["Name"])+"= "+self.GetInitValueAttributPython(str(lst["Type"]))+"""
        """+VarSetType+"""
        $$Attributs"""
        code = base.replace("$$Attributs",line)
        if lst["Public-Private"] == "Public":
            code = code.replace("$$AttVisible", '"'+str(lst["Name"])+'"'+",$$AttVisible")
            code = code.replace("$$DataSave", self.GetSaveValueAttributPython(str(lst["Type"]),str(lst["Name"])) + ",\n$$DataSave")
            line2=self.GetLoadValueAttributPython(str(lst["Type"]),str(lst["Name"]))+"""
        $$DataLoad"""
            code = code.replace("$$DataLoad",line2)
        return code

    def CplPythonCreateVariableList(self,lst,base):
        TypeVar = lst["Type"]
        if lst["IsArray"]:
            TypeVar = TypeVar[:-1]
            info = "Array" + "<" + str(TypeVar) + ">"
        if lst["IsList"]:
            info = TypeVar
        VarSetType = 'self.TypeVariables["'+str(lst["Name"])+'"] = '+self.GetSetTypeDicoPython(str(info))
        line = "self."+str(lst["Name"])+"= []"+"""
        """+VarSetType+"""
        $$Attributs"""
        code = base.replace("$$Attributs",line)
        if lst["Public-Private"] == "Public":
            code = code.replace("$$AttVisible", '"'+str(lst["Name"])+'"'+",$$AttVisible")
            code = code.replace("$$DataSave", self.GetSaveValueAttributPython(str(TypeVar),str(lst["Name"])) + ",\n$$DataSave")
            line2=self.GetLoadValueAttributPython(str(TypeVar),str(lst["Name"]))+"""
        $$DataLoad"""
            code = code.replace("$$DataLoad",line2)
        return code

    def GetSetTypeDicoPython(self,Type):
        if Type == "int":
            return '{"Type":int}'
        elif Type == "float":
            return '{"Type":float}'
        elif Type == "unsigned char*":
            return '{"Type":str}'
        elif Type == "bool":
            return '{"Type":bool}'
        elif Type == "Vector2*":
            return '{"Type":Vector2}'
        elif Type == "Texture*":
            return '{"Type":Texture}'
        elif Type[:4]=='List':
            return '{"Type":list,"LstValueType":'+\
                   self.GetSetTypeDicoPython(((Type.split("<",1)[1]).split(">",1)[0]))+',"LstType":"List"}'
        elif Type[:5]=='Array':
            return '{"Type":list,"LstValueType":'+\
                   self.GetSetTypeDicoPython(((Type.split("<",1)[1]).split(">",1)[0]))+',"LstType":"Array"}'
        else:
            return '{"Type":self.GetTypeObject("'+Type+'")}'
    def GetInitValueAttributPython(self,Type):
        if Type == "int":
            return "0"
        elif Type == "float":
            return "0"
        elif Type == "unsigned char*":
            return '""'
        elif Type == "bool":
            return "False"
        elif Type == "Vector2*":
            return "Vector2()"
        elif Type == "Texture*":
            return 'self.texture = self.Particule.FolderWindow.TextureVide'
        elif Type[:4] == 'List' or Type[:5] == 'Array':
            return "[]"
        elif Type[:14] == 'ParticuleEvent':
            return 'ParticuleEvent(templateID="T")'
        else:
            return "None"
    def GetSaveValueAttributPython(self,Type,name):
        if Type in ["int","float","unsigned char*","bool"]:
            return '"'+name+'":self.'+name
        elif Type == "Vector2*":
            return '"'+name+'":self.'+name+".get()"
        elif Type == "Texture*":
            return '"'+name+'":self.'+name+".ID"
        elif Type[:4] == 'List' or Type[:5]=='Array':
            return '"' + name + '":self.' + name
        elif Type[:14] == 'ParticuleEvent':
            return '"'+name+'":self.'+name+".get()"
        else:
            return '"'+name+'":self.try_or(lambda: self.'+name+'.ID, default=None)'
    def GetLoadValueAttributPython(self,Type,name):
        if Type in ["int","float","unsigned char*","bool"]:
            return 'self.'+name+'= dataCompo["'+name+'"]'
        elif Type == "Vector2*":
            return 'self.'+name+'= Vector2.set(Vector2(),dataCompo["'+name+'"])'
        elif Type == "Texture*":
            return 'self.'+name+'= self.Particule.GetTextureUUID(dataCompo["'+name+'"])'
        elif Type[:4] == 'List' or Type[:5]=='Array':
            return 'self.'+name+'= dataCompo["'+name+'"]'
        elif Type[:14] == 'ParticuleEvent':
            return 'self.'+name+'= '+\
                   'ParticuleEvent(self.try_or(lambda:self.Particule.GetObjectWithUUID((dataCompo["'+name+'"])[0]), default=None),' \
                                            '(dataCompo["'+name+'"])[1],(dataCompo["'+name+'"])[2])'
        else:
            return 'self.'+name+'= self.try_or(lambda:self.Particule.GetObjectWithUUID(dataCompo["'+name+'"]), default=None)'

def CompileSLN(PathSLN):
    with open(PathSLN, "r") as fic:
        dataSLN = fic.read()
    SLN = json.loads(dataSLN)
    ALLfiles = SLN["Files"]
    AllScriptPython=[]
    AllScriptCasio=[]
    for i in ALLfiles:
        temp = VisualScratch(i)
        AllScriptPython.append((i,temp.GeneratePythonCode()))
        AllScriptCasio.append((i,temp.GenerateCasioCode()))
    return (AllScriptPython,AllScriptCasio)