from SystemExt import read_file as rf
# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

#_tkinter.TclError: No more menus can be allocated.

from Particule import Particule
from ParticuleHub import ParticuleHub
WinParticuleHub=ParticuleHub()
if WinParticuleHub.Start:
    WinEdit = Particule(rf.found("setup.txt", "FolderProject"))
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
