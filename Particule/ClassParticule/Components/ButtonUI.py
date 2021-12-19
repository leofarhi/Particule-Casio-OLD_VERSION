from Particule import *
from ClassParticule.Component import Component
from ClassParticule.Vector2 import Vector2
from ClassParticule.Components.Sprite import Sprite
from ClassParticule.Texture import Texture
class ButtonUI(Component):
    def __init__(self,gameObject,**kwargs):
        Component.__init__(self, gameObject, __name__.split(".")[-1],**kwargs)

        self.NormalTexture = self.Particule.FolderWindow.TextureVide
        self.HighlightedTexture = self.Particule.FolderWindow.TextureVide

        ################################
        self.functionClass = "Object"
        self.functionParam = ""
        self.FindGameObjectName = ""

        self.TypeVariables.update({"functionClass": {"Type": str},
                                   "functionParam": {"Type": str},
                                   "FindGameObjectName": {"Type": str},
                                   "NormalTexture": {"Type": Texture},
                                   "HighlightedTexture": {"Type": Texture}})
        self.AttributVisible = ["functionClass", "functionParam","FindGameObjectName","NormalTexture","HighlightedTexture"]
        ################################

        self.SpriteCompo = self.gameObject.GetComponent(Sprite)

    def UpdateOnGUI(self):
        if self.SpriteCompo==None:
            self.SpriteCompo = self.gameObject.GetComponent(Sprite)
            if self.SpriteCompo != None:
                self.Size = Vector2(self.SpriteCompo.width, self.SpriteCompo.height)
                self.Center = Vector2(self.SpriteCompo.width // 2, self.SpriteCompo.height // 2)

    def BuildValue(self):
        #################
        if self.FindGameObjectName=="":
            self.FindGameObjectName=self.gameObject.name
        gmObj = self.Particule.Hierarchy.FindWithName(self.FindGameObjectName)
        ####################

        classCompo = getattr(sys.modules['Particule'], self.functionClass)
        self.ComponentParam = gmObj.GetComponent(classCompo)

        initV= "ButtonUI<"+self.functionClass+">"+"* "+self.ID+";\n"
        ResteParametre = self.GetParam(["NormalTexture","HighlightedTexture"])

        setParam = self.ID+" = new ButtonUI<"+self.functionClass+">"+'('+self.gameObject.ID+ResteParametre+'"'+self.ID+'");\n'

        return (initV,setParam)

    def GetParam(self,AttributVisible):
        if type(self).__name__ == "Transform":
            return ("\n","\n")
        CodeBefore=""
        CodeAfter=""
        parametres=","
        for indexAtt,i in enumerate(AttributVisible):
            var = getattr(self,i)
            #print(var, i,eval("self."+i))
            dicoVar= self.TypeVariables[i]
            if dicoVar["Type"] in [int,float,str]:
                if dicoVar["Type"] is str:
                    parametres +='(unsigned char*)"'
                parametres+= str(var)
                if dicoVar["Type"] is str:
                    parametres+='"'
            elif dicoVar["Type"] is bool:
                parametres += str(var).lower()
            else:
                if dicoVar["Type"] is Vector2:
                    parametres+="new Vector2("+str(var.x)+","+str(var.y)+")"
                elif dicoVar["Type"] is Texture:
                    path = os.path.basename(var.path)
                    path = os.path.splitext(path)[0]
                    if (var.path=="Library/lib/vide.png"):
                        parametres +="Texture_TextureVide" #"new Texture()"
                    else:
                        parametres += "Texture_"+path
                elif dicoVar["Type"] is list:
                    typeRecur = (dicoVar["LstValueType"])['Type']
                    if typeRecur==list:
                        raise Exception("les listes de listes ne sont pas encore pris en compte")
                    elif dicoVar["LstType"]=="List":
                        code=""
                        for ind,o in enumerate(var):
                            if typeRecur==str:o = "(unsigned char*)"+'"' + str(o) + '"'
                            code +=str(self.ID)+"->"+str(i)+".Add("+str(o)+");\n"
                        CodeAfter += code
                        parametres += ""  # "
                        continue
                    elif dicoVar["LstType"]=="Array":
                        Etoile="*"
                        if not typeRecur in [int,float,str,bool]:
                            Etoile+="*"
                        Etoile += " "
                        code = "static "+typeRecur.__name__+Etoile+"Lst_"+str(i)+"_"+str(indexAtt)+"_"+str(self.ID)+\
                               "= new "+ typeRecur.__name__+(Etoile[:-2])+"["+str(len(var))+"];\n"
                        print(typeRecur)
                        for ind,o in enumerate(var):
                            if typeRecur == str: o = "(unsigned char*)"+'"' + str(o) + '"'
                            code+="Lst_"+str(i)+"_"+str(indexAtt)+"_"+str(self.ID)+"["+str(ind)+"] = "+str(o)+";\n"
                        code += str(self.ID) + "->" + str(i) +"="+"Lst_"+str(i)+"_"+str(indexAtt)+"_"+str(self.ID)+";\n"
                        CodeAfter+=code
                        parametres +=""#"Lst_"+str(i)+"_"+str(indexAtt)+"_"+str(self.ID)
                        continue
                else:
                    #print(eval("self."+i))
                    parametres +=var.ID
            parametres+=","
        return parametres

    def AddScriptAfterInitCasio(self):
        if self.functionParam!="":
            return self.ID+"->OnClick.Set((&"+self.functionClass+"::"+self.functionParam+"), "+self.ComponentParam.ID+");\n"
        return ""

    def SaveDataDict(self):
        data = Component.SaveDataDict(self)

        data.update({
            "functionClass": self.functionClass,
            "functionParam": self.functionParam,
            "FindGameObjectName": self.FindGameObjectName,
            "NormalTexture": self.NormalTexture.ID,
            "HighlightedTexture": self.HighlightedTexture.ID,
        })
        return data

    def LoadDataDict(self, data, component, dataCompo, dicoGameObject, dicoComponent):
        Component.LoadDataDict(self, data, component, dataCompo, dicoGameObject, dicoComponent)
        self.functionClass = dataCompo["functionClass"]
        self.functionParam = dataCompo["functionParam"]
        self.FindGameObjectName = dataCompo["FindGameObjectName"]
        self.NormalTexture = self.Particule.GetTextureUUID(dataCompo["NormalTexture"])
        self.HighlightedTexture = self.Particule.GetTextureUUID(dataCompo["HighlightedTexture"])