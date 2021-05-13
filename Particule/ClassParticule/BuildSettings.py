from Particule import *
from ClassSystem.ScrollableFrame import ScrollableFrame

class BuildSettings(EditorWindow):
    def __init__(self, RootWindow):
        #bt = RootWindow.Particule.Inspector.Bouton_AddComponent
        #geo = str(bt.winfo_width()) + "x250"
        #geo += "+" + str(bt.winfo_rootx()) + "+" + str(bt.winfo_rooty() + bt.winfo_height())
        EditorWindow.__init__(self, RootWindow,
                              ExternalWindow={"name": "Build Settings", "geometry": "400x400"},
                              Resize=False, ScrollbarShow=False)
        self.pack(fill=tkinter.BOTH, expand=True)

        self.WTypeCompileLabel = LabelFrame(self, text="Scene in Build")
        self.WTypeCompileLabel.pack(fill=BOTH, expand=True)



        '''ChoixScenes = rf.GetList(FolderProject + "/setup.txt", "ScenesActive")
        if ChoixScenes == False:
            rf.save(FolderProject + "/setup.txt", "ScenesActive", [[str(ActuScene), True]])
            ChoixScenes = rf.GetList(FolderProject + "/setup.txt", "ScenesActive")

        WTypeCompileListScene = ChecklistBox(WTypeCompileLabel, ChoixScenes, SceneChangeActiveOnCompile, "Scene ", bd=1,
                                             relief="sunken", background="white")
        '''

        self.WTypeCompilemainframe = Frame(self)
        self.WTypeCompilemainframe.pack(fill=BOTH)

        WTypeCompileListPlatform = Listbox(self.WTypeCompilemainframe)
        for item in ["SDK casio"]:#Pj.Platforms:
            WTypeCompileListPlatform.insert(END, item)
        WTypeCompileListPlatform.grid(row=0, column=0, sticky='EWNS')

        WTypeCompileListPlatform.selection_set(0)

        WInfoCompileFrame = Frame(self.WTypeCompilemainframe)
        WInfoCompileFrame.grid(row=0, column=1, sticky='EWNS')

        ArchitectureLabel = Label(WInfoCompileFrame, text="Architecture: ")
        ArchitectureLabel.grid(row=0, column=0)
        CompileArchitecCombobox = ttk.Combobox(WInfoCompileFrame, values=[
            "SDK Graph 75 85 95"])  # os.listdir("lib/ScriptBlocks/Compilateur"))
        CompileArchitecCombobox.grid(row=0, column=1)
        CompileArchitecCombobox.current(0)

        Bouton_TypeCompile = Button(self, text="Build")#, command=partial(BuildForCasio, (
        #WTypeCompileListPlatform, CompileArchitecCombobox, WTypeCompileListScene)))  # , command = ImportImage)
        Bouton_TypeCompile.pack(side=RIGHT, padx=5, pady=5)
        """
        Bouton_TypeCompile2 = Button(WTypeCompilemainframe, text ="Annuler", command=WTypeCompile.destroy)#, command = ImportImage)
        Bouton_TypeCompile2.grid(row=0,column=1)
        """
        #WTypeCompile.mainloop()
        #WTypeCompile.destroy()