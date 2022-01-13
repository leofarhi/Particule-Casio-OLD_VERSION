
class CasioComponent:
    def __init__(self):
        self.Settings=[]
        self.NameComponent = ""
        self.Inheritance = "MonoBehaviour"
        self.Variables = []
        self.Methods = []
        self.Templates = []

    def Load(self,pathFile):
        with open(pathFile,"r") as fic:
            txt = fic.read()
        if not "#Editor C++" in txt:
            raise Exception("Ce code ne peut pas être décodé")
        code = (txt.split("class",1)[1]).split("{",1)[0]
        code = code.split(":")
        if len(code)!=2:
            self.Inheritance = None
        else:
            self.Inheritance = code[1].replace("public","").replace(" ","")
        self.NameComponent = code[0].replace("class","").replace(" ","")
        txt = (((txt.split("{",1)[1])[::-1]).split("}",1)[1])[::-1]

        code = (txt.split("//<InitVar>",1)[1]).split("//<\\InitVar>",1)[0]
        codePrivate= (code.split("//<PrivateVar>",1)[1]).split("//<\\PrivateVar>",1)[0]
        codePublic = (code.split("//<PublicVar>", 1)[1]).split("//<\\PublicVar>", 1)[0]
        codePrivate = codePrivate.split(";")
        codePublic = codePublic.split(";")
        codePrivate = [(i,False) for i in codePrivate]
        codePublic = [(i, True) for i in codePublic]
        code = codePrivate+codePublic
        self.Variables = []
        temp=[]
        for i in code:
            line = i[0]
            for o in range(100):
                line = line.replace("\n","").replace("\t","").replace("  "," ")
            line = line.replace(" * ", "* ").replace(" & ", "& ")
            line = line.replace(" *","* ").replace(" &","& ")
            line = line.replace("*", "* ").replace("&", "& ")
            line = line.replace("\n", "").replace("\t", "").replace("  ", " ")
            if line==" " or line=="":
                continue
            if line[0]==" ":
                line = line[1:]
            if line[-1]==" ":
                line = line[:-1]
            temp.append((line,i[1]))
        code = temp

        for i in code:
            line=i[0]
            dicoTemp={}
            dicoTemp["IsArray"] = "//Array" in line
            dicoTemp["IsList"] = "//List" in line
            dicoTemp["NotInInit"] = False
            if dicoTemp["IsArray"] or dicoTemp["IsList"]:
                dicoTemp["NotInInit"]=True

            line = line.replace("//Array","")
            line = line.replace("//List", "")
            while line[0]==" ":
                line=line[1:]
            while line[-1]==" ":
                line=line[:-1]
            line = ([o[::-1] for o in line[::-1].split(" ",1)])[::-1]
            typeVar= line[0]
            nameVar = line[1]
            dicoTemp["Name"] = nameVar
            dicoTemp["Type"] = typeVar
            if i[1]:
                dicoTemp["Public-Private"] = "Public"
            else:
                dicoTemp["Public-Private"] = "Private"
                dicoTemp["NotInInit"] = True
            if typeVar[:14]=="ParticuleEvent":
                dicoTemp["NotInInit"] = True
            self.Variables.append(dicoTemp)

        code = (txt.split("//<Methods>", 1)[1]).split("//<\\Methods>", 1)[0]
        codePrivate = (code.split("//<PrivateMethods>", 1)[1]).split("//<\\PrivateMethods>", 1)[0]
        codePublic = (code.split("//<PublicMethods>", 1)[1]).split("//<\\PublicMethods>", 1)[0]
        self.Methods = []
        self.ParseMethods(codePrivate, "Private")
        self.ParseMethods(codePublic, "Public")
        for i in codePrivate:
            dicoTemp = {}
            dicoTemp["Public-Private"] = "Private"

    def ParseMethods(self,code,Public_Private):

        typesFounds = ["Constructor","Method"]
        AllMethods = []
        size = -1
        while size != len(AllMethods):
            size = len(AllMethods)
            for typeSearch in typesFounds:
                temp = code.split("//<"+typeSearch+">",1)
                if len(temp)!=2:
                    continue
                p1 = temp[0]
                temp = (temp[1]).split("//<\\"+typeSearch+">",1)
                p2 = temp[1]
                code = p1+p2
                dicoTemp = {}
                dicoTemp["Public-Private"] = Public_Private
                dicoTemp["Type"] = typeSearch
                temp = temp[0]
                AllMethods.append((dicoTemp,temp))

        for data in AllMethods:
            dicoTemp, temp = data
            typeSearch = dicoTemp["Type"]
            MethodInit = temp.split("{",1)[0]
            for o in range(100):
                MethodInit = MethodInit.replace("\n","").replace("\t","").replace("  "," ")
            if MethodInit[0]==" ":
                MethodInit = MethodInit[1:]
            if MethodInit[-1]==" ":
                MethodInit = MethodInit[:-1]
            MethodCode = (((temp.split("{",1)[1])[::-1]).split("}",1)[1])[::-1]
            dicoTemp["CodeInterne"] = MethodCode
            for i in range(10):
                MethodInit = MethodInit.replace(" (","(")
            if typeSearch=="Constructor":
                dicoTemp["Name"] = MethodInit.split("(",1)[0]
                dicoTemp["Parameters"] = "("+MethodInit.split("(", 1)[1]
            elif typeSearch=="Method":
                temp2 = MethodInit.split("(", 1)[0]
                temp2 = temp2.replace(" * ", "* ").replace(" & ", "& ")
                temp2 = temp2.replace(" *", "* ").replace(" &", "& ")
                temp2 = temp2.replace("*", "* ").replace("&", "& ")
                temp2 = temp2.replace("\n", "").replace("\t", "").replace("  ", " ")
                temp2 = ([o[::-1] for o in temp2[::-1].split(" ", 1)])[::-1]
                dicoTemp["ReturnType"] = temp2[0]
                dicoTemp["Name"] = temp2[1]
                dicoTemp["Parameters"] = "("+MethodInit.split("(", 1)[1]
            self.Methods.append(dicoTemp)

    def AddConstructor(self,parametres):
        assert self.Inheritance=="MonoBehaviour"
        final = {"Name": self.NameComponent,"Type":"Constructor","Public-Private": "Public"}
        txt="(GameObject* gameObject,"
        for i in parametres:
            if not i["NotInInit"]:
                txt+=i["Type"]+" "+i["Name"]+","
        txt+='const char* UUID = NULL) : MonoBehaviour("'
        txt+=self.NameComponent
        txt+='", gameObject, UUID)'
        final["Parameters"] = txt

        txt="\n"
        tempLst = []
        for i in parametres:
            if not i["NotInInit"]:
                txt += "this->"+i["Name"]+"="+i["Name"]+";\n"
                tempLst.append(i["Name"])
        for i in self.Variables:
            if not i["Name"] in tempLst:
                if not i["NotInInit"]:
                    tmp=self.GetInitValueAttributCasio(i["Type"])
                    if tmp!=None:
                        txt += "this->" + i["Name"] + "=" + tmp + ";\n"
        txt+="\n"
        final["CodeInterne"] = txt
        return final

    def WriteMethode(self,dico,cpp=False):
        typeSearch =dico["Type"]
        code="""        //<"""+typeSearch+""">
$(code)
        //<\\"""+typeSearch+""">"""
        init =""
        if typeSearch=="Constructor":
            code = code.replace("$(code)",dico["Name"]+dico["Parameters"]+"{"+\
                                dico["CodeInterne"]+"};")
            init =dico["Name"]+dico["Parameters"]+";"
        elif typeSearch=="Method":
            txtCpp = ""
            if cpp:
                txtCpp = self.NameComponent+"::"
            code = code.replace("$(code)", dico["ReturnType"] + " " + txtCpp +dico["Name"] +\
                                dico["Parameters"] + "{" + dico["CodeInterne"] + "};")
            init = dico["ReturnType"] + " " + dico["Name"] + dico["Parameters"] + ";"
        return init,code

    def Print(self):
        print(self.NameComponent)
        print(self.Inheritance)
        print(self.Variables)
        print(self.Methods)

    def RemoveAllConstructor(self):
        inds=[]
        for i in self.Methods:
            if i["Type"] == "Constructor":
                inds.append(i)
        for i in inds:
            self.Methods.remove(i)

    def Save(self):
        self.RemoveAllConstructor()
        self.Methods.append(self.AddConstructor([]))
        self.Methods.append(self.AddConstructor(self.Variables))

        Inheritance = ""
        if self.Inheritance!=None:
            Inheritance="public "+self.Inheritance
        PublicVar = ""
        PrivateVar = ""
        for i in self.Variables:
            temp = "        "+i["Type"]+" "+i["Name"]+";\n"
            if i["Public-Private"]=="Public":
                PublicVar+=temp
            else:
                PrivateVar+=temp
        PublicVar =PublicVar[:-1]
        PrivateVar = PrivateVar[:-1]

        PublicMethods = ""
        PrivateMethods = ""
        for i in self.Methods:
            if i["Public-Private"]=="Public":
                _,temp=self.WriteMethode(i)
                PublicMethods+=temp+"\n"
            else:
                _,temp = self.WriteMethode(i)
                PrivateMethods +=temp+"\n"

        PublicMethods = PublicMethods[:-1]
        PrivateMethods = PrivateMethods[:-1]
        code="""//#Editor C++
class """+self.NameComponent+""" : """+Inheritance+""" {
    //<InitVar>
    private:
        //<PrivateVar>
"""+PrivateVar+"""
        //<\PrivateVar>
    public:
        //<PublicVar>
"""+PublicVar+"""
        //<\PublicVar>
    //<\InitVar>
    //<Methods>
    private:
        //<PrivateMethods>
"""+PrivateMethods+"""
        //<\PrivateMethods>
    public:
        //<PublicMethods>
"""+PublicMethods+"""
        //<\PublicMethods>
    //<\Methods>
};
        """
        return code

    def SaveHppCpp(self):
        self.RemoveAllConstructor()
        self.Methods.append(self.AddConstructor([]))
        self.Methods.append(self.AddConstructor(self.Variables))
        Inheritance = ""
        if self.Inheritance != None:
            Inheritance = "public " + self.Inheritance
        PublicVar = ""
        PrivateVar = ""
        for i in self.Variables:
            temp = "        " + i["Type"] + " " + i["Name"] + ";\n"
            if i["Public-Private"] == "Public":
                PublicVar += temp
            else:
                PrivateVar += temp
        PublicVar = PublicVar[:-1]
        PrivateVar = PrivateVar[:-1]

        PublicMethods = ""
        PrivateMethods = ""
        MethodsCpp = ""
        for i in self.Methods:
            cppBool = not i["Type"] in ["Constructor"]
            initTemp,Temp = self.WriteMethode(i,cppBool)
            if i["Public-Private"] == "Public":
                if cppBool:
                    PublicMethods += initTemp+ "\n"
                    MethodsCpp += Temp+ "\n"
                else:
                    PublicMethods += Temp+ "\n"
            else:
                if cppBool:
                    PrivateMethods += initTemp+ "\n"
                    MethodsCpp += Temp + "\n"
                else:
                    PrivateMethods += Temp+ "\n"

        PublicMethods = PublicMethods[:-1]
        PrivateMethods = PrivateMethods[:-1]
        codeHpp = """class """ + self.NameComponent + """ : """ + Inheritance + """ {
    private:
""" + PrivateVar + """
    public:
""" + PublicVar + """
    private:
""" + PrivateMethods + """
    public:
""" + PublicMethods + """
};
"""
        size = -1
        while size!=len(MethodsCpp):
            size = len(MethodsCpp)
            p1 = MethodsCpp.split("//<",1)
            if len(p1)!=2:
                break
            p2 = (p1[1]).split(">",1)
            MethodsCpp = p1[0]+p2[1]
        return codeHpp,MethodsCpp

    def GetInitValueAttributCasio(self,Type):
        if Type == "int":
            return "0"
        elif Type == "float":
            return "0"
        elif Type == "unsigned char*":
            return '""'
        elif Type == "bool":
            return "false"
        elif Type == "Vector2*":
            return "new Vector2()"
        elif Type == "Texture*":
            return 'new Texture()'
        elif Type[:4] == 'List' or Type[:5] == 'Array':
            return None
        elif Type[:14] == 'ParticuleEvent':
            return None
        else:
            return "NULL"





