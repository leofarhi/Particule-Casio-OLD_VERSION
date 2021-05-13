#import EditorComponent as InspectorCompo
from Moteur import *
import Moteur as M
from tkinter import *
import tkinter
from tkinter.messagebox import *
from tkinter import ttk
from functools import partial
import _pickle as cPickle
import traceback
import os
import sys
from SystemExt import read_file
#sys.setrecursionlimit(10000)

def ConvertNameInvalid(name):
   NewName=""
   for Ind,char in enumerate(name):
      if (char.isalpha() or char.isalnum()):
         if (Ind==0 and char.isdecimal()):
            NewName+="V"
         NewName+=char
      else:
         NewName+="IvC"
   return NewName
def CorrigeBind(textvariable,event):
   textvariable.set(ConvertNameInvalid(textvariable.get()))

   
Game_OS="win"
ScratchBlockIcon=[]
FolderProject=""
RepFolderSaveLoad="__pycache__"
RepFolderBlocks="Blocks"
RepFolderPython="Python"
TypeBox=["Editeur","Evenements","Controle","Variable","Opérateurs","Capteurs","Mouvement","Apparence","Stylo","Mes Blocs"]
OngletTypeTk=[]
Forme=["Rectangle","Cercle","Losange","Encadrement","Vague","EndBox"]
ListFormeInFront=["Cercle","Losange"]#,"Encadrement"]
FormeParametre=["Cercle","Losange"]

Variables=[]

PosX,PosY=0,0
LastPosX,LastPosY=0,0

WindCanvas=None

class Couleurs:
    bleu_fonce=(76,151,255)
    violet=(153,102,255)
    magenta=(207,99,207)
    jaune=(255,191,0)
    orange=(255,171,25)
    bleu_clair=(92,177,214)
    vert=(89,192,89)
    orange_fonce=(255,140,26)
    rose=(255,102,128)
    vert_fonce=(15,189,140)
    gris=(128,128,128)
    gris_clair=(208,208,208)
    noir=(0,0,0)
def color(colore):
    try:
        colore="#%02x%02x%02x" % colore
    except:
        pass
    return colore
def AddCodeLst(Widget):
        Refuser=["Label"]
        TypeParametre=["Booleen","EmptyCercle"]
        
        ActuLstNextBlock=[]
        ActuLstParametre=[]
        Parametres=Widget.SaveParametre(Widget.Parametres)
        for ind,i in enumerate(Widget.GroupeParametre):
            #print(i)
            if i[0] in TypeParametre:
                if i[1]!=None:
                    ActuLstParametre.append(AddCodeLst(WindCanvas.AllWidget.get(i[1])))
                else:
                    ActuLstParametre.append(None)
            else:
                if not (Widget.Parametres[ind])[0] in Refuser:
                    ActuLstParametre.append(Parametres[ind])
        for i in Widget.NextBlockIn:
            if i!=None:
                ActuLstNextBlock.append(AddCodeLst(WindCanvas.AllWidget.get(i)))
        return [Widget.Name.replace(".txt",""),ActuLstParametre,ActuLstNextBlock]
def GetCodeLst():
    SaveAllWidget()
    MyLst=[]
    for i in list(WindCanvas.AllWidget.values()):
        if i==None:continue
        if i.TypeForme == "Vague":
            MyLst.append(i)
    CodeFinal=[]
    for i in MyLst:
        CodeFinal.append(AddCodeLst(i))
    return CodeFinal

   
def SaveAllWidget():
   if RepFolderSaveLoad=="":return
   Lst=[]
   read_file.save(RepFolderSaveLoad+"/settings.txt","Variables",str(Variables))
   for forme in list(WindCanvas.AllWidget.values()):
      Lst.append(forme.SaveData())
   read_file.save(RepFolderSaveLoad+"/Widgets.SBAsset","AllWidget",str(Lst))
   for forme in list(WindCanvas.AllWidget.values()):
      if forme.ParentBlock==None:
         forme.update()
def LoadAllWidget():
   global _iI
   for forme in list(WindCanvas.AllWidget.values()):
      if forme.ParentBlock==None:
         forme.RemoveSelf()
   WindCanvas.CamX=0
   WindCanvas.CamY=0
   Variables=read_file.GetList(RepFolderSaveLoad+"/settings.txt","Variables")
   Lst=read_file.GetList(RepFolderSaveLoad+"/Widgets.SBAsset","AllWidget")
   if Lst == False:return
   LstWid=[]
   for i in range(len(Lst)):
      file=RepFolderBlocks+"/"+(Lst[i])[6]
      para=read_file.GetList(file,"Parametres")
      color=eval("Couleurs."+read_file.found(file,"Color"))
      Options=read_file.GetList(file,"Options")
      if Options==False:
            Options=[]
      if cherchefichier((file.split("/")[-1]).replace(".txt",".py"),RepFolderPython):
           with open(RepFolderPython+"/"+(file.split("/")[-1]).replace(".txt",".py"),"r") as fic:
              PythonScript=fic.read()
      else:PythonScript=None
      LstWid.append(CreateWidget((Lst[i])[6].replace(".txt","")))
      #eval(compile(read_file.found(file,"TypeForme")+"( (Lst[i])[0],(Lst[i])[1],para,color,(Lst[i])[6],Options=Options,PythonScript=PythonScript,Load=Lst[i])", '<string>', 'exec'),globals(),locals())
   WindCanvas.AllWidget = {}
   for ind,i in enumerate(LstWid):
      i.WidgetIndex=(Lst[ind])[2]
      WindCanvas.AllWidget.update({i.WidgetIndex:i})
   for ind,i in enumerate(LstWid):
      i.LoadData(Lst[ind])
   for forme in list(WindCanvas.AllWidget.values()):
      if forme.ParentBlock==None:
         forme.update()
