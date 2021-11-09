from Particule import *
from ClassSystem.ScrollableFrame import ScrollableFrame
from ClassSystem.CheckboxTreeview import *
from PIL import ImageFilter
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


        self.checkBoxTree = CheckboxTreeview(self.WTypeCompileLabel)
        self.checkBoxTree.pack(fill=X, expand=True)

        scenes = rf.GetList(self.Particule.FolderProject + "/ProjectSettings/BuildSettings.txt","ScenesInBuild")
        for ind,i in enumerate(scenes):
            self.checkBoxTree.insert(parent='',iid=ind,index='end',text=i[0])
            if i[1]:
                self.checkBoxTree.item_check(ind)
        #self.checkBoxTree.column("Ordre")
        #self.checkBoxTree.column("Path")

        self.addScene = Button(self.WTypeCompileLabel,text="Add Current Scene",command=self.AddCurrentScene)
        self.addScene.pack(side=RIGHT, padx=5, pady=5)


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

        Bouton_TypeCompile = Button(WInfoCompileFrame, text="Build", command = self.BuildAll)#, command=partial(BuildForCasio, (
        #WTypeCompileListPlatform, CompileArchitecCombobox, WTypeCompileListScene)))  # , command = ImportImage)
        Bouton_TypeCompile.grid(row=1, column=1)
        """
        Bouton_TypeCompile2 = Button(WTypeCompilemainframe, text ="Annuler", command=WTypeCompile.destroy)#, command = ImportImage)
        Bouton_TypeCompile2.grid(row=0,column=1)
        """
        #WTypeCompile.mainloop()
        #WTypeCompile.destroy()

    def AddCurrentScene(self,*args):
        scenes = rf.GetList(self.Particule.FolderProject + "/ProjectSettings/BuildSettings.txt", "ScenesInBuild")
        for i in self.Particule.Scene.scenes:
            if not i in scenes:
                scenes.append([i,True])
                self.checkBoxTree.insert(parent='', iid=len(scenes), index='end', text=i)

        rf.save(self.Particule.FolderProject + "/ProjectSettings/BuildSettings.txt", "ScenesInBuild", scenes)

    def BuildAll(self,*args):
        self.Particule.SaveData.SaveScene()
        AllImages=""
        CodeOfScenes = ""

        path = self.Particule.FolderProject + "/Library/ImagesBmpCache"
        for i in os.listdir(path):
            if ".meta" in i : continue
            name = os.path.basename(i)
            name = os.path.splitext(name)[0]
            img = SpriteCoder.ConvertImg(path+"/"+i,name)[0]
            AllImages+=img+"\n"

            Img = ImageTk.Image.open(path+"/"+i)
            width = Img.width
            height = Img.height
            CodeOfScenes += "Texture* Texture_"+name+'= new Texture("Texture",' + str(width) + "," + str(height) + "," + name+');\n'

        #print(AllImages)
        scenes = rf.GetList(self.Particule.FolderProject + "/ProjectSettings/BuildSettings.txt", "ScenesInBuild")

        for ind,i in enumerate(scenes):
            if i[1]:
                CodeOfScenes+="if (index == "+str(ind)+"){\n"
                code = ""
                CodeInit = ""
                components = ""
                self.Particule.SaveData.LoadScene(i[0])
                for i in self.Particule.Hierarchy.allGameObjectOnScene.items():
                    CodeInit+="GameObject* "+i[0]+";\n"
                    code += i[0]+'= new GameObject(newScene, "'+i[1].name+'","'+i[0]+'");\n'
                    code += i[0]+"->activeSelf = "+str(i[1].activeSelf).lower()+";\n"
                    code += i[0] + "->activeInHierarchy = " + str(i[1].activeInHierarchy).lower() + ";\n"
                    code += i[0] + "->isStatic = " + str(i[1].isStatic).lower() + ";\n"
                    code += i[0]+'->transform->position->Set('+str(i[1].transform.position.x)+','+str(i[1].transform.position.y)+');\n'
                    code += i[0] + '->transform->localPosition->Set(' + str(i[1].transform.localPosition.x) + ',' + str(i[1].transform.localPosition.y) + ');\n'
                    if i[1].transform.parent!=None:
                        code+=i[0]+"->transform->SetParent("+i[1].transform.parent.gameObject.ID+"->transform);"
                    for compo in i[1].ListOfComponent:
                        data = compo.BuildValue()
                        code = data[0]+code
                        components+=compo.AddScriptBeforInitCasio()+"\n"
                        components+=data[1]
                        if type(compo).__name__ != "Transform":
                            components +=i[0]+"->AddComponent((Component*)"+compo.ID+");\n"
                        components += compo.AddScriptAfterInitCasio() + "\n"
                    code+="newScene->AddGameObject("+i[0]+");\n"
                code +=components
                code = CodeInit+code
                CodeOfScenes +=code
                CodeOfScenes +="\n}"

        Announcement,CasioCode = self.GetCodeCasioFromVisualScratch()


        desti = self.Particule.FolderProject + "/Temp/Compile"
        M.create_rep(desti)
        for i in os.listdir(desti):
            try:
                os.remove(desti + "/" + i)
            except:
                shutil.rmtree(desti + "/" + i)
        for i in os.listdir("lib/Moteur/SDK Graph 75 85 95"):
            try:
                shutil.copy("lib/Moteur/SDK Graph 75 85 95/" + i, desti + "/" + i)
            except:
                shutil.copytree("lib/Moteur/SDK Graph 75 85 95/" + i, desti + "/" + i)

        with open(desti+"/Ressources.h","r") as fic:
            txt=fic.read()
        txt = txt.replace("//AddImages",AllImages)
        with open(desti+"/Ressources.h","w") as fic:
            fic.write(txt)

        with open(desti+"/ParticuleEngine.hpp","r") as fic:
            txt=fic.read()
        txt = txt.replace("//AddScenes",CodeOfScenes)
        txt = txt.replace("//Components", CasioCode)
        with open(desti+"/ParticuleEngine.hpp","w") as fic:
            fic.write(txt)

        with open(desti+"/Announcement.h","r") as fic:
            txt=fic.read()
        txt +=Announcement
        with open(desti+"/Announcement.h","w") as fic:
            fic.write(txt)

        #subprocess.Popen(r'explorer /select,"' + desti+"/ParticuleEngine.h" + '"')
        FILEBROWSER_PATH = os.path.join(os.getenv('WINDIR'), 'explorer.exe')
        subprocess.run([FILEBROWSER_PATH, os.path.abspath(desti)])


    def GetCodeCasioFromVisualScratch(self):
        for i in os.listdir(self.Particule.FolderProject+ "/Library/ScriptEditor/"):
            if ".py" in i:
                os.remove(self.Particule.FolderProject+ "/Library/ScriptEditor/"+i)
        process = subprocess.Popen([self.Particule.VisualScratchPath,self.Particule.FolderProject + '/SLN/Solution.sls',"True"], stdout=subprocess.PIPE)
        #print(eval(process.stdout.readlines()[-1]))
        code=eval(process.stdout.readlines()[-1])
        CasioCodeLst=code[1]
        CasioCode=""
        for i in CasioCodeLst:
            CasioCode+=i[1]+"\n"
        Announcement="\n"
        for i in CasioCodeLst:
            name = os.path.basename(i[0])
            name = os.path.splitext(name)[0]
            Announcement+="class "+name+";\n"
        return (Announcement,CasioCode)