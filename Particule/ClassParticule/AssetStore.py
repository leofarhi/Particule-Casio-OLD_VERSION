from Particule import *
from ClassSystem.WinFrameBas import WinFrameBas
class AssetStore:
    def __init__(self, frame,_Particule):
        self.Particule = _Particule
        self.Oframe = frame
        self.FrameAssetStore = Frame(frame)  # ,width = 127*LastScaleScreen, height =63*LastScaleScreen)
        self.FrameAssetStore.pack(fill=BOTH, expand=True)

        self.FrameAssetImport = Frame(frame)  # ,width = 127*LastScaleScreen, height =63*LastScaleScreen)
        self.FrameAssetImport.pack(fill=BOTH, expand=True)

        threading.Thread(target=self.LoadStore).start()
        self.AllMyAssetStore()
        # self.label_Error=Label(self.FrameAssetStore, text="L'Asset Store n'est pas encore disponible.")
        # self.label_Error.pack()

        self.AllMyAsset()

    def AssetStoreframeconfig(self, event):
        self.AssetStoreCanvasScroll.configure(
            scrollregion=self.AssetStoreCanvasScroll.bbox("all"))  # ,width=200,height=200)

    def DownloadAsset(self, url):
        Dwn.Import(url, rep_sys + "/lib/Assets")
        SaveAll()
        All_load_on_start(True)
        All_load_Element_Start(True)
        self.UpdateScreen()

    def MyAssetStoreShow(self, frame, i, ind):
        urlElem = (i[2]).replace("/tree/", "/raw/")
        t = Dwn.web(urlElem + "/info.txt")
        a = LabelFrame(frame, text=i[1], bg="white")
        a.pack(fill=X, padx=5, pady=5, anchor='nw', side=TOP)
        try:
            b = Dwn.web_import_picture(urlElem + "/icon.png")
        except:
            b = Dwn.web_import_picture(urlElem + "/Icon.png")
        pygame.image.save(b, "lib/temp_lib/iconWeb.png")
        self.ImgMyAssetStore.append(PhotoImage(file=str("lib/temp_lib/iconWeb.png")))
        can1 = Canvas(a, width=50, height=50, bg='white')
        can1.create_image(0, 0, anchor=NW, image=self.ImgMyAssetStore[ind])
        can1.pack(side="left")
        frame_label = Frame(a, bg="white")
        frame_label.pack(side="left")
        label_name = Label(frame_label, text=TradTxt("Fait par : ") + i[0], bg="white", justify="left")
        label_name.pack(anchor='nw')
        label_info = Label(frame_label, text=t, bg="white", justify="left")
        label_info.pack(anchor='nw')

        if i[1] in os.listdir("lib/Assets"):
            label_imp = Label(a, text=TradTxt("Telechargé"), bg="white")
            label_imp.pack(side="right")
        else:
            Bouton = Button(a, text=TradTxt('Telecharger'), command=partial(self.DownloadAsset, urlElem + "/File.zip"))
            Bouton.pack(side="right")

    def LoadStore(self):
        self.DataAssetStore = []
        inc = 0
        t1 = ""
        t2 = "0"
        self.ImgMyAssetStore = []
        url_1 = Dwn.web("https://github.com/leofarhi/AssetsStoreParticule/raw/master/URL.txt").rstrip()
        Preload = True
        while t1 != t2:
            inc += 1
            url = url_1.replace("#Rp#", str(inc))
            t2 = t1
            # try:
            t1 = Dwn.LoadWeb(url)
            # except:
            #   return
            if t1 == t2:
                break
            data = []
            for i in t1:
                try:
                    i = i.split("[/Asset]")[1]
                    i = i.split("[\\Asset]")[0]
                    name = i.split("[/Name]")[1]
                    name = name.split("[\\Name]")[0]
                    project = i.split("[/Project]")[1]
                    project = project.split("[\\Project]")[0]
                    URL = i.split("[/URL]")[1]
                    URL = URL.split("[\\URL]")[0]
                    data.append([name, project, URL.replace('<a href="', "")])
                except:
                    ""
            self.DataAssetStore = self.DataAssetStore + data
            if len(self.DataAssetStore) > 0 and Preload == True:
                Preload = False
                threading.Thread(target=self.ShowStore).start()
        # print(self.DataAssetStore)

    def ShowStore(self):
        # print(self.DataAssetStore)
        for ind, i in enumerate(self.DataAssetStore):
            try:
                self.MyAssetStoreShow(self.Main_frame, i, ind)
            except:
                ""

    def AllMyAssetStore(self):
        self.AssetStoreFrameScroll = Frame(self.FrameAssetStore, bg="white")  # ,width=50,height=100,bd=1)
        self.AssetStoreFrameScroll.pack(fill=BOTH, expand=True)  # .grid(row=3,column=0, sticky='EWNS')

        self.AssetStoreCanvasScroll = Canvas(self.AssetStoreFrameScroll, bg="white")

        self.AllAssetStoreframe = Frame(self.AssetStoreCanvasScroll, bg="white")
        self.AllAssetStoreframe.pack(fill=BOTH, expand=True)

        # self.MyAssetShow(self.AllAssetStoreframe,i,ind)
        ###

        self.var_Entry_found = StringVar()
        # var_Entry_found.trace("w", updatefound)
        self.found_frame = LabelFrame(self.AllAssetStoreframe)
        self.found_frame.pack(fill=X, expand=True, anchor='nw', padx=5, pady=5)
        self.entry_found = Entry(self.found_frame, textvariable=self.var_Entry_found)
        self.entry_found.pack(side="left", fill=BOTH, expand=True)
        self.loupe_Img = PhotoImage(file='lib/loupe.png')
        Bouton_found = Button(self.found_frame, image=self.loupe_Img, command=partial(self.var_Entry_found.set,
                                                                                      "La barre de recherche n'est pas encore disponible."))  # , command = ImportImage)
        Bouton_found.pack(side="right")

        self.Main_frame = Frame(self.AllAssetStoreframe)
        self.Main_frame.pack(fill=BOTH, expand=True)

        ###

        self.AssetStoreScroll = Scrollbar(self.AssetStoreFrameScroll, orient="vertical",
                                          command=self.AssetStoreCanvasScroll.yview)
        self.AssetStoreCanvasScroll.configure(yscrollcommand=self.AssetStoreScroll.set)

        self.AssetStoreScroll2 = Scrollbar(self.AssetStoreFrameScroll, orient="horizontal",
                                           command=self.AssetStoreCanvasScroll.xview)
        self.AssetStoreCanvasScroll.configure(xscrollcommand=self.AssetStoreScroll2.set)

        self.AssetStoreScroll.pack(side="right", fill="y")
        self.AssetStoreScroll2.pack(side=BOTTOM, fill="x")

        self.AssetStoreCanvasScroll.pack(side="left", fill=BOTH, expand=True)
        self.Particule.LastScaleScreen = 8
        if self.Particule.LastScaleScreen > 6:
            self.AssetStoreCanvasCWin = self.AssetStoreCanvasScroll.create_window((0, 0),
                                                                                  window=self.AllAssetStoreframe,
                                                                                  anchor='nw',
                                                                                  width=124 * self.Particule.LastScaleScreen)
        else:
            self.AssetStoreCanvasCWin = self.AssetStoreCanvasScroll.create_window((0, 0),
                                                                                  window=self.AllAssetStoreframe,
                                                                                  anchor='nw', width=124 * 6)
        self.AllAssetStoreframe.bind("<Configure>", self.AssetStoreframeconfig)
        threading.Thread(target=self.ShowStore).start()

    def UpdateScreen(self):
        self.AssetStoreFrameScroll.destroy()
        self.AllMyAssetStore()
        self.AssetFrameScroll.destroy()
        self.AllMyAsset()

    def AssetImporteFonc(self, name):
        shutil.copytree("lib/Assets/" + name, FolderProject + "/Assets/" + name)
        SaveAll()
        All_load_on_start(True)
        All_load_Element_Start(True)
        self.AssetFrameScroll.destroy()
        self.AllMyAsset()

    def Assetframeconfig(self, event):
        self.AssetCanvasScroll.configure(scrollregion=self.AssetCanvasScroll.bbox("all"))  # ,width=200,height=200)

    def MyAssetShow(self, frame, i, ind):
        with open("lib/Assets/" + i + "/info.txt", 'r', encoding="utf-8") as fic:
            t = fic.read()
        a = LabelFrame(frame, text=i, bg="white")
        a.pack(fill=X, padx=5, pady=5, anchor='nw', side=TOP)
        try:
            self.ImgMyAsset.append(PhotoImage(file=str("lib/Assets/" + i + '/icon.png')))
        except:
            try:
                self.ImgMyAsset.append(PhotoImage(file=str("lib/Assets/" + i + '/Icon.png')))
            except:
                pass
        can1 = Canvas(a, width=50, height=50, bg='white')
        can1.create_image(0, 0, anchor=NW, image=self.ImgMyAsset[ind])
        can1.pack(side="left")
        label_info = Label(a, text=t, bg="white", justify="left")
        label_info.pack(side="left")
        if i in os.listdir(self.Particule.FolderProject + "/Assets/"):
            label_imp = Label(a, text=TradTxt("Importé"), bg="white")
            label_imp.pack(side="right")
        else:
            Bouton = Button(a, text=TradTxt('Importer'), command=partial(self.AssetImporteFonc, i))
            Bouton.pack(side="right")

    def AllMyAsset(self):
        self.AssetFrameScroll = Frame(self.FrameAssetImport, bg="white")  # ,width=50,height=100,bd=1)
        self.AssetFrameScroll.pack(fill=BOTH, expand=True)  # .grid(row=3,column=0, sticky='EWNS')

        self.AssetCanvasScroll = Canvas(self.AssetFrameScroll, bg="white")

        self.AllAssetframe = Frame(self.AssetCanvasScroll, bg="white")
        self.AllAssetframe.pack(fill=BOTH, expand=True)
        self.ImgMyAsset = []
        for ind, i in enumerate(os.listdir("lib/Assets")):
            self.MyAssetShow(self.AllAssetframe, i, ind)

        self.AssetScroll = Scrollbar(self.AssetFrameScroll, orient="vertical", command=self.AssetCanvasScroll.yview)
        self.AssetCanvasScroll.configure(yscrollcommand=self.AssetScroll.set)

        self.AssetScroll2 = Scrollbar(self.AssetFrameScroll, orient="horizontal", command=self.AssetCanvasScroll.xview)
        self.AssetCanvasScroll.configure(xscrollcommand=self.AssetScroll2.set)

        self.AssetScroll.pack(side="right", fill="y")
        self.AssetScroll2.pack(side=BOTTOM, fill="x")

        self.AssetCanvasScroll.pack(side="left", fill=BOTH, expand=True)
        if self.Particule.LastScaleScreen > 6:
            self.AssetCanvasCWin = self.AssetCanvasScroll.create_window((0, 0), window=self.AllAssetframe, anchor='nw',
                                                                        width=124 * self.Particule.LastScaleScreen)
        else:
            self.AssetCanvasCWin = self.AssetCanvasScroll.create_window((0, 0), window=self.AllAssetframe, anchor='nw',
                                                                        width=124 * 6)
        self.AllAssetframe.bind("<Configure>", self.Assetframeconfig)