def CreateWidget(Block):
      Block+=".txt"
      file=RepFolderBlocks+"/"+Block
      para=read_file.GetList(file,"Parametres")
      color=eval("Couleurs."+read_file.found(file,"Color"))
      Options=read_file.GetList(file,"Options")
      if Options==False:
            Options=[]
      if cherchefichier((file.split("/")[-1]).replace(".txt",".py"),RepFolderPython):
           with open(RepFolderPython+"/"+(file.split("/")[-1]).replace(".txt",".py"),"r") as fic:
              PythonScript=fic.read()
      else:PythonScript=None
      eval(compile(read_file.found(file,"TypeForme")+"( 100,100,para,color,Block,Options=Options,PythonScript=PythonScript)", '<string>', 'exec'),globals(),locals())
      return list(WindCanvas.AllWidget.values())[-1]
class Window:
   def __init__(self,frame,surfaceW,surfaceH):
      global WindCanvas
      WindCanvas = self
      self.CamX=0
      self.CamY=0
      self.Zoom = 2
      self.MainCanvas = Canvas(frame,width = surfaceW, height =surfaceH, background=color(Couleurs.gris_clair))
      self.ClassMoveObject=MoveObject()
      self.MainCanvas.bind('<Button-1>',self.ClassMoveObject.Clic) # evevement clic gauche (press)
      self.MainCanvas.bind('<B1-Motion>',self.ClassMoveObject.Drag)
      self.MainCanvas.bind('<ButtonRelease-1>',self.ClassMoveObject.Drop)
      self.MainCanvas.bind('<Button-2>',self.ClassMoveObject.ClicDuMilleu)
      self.MainCanvas.bind('<B2-Motion>',self.ClassMoveObject.ClicDuMilleuDrag)
      #self.CanvasScriptEditor.bind("<Key-Right>", keyRIGHT)
      #self.CanvasScriptEditor.bind("<Key-Left>", keyLEFT)
      #self.CanvasScriptEditor.bind("<Key-Up>", keyUP)
      #self.CanvasScriptEditor.bind("<Key-Down>", keyDOWN)
      
      self.MainCanvas.pack(fill = BOTH, expand = True)
      self.AllWidget = {} #dictionnaire
def AddWidget(widget):
    global WindCanvas
    WindCanvas.AllWidget.update({widget.WidgetIndex:widget})
def GetNewIndexWidget():
    global WindCanvas
    lst=list(WindCanvas.AllWidget.keys())
    count=0
    while "Forme"+str(count) in lst: count+=1;
    return "Forme"+str(count)
