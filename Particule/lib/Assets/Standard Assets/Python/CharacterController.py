class ImportComponent:
	def __init__(self,indCompo):
		self.name="CharacterController"
		self.nameCasio="CharacterController"
		self.mainframe=LabelFrame(AllComponentframe, text="Character Controller")
		self.mainframe.pack()
		self.varActif=IntVar()
		self.varActif.set(1)
		self.CheckActif = Checkbutton(self.mainframe,variable=self.varActif,text="Actif",state= ACTIVE,offvalue=0,onvalue=1)
		self.CheckActif.grid(row=0,column=0)
		self.Bouton_Remove = Button(self.mainframe, text ="Remove", command=self.Remove)
		self.Bouton_Remove.grid(row=0,column=1)



		self.Entry_vitesse1frame=Frame(self.mainframe)
		self.Entry_vitesse1frame.grid(row=1,column=0)
		self.label_vitesse1=Label(self.Entry_vitesse1frame, text='vitesse :')
		self.label_vitesse1.grid(row=0,column=0)
		self.var_Entry_vitesse1=StringVar()
		self.var_Entry_vitesse1.set("0")
		self.var_Entry_vitesse1.trace("w", self.updatevitesse1)
		self.entry_vitesse1=Entry(self.Entry_vitesse1frame,textvariable=self.var_Entry_vitesse1)
		self.entry_vitesse1.grid(row=0,column=1)

		self.AllvarNew=['var_Entry_vitesse1']
		self.AllvarORG=['frame', 'vitesse']

	def Remove(self):
		for ind,i in enumerate((Pj.Elements[Pj.selected]).listComponent):
			if i[0].mainframe==self.mainframe:
				del (Pj.Elements[Pj.selected]).listComponent[ind]
		self.mainframe.destroy()

	def SaveData(self):
		return {"varActif":int(self.varActif.get()),"var_Entry_vitesse1":int(self.var_Entry_vitesse1.get())}

	def DataCompile(self):
		a=self.SaveData()
		#a.insert(1,self.nameCasio)#for last version
		return a
	def LoadData(self,Data):
		try:vitesse1=Data.get('vitesse1')
		except:vitesse1=0
		self.varActif.set(str(varActif))
		self.var_Entry_vitesse1.set(str(var_Entry_vitesse1))


	def updatevitesse1(self,*args):
		try:
			self.var_Entry_vitesse1.set(str(int(self.var_Entry_vitesse1.get())))
		except:
			self.var_Entry_vitesse1.set("0")

