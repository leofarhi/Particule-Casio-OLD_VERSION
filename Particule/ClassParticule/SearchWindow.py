from Particule import *
from ClassSystem.ScrollableFrame import ScrollableFrame
from ClassSystem.Notebook import Notebook
from tkinter import ttk

class SearchWindow(EditorWindow):
    def __init__(self, RootWindow):
        #bt = RootWindow.Particule.Inspector.Bouton_AddComponent
        #geo = str(bt.winfo_width()) + "x250"
        #geo += "+" + str(bt.winfo_rootx()) + "+" + str(bt.winfo_rooty() + bt.winfo_height())
        EditorWindow.__init__(self, RootWindow,
                              ExternalWindow={"name": "Search", "geometry": "250x250"},
                              Resize=False, ScrollbarShow=False)
        self.pack(fill=tkinter.BOTH, expand=True)
        self.focus_set()



        self.var_barreRecherche = StringVar()
        self.SearchBar =  Entry(self, textvariable=self.var_barreRecherche)
        self.SearchBar.pack(fill=X)

        onglets = ttk.Notebook(self)
        onglets.pack(fill=BOTH, expand=True)

        self.FolderFrame = ttk.Frame(onglets)
        self.SceneFrame = ttk.Frame(onglets)
        self.FolderFrame.pack(fill=BOTH, expand=True)
        self.SceneFrame.pack(fill=BOTH, expand=True)

        onglets.add(self.FolderFrame, text='Folder')
        onglets.add(self.SceneFrame, text='Scene')

        scrollbarFolder = Scrollbar(self.FolderFrame)
        scrollbarFolder.pack(side=RIGHT, fill=Y)

        self.mylistFolder = Listbox(self.FolderFrame, yscrollcommand=scrollbarFolder.set)
        for line in range(100):
            self.mylistFolder.insert(END, "This is line Folder " + str(line))

        self.mylistFolder.pack(side=LEFT, fill=BOTH, expand=True)
        scrollbarFolder.config(command=self.mylistFolder.yview)

        self.mylistFolder.delete(0, END)


        #####################

        scrollbarScene = Scrollbar(self.SceneFrame)
        scrollbarScene.pack(side=RIGHT, fill=Y)

        self.mylistScene = Listbox(self.SceneFrame, yscrollcommand=scrollbarScene.set)
        for line in range(100):
            self.mylistScene.insert(END, "This is line Scene " + str(line))

        self.mylistScene.pack(side=LEFT, fill=BOTH, expand=True)
        scrollbarScene.config(command=self.mylistScene.yview)

    def ClearListe(self):
        self.mylistFolder.delete(0, END)
        self.mylistScene.delete(0, END)


    def OnLostFocus(self,_=None):
        self.RootWindow.destroy()