class Forme:
   def __init__(self,x,y,Parametres,Color,Name,Options=[],PythonScript=None,Load=False):
         global _i,ScriptBlockPython
         self.WidgetIndex=GetNewIndexWidget()
         self.Options = Options
         self.Parametres = Parametres
         self.Canevas = WindCanvas.MainCanvas
         self.Color = "#%02x%02x%02x" % Color
         self.x = x
         self.y = y
         self.Zoom = WindCanvas.Zoom
         self.Name=Name
         self.NextBlockPosY=[15*2]
         self.NextBlockIn=[None]
         self.ParentBlock=None

         #---------
         self.PythonScript=None
         self.PythonScriptCode=None
         if PythonScript!=None:
            self.PythonScriptCode=PythonScript
            _i=PythonScript
            eval(compile(_i, '<string>', 'exec'),globals(),globals())
            self.PythonScript=ScriptBlockPython(self)
         ScriptBlockPython=None
         #------------

         self.GroupeParametre=[]
         for i in self.Parametres:
            self.GroupeParametre.append([i[0],None])

         AddWidget(self)
         if Load!=False:self.LoadData(Load)
         
   def Init(self):
         self.h=15
         self.h_add=0
         self.x_add=[0]
         self.r=0
         self.GroupeWidget=[]
         self.BoxCollider=[]
         self.CanAddBlock=False
         self.CanPutInBlock=False
         self.TypeParametreSyc=None

         self.ParametrePosi=[]
         self.BoxColiParametre=[]
   def SaveParametre(self,Para):
        Parametre=[]
        for ind,i in enumerate(Para):
            if i[0]=="TexteEtNombre":
                if type(i[1])==tkinter.StringVar:
                    Parametre.append([i[0],None])
                    (Parametre[ind])[1]=str(i[1].get())
            elif i[0]=="Liste":
                if type(i[2])==tkinter.StringVar:
                    Parametre.append([i[0],i[1],None])
                    (Parametre[ind])[2]=str(i[2].get())
            else:
               Parametre.append(i)
        return Parametre
   def SaveData(self):
      Parametre=self.SaveParametre(self.Parametres)
      Option=[]
      for ind,i in enumerate(self.Options):
            Option.append(i)
            if i[0]=="Parametres":
                (Option[ind])[1]=self.SaveParametre(i[1])
      X=self.x-WindCanvas.CamX
      Y=self.y-WindCanvas.CamY
      return [X,Y,self.WidgetIndex,self.NextBlockIn,self.ParentBlock,self.GroupeParametre,self.Name,Parametre,Option,self.PythonScriptCode]
   def LoadData(self,Data):
      self.x,self.y,self.WidgetIndex,self.NextBlockIn,self.ParentBlock,self.GroupeParametre,self.Name,self.Parametres,self.Options,self.PythonScriptCode=Data
      #print(self.GroupeParametre,self.Parametres,self.Options)
      if self.PythonScriptCode!=None:
            _i=self.PythonScriptCode
            eval(compile(_i, '<string>', 'exec'),globals(),globals())
            self.PythonScript=ScriptBlockPython(self)
   def RemoveSelf(self):
      for ind,i in enumerate(self.GroupeParametre):
            if i[1]!=None:(WindCanvas.AllWidget.get(i[1])).RemoveSelf()
      for i in self.NextBlockIn:
            if i!=None:
                (WindCanvas.AllWidget.get(i)).RemoveSelf()
      for A in self.GroupeWidget:
            for i in A:
                try:
                    self.Canevas.delete(i)
                except:
                    i.destroy()
      del WindCanvas.AllWidget[self.WidgetIndex]
      del self
      return
   def lenBlock(self,Widget,e):
        e+=Widget.h+Widget.h_add
        for i in Widget.NextBlockIn:
            if i!=None:
                e=self.lenBlock(WindCanvas.AllWidget.get(i),e)
        return e
   def espace(self,r):
        for ind,i in enumerate(self.Parametres):
            try:
                #print(self.GroupeParametre[ind])
                if i[0]=="Label":
                    tempV=0
                    if Game_OS=="Mac":tempV=0.5
                    r+=len(i[1])*(3+tempV)
                if i[0]=="EmptyCercle":
                    h=10
                    r+=2
                    d=5
                    if (self.GroupeParametre[ind])[1]!=None:
                        r+=WindCanvas.AllWidget.get((self.GroupeParametre[ind])[1]).r/self.Zoom
                    else:
                        r+=d+h+4
                if i[0]=="TexteEtNombre":
                    h=10
                    r+=3
                    d=5
                    r+=d+h+25
                if i[0]=="Liste":
                    h=10
                    r+=3
                    d=5
                    r+=d+h+45
                if i[0]=="Booleen":
                    r+=2
                    h=10
                    d=5
                    if (self.GroupeParametre[ind])[1]!=None:
                        r+=WindCanvas.AllWidget.get((self.GroupeParametre[ind])[1]).r/self.Zoom
                    else:
                        r+=d+h+h+4
            except:
                pass
        return r
   def ShowParametre(self,r,h,MyGroupWidget,x,y,opts=None):
        A=None
        Autorise=["Label","TexteEtNombre","Liste"]
        for ind,i in enumerate(self.Parametres):
            try:
                #if (self.GroupeParametre[ind])[0] in Autorise or (self.GroupeParametre[ind])[1]==None
                    if i[0]=="Label":
                        A=self.Canevas.create_text(x+(r*self.Zoom),y,text=i[1],anchor='w',fill="white",font=("TkDefaultFont", int(10*(self.Zoom/2)) ))
                        tempV=0
                        if Game_OS=="Mac":tempV=0.5
                        r+=len(i[1])*(3+tempV)
                        MyGroupWidget.append(A)
                        self.BoxColiParametre.append([0,0,0,0])
                        self.ParametrePosi.append([0,0])
                    if i[0]=="EmptyCercle":
                        h=10
                        r+=2
                        o=(r*self.Zoom)
                        d=5
                        self.ParametrePosi.append([x+o,y])
                        self.BoxColiParametre.append([x+o,y-((h/2)*self.Zoom),x+(h*self.Zoom)+(d*self.Zoom)+o,y+((h/2)*self.Zoom)])
                        if (self.GroupeParametre[ind])[1]==None:
                            
                            A=self.Canevas.create_oval(x+o,y-((h/2)*self.Zoom), x+(h*self.Zoom)+o,y+((h/2)*self.Zoom), outline=color(Couleurs.gris), fill=color(Couleurs.gris))
                            MyGroupWidget.append(A)
                            A=self.Canevas.create_oval(x+(d*self.Zoom)+o,y-((h/2)*self.Zoom), x+(h*self.Zoom)+(d*self.Zoom)+o,y+((h/2)*self.Zoom), outline=color(Couleurs.gris), fill=color(Couleurs.gris))
                            MyGroupWidget.append(A)
                            A=self.Canevas.create_rectangle(x+((h/2)*self.Zoom)+o,y-((h/2)*self.Zoom), x+(d*self.Zoom)+o+((h/2)*self.Zoom),y+((h/2)*self.Zoom), outline=color(Couleurs.gris), fill=color(Couleurs.gris))
                            MyGroupWidget.append(A)
                            r+=d+h+4
                            
                        else:
                            r+=WindCanvas.AllWidget.get((self.GroupeParametre[ind])[1]).r/self.Zoom
                    if i[0]=="TexteEtNombre":
                        h=15
                        r+=3
                        if len(i)<2:
                            tx=StringVar()
                            self.Parametres[ind].append(tx)
                        else:
                            if type(i[1])==tkinter.StringVar:
                                tx=i[1]
                            else:
                                tx=StringVar()
                                tx.set(str(i[1]))
                                (self.Parametres[ind])[1]=tx
                        tempWidth=int(10*(self.Zoom/2))
                        if Game_OS=="Mac":tempWidth=6
                        A=Entry(self.Canevas,textvariable=tx,width=tempWidth)
                        #A.bind("<FocusOut>",partial(CorrigeBind,tx))
                        tempMacAddY=0
                        if Game_OS=="Mac":tempMacAddY=int(h/2)
                        A.place(x=x+(r*self.Zoom),y=y-int(int(h/2)+tempMacAddY))
                        #self.Parametres[ind].append(A)
                        MyGroupWidget.append(A)
                        d=5
                        r+=d+10+25
                        self.BoxColiParametre.append([0,0,0,0])
                        self.ParametrePosi.append([0,0])
                    if i[0]=="Liste":
                        h=15
                        r+=3
                        if len(i)<3:
                            tx=StringVar()
                            self.Parametres[ind].append(tx)
                        else:
                            if type(i[2])==tkinter.StringVar:
                                tx=i[2]
                            else:
                                tx=StringVar()
                                tx.set(str(i[2]))
                                (self.Parametres[ind])[2]=tx
                        tempWidth=int(15*(self.Zoom/2))
                        if Game_OS=="Mac":tempWidth=9
                        A=ttk.Combobox(self.Canevas,textvariable=tx,width=tempWidth)
                        A['values'] = tuple(i[1])
                        tempMacAddY=0
                        if Game_OS=="Mac":tempMacAddY=int(h/4)
                        A.place(x=x+(r*self.Zoom),y=y-int(int(h/2)+tempMacAddY))
                        #self.Parametres[ind].append(A)
                        MyGroupWidget.append(A)
                        d=5
                        r+=d+10+45
                        self.BoxColiParametre.append([0,0,0,0])
                        self.ParametrePosi.append([0,0])
                    if i[0]=="Booleen":
                        r+=2
                        o=(r*self.Zoom)
                        h=10
                        d=5
                        self.ParametrePosi.append([x+o,y-(h*self.Zoom)])
                        self.BoxColiParametre.append([x+o,y-((h/2)*self.Zoom),x+(d*self.Zoom)+o+((h*2)*self.Zoom),y+(h*self.Zoom-((h/2)*self.Zoom))])
                        #print(self.GroupeParametre[ind])
                        if (self.GroupeParametre[ind])[1]==None:
                            
                            #print(r,self.Parametres)
                            posi=(x+(h*self.Zoom)+o,y-((h/2)*self.Zoom),
                                  x+(d*self.Zoom)+o+(h*self.Zoom),y-((h/2)*self.Zoom),
                                  x+(d*self.Zoom)+o+((h*self.Zoom)*2),y,
                                  x+(d*self.Zoom)+o+(h*self.Zoom),y+(h*self.Zoom-((h/2)*self.Zoom)),
                                  x+(h*self.Zoom)+o,y+(h*self.Zoom)-((h/2)*self.Zoom),
                                  x+o,y)
                    
                            A=self.Canevas.create_polygon(posi, outline=color(Couleurs.gris), fill=color(Couleurs.gris))
                            MyGroupWidget.append(A)
                            r+=d+h+h+4
                        else:
                            r+=WindCanvas.AllWidget.get((self.GroupeParametre[ind])[1]).r/self.Zoom
                        #self.BoxColiParametre.append([x+o,0,0,0])
            except:
                pass
            if opts!=None:
               if opts=="NotBoxColi":
                  del self.BoxColiParametre[-1]
        return MyGroupWidget
   def SetXY(self,x,y):
      if WindCanvas.ClassMoveObject.WidgetIsDrabed==self:
         if x-WindCanvas.CamX<0:
            x=WindCanvas.CamX
         if y-WindCanvas.CamY<0:
            y=WindCanvas.CamY
      for A in self.GroupeWidget:
         for i in A:
               try:
                  LstCoo=[]
                  lst=self.Canevas.coords(i)
                  for ind,o in enumerate(lst):
                      if ind%2==0:LstCoo.append((o-(self.x-x)))
                      else:LstCoo.append((o+((-self.y)+y)))
                  self.Canevas.coords(i,tuple(LstCoo))
                  try:
                      Canevas.tag_raise(i)
                  except:
                      pass
               except:
                  try:
                      i.place(x=(int(i.place_info().get("x"))-(self.x-x)),y=(int(i.place_info().get("y"))+((-self.y)+y)))
                  except:
                      pass
      for ind2 in range(len(self.BoxCollider)):
         LstCoo=[]
         for ind,o in enumerate(self.BoxCollider[ind2]):
             if ind%2==0:LstCoo.append((o-(self.x-x)))
             else:LstCoo.append((o+((-self.y)+y)))
         self.BoxCollider[ind2]=LstCoo
      for i in self.NextBlockIn:
         if i!=None:
            TempWidget=WindCanvas.AllWidget.get(i)
            TempWidget.SetXY(TempWidget.x-(self.x-x),TempWidget.y+((-self.y)+y))
      for ind,i in enumerate(self.GroupeParametre):
        if i[1]!=None:
            TempWidget=WindCanvas.AllWidget.get(i[1])
            TempWidget.SetXY(TempWidget.x-(self.x-x),TempWidget.y+((-self.y)+y))
      self.x=x
      self.y=y
   def childUpdate(self):
        for ind,i in enumerate(self.GroupeParametre):
            if i[1]!=None:(WindCanvas.AllWidget.get(i[1])).Refresh()
        for i in self.NextBlockIn:
            if i!=None:
                (WindCanvas.AllWidget.get(i)).Refresh()
   def Refresh(self):
        if self.PythonScript!=None:self.PythonScript.WhenUpdate()
            
        
        for A in self.GroupeWidget:
            for i in A:
                try:
                    self.Canevas.delete(i)
                except:
                    i.destroy()
        
        self.Init()
        if self.ParentBlock!=None and (not self.TypeForme in FormeParametre):
           tempB=WindCanvas.AllWidget.get(self.ParentBlock)
           o=tempB.NextBlockPosY[tempB.NextBlockIn.index(self.WidgetIndex)]
           ind=tempB.NextBlockIn.index(self.WidgetIndex)
           MoveWidget(self,self.x,self.y,
                           tempB.x+tempB.x_add[ind],tempB.y + o)
        elif self.ParentBlock!=None and self.TypeForme in FormeParametre:
            tempB=WindCanvas.AllWidget.get(self.ParentBlock)
            for ind,i in enumerate(tempB.GroupeParametre):
                if i[1]==self.WidgetIndex:
                    A=ind
                    break
            x_add,y_add=tempB.ParametrePosi[A]
            MoveWidget(self,self.x,self.y,
                               x_add,y_add)
        self.StartType()
        self.childUpdate()
   def update(self):
      if self.ParentBlock==None:
         self.Refresh()
      else:
         TempWidget=WindCanvas.AllWidget.get(self.ParentBlock)
         TempWidget.update()
