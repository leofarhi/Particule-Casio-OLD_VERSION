from SystemExt import Project as Pj
def Init(Lst,name):
    global nameCompo,Variables,VariableCount,AddInTheEnd,SaveDataList,AllVariableName,AddSysSaveData,OrgAllVarName,AllVariableNameCpl
    nameCompo=name
    OrgAllVarName=[]
    Variables=[]
    AllVariableNameCpl=[]
    VariableCount=1
    AddInTheEnd="\n"
    SaveDataList='{"varActif":int(self.varActif.get()),'
    AllVariableName=[]
    AddSysSaveData=""
    NewLst=[]
    for i in Lst:
        if i[0]=="InEditor":
            NewLst=i
            break
    return GetCode(NewLst)+AddInTheEnd+"\n"
def GetCode(lst):
    global _i
    if lst==[]:
        return ""
    if lst==None:
        return "True"
    try:
        for i in range(4):
            lst[2].append([])
    except:
        pass
    _i=lst
    if True:#try:
        eval(compile("_i="+_i[0]+"(_i)", '<string>', 'exec'),globals(),globals())
    #except:
    #    print("erreur: Le block ne peut pas être utilisé dans l'éditeur")
    return _i
def InEditor(lst):
    code="class ImportComponent:\n\tdef __init__(self,indCompo,_Particule):\n\t\t"\
          +'self.name="'+nameCompo+'"\n\t\tself.nameCasio="'+nameCompo+'"'\
          +'\n\t\tself.Particule=_Particule'\
          +'\n\t\tself.mainframe=LabelFrame(self.Particule.Component.AllComponentframe, text="'+BeautifulText(nameCompo,True)+'")'\
          +'\n\t\tself.mainframe.pack()\n\t\tself.varActif=IntVar()\n\t\tself.varActif.set(1)\n\t\tself.CheckActif = Checkbutton(self.mainframe,variable=self.varActif,text="Actif",state= ACTIVE,offvalue=0,onvalue=1)'\
          +'\n\t\tself.CheckActif.grid(row=0,column=0)\n\t\tself.Bouton_Remove = Button(self.mainframe, text ="Remove", command=self.Remove)\n\t\tself.Bouton_Remove.grid(row=0,column=1)\n'\
          +GetCode((lst[2])[0])+"\n"
    code+='\t\tself.AllvarNew='+str(AllVariableNameCpl)+"\n"
    code+='\t\tself.AllvarORG='+str(OrgAllVarName)+"\n"
    code+="""
\tdef Remove(self):
\t\tfor ind,i in enumerate((Pj.Elements[Pj.selected]).listComponent):
\t\t\tif i[0].mainframe==self.mainframe:
\t\t\t\tdel (Pj.Elements[Pj.selected]).listComponent[ind]
\t\tself.mainframe.destroy()\n"""
    code+="""
\tdef SaveData(self):
\t\treturn """+SaveDataList[:-1]+"""}\n"""
    code+="""
\tdef DataCompile(self):
\t\ta=self.SaveData()
\t\t#a.insert(1,self.nameCasio)#for last version
\t\treturn a\n"""
    code+="\tdef LoadData(self,Data):\n\t\t"
    TempListV=[i[0] for i in AllVariableName]
    """#last version
    code+=TempListV[0]
    del TempListV[0]
    for i in TempListV:
        code+=","+str(i)
    code+="=Data\n\t\t"
    """
    for i in TempListV:
        code+="try:"+str(i)+"=Data.get('"+str(i)+"')\n\t\t"
        code+="except:"+str(i)+"=0\n\t\t"
    code+="self.varActif.set(str(varActif))\n"
    code+=AddSysSaveData
    return code

def HideInInspector(lst):
    global AllVariableName
    code='\t\t"""'+GetCode((lst[2])[0])+'\n\t\t"""\n'
    code+=GetCode((lst[2])[1])
    return code
