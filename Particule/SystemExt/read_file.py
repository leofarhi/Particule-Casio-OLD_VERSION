
import sys
import os
import json

rep=os.getcwd()
def cherchefichier(fichier):
    if os.path.exists(fichier):
        return os.path.isfile(fichier)
             
    return False

def setup_file(file):
    if not cherchefichier(file):return {}
    try:
        with open(file,"r", encoding="ISO-8859-1") as fic:
            data = fic.read()
    except:
        with open(file,"r", encoding='latin-1') as fic:
            data = fic.read()
    if data=="":
        dico={}
    else:
        dico = json.loads(data)
    return dico
def found(file, var):
    dico = setup_file(file)
    if var in dico:
        return dico[var]
    return None
def save(file,var,value):
    dico = setup_file(file)
    dico[var] = value
    saveDico(file,dico)
def saveDico(file,dico):
    dataSaved = json.dumps(dico, indent=4)
    with open(file,"w") as fic:
        fic.write(dataSaved)
def remove(file,var):
    dico = setup_file(file)
    if var in dico:
        del dico[var]
    saveDico(file,dico)

def GetList(file,var):
    val = found(file, var)
    if type(val) == str:
        if "[" in val:
            try:
                val = eval(val)
            except:
                pass
    if type(val)==list:
        return val
    return None