class Rectangle(Forme):
   def __init__(self,x,y,Parametres,Color,Name,Options=[],PythonScript=None,Load=False):
      self.TypeForme="Rectangle"
      Forme.__init__(self,x,y,Parametres,Color,Name,Options,PythonScript,Load)
      self.Init()
      self.StartType()
   def StartType(self):
        self.CanPutInBlock=True
        self.CanAddBlock=True
        MyGroupWidget=[]
        r=25
        r=self.espace(r)
        h=15
        #print(r,self.Parametres)
        posi=(self.x,self.y,
              self.x+(5*self.Zoom),self.y, self.x+(10*self.Zoom),self.y+(5*self.Zoom), self.x+(15*self.Zoom),self.y+(5*self.Zoom), self.x+(20*self.Zoom),self.y,
              self.x+(r*self.Zoom),self.y, self.x+(r*self.Zoom),self.y+(h*self.Zoom),
              self.x+(20*self.Zoom),self.y+(h*self.Zoom), self.x+(15*self.Zoom),self.y+(h*self.Zoom)+(5*self.Zoom), self.x+(10*self.Zoom),self.y+(h*self.Zoom)+(5*self.Zoom), self.x+(5*self.Zoom),self.y+(h*self.Zoom),
              self.x,self.y+(h*self.Zoom))
        
        A=self.Canevas.create_polygon(posi, outline=color(Couleurs.gris), fill=self.Color)
        MyGroupWidget.append(A)
        self.BoxCollider.append([self.x,self.y , self.x+(r*self.Zoom),self.y+(h*self.Zoom)])
        
        MyGroupWidget=self.ShowParametre(20,h,MyGroupWidget,self.x,self.y+((h/2)*self.Zoom))
        self.GroupeWidget.append(MyGroupWidget)