def BeautifulText(text,space=False):
    text=str(text)
    Newtext=""
    for Ind,char in enumerate(text):
        if char.isupper() and Ind!=0 and space:
            Newtext+=" "
        Newtext+=char
    return Newtext
def VariableInt(Nom):
    global AddInTheEnd,SaveDataList,AllVariableName,AddSysSaveData,AllVariableNameCpl
    code="""\n\n
\t\tself.Entry_"""+(Nom+str(VariableCount))+"""frame=Frame(self.mainframe)
\t\tself.Entry_"""+(Nom+str(VariableCount))+"""frame.grid(row="""+str(VariableCount)+""",column=0)
\t\tself.label_"""+(Nom+str(VariableCount))+"""=Label(self.Entry_"""+(Nom+str(VariableCount))+"""frame, text='"""+BeautifulText(Nom,True)+""" :')
\t\tself.label_"""+(Nom+str(VariableCount))+""".grid(row=0,column=0)
\t\tself.var_Entry_"""+(Nom+str(VariableCount))+"""=StringVar()
\t\tself.var_Entry_"""+(Nom+str(VariableCount))+""".set("0")
\t\tself.var_Entry_"""+(Nom+str(VariableCount))+""".trace("w", self.update"""+(Nom+str(VariableCount))+""")
\t\tself.entry_"""+(Nom+str(VariableCount))+"""=Entry(self.Entry_"""+(Nom+str(VariableCount))+"""frame,textvariable=self.var_Entry_"""+(Nom+str(VariableCount))+""")
\t\tself.entry_"""+(Nom+str(VariableCount))+""".grid(row=0,column=1)\n"""
    AddInTheEnd+="""
\tdef update"""+(Nom+str(VariableCount))+"""(self,*args):
\t\ttry:
\t\t\tself.var_Entry_"""+(Nom+str(VariableCount))+""".set(str(int(self.var_Entry_"""+(Nom+str(VariableCount))+""".get())))
\t\texcept:
\t\t\tself.var_Entry_"""+(Nom+str(VariableCount))+""".set("0")\n"""
    SaveDataList+='"var_Entry_'+(Nom+str(VariableCount))+'":'+"int(self.var_Entry_"+(Nom+str(VariableCount))+".get()),"
    AllVariableNameCpl.append('var_Entry_'+(Nom+str(VariableCount)))
    AllVariableName.append([(Nom+str(VariableCount)),"int"])
    AddSysSaveData+="\t\tself.var_Entry_"+(Nom+str(VariableCount))+".set(str(var_Entry_"+(Nom+str(VariableCount))+"))\n"
    return code
def VariableFloat(Nom):
    global AddInTheEnd,SaveDataList,AllVariableName,AddSysSaveData,AllVariableNameCpl
    code="""\n\n
\t\tself.Entry_"""+(Nom+str(VariableCount))+"""frame=Frame(self.mainframe)
\t\tself.Entry_"""+(Nom+str(VariableCount))+"""frame.grid(row="""+str(VariableCount)+""",column=0)
\t\tself.label_"""+(Nom+str(VariableCount))+"""=Label(self.Entry_"""+(Nom+str(VariableCount))+"""frame, text='"""+BeautifulText(Nom,True)+""" :')
\t\tself.label_"""+(Nom+str(VariableCount))+""".grid(row=0,column=0)
\t\tself.var_Entry_"""+(Nom+str(VariableCount))+"""=StringVar()
\t\tself.var_Entry_"""+(Nom+str(VariableCount))+""".set("0")
\t\tself.var_Entry_"""+(Nom+str(VariableCount))+""".trace("w", self.update"""+(Nom+str(VariableCount))+""")
\t\tself.entry_"""+(Nom+str(VariableCount))+"""=Entry(self.Entry_"""+(Nom+str(VariableCount))+"""frame,textvariable=self.var_Entry_"""+(Nom+str(VariableCount))+""")
\t\tself.entry_"""+(Nom+str(VariableCount))+""".grid(row=0,column=1)\n"""
    AddInTheEnd+="""
\tdef update"""+(Nom+str(VariableCount))+"""(self,*args):
\t\ttry:
\t\t\tself.var_Entry_"""+(Nom+str(VariableCount))+""".set(str(float(self.var_Entry_"""+(Nom+str(VariableCount))+""".get())))
\t\texcept:
\t\t\tself.var_Entry_"""+(Nom+str(VariableCount))+""".set("0")\n"""
    SaveDataList+='"var_Entry_'+(Nom+str(VariableCount))+'":'+"int(self.var_Entry_"+(Nom+str(VariableCount))+".get()),"
    AllVariableNameCpl.append('var_Entry_'+(Nom+str(VariableCount)))
    AllVariableName.append([(Nom+str(VariableCount)),"float"])
    AddSysSaveData+="\t\tself.var_Entry_"+(Nom+str(VariableCount))+".set(str(var_Entry_"+(Nom+str(VariableCount))+"))\n"
    return code
