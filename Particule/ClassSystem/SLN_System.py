from Particule import *
import shutil
class SLN_System:
    def __init__(self,Particule):
        self.Particule = Particule
        #self.InitSLN()
        self.UpdateSLN()

    def InitSLN(self):#A Terminer
        src = "lib/SLN/Particule"
        dst = self.Particule.FolderProject + "/SLN/VisualStudio"
        if os.path.exists(dst):
            shutil.rmtree(dst)
        shutil.copytree(src, dst)
        SDK="lib/Moteur/SDK Graph 75 85 95/"
        LstElem=[]
        for i in os.listdir(SDK):
            if os.path.splitext(i)[1] in [".h",".cpp",".c"]:
                shutil.copyfile(SDK+i, dst+"/Particule/"+i)
                LstElem.append(i)
        Txt_vcxproj=""
        Txt_filters=""
        for i in LstElem:
            Txt_filters+='''<ClInclude Include="'''+i+'''.h">
      <Filter>Fichiers sources\Moteur</Filter>
    </ClInclude>\n'''
            Txt_vcxproj+='<ClInclude Include="'+i+'" />\n'


        with open(dst+"/Particule/Particule.vcxproj","r") as fic:
            File_vcxproj = fic.read()
        with open(dst+"/Particule/Particule.vcxproj.filters","r") as fic:
            File_filters = fic.read()

        File_vcxproj = File_vcxproj.replace("//INCLUDEFILE",Txt_vcxproj)
        File_filters = File_filters.replace("//INCLUDEFILE",Txt_filters)

        with open(dst+"/Particule/Particule.vcxproj","w") as fic:
            fic.write(File_vcxproj)
        with open(dst+"/Particule/Particule.vcxproj.filters","w") as fic:
            fic.write(File_filters)


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
            if ".hpp" == (os.path.splitext(i)[1]).lower() and os.path.isfile(rep + "/" + i):
                if not self.Particule.FolderProject+"/Temp" in os.path.abspath(i):
                    lst.append(rep + "/" + i)
            if not os.path.isfile(rep+"/"+i):
                self.FoundFile(lst,rep+"/"+i)
        return lst