class Cercle(Forme):
   def __init__(self,x,y,Parametres,Color,Name,Options=[],PythonScript=None,Load=False):
      self.TypeForme="Cercle"
      Forme.__init__(self,x,y,Parametres,Color,Name,Options,PythonScript,Load)
      self.Init()
      self.StartType()
   def StartType(self):
        self.TypeParametreSyc="EmptyCercle"
        MyGroupWidget=[]
        r=0
        r=self.espace(r)
        h=15
        A=self.Canevas.create_oval(self.x,self.y-((h/2)*self.Zoom), self.x+(h*self.Zoom),self.y+((h/2)*self.Zoom), outline=color(Couleurs.gris), fill=self.Color)
        MyGroupWidget.append(A)
        A=self.Canevas.create_oval(self.x+(r*self.Zoom),self.y-((h/2)*self.Zoom), self.x+(h*self.Zoom)+(r*self.Zoom),self.y+((h/2)*self.Zoom), outline=color(Couleurs.gris), fill=self.Color)
        MyGroupWidget.append(A)
        A=self.Canevas.create_rectangle(self.x+((h/2)*self.Zoom),self.y-((h/2)*self.Zoom), self.x+(r*self.Zoom)+((h/2)*self.Zoom),self.y+((h/2)*self.Zoom), outline=color(Couleurs.gris), fill=self.Color)
        MyGroupWidget.append(A)
        
        self.BoxCollider.append([self.x,self.y-((h/2)*self.Zoom) , self.x+(h*self.Zoom)+(r*self.Zoom),self.y+((h/2)*self.Zoom)])
        
        MyGroupWidget=self.ShowParametre(0,h,MyGroupWidget,self.x+((h/2)*self.Zoom),self.y)
        self.GroupeWidget.append(MyGroupWidget)
        self.r=(h*self.Zoom)+(r*self.Zoom)
class Losange(Forme):
   def __init__(self,x,y,Parametres,Color,Name,Options=[],PythonScript=None,Load=False):
      self.TypeForme="Losange"
      Forme.__init__(self,x,y,Parametres,Color,Name,Options,PythonScript,Load)
      self.Init()
      self.StartType()
   def StartType(self):
        self.TypeParametreSyc="Booleen"
        MyGroupWidget=[]
        r=5
        r=self.espace(r)
        h=15
        #print(r,self.Parametres)
        posi=(self.x+(h*self.Zoom),self.y,
              self.x+(r*self.Zoom)+(h*self.Zoom),self.y,
              self.x+(r*self.Zoom)+((h*self.Zoom)*2),self.y+((h/2)*self.Zoom),
              self.x+(r*self.Zoom)+(h*self.Zoom),self.y+(h*self.Zoom),
              self.x+(h*self.Zoom),self.y+(h*self.Zoom),
              self.x,self.y+((h/2)*self.Zoom))

        A=self.Canevas.create_polygon(posi, outline=color(Couleurs.gris), fill=self.Color)
        MyGroupWidget.append(A)
        self.BoxCollider.append([self.x,self.y , self.x+(r*self.Zoom)+((h*self.Zoom)*2),self.y+(h*self.Zoom)])
        
        MyGroupWidget=self.ShowParametre(0,h,MyGroupWidget,self.x+(h*self.Zoom),self.y+((h/2)*self.Zoom))
        self.GroupeWidget.append(MyGroupWidget)
        self.r=(r*self.Zoom)+((h*self.Zoom)*2)
