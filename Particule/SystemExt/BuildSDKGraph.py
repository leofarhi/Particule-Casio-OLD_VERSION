from SystemExt import EditorComponent as InspectorCompo
from SystemExt import Project as Pj
KeyCalculatrice=["KEY_CHAR_0","KEY_CHAR_1","KEY_CHAR_2","KEY_CHAR_3","KEY_CHAR_4","KEY_CHAR_5","KEY_CHAR_6","KEY_CHAR_7","KEY_CHAR_8","KEY_CHAR_9","KEY_CHAR_DP","KEY_CHAR_EXP","KEY_CHAR_PMINUS","KEY_CHAR_PLUS","KEY_CHAR_MINUS","KEY_CHAR_MULT","KEY_CHAR_DIV","KEY_CHAR_FRAC","KEY_CHAR_LPAR","KEY_CHAR_RPAR","KEY_CHAR_COMMA","KEY_CHAR_STORE","KEY_CHAR_LOG","KEY_CHAR_LN","KEY_CHAR_SIN","KEY_CHAR_COS","KEY_CHAR_TAN","KEY_CHAR_SQUARE","KEY_CHAR_POW","KEY_CTRL_EXE","KEY_CTRL_DEL","KEY_CTRL_AC","KEY_CTRL_FD","KEY_CTRL_EXIT","KEY_CTRL_SHIFT","KEY_CTRL_ALPHA","KEY_CTRL_OPTN","KEY_CTRL_VARS","KEY_CTRL_UP","KEY_CTRL_DOWN","KEY_CTRL_LEFT","KEY_CTRL_RIGHT","KEY_CTRL_F1","KEY_CTRL_F2","KEY_CTRL_F3","KEY_CTRL_F4","KEY_CTRL_F5","KEY_CTRL_F6","KEY_CTRL_MENU"]
def ConvertNameInvalid(name):
   NewName=""
   for Ind,char in enumerate(name):
      if (char.isalpha() or char.isdecimal()):
         if (Ind==0 and char.isdecimal()):
            NewName+="I"
         NewName+=char
      else:
         NewName+="IvC"
   return NewName
def Init(lst,nameCompo,allVagueScratch,allCompoName):
    global NameCompo,LstOfAddImage,AllVariableInit,AllVagueScratch,AllCompoName
    NameCompo=nameCompo
    AllCompoName=allCompoName
    AllVagueScratch=allVagueScratch
    LstOfAddImage=[]
    AllVariableInit=[]
    return GetCode(lst)
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
    eval(compile("_i="+_i[0]+"(_i)", '<string>', 'exec'),globals(),globals())
    return _i
def IfCondition(lst):
    code="if ("+GetCode((lst[1])[0])+"){\n"+GetCode((lst[2])[0])+"\n}\n"
    code+=GetCode((lst[2])[1])
    return code
def IfElseCondition(lst):
    code="if ("+GetCode((lst[1])[0])+"){\n"+GetCode((lst[2])[0])+"\n}"
    code+="else {"+GetCode((lst[2])[1])+"\n}\n"
    code+=GetCode((lst[2])[2])
    return code
def OnStart(lst):
    code="OnStart(){\n"+GetCode((lst[2])[0])+"\n}"
    return code
def OnUpdate(lst):
    code="OnUpdate(){\n"+GetCode((lst[2])[0])+"\n}"
    return code
def TouchingElement(lst):
    #code="(touch=="+((lst[1])[0])[2]+")"
    tempLst=[i.name for i in Pj.Elements]
    code="""(gameObject->x < gameObject->Scene->AllElem[]->x + gameObject->Scene->AllElem[]->w &&
    gameObject->x + gameObject->w > gameObject->Scene->AllElem[]->x &&
    gameObject->y < gameObject->Scene->AllElem[]->y + gameObject->Scene->AllElem[]->h &&
    gameObject->h + gameObject->y > gameObject->Scene->AllElem[]->y)"""
    code = code.replace("AllElem[]","AllElem["+str(tempLst.index(((lst[1])[0])[2]))+"]")
    return code
def Stop(lst):
    code="\n"+"return 1;\n"
    return code
def BroadcastMessage(lst):
    code="send "+((lst[1])[0])[1]+" ;"
    return code
def WhenKeyPressed(lst):
    code="IsKeyDown(KEY_"+((lst[1])[0])[2]+")"
    return code
