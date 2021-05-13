import inspect
from Particule import *
from ClassParticule.Vector2 import Vector2
from ClassSystem.TypeGUI import TypeGUI

from ClassParticule.Object import Object
class Component(Object):
    name=""
    def __init__(self,gameObject,name,**kwargs):
        Object.__init__(self,gameObject.Particule,name=name,**kwargs)
        self.gameObject = gameObject
        self.AttributVisible=[]
        self.myFrame = None
        self._valueGUI = []

    def SaveDataDict(self):
        return {"name":self.name,
                "gameObject":self.gameObject.ID}
    def LoadDataDict(self,data,component,dataCompo,dicoGameObject,dicoComponent):
        self.gameObject = dicoGameObject[dataCompo["gameObject"]]
        self.name = dataCompo["name"]

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
        if self.myFrame != None:
            self.myFrame.destroy()
        self.myFrame = LabelFrame(self.Particule.Inspector.mainComponentsFrame, text=self.name)
        self.myFrame.Particule = self.Particule
        #self.myFrame.pack(fill=tkinter.BOTH, expand=True)
        self.myFrame.bind("<Button-3>", self.popup)
        self.contextMenu = Menu(self.Particule.Mafenetre, tearoff=False)
        self.contextMenu.add_command(label="Copy")
        self.contextMenu.add_command(label="Past")
        self.contextMenu.add_separator()
        self.contextMenu.add_command(label="Duplicate")
        self.contextMenu.add_command(label="Delete", command=self.Destroy)
        one = False
        count = 0
        for i in self.GetAttribut():
            if i[0] in self.AttributVisible:
                # print(i[0],getattr(self,i[0]))
                one = True
                tempUI = TypeGUI(self.myFrame, self, i[0])
                tempUI.grid(row=count, column=0, sticky='EWNS')
                self._valueGUI.append(tempUI)
                count += 1
                # Button(self.myFrame,text=self.gameObject.name+i[0]+" : "+str(i[1].get())).pack()
        if not one:
            Label(self.myFrame, text="Pas de paramètres").pack()

    def PrintOnGui(self):
        if self.myFrame ==None:
            self.RefreshGUI()
        self.myFrame.pack(fill=tkinter.BOTH, expand=True)
        for i in self._valueGUI:
            i.Update()

    def popup(self, event):
        self.contextMenu.post(event.x_root, event.y_root)
    def Destroy(self,*args):
        self.gameObject.ListOfComponent.remove(self)
        if (self.myFrame!=None):
            self.myFrame.destroy()
        self.Particule.Inspector.UpdateItemSelected()