class Encadrement(Forme):
   def __init__(self,x,y,Parametres,Color,Name,Options=[],PythonScript=None,Load=False):
      self.TypeForme="Encadrement"
      Forme.__init__(self,x,y,Parametres,Color,Name,Options,PythonScript,Load)
      self.Init()
      self.StartType()
   def StartType(self):
        self.CanPutInBlock=True
        self.CanAddBlock=True
        Encoche=1
        End=False
        Parametre=[self.Parametres]
        for i in self.Options:
            if i[0]=="Encoche":
                Encoche=i[1]
            if i[0]=="End":
                End=i[1]
            if i[0]=="Parametres":
                Parametre.append(i[1])
        h=15
        d=0
        e=0
        PosYpara=[]
        h_add=0
        if len(self.NextBlockIn)<2:
            for i in range(Encoche+2):
                self.NextBlockIn.append(None)
                self.NextBlockPosY.append(0)
        for i in range(Encoche):
            MyGroupWidget=[]
            try:
                self.Parametres=Parametre[i]
            except:
                self.Parametres=[]
            d+=e
            r=30
            r=self.espace(r)
            e=0
            if i==0:
                posi=(self.x,self.y,
                      self.x+(5*self.Zoom),self.y, self.x+(10*self.Zoom),self.y+(5*self.Zoom), self.x+(15*self.Zoom),self.y+(5*self.Zoom), self.x+(20*self.Zoom),self.y,
                      self.x+(r*self.Zoom),self.y, self.x+(r*self.Zoom),self.y+(h*self.Zoom))
                
                self.BoxCollider.append([self.x,self.y , self.x+(r*self.Zoom),self.y+(h*self.Zoom)])
                self.NextBlockPosY[0]=(((h)*self.Zoom))
                self.x_add[0]=(3*self.Zoom)
            else:
                self.NextBlockPosY[i]=(((h)*self.Zoom)+(d*self.Zoom))
            
            if i==0:PosYpara.append(self.y+((h/2)*self.Zoom)+(d*self.Zoom))
            else:PosYpara.append(self.y+(int(h/1.5)*self.Zoom)+(d*self.Zoom))
            
            if self.NextBlockIn[i]!=None:
                self.h_add=(h/2)
                try:
                    e=self.lenBlock(WindCanvas.AllWidget.get(self.NextBlockIn[i]),e)
                except:
                    pass
            else:
                e=h
                h_add+=h
            
            posi+=(self.x+(3*self.Zoom)+(20*self.Zoom),self.y+(h*self.Zoom)+(d*self.Zoom),
                      self.x+(3*self.Zoom)+(15*self.Zoom),self.y+(h*self.Zoom)+(5*self.Zoom)+(d*self.Zoom),
                      self.x+(3*self.Zoom)+(10*self.Zoom),self.y+(h*self.Zoom)+(5*self.Zoom)+(d*self.Zoom),
                      self.x+(3*self.Zoom)+(5*self.Zoom),self.y+(h*self.Zoom)+(d*self.Zoom))
            
            posi+=(self.x+(3*self.Zoom),self.y+(h*self.Zoom)+(d*self.Zoom),
                  
                  self.x+(3*self.Zoom),self.y+((h)*self.Zoom)+(e*self.Zoom)+(d*self.Zoom),
                  self.x+(3*self.Zoom)+(5*self.Zoom),self.y+((h)*self.Zoom)+(e*self.Zoom)+(d*self.Zoom),
                  self.x+(3*self.Zoom)+(10*self.Zoom),self.y+((h)*self.Zoom)+(e*self.Zoom)+(5*self.Zoom)+(d*self.Zoom),
                  self.x+(3*self.Zoom)+(15*self.Zoom),self.y+((h)*self.Zoom)+(e*self.Zoom)+(5*self.Zoom)+(d*self.Zoom),
                  self.x+(3*self.Zoom)+(20*self.Zoom),self.y+((h)*self.Zoom)+(e*self.Zoom)+(d*self.Zoom),
                  self.x+(r*self.Zoom),self.y+((h)*self.Zoom)+(e*self.Zoom)+(d*self.Zoom),
                  self.x+(r*self.Zoom),self.y+((h)*self.Zoom)+(e*self.Zoom)+((h/2)*self.Zoom)+(d*self.Zoom))
    
            if i+1==Encoche:
                if End:
                    posi+=(self.x,self.y+((h)*self.Zoom)+(e*self.Zoom)+((h/2)*self.Zoom)+(d*self.Zoom))
                else:
                    posi+=(self.x+(20*self.Zoom),self.y+((h)*self.Zoom)+(e*self.Zoom)+((h/2)*self.Zoom)+(d*self.Zoom),
                           self.x+(15*self.Zoom),self.y+((h)*self.Zoom)+(e*self.Zoom)+((h/2)*self.Zoom)+(d*self.Zoom)+(5*self.Zoom),
                           self.x+(10*self.Zoom),self.y+((h)*self.Zoom)+(e*self.Zoom)+((h/2)*self.Zoom)+(d*self.Zoom)+(5*self.Zoom),
                           self.x+(5*self.Zoom),self.y+((h)*self.Zoom)+(e*self.Zoom)+((h/2)*self.Zoom)+(d*self.Zoom),
                           self.x,self.y+((h)*self.Zoom)+(e*self.Zoom)+((h/2)*self.Zoom)+(d*self.Zoom))
    
                    self.NextBlockPosY[i+1]=(((h)*self.Zoom)+((h/2)*self.Zoom)+(e*self.Zoom)+(d*self.Zoom))
                    self.BoxCollider.append([self.x,self.y+((h)*self.Zoom)+(e*self.Zoom)+(d*self.Zoom),
                                     self.x+(r*self.Zoom),self.y+(h*self.Zoom) +((h)*self.Zoom)+(e*self.Zoom)+(d*self.Zoom)])
                    try:
                        self.x_add[i+1]=0
                    except:
                        self.x_add.append(0)
            else:
                self.NextBlockPosY[i+1]=(((h*2)*self.Zoom)+(e*self.Zoom)+(d*self.Zoom))
                self.BoxCollider.append([self.x,self.y+((h)*self.Zoom)+(e*self.Zoom)+(d*self.Zoom),
                                     self.x+(r*self.Zoom),self.y+(h*self.Zoom) +((h)*self.Zoom)+(e*self.Zoom)+(d*self.Zoom)])
                try:
                    self.x_add[i+1]=(3*self.Zoom)
                except:
                    self.x_add.append((3*self.Zoom))
            e+=(h/2)
            
            
            
        
        A=self.Canevas.create_polygon(posi, outline=color(Couleurs.gris), fill=self.Color)
        for i in range(Encoche):
            MyGroupWidget=[]
            try:
                self.Parametres=Parametre[i]
            except:
                self.Parametres=[]
            opts=None
            if i!=0:
               opts="NotBoxColi"
            MyGroupWidget=self.ShowParametre(20+3,h,MyGroupWidget,self.x,PosYpara[i],opts=opts)
            self.GroupeWidget.append(MyGroupWidget)
        self.GroupeWidget[0].insert(0,A)
        self.Parametres=Parametre[0]
        self.h_add=(h/2)*Encoche+h_add