def VariableString(Nom):
    global AddInTheEnd,SaveDataList,AllVariableName,AddSysSaveData,AllVariableNameCpl
    code="""\n\n
\t\tself.Entry_"""+(Nom+str(VariableCount))+"""frame=Frame(self.mainframe)
\t\tself.Entry_"""+(Nom+str(VariableCount))+"""frame.grid(row="""+str(VariableCount)+""",column=0)
\t\tself.label_"""+(Nom+str(VariableCount))+"""=Label(self.Entry_"""+(Nom+str(VariableCount))+"""frame, text='"""+BeautifulText(Nom,True)+""" :')
\t\tself.label_"""+(Nom+str(VariableCount))+""".grid(row=0,column=0)
\t\tself.var_Entry_"""+(Nom+str(VariableCount))+"""=StringVar()
\t\tself.var_Entry_"""+(Nom+str(VariableCount))+""".set("")
\t\tself.entry_"""+(Nom+str(VariableCount))+"""=Entry(self.Entry_"""+(Nom+str(VariableCount))+"""frame,textvariable=self.var_Entry_"""+(Nom+str(VariableCount))+""")
\t\tself.entry_"""+(Nom+str(VariableCount))+""".grid(row=0,column=1)\n"""
    SaveDataList+='"var_Entry_"'+(Nom+str(VariableCount))+"':"+"int(self.var_Entry_"+(Nom+str(VariableCount))+".get()),"
    AllVariableNameCpl.append('var_Entry_'+(Nom+str(VariableCount)))
    AllVariableName.append([(Nom+str(VariableCount)),"string"])
    AddSysSaveData+="\t\tself.var_Entry_"+(Nom+str(VariableCount))+".set(str(var_Entry_"+(Nom+str(VariableCount))+"))\n"
    return code
def VariableBool(Nom):
    global AddInTheEnd,SaveDataList,AllVariableName,AddSysSaveData,AllVariableNameCpl
    code="""\n\n
\t\tself.var"""+(Nom+str(VariableCount))+"""=IntVar()
\t\tself.var"""+(Nom+str(VariableCount))+""".set(0)
\t\tself.Check"""+(Nom+str(VariableCount))+""" = Checkbutton(self.mainframe,variable=self.var"""+(Nom+str(VariableCount))+""",text='"""+BeautifulText(Nom,True)+"""',offvalue=0,onvalue=1)
\t\tself.Check"""+(Nom+str(VariableCount))+""".grid(row="""+str(VariableCount)+""",column=0)\n"""
    SaveDataList+='"var'+(Nom+str(VariableCount))+'":'+"int(self.var"+(Nom+str(VariableCount))+".get()),"
    AllVariableNameCpl.append('var'+(Nom+str(VariableCount)))
    AllVariableName.append([(Nom+str(VariableCount)),"bool"])
    AddSysSaveData+="\t\tself.var"+(Nom+str(VariableCount))+".set(str(var"+(Nom+str(VariableCount))+"))\n"
    return code
