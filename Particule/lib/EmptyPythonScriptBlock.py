class ImportComponent:
    def __init__(self,indCompo):
        self.name="$$NamePython$$" #nom du component
        self.nameCasio=(self.name.replace(" ",""))[:8]
        self.mainframe=LabelFrame(AllComponentframe, text=self.name)
        self.mainframe.pack()
        #---Vérifie si le component est actif---
        self.varActif=IntVar()
        self.varActif.set(1)
        self.CheckActif = Checkbutton(self.mainframe,variable=self.varActif,text="Actif",state= ACTIVE,offvalue=0,onvalue=1)
        self.CheckActif.grid(row=0,column=0)
        #------
        #Bouton de suppression--
        self.Bouton_Remove = Button(self.mainframe, text ='Remove', command=self.Remove)
        self.Bouton_Remove.grid(row=0,column=1)
        #---

    def Remove(self):# à garder sans modifier
        for ind,i in enumerate((Pj.Elements[Pj.selected]).listComponent):
            if i[0].mainframe==self.mainframe:
                del (Pj.Elements[Pj.selected]).listComponent[ind]
        self.mainframe.destroy()
        
    def SaveData(self):#sauvegarde des paramètres
        return [int(self.varActif.get())]
    
    def DataCompile(self):
        a=self.SaveData()
        a.insert(1,self.nameCasio)
        return a
    
    def LoadData(self,Data):#charge les paramètres au lancement du programme
        varActif=Data
        self.varActif.set(str(varActif))