class Vague(Forme):
   def __init__(self,x,y,Parametres,Color,Name,Options=[],PythonScript=None,Load=False):
      self.TypeForme="Vague"
      Forme.__init__(self,x,y,Parametres,Color,Name,Options,PythonScript,Load)
      self.Init()
      self.StartType()
   def StartType(self):
        self.CanPutInBlock=False
        self.CanAddBlock=True
        MyGroupWidget=[]
        r=10
        r=self.espace(r)
        h=15
        #print(r,self.Parametres)
        posi=(self.x,self.y,
              self.x+(10*self.Zoom),self.y-(10*self.Zoom),
              self.x+(20*self.Zoom),self.y-(10*self.Zoom),
              #self.x+(int(r*0,5)*self.Zoom),self.y,
              self.x+(r*self.Zoom),self.y,
              self.x+(r*self.Zoom),self.y+(h*self.Zoom),
              self.x+(20*self.Zoom),self.y+(h*self.Zoom),
              self.x+(15*self.Zoom),self.y+(h*self.Zoom)+(5*self.Zoom),
              self.x+(10*self.Zoom),self.y+(h*self.Zoom)+(5*self.Zoom),
              self.x+(5*self.Zoom),self.y+(h*self.Zoom),
              self.x,self.y+(h*self.Zoom))
        
        A=self.Canevas.create_polygon(posi, outline=color(Couleurs.gris), fill=self.Color)
        MyGroupWidget.append(A)
        self.BoxCollider.append([self.x,self.y , self.x+(r*self.Zoom),self.y+(h*self.Zoom)])
        
        MyGroupWidget=self.ShowParametre(5,h,MyGroupWidget,self.x,self.y+((h/2)*self.Zoom))
        self.GroupeWidget.append(MyGroupWidget)
class EndBox(Forme):
   def __init__(self,x,y,Parametres,Color,Name,Options=[],PythonScript=None,Load=False):
      self.TypeForme="EndBox"
      Forme.__init__(self,x,y,Parametres,Color,Name,Options,PythonScript,Load)
      self.Init()
      self.StartType()
   def StartType(self):
        self.CanPutInBlock=True
        self.CanAddBlock=False
        MyGroupWidget=[]
        r=25
        r=self.espace(r)
        h=15
        posi=(self.x,self.y, self.x+(5*self.Zoom),self.y, self.x+(10*self.Zoom),self.y+(5*self.Zoom), self.x+(15*self.Zoom),self.y+(5*self.Zoom), self.x+(20*self.Zoom),self.y, self.x+(r*self.Zoom),self.y, self.x+(r*self.Zoom),self.y+(h*self.Zoom), self.x,self.y+(h*self.Zoom))
        A=self.Canevas.create_polygon(posi, outline=color(Couleurs.gris), fill=self.Color)
        MyGroupWidget.append(A)
        self.BoxCollider.append([self.x,self.y , self.x+(r*self.Zoom),self.y+(h*self.Zoom)])
        
        MyGroupWidget=self.ShowParametre(20,h,MyGroupWidget,self.x,self.y+((h/2)*self.Zoom))
        self.GroupeWidget.append(MyGroupWidget)

def MoveAll(x,y,x2,y2):
   for forme in list(WindCanvas.AllWidget.values()):
      if forme.ParentBlock==None:
         forme.SetXY(forme.x+(x2-x),forme.y+(y2-y))
def MoveWidget(forme,x,y,x2,y2):
   forme.SetXY(forme.x+(x2-x),forme.y+(y2-y))
