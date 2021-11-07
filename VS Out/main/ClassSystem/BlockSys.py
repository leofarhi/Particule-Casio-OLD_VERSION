from inspect import isclass
from pkgutil import iter_modules
import pkgutil
from pathlib import Path
from importlib import import_module
import importlib.util
import os,sys
class BlockSys:
    def __init__(self,_Sys):
        self.Sys = _Sys
        path = "Blocks/Data/"
        for (_, module_name, _) in iter_modules([path]):

            # import the module and iterate through its attributes
            module = import_module(f"Blocks.Data.{module_name}")
            for attribute_name in dir(module):
                attribute = getattr(module, attribute_name)

                if isclass(attribute):
                    # Add the class to this package's variables
                    globals()[attribute_name] = attribute
                    # print(attribute_name)
    def GetCode(self,lst):
        #global _i
        if lst==[]:
            return ""
        if lst==None:
            return "true"
        try:
            for i in range(4):
                lst[2].append([])
        except:
            pass
        _i=lst
        Block = _i[0]
        file = "Blocks/Data/" + Block + ".py"
        spec = importlib.util.spec_from_file_location(Block, file)
        module = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = module
        spec.loader.exec_module(module)
        PythonScript = getattr(module, "ScriptBlockPython")(self.Sys)
        #print(module)
        _i = PythonScript.WhenCompileForCasio(_i)
        #eval(compile("_i="+_i[0]+"(_i)", '<string>', 'exec'),globals(),globals())
        return _i

    def GetCodePython(self,lst,base):
        #global _i
        if lst==[]:
            return base
        if lst==None:
            return base
        try:
            for i in range(4):
                lst[2].append([])
        except:
            pass
        _i=lst
        Block = _i[0]
        file = "Blocks/Data/" + Block + ".py"
        spec = importlib.util.spec_from_file_location(Block, file)
        module = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = module
        spec.loader.exec_module(module)
        PythonScript = getattr(module, "ScriptBlockPython")(self.Sys)
        _i = PythonScript.WhenCompileForPython(_i,base)
        #eval(compile("_i="+_i[0]+"(_i)", '<string>', 'exec'),globals(),globals())
        return _i


    def GetParametre(self,lst,index):
        return self.GetCode((lst[1])[index])
    def GetVariable(self,lst,index):
        return ((lst[1])[index])
    def GetSuite(self,lst,index):
        return self.GetCode((lst[2])[index])
    def GetSuitePython(self,lst,base,index):
        return self.GetCodePython((lst[2])[index],base)

    TypeAttributs = ["int","float","string","bool","Vector2","Texture"]
    def GetInitValueAttributPython(self,Type):
        if Type == "int":
            return "0"
        elif Type == "float":
            return "0"
        elif Type == "string":
            return '""'
        elif Type == "bool":
            return "False"
        elif Type == "Vector2":
            return "Vector2()"
        elif Type == "Texture":
            return 'Texture(self.Particule,name="None")'
    def GetSaveValueAttributPython(self,Type,name):
        if Type in ["int","float","string","bool"]:
            return '"'+name+'":self.'+name
        elif Type == "Vector2":
            return '"'+name+'":self.'+name+".get()"
        elif Type == "Texture":
            return '"'+name+'":self.'+name+".path"
    def GetSetTypeDicoPython(self,Type):
        if Type == "int":
            return '{"Type":int}'
        elif Type == "float":
            return '{"Type":float}'
        elif Type == "string":
            return '{"Type":str}'
        elif Type == "bool":
            return '{"Type":bool}'
        elif Type == "Vector2":
            return '{"Type":Vector2}'
        elif Type == "Texture":
            return '{"Type":Texture}'
        elif Type == "list(int)":
            return '{"Type":list,"LstValueType":int,"LstType":"List"}'
        elif Type == "array(int)":
            return '{"Type":list,"LstValueType":int,"LstType":"Array"}'
    def GetLoadValueAttributPython(self,Type,name):
        if Type in ["int","float","string","bool"]:
            return 'self.'+name+'= dataCompo["'+name+'"]'
        elif Type == "Vector2":
            return 'self.'+name+'= Vector2.set(Vector2(),dataCompo["'+name+'"])'
        elif Type == "Texture":
            return 'self.'+name+'= Texture(self.Particule,Path=dataCompo["'+name+'"],name=os.path.basename(dataCompo["'+name+'"]))'
    def GetInitValueAttributCasio(self,Type):
        if Type == "int":
            return "0"
        elif Type == "float":
            return "0"
        elif Type == "string":
            return '""'
        elif Type == "bool":
            return "false"
        elif Type == "Vector2":
            return "new Vector2()"
        elif Type == "Texture":
            return 'new Texture()'

    def GetTypeValueAttributCasio(self,Type):
        if Type in ["int","float","bool","Vector2"]:
            return Type
        elif Type=="string":
            return "unsigned char*"
        else:
            return Type+"*"
