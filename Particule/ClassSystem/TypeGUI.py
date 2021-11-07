import inspect
from ClassSystem.PFrame import PFrame
from ClassParticule.Vector2 import Vector2
from Particule import *
from ClassParticule.SearchWindow import SearchWindow
from functools import partial

def ChangeLst(Objet,NameLst,Index,Value):
    lst = getattr(Objet, NameLst)
    lst[Index] = Value
    setattr(Objet, NameLst, lst)

class ListVar:
    def __init__(self):
        self.Val= []
        self.index=0
    def set(self,val):
        self.Val[self.index] = val
    def setIndex(self,index,val):
        self.Val[index] = val
    def getIndex(self,index):
        return self.Val[index]
    def GetAll(self):
        return self.Val
class TypeGUI(PFrame):
    def __init__(self,root,Objet,VarName,Recursion=None,Value=None):
        PFrame.__init__(self,root)
        self.Objet = Objet
        self.VarName = VarName
        if Recursion:
            variable = Value
        else:
            variable = getattr(Objet,VarName)
        self.IsDragable = False
        self.Data = None
        if (type(variable)==int):
            self.var = IntVar()
            self.var.set(variable)
            Label(self, text=self.VarName).grid(row=0, column=0)
            self.entry = Entry(self, textvariable=self.var)
            self.entry.bind('<KeyRelease>', self.changeIntFloatStrBool)
            self.entry.grid(row=0, column=1, sticky='EWNS')#.pack(fill=tkinter.BOTH, expand=True)
        elif (type(variable)==float):
            self.var = DoubleVar()
            self.var.set(variable)
            Label(self, text=self.VarName).grid(row=0, column=0)
            self.entry = Entry(self, textvariable=self.var)
            self.entry.bind('<KeyRelease>', self.changeIntFloatStrBool)
            self.entry.grid(row=0, column=1, sticky='EWNS')#.pack(fill=tkinter.BOTH, expand=True)
        elif type(variable)==str:
            self.var = StringVar()
            self.var.set(variable)
            Label(self, text=self.VarName).grid(row=0, column=0)
            self.entry = Entry(self, textvariable=self.var)
            self.entry.bind('<KeyRelease>', self.changeIntFloatStrBool)
            self.entry.grid(row=0, column=1, sticky='EWNS')#.pack(fill=tkinter.BOTH, expand=True)
        elif type(variable)==bool:
            self.var = IntVar()
            self.var.set(0)
            self.check = Checkbutton(self, variable=self.var, text=self.VarName, offvalue=0, onvalue=1,command=self.changeIntFloatStrBool)
            self.check.bind('<KeyRelease>', self.changeIntFloatStrBool)
            self.check.grid(row=0, column=1, sticky='EWNS')#.pack(fill=tkinter.BOTH, expand=True)
        elif type(variable)==list:
            self.FrameList = LabelFrame(self,text = str(VarName))
            self.FrameList.Particule = self.Particule
            self.FrameList.pack(fill=tkinter.BOTH, expand=True)
            self.AllValueUI = []
            self.SizeLst = IntVar()
            self.var = ListVar()
            self.SizeLst.set(len(variable))
            self.entrySize = Entry(self.FrameList, textvariable=self.SizeLst)
            self.entrySize.bind('<Return>', self.ChangeSizeLst)
            self.entrySize.grid(row=0, column=0, sticky='EWNS')  # .pack(fill=tkinter.BOTH, expand=True)
            for ind, i in enumerate(variable):
                self.var.Val.append(i)
                tempUI = TypeGUI(self.FrameList, self.var, ind,True,i)
                tempUI.grid(row=ind+1, column=0, sticky='EWNS')
                self.AllValueUI.append(tempUI)
        elif type(variable)==Vector2:
            self.var1 = IntVar()
            self.var2 = IntVar()
            self.var1.set(variable.x)
            self.var2.set(variable.y)
            Label(self, text=self.VarName).grid(row=0, column=0)
            Label(self, text="x :").grid(row=1, column=0)
            Label(self, text="y :").grid(row=1, column=2)
            self.entry1 = Entry(self, textvariable=self.var1)
            self.entry1.bind('<KeyRelease>', self.changeVector2)
            self.entry1.grid(row=1, column=1, sticky='EWNS')#.pack(fill=tkinter.BOTH, expand=True)
            self.entry2 = Entry(self, textvariable=self.var2)

            self.entry2.bind('<KeyRelease>', self.changeVector2)
            self.entry2.grid(row=1, column=3, sticky='EWNS')#.pack(fill=tkinter.BOTH, expand=True)
        else:
            self.Data = variable
            self.IsDragable = True
            self.var = StringVar()
            self.var.set(variable)
            Label(self, text=self.VarName).grid(row=0, column=0)
            self.entry = Entry(self, textvariable=self.var)#, state=DISABLED)###########
            self.entry.bind('<KeyRelease>', self.changeIntFloatStrBool)############
            #self.entry.bind("<ButtonRelease-1>", self.mouseRelease)
            #self.entry.bind("<Enter>", self.mouseEnter)
            #self.entry.bind("<Motion>", self.mouseEnter)
            # self.entry.bind("<Leave>", self.mouserelease)
            self.entry.grid(row=0, column=1, sticky='EWNS')  # .pack(fill=tkinter.BOTH, expand=True)
            self.entry.xview_moveto(1)
            self.bouttonSlc = Button(self,command = partial(SearchWindow,self.Particule.Mafenetre))
            self.bouttonSlc.grid(row=0, column=2, sticky='EWNS')

    """def mouseRelease(self, event):
        print("ok")
        print(self.Particule.Mafenetre.winfo_pointerx(),self.Particule.Mafenetre.winfo_pointery())
        print(self.winfo_rootx(), self.winfo_rooty(),self.winfo_width(),self.winfo_height())

    def mouseEnter(self,event):
        return
        print("ok1")
        print(event.x,event.y)
        self.focus()"""
    def Drop(self,Data):#DragAndDropSys
        #print(type(Data["Object"]),type(getattr(self.Objet,self. VarName)))
        if (not self.IsDragable) or type(Data["Object"])!=type(getattr(self.Objet,self. VarName)):
        #if (not self.IsDragable) or Data["Type"] != type(getattr(self.Objet, self.VarName)).__name__:
            return
        #print(Data["Object"].ToString())
        self.var.set(Data["Object"].ToString())
        self.Data = Data["Object"]
        self.changeOther()

    def ChangeSizeLst(self,*args):
        long= int(self.SizeLst.get())
        if len(self.var.Val)==long:
            return
        elif len(self.var.Val)<=long:
            for ind in range(len(self.var.Val),long):
                self.var.Val.append(0)
                tempUI = TypeGUI(self.FrameList, self.var, ind, True, 0)
                tempUI.grid(row=ind + 1, column=0, sticky='EWNS')
                self.AllValueUI.append(tempUI)
        elif len(self.var.Val) >= long:
            for i in range(len(self.var.Val)-long):
                self.AllValueUI[-1].destroy()
                del self.AllValueUI[-1]
                del self.var.Val[-1]
    def Update(self):
        if type(self.Objet)==ListVar:
            variable = self.Objet.Val[self.VarName]
        else:
            variable = getattr(self.Objet,self.VarName)
        if (type(variable) == int):
            self.var.set(variable)
        elif type(variable) == str:
            self.var.set(variable)
        elif type(variable) == list:
            self.var.Val = variable
        elif type(variable) == Vector2:
            self.var1.set(variable.x)
            self.var2.set(variable.y)
        else:
            try:
                self.var.set(variable.ToString())
            except:
                self.var.set(str(variable))

    def changeIntFloatStrBool(self,event):
        if type(self.Objet)==ListVar:
            self.Objet.Val[self.VarName] = self.var.get()
        else:
            setattr(self.Objet, self.VarName, self.var.get())


    def changeVector2(self,event):
        if type(self.Objet)==ListVar:
            return
        try:
            [self.var1.get(),self.var2.get()]
            v = getattr(self.Objet, self.VarName)
            v.x = int(self.var1.get())
            v.y = int(self.var2.get())
        except:
            pass
    def changeOther(self,event=None):
        if type(self.Objet) == ListVar:
            return
        try:
            setattr(self.Objet, self.VarName, self.Data)
        except:
            pass