class MoveObject:
    def __init__(self):
       self.X=0
       self.Y=0
       self.canevas=WindCanvas.MainCanvas
       self.WidgetIsDrabed=False
       self.DragAndInOtherBlock=False
       self.LastMclicX=None
       self.LastMclicY=None
    def ClicDuMilleu(self,event):
       self.LastMclicX = event.x
       self.LastMclicY = event.y
    def ClicDuMilleuDrag(self,event):
       X = event.x
       Y = event.y
       self.X=X
       self.Y=Y
       if WindCanvas.CamX+(X-self.LastMclicX)>=0:
          X-=abs(WindCanvas.CamX+(X-self.LastMclicX))
       if WindCanvas.CamY+(Y-self.LastMclicY)>=0:
          Y-=abs(WindCanvas.CamY+(Y-self.LastMclicY))
       MoveAll(self.LastMclicX,self.LastMclicY,X,Y)
       WindCanvas.CamX=WindCanvas.CamX+(X-self.LastMclicX)
       WindCanvas.CamY=WindCanvas.CamY+(Y-self.LastMclicY)
       self.LastMclicX=X
       self.LastMclicY=Y
    def Clic(self,event):
       self.canevas.focus_set()
       self.LastMclicX = event.x
       self.LastMclicY = event.y
       self.X=self.LastMclicX 
       self.Y=self.LastMclicY
       maxTemp=0
       for i in list(WindCanvas.AllWidget.values()):
          if i==None:continue
          temp = i.TypeForme in FormeParametre
          [xmin,ymin,xmax,ymax] = i.BoxCollider[0]
          if xmin<=self.LastMclicX<=xmax and ymin<=self.LastMclicY<=ymax:
             for A in i.GroupeWidget:
                for W in A:
                   if type(W)==int and W>maxTemp:
                      self.WidgetIsDrabed=i
                      maxTemp=W
    def Drag(self,event):
       X = event.x
       Y = event.y
       if X<0:
          return#X = self.LastMclicX
       if Y<0:
          return#Y = self.LastMclicY
       if self.WidgetIsDrabed==False:
            return
       if self.WidgetIsDrabed.ParentBlock!=None:
            if self.WidgetIsDrabed.TypeForme in FormeParametre:
                tempObj=WindCanvas.AllWidget.get(self.WidgetIsDrabed.ParentBlock)
                for ind2,o in enumerate(tempObj.GroupeParametre):
                    if o[1]==self.WidgetIsDrabed.WidgetIndex:
                        (tempObj.GroupeParametre[ind2])[1]=None
                        tempObj.update()
                        break
            else:
                tempNb=WindCanvas.AllWidget.get(self.WidgetIsDrabed.ParentBlock).NextBlockIn.index(self.WidgetIsDrabed.WidgetIndex)
                WindCanvas.AllWidget.get(self.WidgetIsDrabed.ParentBlock).NextBlockIn[tempNb]=None
                WindCanvas.AllWidget.get(self.WidgetIsDrabed.ParentBlock).update()
            self.WidgetIsDrabed.ParentBlock=None
        
        #print(self.WidgetIsDrabed.NextBlockIn)
        
       self.DragAndInOtherBlock=False
       for ind,i in enumerate(list(WindCanvas.AllWidget.values())):
            if i==None or i==self.WidgetIsDrabed:continue
            if ind != self.WidgetIsDrabed.WidgetIndex:
                for ind2,o in enumerate(i.BoxCollider):
                    [xmin,ymin,xmax,ymax] = o
                    if xmin<=self.X<=xmax and ymin<=self.Y<=ymax:
                        self.DragAndInOtherBlock=i
                        self.NbBoxCollider=ind2
       MoveWidget(self.WidgetIsDrabed,self.LastMclicX,self.LastMclicY,X,Y)
       if self.WidgetIsDrabed!=False:
            self.WidgetIsDrabed.update()
       self.LastMclicX=X
       self.LastMclicY=Y
       self.X=X
       self.Y=Y
    def Drop(self,event):
       Done=False
       if self.WidgetIsDrabed!=False:
            if self.WidgetIsDrabed.TypeForme in FormeParametre:
                for ind,i in enumerate(list(WindCanvas.AllWidget.values())):
                    if Done:break
                    if i==None or i==self.WidgetIsDrabed:continue
                    for ind2,o in enumerate(i.BoxColiParametre):
                        #print(i.GroupeParametre,i.BoxColiParametre,ind2,i.WidgetIndex)
                        if Done:break
                        if (i.GroupeParametre[ind2])[0]==self.WidgetIsDrabed.TypeParametreSyc:
                            [xmin,ymin,xmax,ymax] = o
                            if xmin<=self.X<=xmax and ymin<=self.Y<=ymax:
                                if (i.GroupeParametre[ind2])[1]!=None:continue
                                (i.GroupeParametre[ind2])[1]=self.WidgetIsDrabed.WidgetIndex
                                self.WidgetIsDrabed.ParentBlock=i.WidgetIndex
                                Done=True
                                break
       if 10<=event.x<=60 and 10<=event.y<=60 and self.WidgetIsDrabed!=False:
            self.WidgetIsDrabed.RemoveSelf()
            self.WidgetIsDrabed=False
       else:
          if self.DragAndInOtherBlock!=False and self.WidgetIsDrabed!=False:
               #print("ok")
               #print(self.DragAndInOtherBlock.CanAddBlock,self.WidgetIsDrabed.CanPutInBlock)
               if self.DragAndInOtherBlock.CanAddBlock==True and self.WidgetIsDrabed.CanPutInBlock==True:
                   #print(self.NbBoxCollider,self.DragAndInOtherBlock.NextBlockIn)
                   if self.DragAndInOtherBlock.NextBlockIn[self.NbBoxCollider]!=None:
                       tempB=WindCanvas.AllWidget.get(self.DragAndInOtherBlock.NextBlockIn[self.NbBoxCollider])

                       self.DragAndInOtherBlock.NextBlockIn[self.NbBoxCollider]=None
                       tempB.ParentBlock=None

                       MoveWidget(tempB,tempB.x,tempB.y,tempB.x+20,tempB.y + 20)
                       tempB.update()
                   
                   #self.DragAndInOtherBlock.GroupeWidget+=self.WidgetIsDrabed.GroupeWidget
                   self.DragAndInOtherBlock.NextBlockIn[self.NbBoxCollider]=self.WidgetIsDrabed.WidgetIndex
                   self.WidgetIsDrabed.ParentBlock=self.DragAndInOtherBlock.WidgetIndex
                   
       self.FrontPlanObject()
       if self.WidgetIsDrabed!=False:
            self.WidgetIsDrabed.update()
       self.WidgetIsDrabed=False
       self.DragAndInOtherBlock=False
       MoveObjetDobe=True
    def FrontPlanObject(self):
        for Widget in list(WindCanvas.AllWidget.values()):
            if Widget==None:continue
            if Widget.TypeForme=="Encadrement":
                Widget.update()
        for Widget in list(WindCanvas.AllWidget.values()):
            if Widget==None:continue
            if Widget.TypeForme in ListFormeInFront:
                Widget.update()
