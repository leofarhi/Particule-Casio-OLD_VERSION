from SystemExt import read_file as rf
import os
import SystemExt.Moteur as M
import time
import shutil
# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



#_tkinter.TclError: No more menus can be allocated.

from Particule import Particule
from ParticuleHub import ParticuleHub


#shutil.rmtree(os.getcwd() + "/lib/temp_lib")
os.system('rmdir /S /Q "{}"'.format(os.getcwd() + "/lib/temp_lib"))
time.sleep(1)
M.create_rep(os.getcwd() + "/lib/temp_lib")
WinParticuleHub=ParticuleHub()
if WinParticuleHub.Start:
    WinEdit = Particule(rf.found("setup.txt", "FolderProject"))
# Press the green button in the gutter to run the script.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
