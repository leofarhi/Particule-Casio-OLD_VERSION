from Particule import *

class ParticuleHub:
    def __init__(self):
        self.Start = False
        self.RootHub = Tk()
        self.RootHub.title('Particule - Hub')
        self.RootHub.resizable(False, False)
        self.RootHub.grid_columnconfigure(0, weight=1)
        self.RootHub.grid_rowconfigure(0, weight=1)
        self.w = int(GetSystemMetrics(0) * 0.5)
        self.h = int(GetSystemMetrics(1) * 0.5)
        self.RootHub.geometry(str(self.w) + "x" + str(self.h))
        if Game_OS == "linux":
            try:
                self.RootHub.iconbitmap('@lib/logo.xbm')
            except:
                pass
            try:
                tempimg = tkinter.PhotoImage(file='lib/logo.png')
                self.RootHub.tk.call('wm', 'iconphoto', self.RootHub._w, tempimg)
            except:
                pass
        else:
            try:
                self.RootHub.iconbitmap('lib/logo.ico')
            except:
                pass

        self.BarreOnTop()
        self.FrameMain = Frame(self.RootHub)
        self.FrameMain.pack(fill=BOTH, expand=True, side=LEFT)

        self.Onglets()

        self.WinMain = LabelFrame(self.FrameMain)
        self.WinMain.pack(fill=BOTH, expand=True, side=LEFT)

        self.WinProjet()

        self.RootHub.mainloop()

    def NewProject(self):
        Folder = self.AddProject()
        M.create_rep(Folder+ "/Assets")
        M.create_rep(Folder + "/Assets/MyAsset")
        M.create_rep(Folder + "/Library")
        M.create_rep(Folder + "/Library/ImagesBmpCache")
        M.create_rep(Folder + "/Library/ScriptEditor")
        M.create_rep(Folder + "/Library/lib")
        M.create_rep(Folder + "/Package")
        M.create_rep(Folder + "/ProjectSettings")
        M.create_rep(Folder + "/Temp")
        M.create_rep(Folder + "/Temp/Compile")
        M.create_rep(Folder + "/SLN")
        shutil.copyfile("lib/vide.png", Folder + "/Library/lib/vide.png")

    def EditScriptBlock(self):
        self.RootHub.resizable(True, True)
        TempFrame = Frame(self.WinMain)
        TempFrame.pack(fill=BOTH, expand=True, side=LEFT)
        CSBT = AddBlockTk.CreateScriptBlockTk()
        CSBT.CreateBlockInFile(TempFrame)

    def BarreOnTop(self):
        Cheight = int(self.h * 0.1)
        self.CbarreTop = Canvas(self.RootHub, height=Cheight, bg="white")
        self.CbarreTop.pack(fill=X)
        self.img = Image.open("lib/LogoText.png")
        Wimg, Himg = self.img.size
        Wimg, Himg = int(Wimg * (Cheight / Himg)), int(Himg * (Cheight / Himg))
        self.img = self.img.resize((Wimg, Himg))  # , Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(self.img)
        self.CbarreTop.create_image(0, 0, anchor=NW, image=self.photo)

    def WinLearn(self):
        TempFrame = Frame(self.WinMain)
        TempFrame.pack(fill=BOTH, expand=True, side=LEFT)
        BoutonLearn = Button(TempFrame, text=TradTxt("Aller à la vidéo"), width=20, height=5,
                             command=partial(webbrowser.open, "https://youtu.be/WSUmLMhd7HQ"))
        BoutonLearn.pack(fill=X)
        # webbrowser.open('http://www.python.org')

    def ChangeOnglet(self, WinFrame):
        self.WinMain.destroy()
        self.WinMain = LabelFrame(self.FrameMain)
        self.WinMain.pack(fill=BOTH, expand=True, side=LEFT)
        WinFrame()

    def Onglets(self):
        self.Options = Frame(self.FrameMain, width=int(self.w * 0.2))
        self.Options.pack(side=LEFT, fill=Y)  # fill = BOTH, expand = True,side=LEFT)
        self.Options.configure(width=int(self.w * 0.2))
        self.BoutonProjet = Button(self.Options, text=TradTxt("Projets"), width=20, height=5,
                                   command=partial(self.ChangeOnglet, self.WinProjet))
        self.BoutonProjet.pack(fill=X)
        self.BoutonLearn = Button(self.Options, text=TradTxt("Apprendre"), width=20, height=5,
                                  command=partial(self.ChangeOnglet, self.WinLearn))
        self.BoutonLearn.pack(fill=X)

        self.BoutonLearn = Button(self.Options, text=TradTxt("Installs"), width=20,
                                  height=5)  # , command=partial(self.ChangeOnglet,self.WinLearn))
        self.BoutonLearn.pack(fill=X)

        self.BoutonLearn = Button(self.Options, text="Add ScriptBlock", width=20, height=5,
                                  command=partial(self.ChangeOnglet, self.EditScriptBlock))
        # self.BoutonLearn.pack(fill = X)

    def Compoframeconfig(self, event):
        self.FWinProjetCanvasScroll.configure(
            scrollregion=self.FWinProjetCanvasScroll.bbox("all"))  # ,width=200,height=200)

    def AddProject(self):
        global _i
        rep = Fl.open_folder()
        LstProjects = rf.GetList("setup.txt", "AllProjects")
        LstProjects.append([rep.split("/")[-1], rep])
        rf.save("setup.txt", "AllProjects", str(LstProjects))
        self.FrameWinProjet.destroy()
        self.WinProjet()
        return rep

    def BouttonOpen(self, Data):
        rf.save("setup.txt", "FolderProject", str(Data[1]))
        self.Start = True
        self.RootHub.destroy()

    def DelProject(self, Data):
        global _i
        LstProjects = rf.GetList("setup.txt", "AllProjects")
        LstProjects.remove(Data)
        rf.save("setup.txt", "AllProjects", str(LstProjects))
        self.FrameWinProjet.destroy()
        self.WinProjet()

    def WinProjet(self):
        global _i
        self.FrameWinProjet = Frame(self.WinMain)
        self.FrameWinProjet.pack(fill=BOTH, expand=True, side=LEFT)
        self.FrameBoutton = Frame(self.FrameWinProjet)
        self.FrameBoutton.pack(side=TOP, fill=X)

        self.BoutonNew = Button(self.FrameBoutton, text=TradTxt("Nouveau Projet"), bg="#2297f3", fg="white",
                                command=self.NewProject)
        self.BoutonNew.pack(side=RIGHT, padx=5, pady=5)

        self.BoutonAdd = Button(self.FrameBoutton, text=TradTxt("Ajouter un Projet"), bg="#2297f3", fg="white",
                                command=self.AddProject)
        self.BoutonAdd.pack(side=RIGHT, padx=5, pady=5)

        self.FWinProjet = LabelFrame(self.FrameWinProjet, text="Projets")  # ,width=50,height=100,bd=1)
        self.FWinProjet.pack(fill=BOTH, expand=True, side=LEFT)

        self.FWinProjetCanvasScroll = Canvas(self.FWinProjet)

        self.AllWinProjetframe = Frame(self.FWinProjetCanvasScroll)

        self.CompoScroll = Scrollbar(self.FWinProjet, orient="vertical", command=self.FWinProjetCanvasScroll.yview)
        self.FWinProjetCanvasScroll.configure(yscrollcommand=self.CompoScroll.set)

        self.CompoScroll.pack(side="right", fill="y")
        self.FWinProjetCanvasScroll.pack(side="left", fill="both", expand=True)

        self.FWinProjetCanvasScroll.create_window((0, 0), window=self.AllWinProjetframe, anchor='nw',
                                                  width=int(self.w * 0.75))
        self.AllWinProjetframe.bind("<Configure>", self.Compoframeconfig)

        LstProjects = rf.GetList("setup.txt", "AllProjects")

        if LstProjects == False:
            rf.save("setup.txt", "AllProjects", "[]")
            LstProjects = []
        else:
            for i in LstProjects:
                FrameLstP = LabelFrame(self.AllWinProjetframe, bg="white")  # ,width = self.FWinProjet.winfo_width())
                FrameLstP.pack(fill=X, side=TOP)  # , padx = 5, pady = 5,anchor='nw')#,fill = X)
                FrameLstPLabel = Frame(FrameLstP, bg="white")
                FrameLstPLabel.pack(side=LEFT)
                LabelLstP = Label(FrameLstPLabel, text=i[0], justify="left", bg="white")
                LabelLstP.grid(row=0, column=0, sticky="w")

                LabelLstPRep = Label(FrameLstPLabel, text=i[1], justify="left", bg="white")
                LabelLstPRep.grid(row=1, column=0, sticky="w")

                bouttonDel = Button(FrameLstP, text=TradTxt("Retirer"), command=partial(self.DelProject, i))
                bouttonDel.pack(side=RIGHT, padx=5, pady=5)

                bouttonOuvrir = Button(FrameLstP, text=TradTxt("Ouvrir"), command=partial(self.BouttonOpen, i))
                bouttonOuvrir.pack(side=RIGHT, padx=5, pady=5)