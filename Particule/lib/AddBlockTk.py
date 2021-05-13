from tkinter import *
import tkinter
from tkinter.messagebox import *
from tkinter import ttk
from SystemExt import read_file as rf
from functools import partial
from SystemExt import Scratch
class CreateScriptBlockTk:
    def NewCreateBlockInFile(self,frame):
        frame[0].destroy()
        self.CreateBlockInFile(frame[1])
    def DelParametreInEditBlock(self,Index):
        (self.LstParametreEditBlockFile[Index])[0].destroy()
        self.LstParametreEditBlockFile[Index]=None
    def AddParametreInEditBlock(self,frame,Value):
        Value=Value.get()
        TempFrame=LabelFrame(frame)
        TempFrame.pack(fill = BOTH, expand = True)
        NameLtx=None
        Label(TempFrame,text=Value).pack(side=LEFT)
        if Value in ["Label","TexteEtNombre","Liste"]:
           NameLtx=StringVar()
           NameL=Entry(TempFrame,textvariable=NameLtx)
           NameL.pack(side=LEFT) 
        TempBadd=Button(TempFrame,text="Supprimer",command=partial(self.DelParametreInEditBlock,len(self.LstParametreEditBlockFile)))
        TempBadd.pack(side=RIGHT)
        self.LstParametreEditBlockFile.append([TempFrame,Value,NameLtx])
    def ValideBlockInFile(self,Data):
        global _i
        NameFtx,TempA,TempB,txC,Lst,TempE=Data
        NameFile=NameFtx.get()
        if NameFile=="":return
        Onglet=TempA.get()
        TypeForme=TempB.get()
        Texte=txC.get()
        for i in range(len(Lst)):
           if None in Lst:
              Lst.remove(None)
        Parametres=[]
        for i in Lst:
           try:
               i[1]=i[1].get()
           except:
               pass
           try:
               if i[2]!=None:i[2]=i[2].get()
           except:
               pass
           if i[1]=="Liste":
              _i=i[2]
              eval(compile("_i="+_i, '<string>', 'exec'),globals(),globals())
              i[2]=_i
              Parametres.append([i[1],i[2]])
           else:
              if i[2]==None:
                 Parametres.append([i[1]])
              else:
                 Parametres.append([i[1],i[2]])
        Color=TempE.get()
        a=open("lib/ScriptBlocks/Blocks/"+NameFile+".txt","w")
        a.close()
        Trep="lib/ScriptBlocks/Blocks/"+NameFile+".txt"
        rf.save(Trep,"Onglet",Onglet)
        rf.save(Trep,"TypeForme",TypeForme)
        rf.save(Trep,"Texte",Texte)
        rf.save(Trep,"Parametres",str(Parametres))
        rf.save(Trep,"Color",Color)

    def CreateBlockInFile(self,mainFrame):
        TempFrame=ttk.Frame(mainFrame)
        TempFrame.pack()
        
        TempNew=Button(TempFrame,text="New File",command=partial(self.NewCreateBlockInFile,(TempFrame,mainFrame)))
        TempNew.pack()
        Label(TempFrame,text="Nom du fichier").pack()
        NameFtx=StringVar()
        NameF=Entry(TempFrame,textvariable=NameFtx)
        NameF.pack()
        
        Label(TempFrame,text="Onglet").pack()
        txA=StringVar()
        TempA=ttk.Combobox(TempFrame,textvariable=txA)
        TempA['values'] = tuple(Scratch.TypeBox)
        TempA.pack()
        Label(TempFrame,text="TypeForme").pack()
        txB=StringVar()
        TempB=ttk.Combobox(TempFrame,textvariable=txB)
        TempB['values'] = tuple(Scratch.Forme)
        TempB.pack()
        Label(TempFrame,text="Texte").pack()
        txC=StringVar()
        TempC=Entry(TempFrame,textvariable=txC)
        TempC.pack()
        
        Label(TempFrame,text="Parametres").pack()
        TempFramePara=Frame(TempFrame)
        
        TempFrameParaButton=Frame(TempFrame)
        TempFrameParaButton.pack()
        txTyp=StringVar()
        TempTyp=ttk.Combobox(TempFrameParaButton,textvariable=txTyp)
        TempTyp['values'] = ("Label","EmptyCercle","TexteEtNombre","Liste","Booleen")
        TempTyp.pack(side=LEFT)
        self.LstParametreEditBlockFile=[]
        TempBadd=Button(TempFrameParaButton,text="Add",command=partial(self.AddParametreInEditBlock,TempFramePara,TempTyp))
        TempBadd.pack(side=LEFT)
        TempFramePara.pack()
        
        Label(TempFrame,text="Couleur").pack()
        txE=StringVar()
        TempE=ttk.Combobox(TempFrame,textvariable=txE)
        example=Scratch.Couleurs()
        TempLst=[attr for attr in dir(example) if not callable(getattr(example, attr)) and not attr.startswith("__")]
        TempE['values'] = tuple(TempLst)
        TempE.pack()

        TempZ=Button(TempFrame,text="Valider",command=partial(self.ValideBlockInFile,
                                                              (NameFtx,
                                                               TempA,
                                                               TempB,
                                                               txC,
                                                               self.LstParametreEditBlockFile,
                                                               TempE)))
        TempZ.pack()