def RepeatNb(lst):
    print(lst)
    code="for (int "+str(((lst[1])[0])[1])+"(0); "+str(((lst[1])[0])[1])+" < "+GetCode((lst[1])[1])+"; ++i){\n"+GetCode((lst[2])[0])+"\n}\n"
    code+=GetCode((lst[2])[1])
    return code
def While(lst):
    code="while ("+GetCode((lst[1])[0])+"){\n"+GetCode((lst[2])[0])+"\n}\n"
    code+=GetCode((lst[2])[1])
    return code
def OperatorDivision(lst):
    code = "("+GetCode((lst[1])[0])+"/"+GetCode((lst[1])[1])+")"
    return code
def OperatorMultiplication(lst):
    code = "("+GetCode((lst[1])[0])+"*"+GetCode((lst[1])[1])+")"
    return code
def OperatorSoustraction(lst):
    code = "("+GetCode((lst[1])[0])+"-"+GetCode((lst[1])[1])+")"
    return code
def OperatorAddition(lst):
    code = "("+GetCode((lst[1])[0])+"+"+GetCode((lst[1])[1])+")"
    return code
def OperatorBool(lst):
    if ((lst[1])[0])[2]=="Vrai":
        code="true"
    else:
        code="false"
    return code
def OperatorBoolInverse(lst):
    code="!("+GetCode((lst[1])[0])+")"
    return code
def OperatorAndOr(lst):
    if ((lst[1])[1])[2]=="et":
        code = "(("+GetCode((lst[1])[0])+")&&("+GetCode((lst[1])[2])+"))"
    else:
        code = "(("+GetCode((lst[1])[0])+")||("+GetCode((lst[1])[2])+"))"
    return code
def OperatorComparateur(lst):
    code = "(("+GetCode((lst[1])[0])+")"+((lst[1])[1])[2]+"("+GetCode((lst[1])[2])+"))"
    return code
def OperatorRandom(lst):
    code = "(rand() %"+GetCode((lst[1])[1])+"+"+GetCode((lst[1])[0])+")"
    return code
def OperatorModulo(lst):
    code = "("+GetCode((lst[1])[0])+"%"+GetCode((lst[1])[1])+")"
    return code
def OperatorConcatener(lst):
    code = "("+GetCode((lst[1])[0])+"+"+GetCode((lst[1])[1])+")"
    return code
def OperatorImage(lst):
    code = ConvertNameInvalid(((lst[1])[0])[2])
    return code
def OperatorEntry(lst):
    code= ""
    temp=str(((lst[1])[0])[1])
    try:
        temp_=int(temp)
        code+=str(temp_)
    except:
        try:
            temp_=float(temp.replace(",","."))
            code+=str(temp_)
        except:
            code+='"'+temp+'"'
    return code
def AddValueVariable(lst):
    code=((lst[1])[0])[2]+"+=("+GetCode((lst[1])[1])+");\n"
    code+=GetCode((lst[2])[0])
    return code
def SetValueVariable(lst):
    code=((lst[1])[0])[2]+"=("+GetCode((lst[1])[1])+");\n"
    code+=GetCode((lst[2])[0])
    return code
def VariableValue(lst):
    code = ConvertNameInvalid(((lst[1])[0])[2])
    return code
def GotoY(lst):
    code = "gameObject->y="+GetCode((lst[1])[0])+";\n"
    code+=GetCode((lst[2])[0])
    return code
def GotoX(lst):
    code = "gameObject->x="+GetCode((lst[1])[0])+";\n"
    code+=GetCode((lst[2])[0])
    return code
def AddGotoY(lst):
    code = "gameObject->y+="+GetCode((lst[1])[0])+";\n"
    code+=GetCode((lst[2])[0])
    return code
def AddGotoX(lst):
    code = "gameObject->x+="+GetCode((lst[1])[0])+";\n"
    code+=GetCode((lst[2])[0])
    return code
def GotoXY(lst):
    code = "gameObject->x="+GetCode((lst[1])[0])+";"+"gameObject->y="+GetCode((lst[1])[1])+";\n"
    code+=GetCode((lst[2])[0])
    return code
def VariablePosX(lst):
    return "(gameObject->x)"
def VariablePosY(lst):
    return "(gameObject->y)"
