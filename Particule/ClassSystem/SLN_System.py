from Particule import *
class SLN_System:
    def __init__(self,Particule):
        self.Particule = Particule
        data = {"PathParticule":self.Particule.FolderProject+"/SLN/Solution.sls","Version":self.Particule.version,"Files":self.FoundFile(self.Particule.FolderProject,[])}
        dataSaved = json.dumps(data, indent=4)

        with open(self.Particule.FolderProject+"/SLN/Solution.sls", "w") as fic:
            fic.write(dataSaved)

    def FoundFile(self,rep,lst):
        lstDir = os.listdir(rep)
        for i in lstDir:
            if ".SBAsset" == os.path.splitext(i)[1] and os.path.isfile(rep+"/"+i):
                lst.append(rep+"/"+i)
            if not os.path.isfile(rep+"/"+i):
                self.FoundFile(rep+"/"+i,lst)
        return lst