def VariableList(Nom):
    global AddInTheEnd,SaveDataList,AllVariableName,AddSysSaveData,AllVariableNameCpl
    code="""\n\n
\t\tself.label_"""+(Nom+str(VariableCount))+"""=Label(self.mainframe, text='"""+BeautifulText(Nom,True)+"""')
\t\tself.label_"""+(Nom+str(VariableCount))+""".grid(row="""+str(VariableCount)+""",column=0)
\t\tself.CurSelect"""+(Nom+str(VariableCount))+""" = StringVar()
\t\tself.Lst"""+(Nom+str(VariableCount))+""" = ttk.Combobox(self.mainframe, textvariable=self.CurSelect"""+(Nom+str(VariableCount))+""")
\t\tself.Lst"""+(Nom+str(VariableCount))+""".grid(row="""+str(VariableCount+1)+""",column=0)
\t\tself.UpdateValue"""+(Nom+str(VariableCount))+"""('')
\t\tself.Lst"""+(Nom+str(VariableCount))+""".bind('<<ComboboxSelected>>', self.UpdateValue"""+(Nom+str(VariableCount))+""")\n"""
    AddInTheEnd+="""
\tdef UpdateValue"""+(Nom+str(VariableCount))+"""(self,event):
\t\tself.ElemInLst"""+(Nom+str(VariableCount))+"""=['None']#replace_"""+(Nom+str(VariableCount))+"""\n
\t\tself.Lst"""+(Nom+str(VariableCount))+"""['values'] = tuple(self.ElemInLst"""+(Nom+str(VariableCount))+""")\n"""
    SaveDataList+='"Lst'+(Nom+str(VariableCount))+'":'+"self.Lst"+(Nom+str(VariableCount))+".get(),"
    AllVariableName.append([(Nom+str(VariableCount)),"list"])
    AllVariableNameCpl.append('Lst'+(Nom+str(VariableCount)))
    AddSysSaveData+="""
\t\tself.UpdateValue"""+(Nom+str(VariableCount))+"""('')
\t\tfor ind,i in enumerate(self.ElemInLst"""+(Nom+str(VariableCount))+"""):
\t\t\tif """+(Nom+str(VariableCount))+"""==i:
\t\t\t\tself.Lst"""+(Nom+str(VariableCount))+""".current(ind)
\t\t\t\tbreak\n"""
    return code
def VariableImage(Nom):
    global AddInTheEnd,SaveDataList,AllVariableName,AddSysSaveData,AllVariableNameCpl
    code = VariableList(Nom)
    AddInTheEnd=AddInTheEnd.replace("['None']#replace_"+(Nom+str(VariableCount)),"[(Img[1])[2] for Img in Pj.ImageLoad]")
    del AllVariableName[-1]
    AllVariableName.append([(Nom+str(VariableCount)),"image"])
    return code
def CreateVariable(lst):
    global VariableCount,OrgAllVarName
    AllType=Pj.AllTypeVariable
    Nom=((lst[1])[0])[1]
    OrgAllVarName.append(Nom)
    Type=((lst[1])[1])[2]
    Protection=((lst[1])[2])[2]
    code=""
    if Protection=='public':
        if Type in AllType:
            if Type=="int":code=VariableInt(Nom)
            if Type=="float":code=VariableFloat(Nom)
            if Type=="bool":code=VariableBool(Nom)
            if Type=="string":code=VariableString(Nom)
            if Type=="image":code=VariableImage(Nom)
        else:
            code=VariableList(Nom)
        VariableCount+=1
    code+=GetCode((lst[2])[0])
    return code
def UseImage(lst):
    return GetCode((lst[2])[0])
#a=[['InEditor', [], [['HideInInspector', [], [['CreateVariable', [['TexteEtNombre', 'PosxCoord'], ['Liste', [], 'int'], ['Liste', ['public', 'priver'], 'public']], []]]]]]]
#print(Init(a))
