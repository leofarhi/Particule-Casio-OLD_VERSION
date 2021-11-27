from tkinter import *
import tkinter
from tkinter.messagebox import *
import tkinter.simpledialog
from tkinter.filedialog import *
from tkinter import ttk
import tkinter as tk
from Particule import *
from ClassSystem.PFrame import PFrame
from ClassParticule.Hierarchy import Hierarchy
from ClassSystem.Notebook import Notebook
from ClassParticule.FolderWindow import FolderWindow
from ClassSystem.MenuItem import MenuItem
from ClassParticule.AssetStore import *
from ClassParticule.Inspector import Inspector
from ClassParticule.Scene import Scene
from ClassParticule.Console import Console
from ClassParticule.Animator import Animator
from ClassParticule.ProjectSettingsWindow import ProjectSettingsWindow
from ClassParticule.SaveData import SaveData
from ClassParticule.BuildSettings import BuildSettings
from ClassParticule.WinInspectorType.WindowImage import WindowImage
from SystemExt import File_Folder as Fl

def LoadSizeWindow(name,width,height):
    data = rf.found("lib/ScreenOrganization.txt",name)
    if data!=False:
        width, height = eval(data)
    return width,height

def SaveSizeWindow(name,frame):
    width,height = frame.winfo_width(),frame.winfo_height()
    rf.save("lib/ScreenOrganization.txt",name,str((width,height,)))
