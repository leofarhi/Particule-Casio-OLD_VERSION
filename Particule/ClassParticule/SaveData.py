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
            self.Particule.CreateUUID(index)
            UUID_temp.append(index)
        dataComponent = data["Components"]
        for index, component in dataComponent.items():
            self.Particule.CreateUUID(index)
            UUID_temp.append(index)
        return UUID_temp
    def SaveScene(self):
        H = self.Particule.Hierarchy
        for scene in H.t.get_children(""):
            dico = H.GetDictOfChild(scene,{})
            gameObjects =[]
            for index, i in dico.items():
                if i[0]!="":
                    gameObjects.append(H.allGameObjectOnScene[index])
            data = {"NameScene":H.t.set(scene,"chemin")}
            dataGameObject = {}
            for gameObject in gameObjects:

                TempDico = {"name":gameObject.name,
                            "activeInHierarchy":gameObject.activeInHierarchy,
                            "activeSelf":gameObject.activeSelf,
                            "isStatic":gameObject.isStatic,
                            "layer":gameObject.layer.value,
                            "scene":gameObject.scene,
                            "sceneCullingMask":gameObject.sceneCullingMask,
                            "tag":gameObject.tag.value,
                            "transform":gameObject.transform.ID,
                            "ListOfComponent":[i.ID for i in gameObject.ListOfComponent]
                            }
                dataGameObject.update({gameObject.ID : TempDico})
            data.update({"GameObjects":dataGameObject})
            dataComponent={}
            for gameObject in gameObjects:
                for component in gameObject.ListOfComponent:
                    dataComponent.update({component.ID:component.SaveDataDict()})
            data.update({"Components":dataComponent})
            dataSaved = json.dumps(data, indent=4)
            path = data["NameScene"]
            path = path.replace(self.Particule.FolderProject, "")
            with open(self.Particule.FolderProject+"/"+path,"w") as fic:
                fic.write(dataSaved)
    def LoadScene(self,path="Assets/Scenes/Sample Scene.particule"):
        path = path.replace("\\","/").replace(self.Particule.FolderProject.replace("\\","/"),"")
        with open(self.Particule.FolderProject+"/"+path,"r") as fic:
            dataTxt = fic.read()
        data = json.loads(dataTxt)
        self.PathScene = path
        self.Particule.Scene.scenes = [data["NameScene"]]
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
            gameObject.scene = i["scene"]
            gameObject.sceneCullingMask = i["sceneCullingMask"]
            gameObject.tag = Tag(i["tag"])
            gameObject.transform = dicoComponent[i["transform"]]
            gameObject.ListOfComponent = [dicoComponent[o] for o in i["ListOfComponent"]]

        for component in components:
            try:
                component.LoadDataDict(data,component,dataComponent[str(component.ID)],dicoGameObject,dicoComponent)
            except:
                pass
        dicoHier={}
        for gameObject in gameObjects:
            if gameObject.transform.parent == None:
                dicoHier = self.GetDictOfChild(gameObject,dicoHier)
        H = self.Particule.Hierarchy
        for i in H.t.get_children(""):
            H.DestroyGameObject(i)
        for index,i in H.allGameObjectOnScene.items():
            i.Destroy()
        for i in H.t.get_children(""):
            H.t.delete(i)
        H.allGameObjectOnScene = {}
        H.ItemSelected = None
        H.t.insert("", "end", data["NameScene"], text=(data["NameScene"].split("/")[-1]).split(".")[0], values=(data["NameScene"], "dir"))
        for index,parent in dicoHier.items():
            H.CreateObject(root=parent, name=None, gameObject=dicoGameObject[index])
    def GetDictOfChild(self,parent,dico):
        if parent.transform.parent == None:
            parentID = parent.scene
        else:
            parentID=parent.transform.parent.gameObject.ID
        dico.update({parent.ID:parentID})
        for e in parent.transform.childs:
            dico = self.GetDictOfChild(e.gameObject,dico)
        return dico