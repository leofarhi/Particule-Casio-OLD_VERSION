from Particule import *
import json
from ClassParticule.GameObject import GameObject
import os,sys
from inspect import isclass
from pkgutil import iter_modules
import pkgutil
from pathlib import Path
from importlib import import_module
from ClassParticule.Tag import Tag
from ClassParticule.Layer import Layer
class SaveData:
    def __init__(self,Particule):
        self.Particule=Particule
        self.PathScene=None

    def GetAll_UUID_Scene(self,path):
        with open(path,"r") as fic:
            dataTxt = fic.read()
        data = json.loads(dataTxt)
        dataGameObject = data["GameObjects"]
        UUID_temp=[]
        for index, i in dataGameObject.items():
            #self.Particule.CreateUUID(i,index)
            UUID_temp.append(index)
        dataComponent = data["Components"]
        for index, component in dataComponent.items():
            #self.Particule.CreateUUID(component,index)
            UUID_temp.append(index)
        return UUID_temp
    def GetDataScene(self,scene):
        H = self.Particule.Hierarchy
        try:
            dico = H.GetDictOfChild(scene, {})
        except:return {}
        gameObjects = []
        for index, i in dico.items():
            if i[0] != "":
                gameObjects.append(H.allGameObjectOnScene[index])
        data = {"NameScene": H.t.set(scene, "chemin")}
        dataGameObject = {}
        for gameObject in gameObjects:
            TempDico = gameObject.SaveDataDict()

            dataGameObject.update({gameObject.ID: TempDico})
        data.update({"GameObjects": dataGameObject})
        dataComponent = {}
        for gameObject in gameObjects:
            for component in gameObject.ListOfComponent:
                dataComponent.update({component.ID: component.SaveDataDict()})
        data.update({"Components": dataComponent})
        return data
    def SaveScene(self):
        if self.SaveScene in self.Particule.Process:
            return
        if self.LoadScene in self.Particule.Process:
            return
        self.Particule.Process.append(self.SaveScene)
        H = self.Particule.Hierarchy
        for scene in H.t.get_children(""):
            data = self.GetDataScene(scene)
            dataSaved = json.dumps(data, indent=4)
            path = data["NameScene"]
            path = path.replace(self.Particule.FolderProject, "")
            with open(self.Particule.FolderProject+"/"+path,"w") as fic:
                fic.write(dataSaved)
        self.Particule.Process.remove(self.SaveScene)
    def UnloadScenes(self):
        H = self.Particule.Hierarchy
        for i in H.t.get_children(""):
            H.DestroyGameObject(i)
        for index, i in H.allGameObjectOnScene.items():
            i.Destroy()
        for i in H.t.get_children(""):
            H.t.delete(i)

    def LoadScene(self,path="Assets/Scenes/Sample Scene.particule"):
        if self.SaveScene in self.Particule.Process:
            return
        if self.LoadScene in self.Particule.Process:
            return
        self.Particule.Process.append(self.LoadScene)
        self.UnloadScenes()
        self.Particule.Scene.ClearAll()
        path = path.replace("\\","/").replace(self.Particule.FolderProject.replace("\\","/"),"")
        with open(self.Particule.FolderProject+"/"+path,"r") as fic:
            dataTxt = fic.read()
        data = json.loads(dataTxt)
        self.PathScene = path
        self.Particule.Scene.scenes = [path]#[data["NameScene"]]
        self.Particule.Scene.UUID_Objects = [{}]
        dataGameObject = data["GameObjects"]
        gameObjects = []
        dicoGameObject= {}
        #print(dataGameObject)
        for index,i in dataGameObject.items():
            temp = GameObject(self.Particule,UUID=index)
            gameObjects.append(temp)
            dicoGameObject.update({temp.ID:temp})
            dataTxt = dataTxt.replace(str(index),"#$##"+str(temp.ID))
        dataTxt = dataTxt.replace("#$##","")
        data = json.loads(dataTxt)
        dataComponent = data["Components"]
        dicoComponent = {}
        components = []
        for index,component in dataComponent.items():
            try:
                classCompo = getattr(sys.modules['Particule'], component["name"])
            except:
                classCompo = getattr(sys.modules['Particule'], "MissingScript")
            if not component["gameObject"] in dicoGameObject:
                continue
            temp = classCompo(dicoGameObject[component["gameObject"]],UUID=index)
            components.append(temp)
            dicoComponent.update({temp.ID: temp})
            dataTxt = dataTxt.replace(str(index), "#$##" + str(temp.ID))
        dataTxt = dataTxt.replace("#$##", "")
        data = json.loads(dataTxt)
        dataGameObject = data["GameObjects"]
        dataComponent = data["Components"]
        #print(dataGameObject)
        for gameObject in gameObjects:
            i = dataGameObject[str(gameObject.ID)]
            gameObject.name = i["name"]
            gameObject.activeInHierarchy = i["activeInHierarchy"]
            gameObject.activeSelf = i["activeSelf"]
            gameObject.isStatic = i["isStatic"]
            gameObject.layer = Layer(i["layer"])
            gameObject.scene = path#i["scene"]
            gameObject.sceneCullingMask = i["sceneCullingMask"]
            gameObject.tag = Tag(i["tag"])
            gameObject.Order = i["Order"]
            tempTransf = gameObject.transform
            gameObject.transform = dicoComponent[i["transform"]]
            tempTransf.Destroy()

            gameObject.OpenIsHierarchy = i["OpenIsHierarchy"]

            tempListOfComponentDico = []
            for o in i["ListOfComponent"]:
                if o in dicoComponent:
                    tempListOfComponentDico.append(dicoComponent[o])
            gameObject.ListOfComponent = tempListOfComponentDico

        for component in components:
            try:
                """
                print(data)
                print(component)
                print(dataComponent[str(component.ID)])
                print(dicoGameObject)
                print(dicoComponent)"""
                component.LoadDataDict(data,component,dataComponent[str(component.ID)],dicoGameObject,dicoComponent)
            except:
                pass
        dicoHier={}
        for gameObject in gameObjects:
            if gameObject.transform.parent == None:
                dicoHier = self.GetDictOfChild(gameObject,dicoHier)
        H = self.Particule.Hierarchy
        self.UnloadScenes()
        H.allGameObjectOnScene = {}
        H.ItemSelected = None
        H.t.insert("", "end",
                   path,#data["NameScene"],
                   text=(path.split("/")[-1]).split(".")[0], values=(path, "dir"))
        for index,parent in dicoHier.items():
            H.CreateObject(root=parent, name=None, gameObject=dicoGameObject[index])
        for gameObject in gameObjects:
            try:
                H.t.item(gameObject.ID, open=gameObject.OpenIsHierarchy)
            except:pass
        self.Particule.Scene.RefreshOrder()
        self.Particule.Process.remove(self.LoadScene)
    def GetDictOfChild(self,parent,dico):
        if parent.transform.parent == None:
            parentID = parent.scene
        else:
            parentID=parent.transform.parent.gameObject.ID
        dico.update({parent.ID:parentID})
        for e in parent.transform.childs:
            dico = self.GetDictOfChild(e.gameObject,dico)
        return dico