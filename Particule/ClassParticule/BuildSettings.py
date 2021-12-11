from Particule import *
from ClassSystem.ScrollableFrame import ScrollableFrame
from ClassSystem.CheckboxTreeview import *
from PIL import ImageFilter
import platform
import cv2
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
        self.pathProjectSettings = self.Particule.FolderProject + "/ProjectSettings/ProjectSettings.txt"


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
        """
        for item in ["Graph 35+USB/75/85/95 (SD)"]:#Pj.Platforms:
            WTypeCompileListPlatform.insert(END, item)
        """
        WTypeCompileListPlatform.grid(row=0, column=0, sticky='EWNS')

        WTypeCompileListPlatform.selection_set(0)

        WInfoCompileFrame = Frame(self.WTypeCompilemainframe)
        WInfoCompileFrame.grid(row=0, column=1, sticky='EWNS')

        ArchitectureLabel = Label(WInfoCompileFrame, text="Architecture: ")
        ArchitectureLabel.grid(row=0, column=0)
        self.CompileArchitec_var = tk.StringVar()
        self.CompileArchitecCombobox = ttk.Combobox(WInfoCompileFrame, textvariable=self.CompileArchitec_var,
             values=["SDK Graph 75 85 95","Gint"])  # os.listdir("lib/ScriptBlocks/Compilateur"))
        self.CompileArchitecCombobox.grid(row=0, column=1)
        self.CompileArchitecCombobox.current(0)

        Bouton_TypeCompile = Button(WInfoCompileFrame, text="Build", command = self.BuildAll)#, command=partial(BuildForCasio, (
        #WTypeCompileListPlatform, CompileArchitecCombobox, WTypeCompileListScene)))  # , command = ImportImage)
        Bouton_TypeCompile.grid(row=1, column=1)
        """
        Bouton_TypeCompile2 = Button(WTypeCompilemainframe, text ="Annuler", command=WTypeCompile.destroy)#, command = ImportImage)
        Bouton_TypeCompile2.grid(row=0,column=1)
        """
        #WTypeCompile.mainloop()
        #WTypeCompile.destroy()

        self.checkBoxTree.bind("<Button-3>", self.popup)
        self.contextMenu = Menu(self.Particule.Mafenetre, tearoff=False)

        self.contextMenu.add_command(label="Move Up", command=self.moveUp)
        self.contextMenu.add_command(label="Move Down", command=self.moveDown)
        self.contextMenu.add_command(label="Remove", command=self.deleteObject)
        self.contextMenu.add_command(label="Save", command=self.SaveLstScene)

    def popup(self, event):
        """action in event of button 3 on tree view"""
        # select row under mouse
        iid = self.checkBoxTree.identify_row(event.y)
        if iid:
            # mouse pointer over item
            self.checkBoxTree.selection_set(iid)
            self.contextMenu.post(event.x_root, event.y_root)
        else:
            # mouse pointer not over item
            # occurs when items do not fill frame
            # no action required
            pass

    def moveDown(self,*args):
        leaves = self.checkBoxTree.selection()
        for i in reversed(leaves):
            self.checkBoxTree.move(i, self.checkBoxTree.parent(i), self.checkBoxTree.index(i) + 1)
        self.SaveLstScene()

    def moveUp(self,*args):
        leaves = self.checkBoxTree.selection()
        for i in leaves:
            self.checkBoxTree.move(i, self.checkBoxTree.parent(i), self.checkBoxTree.index(i) - 1)
        self.SaveLstScene()

    def deleteObject(self,*args):
        for item in self.checkBoxTree.selection():
            self.checkBoxTree.delete(item)
        self.SaveLstScene()

    def SaveLstScene(self,*args):
        size=len(self.checkBoxTree.get_children())
        Scenes = [None for i in range(size)]
        for i in list(self.checkBoxTree.get_children("")):
            check = (self.checkBoxTree.item(i)['tags'])[0]=='checked'
            Scenes[int(self.checkBoxTree.index(i))]=[self.checkBoxTree.item(i)['text'],check]
        rf.save(self.Particule.FolderProject + "/ProjectSettings/BuildSettings.txt", "ScenesInBuild", Scenes)


    def AddCurrentScene(self,*args):
        scenes = rf.GetList(self.Particule.FolderProject + "/ProjectSettings/BuildSettings.txt", "ScenesInBuild")
        for i in self.Particule.Scene.scenes:
            if not i in scenes:
                scenes.append([i,True])
                self.checkBoxTree.insert(parent='', iid=len(scenes), index='end', text=i)

        rf.save(self.Particule.FolderProject + "/ProjectSettings/BuildSettings.txt", "ScenesInBuild", scenes)

    def BuildAll(self, *args):
        if (self.CompileArchitec_var.get()=="SDK Graph 75 85 95"):
            self.BuildAllForSDKCasio()
        elif (self.CompileArchitec_var.get()=="Gint"):
            self.BuildAllForGint()

    def BuildAllForSDKCasio(self,*args):
        self.Particule.SaveData.SaveScene()
        AllImages=""
        CodeOfScenes = ""
        CreateTexturesCode = ""
        TexturesID = ""

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
            TexturesID+="Texture* Texture_"+name+";\n"
            CreateTexturesCode += "Texture_"+name+'= new Texture("Texture",' + str(width) + "," + str(height) + "," + name+');\n'

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
                    code += i[0] + "->tag = Tag(" + str(i[1].tag.value) + ");\n"
                    code += i[0] + "->layer = Layer(" + str(i[1].layer.value) + ");\n"
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

        Announcement,CasioCode,Cpp = self.GetCodeCasioFromVisualScratch()

        desti = self.Particule.FolderProject + "/Temp/Compile"
        M.create_rep(desti)
        for i in os.listdir(desti):
            try:
                os.remove(desti + "/" + i)
            except:
                shutil.rmtree(desti + "/" + i)
        for i in os.listdir("lib/Moteur/ParticuleEngine"):
            try:
                shutil.copy("lib/Moteur/ParticuleEngine/" + i, desti + "/" + i)
            except:
                shutil.copytree("lib/Moteur/ParticuleEngine/" + i, desti + "/" + i)
        for i in os.listdir("lib/Moteur/SDK Graph 75 85 95"):
            try:
                shutil.copy("lib/Moteur/SDK Graph 75 85 95/" + i, desti + "/" + i)
            except:
                shutil.copytree("lib/Moteur/SDK Graph 75 85 95/" + i, desti + "/" + i)

        with open(desti+"/Ressources.h","r", encoding = "ISO-8859-1") as fic:
            txt=fic.read()
        txt = txt.replace("//AddImages",AllImages)
        with open(desti+"/Ressources.h","w") as fic:
            fic.write(txt)

        with open(desti+"/ParticuleEngine.hpp","r", encoding = "ISO-8859-1") as fic:
            txt=fic.read()
        txt = txt.replace("//AddScenes",CodeOfScenes)
        txt = txt.replace("//Components", CasioCode)

        txt = txt.replace("//CreateTextures", CreateTexturesCode)
        txt = txt.replace("//TexturesID", TexturesID)

        txt = self.ProjectSettingsReplace(txt)

        with open(desti+"/ParticuleEngine.hpp","w") as fic:
            fic.write(txt)

        with open(desti+"/ParticuleEngine.cpp","r", encoding = "ISO-8859-1") as fic:
            txt=fic.read()

        txt+=Cpp

        with open(desti+"/ParticuleEngine.cpp","w") as fic:
            fic.write(txt)

        with open(desti+"/Announcement.h","r", encoding = "ISO-8859-1") as fic:
            txt=fic.read()
        txt +=Announcement
        with open(desti+"/Announcement.h","w") as fic:
            fic.write(txt)

        shutil.copyfile(self.Particule.FolderProject + "/ProjectSettings/MainIcon.bmp",desti+"/MainIcon.bmp")

        #subprocess.Popen(r'explorer /select,"' + desti+"/ParticuleEngine.h" + '"')
        if platform.system()=="Windows":
            FILEBROWSER_PATH = os.path.join(os.getenv('WINDIR'), 'explorer.exe')
            subprocess.run([FILEBROWSER_PATH, os.path.abspath(desti)])
        else:
            try:
                os.system(r'xdg-open '+os.path.abspath(desti))
            except:pass


    def GetCodeCasioFromVisualScratch(self):
        for i in os.listdir(self.Particule.FolderProject+ "/Library/ScriptEditor/"):
            if ".py" in i:
                os.remove(self.Particule.FolderProject+ "/Library/ScriptEditor/"+i)
        if platform.system() == 'Windows':
            process = subprocess.Popen([self.Particule.VisualScratchPath,self.Particule.FolderProject + '/SLN/Solution.sls',"True"], stdout=subprocess.PIPE)
        elif platform.system() == 'Linux':
            process = subprocess.Popen(["python",self.Particule.VisualScratchPath,self.Particule.FolderProject + '/SLN/Solution.sls',"True"], stdout=subprocess.PIPE)
        else:
            raise Exception("Platform Not supporting")
        #print(eval(process.stdout.readlines()[-1]))
        code=eval(process.stdout.readlines()[-1].decode('latin-1'))
        CasioCodeLst=code[1]
        Hpp=""
        Cpp=""
        for i in CasioCodeLst:
            Hpp+=(i[1])[0]+"\n"
            Cpp += (i[1])[1] + "\n"
        Announcement="\n"
        for i in CasioCodeLst:
            name = os.path.basename(i[0])
            name = os.path.splitext(name)[0]
            Announcement+="class "+name+";\n"
        return (Announcement,Hpp,Cpp)

    def BuildAllForGint(self):
        self.Particule.SaveData.SaveScene()
        AllImages = ""
        CodeOfScenes = ""
        CreateTexturesCode = ""
        TexturesID = ""

        desti = self.Particule.FolderProject + "/Temp/Compile"
        destiCode = desti + "/ParticuleGame/src"
        M.create_rep(desti)
        for i in os.listdir(desti):
            try:
                os.remove(desti + "/" + i)
            except:
                try:
                    shutil.rmtree(desti + "/" + i)
                except:
                    if platform.system() == "Windows":
                        os.system('rmdir /S /Q "{}"'.format(desti + "/" + i))


        shutil.copytree("lib/Moteur/Gint/ParticuleGame", desti + "/ParticuleGame")

        for i in os.listdir("lib/Moteur/ParticuleEngine"):
            try:
                shutil.copy("lib/Moteur/ParticuleEngine/" + i, destiCode + "/" + i)
            except:
                shutil.copytree("lib/Moteur/ParticuleEngine/" + i, destiCode + "/" + i)

        for i in os.listdir("lib/Moteur/Gint/ParticuleGame/src/"):
            shutil.copy("lib/Moteur/Gint/ParticuleGame/src/" + i, destiCode + "/" + i)
        os.remove(destiCode + "/usefull.cpp")
        os.remove(destiCode + "/usefull.h")
        os.remove(destiCode + "/time.c")
        os.remove(destiCode + "/time.h")

        path = self.Particule.FolderProject + "/Library/ImagesBmpCache"
        NameTexture=[]
        for i in os.listdir(path):
            if ".meta" in i: continue
            name = os.path.basename(i)
            name = os.path.splitext(name)[0]
            #img = SpriteCoder.ConvertImg(path + "/" + i, name)[0]
            imgTemp = cv2.imread(path + "/" + i)
            cv2.imwrite(desti+"/ParticuleGame/assets-fx/"+name+".png", imgTemp)
            if self.Particule.CalculatriceCouleur:
                FileVar = self.Particule.All_UUID[name]
                if os.path.splitext(FileVar.path)[1].lower() == ".png":
                    shutil.copy(FileVar.path, desti + "/ParticuleGame/assets-cg/" + name + ".png")
                else:
                    imgTemp = cv2.imread(FileVar.path)
                    cv2.imwrite(desti + "/ParticuleGame/assets-cg/" + name + ".png", imgTemp)
            else:
                cv2.imwrite(desti + "/ParticuleGame/assets-cg/" + name + ".png", imgTemp)
            img = "extern bopti_image_t "+name+";"
            AllImages += img + "\n"
            NameTexture.append(name)

            Img = ImageTk.Image.open(path + "/" + i)
            width = Img.width
            height = Img.height
            TexturesID += "Texture* Texture_" + name + ";\n"
            CreateTexturesCode += "sceneManager->Texture_" + name + '= new Texture("Texture",' + str(width) + "," + str(
                height) + ",&" + name + ');\n'


        # print(AllImages)
        scenes = rf.GetList(self.Particule.FolderProject + "/ProjectSettings/BuildSettings.txt", "ScenesInBuild")

        for ind, i in enumerate(scenes):
            if i[1]:
                CodeOfScenes += "if (index == " + str(ind) + "){\n"
                code = ""
                CodeInit = ""
                components = ""
                self.Particule.SaveData.LoadScene(i[0])
                for i in self.Particule.Hierarchy.allGameObjectOnScene.items():
                    CodeInit += "GameObject* " + i[0] + ";\n"
                    code += i[0] + '= new GameObject(newScene, "' + i[1].name + '","' + i[0] + '");\n'
                    code += i[0] + "->activeSelf = " + str(i[1].activeSelf).lower() + ";\n"
                    code += i[0] + "->activeInHierarchy = " + str(i[1].activeInHierarchy).lower() + ";\n"
                    code += i[0] + "->isStatic = " + str(i[1].isStatic).lower() + ";\n"
                    code += i[0] + '->transform->position->Set(' + str(i[1].transform.position.x) + ',' + str(
                        i[1].transform.position.y) + ');\n'
                    code += i[0] + '->transform->localPosition->Set(' + str(i[1].transform.localPosition.x) + ',' + str(
                        i[1].transform.localPosition.y) + ');\n'

                    if i[1].transform.parent != None:
                        code += i[0] + "->transform->SetParent(" + i[1].transform.parent.gameObject.ID + "->transform);"
                    for compo in i[1].ListOfComponent:
                        data = compo.BuildValue()
                        code = data[0] + code
                        components += compo.AddScriptBeforInitCasio() + "\n"
                        components += data[1]
                        if type(compo).__name__ != "Transform":
                            components += i[0] + "->AddComponent((Component*)" + compo.ID + ");\n"
                        components += compo.AddScriptAfterInitCasio() + "\n"
                    code += "newScene->AddGameObject(" + i[0] + ");\n"
                code += components
                code = CodeInit + code
                CodeOfScenes += code
                CodeOfScenes += "\n}"

        Announcement, CasioCode, Cpp = self.GetCodeCasioFromVisualScratch()



        # with open(desti+"/Ressources.h","r", encoding = "ISO-8859-1") as fic:
        #    txt=fic.read()
        # txt = txt.replace("//AddImages",AllImages)
        # with open(desti+"/Ressources.h","w") as fic:
        #    fic.write(txt)

        with open(destiCode + "/ParticuleEngine.hpp", "r", encoding="ISO-8859-1") as fic:
            txt = fic.read()
        txt = txt.replace("//AddScenes", CodeOfScenes)
        txt = txt.replace("//Components", CasioCode)

        #txt = txt.replace("//CreateTextures", CreateTexturesCode)
        txt = txt.replace("//TexturesID", TexturesID)

        ####################################################
        temp=txt.split("//<\LibInclude>", 1)
        txtInclude, txt = temp[0],temp[1]
        txtInclude = txtInclude.replace("//<LibInclude>","")
        txtInclude = txtInclude.split("{",1)[0]+txtInclude.split("}",1)[1]
        txtInclude = """#include <gint/keyboard.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "string.h"
#include <gint/mpu/rtc.h>\n""" + txtInclude
        txtInclude = txtInclude.replace("#include <iostream>", "")
        txtInclude = txtInclude.replace('#include "usefull.h"', "")

        txt = txtInclude + txt
        ####################################################
        txt = self.ProjectSettingsReplace(txt)

        with open(destiCode + "/ParticuleEngine.hpp", "w") as fic:
            fic.write(txt)

        with open(destiCode + "/ParticuleEngine.cpp", "r", encoding="ISO-8859-1") as fic:
            txt = fic.read()

        txt += Cpp

        ####################################################
        temp = txt.split("//<\LibInclude>", 1)
        txtInclude, txt = temp[0], temp[1]
        txtInclude = txtInclude.replace("//<LibInclude>","")
        txtInclude = txtInclude.split("}")[1]
        txtInclude = """#include <gint/keyboard.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "string.h"
#include <gint/mpu/rtc.h>\n"""+txtInclude
        txtInclude = txtInclude.replace("#include <iostream>","")
        txtInclude = txtInclude.replace('#include "usefull.h"', "")

        txt = txtInclude+txt
        ####################################################

        with open(destiCode + "/ParticuleEngine.cpp", "w") as fic:
            fic.write(txt)

        with open(destiCode + "/Announcement.h", "r", encoding="ISO-8859-1") as fic:
            txt = fic.read()
        txt += Announcement
        with open(destiCode + "/Announcement.h", "w") as fic:
            fic.write(txt)

        with open(destiCode + "/main.cpp", "r", encoding="ISO-8859-1") as fic:
            txt = fic.read()
        txt = txt.replace("//AddImages", AllImages)
        txt = txt.replace("//CreateTextures", CreateTexturesCode)
        with open(destiCode + "/main.cpp", "w") as fic:
            fic.write(txt)


        with open(desti + "/ParticuleGame/assets-fx/fxconv-metadata.txt", "a", encoding="ISO-8859-1") as fic:
            for i in NameTexture:
                fic.write(i + """.png:
type: bopti-image
name: """ + i+"\n")

        with open(desti + "/ParticuleGame/assets-cg/fxconv-metadata.txt", "a", encoding="ISO-8859-1") as fic:
            for i in NameTexture:
                fic.write(i + """.png:
type: bopti-image
name: """ + i + "\n")

        with open(desti + "/ParticuleGame/CMakeLists.txt", "r", encoding="ISO-8859-1") as fic:
            txt = fic.read()
        imageAddCMake_fx = "set(ASSETS_fx\n"
        for i in NameTexture:
            imageAddCMake_fx+="  assets-fx/"+i+".png\n"
        imageAddCMake_cg = "set(ASSETS_cg\n"
        for i in NameTexture:
            imageAddCMake_cg += "  assets-cg/" + i + ".png\n"
        txt = txt.replace("set(ASSETS_fx",imageAddCMake_fx)
        txt = txt.replace("set(ASSETS_cg", imageAddCMake_cg)
        with open(desti + "/ParticuleGame/CMakeLists.txt", "w") as fic:
            fic.write(txt)

        imgTemp = cv2.imread(self.Particule.FolderProject + "/ProjectSettings/MainIcon.bmp")
        cv2.imwrite(desti + "/ParticuleGame/assets-fx/icon.png", imgTemp)

        shutil.copy(self.Particule.FolderProject + "/ProjectSettings/icon-sel.png", desti + "/ParticuleGame/assets-cg/icon-sel.png")
        shutil.copy(self.Particule.FolderProject + "/ProjectSettings/icon-uns.png", desti + "/ParticuleGame/assets-cg/icon-uns.png")

        desti = self.Particule.FolderProject + "/Temp/Compile"

        # subprocess.Popen(r'explorer /select,"' + desti+"/ParticuleEngine.h" + '"')
        if platform.system() == "Windows":
            FILEBROWSER_PATH = os.path.join(os.getenv('WINDIR'), 'explorer.exe')
            subprocess.run([FILEBROWSER_PATH, os.path.abspath(desti)])
        else:
            try:
                os.system(r'xdg-open ' + os.path.abspath(desti))
            except:
                pass


    def ProjectSettingsReplace(self,txt):
        # ////////////////////////////- Project Settings -////////////////////////////
        tempGravity = eval(rf.found(self.pathProjectSettings, "Physics2D&Gravity"))
        txt = txt.replace("/*GravityValue*/", str(float(tempGravity[0])) + "f," + str(float(tempGravity[1]))+"f")
        temp = eval(rf.found(self.pathProjectSettings, "Player&ScreenSize"))
        txt = txt.replace("/*ScreenSizeValue*/", str(int(temp[0])) + "," + str(int(temp[1])))
        return txt