class ScreenOrganization:
    def __init__(self,_Particule):
        self.Particule=_Particule
        temp = ProjectSettingsWindow(self.Particule.Mafenetre,OnlyLoad=True)

        if not "BuildSettings.txt" in os.listdir(self.Particule.FolderProject + "/ProjectSettings"):
            rf.save(self.Particule.FolderProject + "/ProjectSettings/BuildSettings.txt","ScenesInBuild",[])

        self.CreateDefaultScene()

        self.Particule.SaveData = SaveData(self.Particule)

        self.CreateWindows()
        self.SetWindows()
        self.SetMenuItem()
        self.Bind_Setup()
        self.Particule.SaveData.LoadScene()
    def SaveScreenOrganization(self):
        SaveSizeWindow("GridCenter",self.GridCenter)
        SaveSizeWindow("GridCenterLeft",self.GridCenterLeft)
        SaveSizeWindow("GridCenterBottom", self.GridCenterBottom)
    def CreateDefaultScene(self):
        if not os.path.exists(self.Particule.FolderProject+"Assets/Scenes"):
            M.create_rep(self.Particule.FolderProject + "/Assets/Scenes")
        if not "Sample Scene.particule" in os.listdir(self.Particule.FolderProject + "/Assets/Scenes"):
            with open(self.Particule.FolderProject + "/Assets/Scenes/Sample Scene.particule","w") as fic:
                data = '''{
                    "NameScene": "Assets/Scenes/Sample Scene.particule",
                    "GameObjects": {},
                    "Components": {}
                }'''
                fic.write(data)
    def CreateWindows(self):
        fn = self.Particule.Mafenetre
        pw = PanedWindow(fn,orient='horizontal')
        pw.Particule = self.Particule
        self.GridRight = Notebook(pw)
        self.GridRight.pack(fill=BOTH, expand=True)
        self.GridLeft = PFrame(pw)
        self.GridLeft.pack(fill=BOTH, expand=True)



        pw.add(self.GridLeft)
        pw.add(self.GridRight)
        pw.pack(fill=BOTH, expand=True, anchor=N)
        pw.configure(sashrelief=RAISED)


        pwCenter = PanedWindow(self.GridLeft,orient='vertical')
        pwCenter.Particule = self.Particule
        self.GridCenterTop = PFrame(pwCenter)
        self.GridCenterTop.pack(fill=BOTH, expand=True)
        _,height = LoadSizeWindow("GridCenterBottom", 0, 500)
        self.GridCenterBottom = Notebook(pwCenter,height=height)
        self.GridCenterBottom.pack(fill=BOTH, expand=True)
        pwCenter.add(self.GridCenterTop)
        pwCenter.add(self.GridCenterBottom)

        pwCenter.pack(fill=BOTH, expand=True)
        pwCenter.configure(sashrelief=RAISED)

        pwTop = PanedWindow(self.GridCenterTop, orient='horizontal')
        pwTop.Particule = self.Particule
        width,height = LoadSizeWindow("GridCenter",885,500)
        self.GridCenter = Notebook(pwTop,width=width,height=height)
        self.GridCenter.pack(fill=BOTH, expand=True)
        width, height = LoadSizeWindow("GridCenterLeft", 230, 500)
        self.GridCenterLeft = Notebook(pwTop,width=width,height=height)
        self.GridCenterLeft.pack(fill=BOTH, expand=True)

        pwTop.add(self.GridCenterLeft)
        pwTop.add(self.GridCenter)

        pwTop.pack(fill=BOTH, expand=True)
        pwTop.configure(sashrelief=RAISED)

    def SetWindows(self):
        #self.CanevasAsset = AssetStore(self.GridCenter, self.Particule)
        self.Particule.Scene = Scene(self.GridCenter)
        self.Particule.Scene.pack(fill=BOTH, expand=True)

        #self.Particule.Animator = Animator(self.GridCenter)
        #self.Particule.Animator.pack(fill=BOTH, expand=True)

        self.GridCenter.add(self.Particule.Scene, text='Scene')
        #self.GridCenter.add(self.Particule.Animator, text='Animator')
        #self.GridCenter.add(self.CanevasAsset.FrameAssetStore, text='Asset Store')
        #self.GridCenter.add(self.CanevasAsset.FrameAssetImport, text='My Asset')

        self.Particule.Hierarchy = Hierarchy(self.GridCenterLeft)
        self.Particule.Hierarchy.pack(side="left",fill=BOTH, expand=True)
        self.GridCenterLeft.add(self.Particule.Hierarchy,text="Hierarchy")

        self.Particule.FolderWindow = FolderWindow(self.GridCenterBottom)
        self.Particule.FolderWindow.pack(fill=BOTH, expand=True)
        self.GridCenterBottom.add(self.Particule.FolderWindow, text="Folder")

        self.Particule.Console = Console(self.GridCenterBottom)
        self.Particule.Console.pack(fill=BOTH, expand=True)
        self.GridCenterBottom.add(self.Particule.Console, text="Console")

        self.Particule.Inspector = Inspector(self.GridRight)
        self.Particule.Inspector.pack(fill=BOTH, expand=True)
        self.GridRight.add(self.Particule.Inspector,text="Inspector")

        self.Particule.WindowImage = WindowImage(self.Particule.Inspector)
        self.ChangeInspector()
    def Bind_Setup(self):
        root = self.Particule.Mafenetre
        root.bind("<FocusIn>", self.Particule.UpdateOnFocus)
    def ChangeInspector(self,Name="Inspector"):
        self.Particule.Inspector.GameObjectWindow.forget()
        self.Particule.WindowImage.forget()
        if Name=="Inspector":
            self.Particule.Inspector.GameObjectWindow.pack(fill=BOTH, expand=True)
        elif Name=="Image":
            self.Particule.WindowImage.pack(fill=BOTH, expand=True)
            self.Particule.WindowImage.Update()

    def CreateScene(self):
        rep = Fl.save_file(self.Particule.FolderProject + "/Assets/Scenes/")
        with open(rep+".particule", "w") as fic:
            data = '''{
                "NameScene": "'''+rep+ '''.particule",
                "GameObjects": {},
                "Components": {}
            }'''
            fic.write(data)
        self.Particule.FolderWindow.CreateMetaFile()

    def CreateCamera(self):
        gameobject = self.Particule.Hierarchy.CreateObject()
        gameobject.AddComponentByName("Camera")
        return gameobject

    def OpenSceneFile(self):
        rep=Fl.open_file(rep =self.Particule.FolderProject)#,filetypes=(("Scene files", "*.particule")))
        self.Particule.SaveData.LoadScene(rep)
    def SetColor(self,TypeColor):
        pathFile = self.Particule.FolderProject + "/ProjectSettings/ProjectSettings.txt"
        if TypeColor=="Monochrome":
            self.Particule.CalculatriceCouleur = False
        elif TypeColor=="RGB":
            self.Particule.CalculatriceCouleur = True
        rf.save(pathFile, "Player&CalculatriceCouleur", self.Particule.CalculatriceCouleur)
        self.Particule.UpdateOnFocus()
    def SetCalculatrice(self,TypeCalculatrice):
        pathFile = self.Particule.FolderProject + "/ProjectSettings/ProjectSettings.txt"
        if TypeCalculatrice=="Graph 35+USB/75/85/95 (SD)":
            self.Particule.CalculatriceCouleur = False
            rf.save(pathFile, "Player&ScreenSize", (127,63))
        elif TypeCalculatrice=="Graph 90+E":
            self.Particule.CalculatriceCouleur = True
            rf.save(pathFile, "Player&ScreenSize", (396,224))
        rf.save(pathFile, "Player&CalculatriceCouleur", self.Particule.CalculatriceCouleur)
        self.Particule.UpdateOnFocus()
    def SetMenuItem(self):
        self.Particule.MenuItem = MenuItem(self.Particule.Mafenetre)
        self.MenuItem = self.Particule.MenuItem
        self.MenuItem.AddItem("Fichier/Creer une Scene" ,self.CreateScene)
        self.MenuItem.AddItem("Fichier/Ouvrir une Scene",self.OpenSceneFile)  # ,self.OpenScene)
        self.MenuItem.Add_separator("Fichier")
        self.MenuItem.AddItem("Fichier/Enregistrer",self.Particule.SaveData.SaveScene)  # ,SaveAll)
        #self.MenuItem.AddItem("Fichier/Enregistrer sous...")  # ,SaveAll)
        #self.MenuItem.Add_separator("Fichier")
        #self.MenuItem.AddItem("Fichier/Nouveau Projet...")  # ,self.LoadSystem.MenuOpenFolder)
        #self.MenuItem.AddItem("Fichier/Ouvrir un Projet...")  # ,self.LoadSystem.MenuOpenFolder)
        self.MenuItem.Add_separator("Fichier")
        self.MenuItem.AddItem("Fichier/Build Settings",partial(BuildSettings,self.Particule.Mafenetre))  # ,WinChoiceTypeCompile)
        # self.MenuItem.AddItem("Fichier/Build And Run")
        self.MenuItem.Add_separator("Fichier")
        self.MenuItem.AddItem("Fichier/Quitter",self.Particule.on_closing)  # ,self.Mafenetre.quit)



        #self.MenuItem.AddItem("Edit/Undo")
        #self.MenuItem.AddItem("Edit/Redo")
        #self.MenuItem.Add_separator("Edit")
        #self.MenuItem.AddItem("Edit/Tout Selectionner")
        #self.MenuItem.AddItem("Edit/Tout Deselectionner")
        #self.MenuItem.AddItem("Edit/Selectionner les enfants")
        #self.MenuItem.AddItem("Edit/Selectionner la Prefab Root")
        #self.MenuItem.AddItem("Edit/Inverser la selection")
        #self.MenuItem.Add_separator("Edit")
        self.MenuItem.AddItem("Edit/Couper")
        self.MenuItem.AddItem("Edit/Copier")
        self.MenuItem.AddItem("Edit/Coller")
        self.MenuItem.Add_separator("Edit")
        self.MenuItem.AddItem("Edit/Dupliquer")
        self.MenuItem.AddItem("Edit/Renommer")
        self.MenuItem.AddItem("Edit/Supprimer")
        self.MenuItem.Add_separator("Edit")
        #self.MenuItem.AddItem("Edit/Frame Selected")
        #self.MenuItem.AddItem("Edit/Lock View to Selected")
        self.MenuItem.AddItem("Edit/Find")
        #self.MenuItem.Add_separator("Edit")
        #self.MenuItem.AddItem("Edit/Play")
        #self.MenuItem.AddItem("Edit/Pause")
        #self.MenuItem.AddItem("Edit/Step")
        #self.MenuItem.Add_separator("Edit")
        #self.MenuItem.AddItem("Edit/Sign in...")
        #self.MenuItem.AddItem("Edit/Sign out")
        self.MenuItem.Add_separator("Edit")
        self.MenuItem.AddItem("Edit/Selection")
        self.MenuItem.Add_separator("Edit")
        self.MenuItem.AddItem("Edit/Parametre du Projet...", partial(ProjectSettingsWindow,self.Particule.Mafenetre))
        self.MenuItem.AddItem("Edit/Preferences...")
        self.MenuItem.AddItem("Edit/Shortcuts...")
        #self.MenuItem.AddItem("Edit/Clear All PlayerPrefs")

        self.MenuItem.AddItem("Asset/Create")
        self.MenuItem.AddItem("Asset/Show in Explorer",self.ShowInExplorer)
        self.MenuItem.AddItem("Asset/Open")
        self.MenuItem.AddItem("Asset/Delete")
        self.MenuItem.AddItem("Asset/Rename")
        self.MenuItem.AddItem("Asset/Copy Path")
        self.MenuItem.Add_separator("Asset")
        self.MenuItem.AddItem("Asset/Open Scene Additive")
        self.MenuItem.Add_separator("Asset")
        self.MenuItem.AddItem("Asset/View in Package Manager")
        self.MenuItem.Add_separator("Asset")
        self.MenuItem.AddItem("Asset/Import New Asset...")
        self.MenuItem.AddItem("Asset/Import Package")
        self.MenuItem.AddItem("Asset/Export Package")
        self.MenuItem.AddItem("Asset/Find References In Scene")
        self.MenuItem.AddItem("Asset/Select Dependencies")
        self.MenuItem.Add_separator("Asset")
        self.MenuItem.AddItem("Asset/Refresh",self.Particule.UpdateOnFocus)
        #self.MenuItem.AddItem("Asset/Reimport")
        #self.MenuItem.Add_separator("Asset")
        #self.MenuItem.AddItem("Asset/Reimport All")
        self.MenuItem.Add_separator("Asset")
        self.MenuItem.AddItem("Asset/Extract From Prefab")
        self.MenuItem.Add_separator("Asset")
        self.MenuItem.AddItem("Asset/Run API Updater")
        self.MenuItem.Add_separator("Asset")
        self.MenuItem.AddItem("Asset/Update UIElements Schema")
        self.MenuItem.Add_separator("Asset")
        self.MenuItem.AddItem("Asset/Open Scratch Project")
        self.MenuItem.AddItem("Asset/ParticuleEditorScripts")

        self.MenuItem.AddItem("GameObject/Creer un Empty",self.Particule.Hierarchy.CreateObject)  # ,partial(CreateEmpty,self))
        self.MenuItem.AddItem("GameObject/2D Object")
        self.MenuItem.AddItem("GameObject/Effects")
        # self.MenuItem.AddItem("GameObject/Light")
        self.MenuItem.AddItem("GameObject/UI")
        self.MenuItem.AddItem("GameObject/Camera",self.CreateCamera)
        self.MenuItem.Add_separator("GameObject")
        self.MenuItem.AddItem("GameObject/Center On Children")
        self.MenuItem.Add_separator("GameObject")
        self.MenuItem.AddItem("GameObject/Make Parent")
        self.MenuItem.AddItem("GameObject/Clear Parent")
        self.MenuItem.Add_separator("GameObject")
        self.MenuItem.AddItem("GameObject/Set as first sibling")
        self.MenuItem.AddItem("GameObject/Set as last sibling")
        self.MenuItem.AddItem("GameObject/Move To View")
        self.MenuItem.AddItem("GameObject/Align With View")
        self.MenuItem.AddItem("GameObject/Align View to Selected")
        self.MenuItem.AddItem("GameObject/Toggle Active State")

        self.MenuItem.AddItem("Component/Add")
        self.MenuItem.AddItem("Component/Mesh")
        self.MenuItem.AddItem("Component/Effects")
        self.MenuItem.AddItem("Component/Physics2D")
        self.MenuItem.AddItem("Component/Navigation")
        # self.MenuItem.AddItem("Component/Light")
        self.MenuItem.AddItem("Component/Rendering")
        self.MenuItem.AddItem("Component/Tilemap")
        self.MenuItem.AddItem("Component/Layout")
        self.MenuItem.AddItem("Component/Playables")
        self.MenuItem.AddItem("Component/AR")
        self.MenuItem.AddItem("Component/Miscellaneous")
        self.MenuItem.AddItem("Component/Scripts")
        self.MenuItem.AddItem("Component/Network")
        self.MenuItem.AddItem("Component/UI")
        self.MenuItem.AddItem("Component/ML Agents")
        self.MenuItem.AddItem("Component/Event")
        self.MenuItem.AddItem("Component/Image Effects")

        self.MenuItem.AddItem("Window/Next Window")
        self.MenuItem.AddItem("Window/Previous Window")
        self.MenuItem.Add_separator("Window")
        self.MenuItem.AddItem("Window/Layouts")
        self.MenuItem.Add_separator("Window")
        self.MenuItem.AddItem("Window/Asset Store")
        self.MenuItem.AddItem("Window/Package Manager")
        self.MenuItem.Add_separator("Window")
        self.MenuItem.AddItem("Window/Asset Management")
        self.MenuItem.Add_separator("Window")
        self.MenuItem.AddItem("Window/General")
        self.MenuItem.AddItem("Window/Renderring")
        self.MenuItem.AddItem("Window/Animation")
        self.MenuItem.AddItem("Window/Sequencing")
        self.MenuItem.AddItem("Window/Analysis")
        self.MenuItem.AddItem("Window/2D")
        self.MenuItem.AddItem("Window/AI")
        self.MenuItem.AddItem("Window/XR")
        self.MenuItem.AddItem("Window/UI")

        for i in self.Particule.ListeCalculatrices:
            self.MenuItem.AddItem("Calculatrice/"+i.replace("/"," "),partial(self.SetCalculatrice,i))
        self.MenuItem.AddItem("Couleur/Monochrome",partial(self.SetColor,"Monochrome"))
        self.MenuItem.AddItem("Couleur/RBG",partial(self.SetColor,"RGB"))

        self.MenuItem.AddItem("Aide/A propos")  # ,show_about)
        self.MenuItem.Add_separator("Aide")
        self.MenuItem.AddItem("Aide/Manuel de Particule")
        self.MenuItem.AddItem("Aide/Scripting Reference")
        self.MenuItem.Add_separator("Aide")
        self.MenuItem.AddItem("Aide/Particule Services")
        self.MenuItem.AddItem("Aide/Particule Forum")
        self.MenuItem.AddItem("Aide/Particule Answers")
        self.MenuItem.AddItem("Aide/Particule Feedback")
        self.MenuItem.Add_separator("Aide")
        self.MenuItem.AddItem("Aide/Check for Updates")
        self.MenuItem.AddItem("Aide/Download Beta...")
        self.MenuItem.Add_separator("Aide")
        self.MenuItem.AddItem("Aide/Manage License")
        self.MenuItem.Add_separator("Aide")
        self.MenuItem.AddItem("Aide/Release Notes")
        self.MenuItem.AddItem("Aide/Software Licenses")
        self.MenuItem.AddItem("Aide/Report a Bug...")
        self.MenuItem.Add_separator("Aide")
        self.MenuItem.AddItem("Aide/Reset Packages to defaults")
        self.MenuItem.Add_separator("Aide")
        self.MenuItem.AddItem("Aide/Troubleshoot Issue...")
        self.MenuItem.Add_separator("Aide")
        self.MenuItem.AddItem("Aide/Quick Search")

        self.MenuItem.Update()

    def ShowInExplorer(self):
        FILEBROWSER_PATH = os.path.join(os.getenv('WINDIR'), 'explorer.exe')
        subprocess.run([FILEBROWSER_PATH, os.path.abspath(self.Particule.FolderProject)])


