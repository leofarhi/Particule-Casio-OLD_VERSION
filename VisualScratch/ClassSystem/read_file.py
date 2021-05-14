
import sys
import os
setup=[]
rep=os.getcwd()
def cherchefichier(fichier, rep_dico):
    # recherche du contenu du répertoire rep (fichiers et sous-répertoires)
    entrees = os.listdir(rep_dico)
             
    # traitement des fichiers du répertoire
    for entree in entrees:
        if (not os.path.isdir(os.path.join(rep_dico, entree))) and (entree==fichier):
            return True
             
    # traitement récursif des sous-répertoires de rep
    for entree in entrees:
        rep2 = os.path.join(rep_dico, entree)
        if os.path.isdir(rep2):
            chemin = cherchefichier(fichier, rep2)
            if chemin!="":
                return chemin
    return False

def setup_file(namePath):
    setup=[]
    try:
        with open(namePath,'r') as fic:
            setup=fic.readlines()
        for i in range(len(setup)):
            setup[i]=setup[i].rstrip()
            setup[i]=setup[i].split("::")
    except:
        """
        with open(namePath,'w') as fic:
            fic.write("Version:0.0")
            setup=[]
        """
        setup=[]
    return setup
def found(file, var,ligne=False):
    setup=setup_file(file)
    o=False
    a=0
    for i in setup:
        if i[0].lower()==str(var).lower():
            o=i[1]
            break
        a=a+1
    if ligne==True:
        return o,a
    else:
        return o
def save(namePath,var,value):
    global setup
    file=namePath
    setup=setup_file(file)
    value=str(value)
    var=str(var)
    a,b=found(file,var,True)
    if a!=False:
        (setup[b])[1]=str(value)
    else:
        setup.append([var,value])
    with open(namePath,'w') as fic:
        for i in setup:
            fic.write(i[0]+"::"+i[1]+"\n")
def DelList(namePath,var,index):
    global _i
    try:
        _i=found(namePath,var)
        eval(compile("_i="+_i, '<string>', 'exec'),globals(),globals())
        del _i[index]
        save(namePath,var,str(_i))
    except:
        return False
def AppendList(namePath,var,value):
    global _i
    try:
        _i=found(namePath,var)
        eval(compile("_i="+_i, '<string>', 'exec'),globals(),globals())
        _i.append(value)
        save(namePath,var,str(_i))
    except:
        return False
def GetList(namePath,var):
    global _i
    try:
        _i=found(namePath,var)
        if _i==False:return False
        eval(compile("_i="+_i, '<string>', 'exec'),globals(),globals())
        return _i
    except:
        return False
def remove(namePath,var):
    global setup
    file=namePath
    setup=setup_file(file)
    var=str(var)
    a,b=found(file,var,True)
    if a!=False:
        with open(namePath,'w') as fic:
            for i in setup:
                if i[0]!= var:fic.write(i[0]+"::"+i[1]+"\n")
