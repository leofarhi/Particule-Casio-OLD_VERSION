from Particule import *
class SLN_System:
    def __init__(self,Particule):
        self.Particule = Particule
        self.UpdateSLN()

    def UpdateSLN(self):
        data = {"PathParticule": self.Particule.FolderProject + "/SLN/Solution.sls", "Version": self.Particule.version,
                "Files": self.FoundFile([])}
        dataSaved = json.dumps(data, indent=4)

        with open(self.Particule.FolderProject + "/SLN/Solution.sls", "w") as fic:
            fic.write(dataSaved)


    def FoundFile(self,lst,rep=None):
        if rep == None:
            rep = self.Particule.FolderProject+"/Assets"
        lstDir = os.listdir(rep)
        for i in lstDir:
            if ".SBAsset" == os.path.splitext(i)[1] and os.path.isfile(rep + "/" + i):
                lst.append(rep + "/" + i)
            if not os.path.isfile(rep+"/"+i):
                self.FoundFile(lst,rep+"/"+i)
        return lst