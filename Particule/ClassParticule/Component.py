import inspect
from Particule import *
from ClassParticule.Vector2 import Vector2
from ClassParticule.Texture import Texture
from ClassSystem.TypeGUI import TypeGUI
import ClassParticule

from ClassParticule.Object import Object
class Component(Object):
    name=""
    def __init__(self,gameObject,name,**kwargs):
        Object.__init__(self,gameObject.Particule,name=name,**kwargs)
        self.gameObject = gameObject
        self.AttributVisible=[]
        self.myFrame = None
        self._valueGUI = []
        self.TypeVariables = {"name":{"Type":str},
                              "gameObject":{"Type":ClassParticule.GameObject.GameObject}
                              }
        if self.gameObject.scene!="" and self.gameObject.scene in self.Particule.Scene.scenes:
            indexScene = self.Particule.Scene.scenes.index(self.gameObject.scene)
            if not self.ID in self.Particule.Scene.UUID_Objects[indexScene]:
                self.Particule.Scene.UUID_Objects[indexScene].update({self.ID:self})

    def SaveDataDict(self):
        return {"name":self.name,
                "gameObject":self.gameObject.ID}
    def LoadDataDict(self,data,component,dataCompo,dicoGameObject,dicoComponent):
        self.gameObject = dicoGameObject[dataCompo["gameObject"]]
        self.name = dataCompo["name"]

    def Copy(self):
        dico = self.SaveDataDict()
        dico["TypeObject"] = self.name
        Data = {self.ID:dico}
        return Data

    def GetAttribut(self):
        lst=[]
        for i in inspect.getmembers(self):
            # to remove private and protected
            # functions
            if not i[0].startswith('_'):
                # To remove other methods that
                # doesnot start with a underscore
                if not inspect.ismethod(i[1]):
                    lst.append(i)
        return lst

    def RefreshGUI(self):
        if self.gameObject.scene!="" and self.gameObject.scene in self.Particule.Scene.scenes:
            indexScene = self.Particule.Scene.scenes.index(self.gameObject.scene)
            if not self.ID in self.Particule.Scene.UUID_Objects[indexScene]:
                self.Particule.Scene.UUID_Objects[indexScene].update({self.ID:self})
        if self.myFrame != None:
            self.myFrame.destroy()
        self.myFrame = LabelFrame(self.Particule.Inspector.mainComponentsFrame, text=self.name)
        self.myFrame.Particule = self.Particule
        self.AddContextMenu()
        one = False
        count = 0
        for i in self.GetAttribut():
            if i[0] in self.AttributVisible:
                # print(i[0],getattr(self,i[0]))
                one = True
                tempUI = TypeGUI(self.myFrame, self, i[0],self.TypeVariables[i[0]])
                tempUI.grid(row=count, column=0, sticky='EWNS')
                self._valueGUI.append(tempUI)
                count += 1
                # Button(self.myFrame,text=self.gameObject.name+i[0]+" : "+str(i[1].get())).pack()
        if not one:
            Label(self.myFrame, text="Pas de paramètres").pack()
    def AddContextMenu(self):
        # self.myFrame.pack(fill=tkinter.BOTH, expand=True)
        self.myFrame.bind("<Button-3>", self.popup)
        self.contextMenu = Menu(self.Particule.Mafenetre, tearoff=False)
        # self.contextMenu.add_command(label="Copy")
        # self.contextMenu.add_command(label="Past")
        self.contextMenu.add_separator()
        # self.contextMenu.add_command(label="Duplicate")
        self.contextMenu.add_command(label="Delete", command=self.Destroy)
    def PrintOnGui(self):
        if self.myFrame ==None:
            self.RefreshGUI()
        self.myFrame.pack(fill=tkinter.BOTH, expand=True)
        for i in self._valueGUI:
            i.Update()

    def popup(self, event):
        self.contextMenu.post(event.x_root, event.y_root)
    def Destroy(self,*args):
        Object.Destroy(self)
        if self.gameObject.scene != "" and self.gameObject.scene in self.Particule.Scene.scenes:
            indexScene = self.Particule.Scene.scenes.index(self.gameObject.scene)
            if self.ID in self.Particule.Scene.UUID_Objects[indexScene]:
                del (self.Particule.Scene.UUID_Objects[indexScene])[self.ID]
        self.gameObject.ListOfComponent.remove(self)
        if (self.myFrame!=None):
            self.myFrame.destroy()
        for i in self._valueGUI:
            i.destroy()
        self.Particule.Inspector.UpdateItemSelected()

    def BuildValue(self):
        if type(self).__name__ == "Transform":
            return ("\n","\n")
        CodeBefore=""
        parametres=","
        for indexAtt,i in enumerate(self.AttributVisible):
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
                        parametres +="new Texture()"
                    else:
                        parametres += "Texture_"+path
                    """
                elif type(var) is Texture:
                    path = os.path.basename(var.path)
                    path = os.path.splitext(path)[0]
                    parametres +='new Texture("'+str(var.name)+'",'+str(var.width)+","+str(var.height)+","+path+',"'+var.ID+'")'
                    """
                elif dicoVar["Type"] is list:
                    typeRecur = (dicoVar["LstValueType"])['Type']
                    if typeRecur==list:
                        raise Exception("les listes de listes ne sont pas encore pris en compte")
                    if dicoVar["LstType"]=="List":
                        raise Exception("les listes ne sont pas encore pris en compte")
                    if dicoVar["LstType"]=="Array":
                        Etoile="*"
                        if not typeRecur in [int,float,str,bool]:
                            Etoile+="*"
                        Etoile += " "
                        code = "static "+typeRecur.__name__+Etoile+"Lst_"+str(i)+"_"+str(indexAtt)+"_"+str(self.ID)+\
                               "= new "+ typeRecur.__name__+(Etoile[-2])+"["+str(len(var))+"];\n"
                        for ind,o in enumerate(var):
                            code+="Lst_"+str(i)+"_"+str(indexAtt)+"_"+str(self.ID)+"["+ind+"] = "+o+";\n"
                            raise Exception("les listes ne sont pas encore pris en compte")
                        raise Exception("rajouter CodeBefore")
                        CodeBefore+=code
                        parametres +="Lst_"+str(i)+"_"+str(indexAtt)+"_"+str(self.ID)
                else:
                    #print(eval("self."+i))
                    parametres +=var.ID
            parametres+=","
        return (type(self).__name__+"* "+self.ID+";\n",
                self.ID+" = new "+type(self).__name__+'('+self.gameObject.ID+parametres+'"'+self.ID+'");\n')

    def AddScriptBeforInitCasio(self):
        return ""

    def AddScriptAfterInitCasio(self):
        return ""