def CameraGotoXY(lst):
    code = "gameObject->Scene->CamX="+GetCode((lst[1])[0])+";"+"gameObject->Scene->CamY="+GetCode((lst[1])[1])+";\n"
    code+=GetCode((lst[2])[0])
    return code
def SetImageGameObject(lst):
    code = "gameObject->Img=(unsigned char*)"+GetCode((lst[1])[0])+";\n"
    code+=GetCode((lst[2])[0])
    return code
def ChangeScene(lst):
    code = "gameObject->Scene->LoadScene("+GetCode((lst[1])[0])+");return;\n"
    return code
def GetDataObject(lst):
    tempLst=[i.name for i in Pj.Elements]
    code = "gameObject->Scene->AllElem["+str(tempLst.index(((lst[1])[1])[2]))+"]"
    code +="->"
    lst2=["abscisse x","ordonnee y","largeur","hauteur","nom"]
    lst3=["x","y","w","h","Name"]
    code+=lst3[lst2.index(((lst[1])[0])[2])]
    return code
def InEditor(lst):
    global AllVagueScratch,AllVariableInit
    AddClassInH=""
    AllVagueScratch.remove("InEditor")
    for i in AllVagueScratch:
        TempTextOver=""
        if i in Pj.ObligeVar:
            TempTextOver="virtual "
        AddClassInH+=TempTextOver+"void "+i+"();\n    "
    code=GetCode((lst[2])[0])

    public="\n"
    priver="\n"
    public+="\n"#GameObject* gameObject;
    for variable in AllVariableInit:
        if variable[1]=="public":
            public+=variable[0]+";\n"
        else:
            priver+=variable[0]+";\n"
    code="class "+NameCompo+" : public Component\n{\npublic:"+ "\n    "+NameCompo+"();" +"\n    "+AddClassInH+"\n"+public+"\nprivate:"+priver+"\n};\n"
    return code
def HideInInspector(lst):
    code=GetCode((lst[2])[0])+'\n'
    code+=GetCode((lst[2])[1])
    return code
def CreateVariable(lst):
    global AllVariableInit
    AllType=Pj.AllTypeVariable
    Nom=((lst[1])[0])[1]
    Type=((lst[1])[1])[2]
    Protection=((lst[1])[2])[2]
    if Type == "image":
        AllVariableInit.append(["unsigned char*"+" "+Nom,Protection])
    elif Type == "string":
        AllVariableInit.append(["unsigned char*"+" "+Nom,Protection])
    elif Type in AllType:
        AllVariableInit.append([Type+" "+Nom,Protection])
    return ""+GetCode((lst[2])[0])
def UseImage(lst):
    global LstOfAddImage
    LstOfAddImage.append(((lst[1])[0])[2])
    return ""+GetCode((lst[2])[0])
#a=[[['OnStart', [], [['IfCondition', [['WhenKeyPressed', [['Liste', ['CHAR_0', 'CHAR_1', 'CHAR_2', 'CHAR_3', 'CHAR_4', 'CHAR_5', 'CHAR_6', 'CHAR_7', 'CHAR_8', 'CHAR_9', 'CHAR_DP', 'CHAR_EXP', 'CHAR_PMINUS', 'CHAR_PLUS', 'CHAR_MINUS', 'CHAR_MULT', 'CHAR_DIV', 'CHAR_FRAC', 'CHAR_LPAR', 'CHAR_RPAR', 'CHAR_COMMA', 'CHAR_STORE', 'CHAR_LOG', 'CHAR_LN', 'CHAR_SIN', 'CHAR_COS', 'CHAR_TAN', 'CHAR_SQUARE', 'CHAR_POW', 'CTRL_EXE', 'CTRL_DEL', 'CTRL_AC', 'CTRL_FD', 'CTRL_EXIT', 'CTRL_SHIFT', 'CTRL_ALPHA', 'CTRL_OPTN', 'CTRL_VARS', 'CTRL_UP', 'CTRL_DOWN', 'CTRL_LEFT', 'CTRL_RIGHTCTRL_F1', 'CTRL_F2', 'CTRL_F3', 'CTRL_F4', 'CTRL_F5', 'CTRL_F6', 'CTRL_MENU'], 'CHAR_3']], []]], []]]]], [['OnStart', [], [['IfCondition', [['TouchingElement', [['Liste', ['Sprite', 'Bord'], 'Bord']], []]], []]]], ['OnUpdate', [], []]], []]
#print(GetCode((a[0])[0]))
