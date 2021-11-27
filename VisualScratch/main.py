

from  VisualScratch import *
import sys,os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
#print(dname)

print(sys.argv)
BuildMode=False
PathSLN=None
try:
    PathSLN=sys.argv[1]
    BuildMode = eval(sys.argv[2])
except:
    pass
if not BuildMode:
    loading = Loading()

#######Debug Test
#PathSLN='/home/farhi/Bureau/PycharmProjects/Particule-Casio/Glacial Project/SLN/Solution.sls'
PathSLN="C:\\Users\\leofa\\OneDrive\\Documents\\PycharmProjects\\NouveauProjet\\SLN\\Solution.sls"
#################

VisualScratch(PathSLN,BuildMode)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
