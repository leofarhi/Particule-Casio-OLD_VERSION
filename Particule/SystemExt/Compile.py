import sys, os
import subprocess
import shutil
import time
from SystemExt import Project as Pj
from SystemExt import TransformImage as Ti
#shutil
#shutil.rmtree(/Folder) supprime tout un dossier
#os.remove("file.txt") supprime un fichier
def CreateSprite(liste):
    w=0
    h=0
    for i in liste:
        if w<i[1]+i[2]:
            w=i[1]+i[2]
        if h<i[0]:
            h=i[0]
    Liste1=[]
    Liste2=[]
    for i in liste:
        Liste2.append(str(-i[0]))#(str(h-i[0]))
        if i[2]==0:
            Liste1.append(str(i[1]))
        else:
            Liste1.append(str(i[1])+"+"+str(i[2])+"T")
    o="{"
    for i in Liste1:
        o+=i+","
    o=o[:-1]+"}"
    Liste1=o
    o="{"
    for i in Liste2:
        o+=i+","
    o=o[:-1]+"}"
    Liste2=o
    o="Graph(X,Y)=(H+"+Liste1+",I+"+Liste2+")"
    return o
"""
def SaveAllSprite(liste,FileName,rep=os.getcwd()):
    Texte=""#"File 1\n"
    for ind,i in enumerate(liste):
        Texte+="If List 2[3] = "+str(ind)+"\nThen "
        Texte+=str(CreateSprite(i))
        Texte+="\nIfEnd\n"
    EncodingCasio(FileName,Texte,rep)
    
def SaveAllSprite(liste,FileName,rep=os.getcwd()):
    Texte=""#"File 1\n"
    for ind,i in enumerate(liste):
       Texte+="I = "+str(ind)+' => '+str(CreateSprite2(i))+' -> Mat A.P\n'
    EncodingCasio(FileName,Texte,rep)
"""
def SaveAllSprite(liste,FileName,rep=os.getcwd()):
    for ind,i in enumerate(liste):
        shutil.copy(i[0],rep+"/"+str(ind+1)+'.bmp')
        Ti.ImageCompile(rep+"/"+str(ind+1)+'.bmp')
    
def SaveAllType(liste,FileName,rep=os.getcwd()):
    Texte=""#"File 1\n"
    for ind,i in enumerate(liste):
        Texte+="List 2[2] = "+str(ind)+' => "'+str(i)+'" -> Str 2\n'
    EncodingCasio(FileName,Texte,rep)
    
def SaveAllName(liste,FileName,rep=os.getcwd()):
    Texte=""#"File 1\n"
    for ind,i in enumerate(liste):
        Texte+="List 2[4] = "+str(ind)+' => "'+str(i)+'" -> Str 1\n'
    EncodingCasio(FileName,Texte,rep)
def SaveAllComponent(liste,FileName,rep=os.getcwd()):
    Texte=""#"File 1\n"
    for ind,i in enumerate(liste):
        Texte+="(List 3[2] = "+str(ind)+' And List 1[14] = 0) Or (List 1[13] = '+str(ind)+' And List 1[14] = 1) => "'+str(i)+'" -> Str 3\n'
        Texte+="List 3[2] = "+str(ind)+' And List 1[14] = 0 => Prog "'+str(i)+'"\n'
    EncodingCasio(FileName,Texte,rep)
    
def SaveAllElements(liste,AllComponent,FileName,ImgBmp,rep=os.getcwd()):
    
    Texte=""#"File 2\n"
    for ind,i in enumerate(liste):
        temp=[len(i[0])]+i[0]
        temp2=[len(i[1])]
        tempadd=0
        for ind2,o in enumerate(i[1]):
            o=o[2]
            temp2.append(len(temp)+1+len(i[1])+2+tempadd)
            tempadd+=len(o)
        temp2.append(len(temp)+1+len(i[1])+2+tempadd)
        temp3=[]
        for o in i[1]:
            o=o[2]
            for ind2,k in enumerate(o):
                if ind2==1:
                    if k in AllComponent:
                        k=AllComponent.index(k)
                    else:
                        AllComponent.append(k)
                        k=len(AllComponent)-1
                elif type(k)==str:
                    k=0
                temp3.append(k)
        Texte+=str(temp+temp2+temp3).replace("[","{").replace("]","}")+" -> List "+str(ind+1+10)+"\n"
    #Texte+="File 1\n"
    Texte+=str(len(liste))+" -> List 1[3]\n"
    Texte+=str(len(ImgBmp))+" -> List 1[18]\n"
    temp=[]
    for o in Pj.TypeOrdre:
        for ind,i in enumerate(Pj.Elements):
            if i.Type==o:
                temp.append(ind)
    Texte+=str(temp).replace("[","{").replace("]","}")+" -> List 6\n"
    EncodingCasio(FileName,Texte,rep)
    return AllComponent,Texte
def EncodingAllElements(liste,FileName,rep=os.getcwd()):
    Texte=""
    for ind,i in enumerate(liste):
        Texte+="If List 1[2]="+str(ind)+"\nThen "
        Texte+=i
        Texte+="\nIfEnd\n"
    EncodingCasio(FileName,Texte,rep)
def EncodingCasio(FileName,texte,rep=os.getcwd()):
    Final='#Program name: '+FileName+'\n#Password: <no password>\n'
    Final+=texte+"\n"
    Final+="#End of part"
    with open(FileName+".bide","w") as fic:
        fic.write(Final)
    time.sleep(1)
    os.system('java -jar BIDE.jar --to-g1m '+FileName+'.g1m '+FileName+'.bide '+FileName+'.g1m')
    time.sleep(1)
    shutil.copy(os.getcwd()+"/"+FileName+'.g1m',rep+"/"+FileName+'.g1m')
    time.sleep(1)
    os.remove(os.getcwd()+"/"+FileName+'.bide')
    os.remove(os.getcwd()+"/"+FileName+'.g1m')
    
