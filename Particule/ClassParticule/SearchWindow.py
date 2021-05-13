from Particule import *
from ClassSystem.ScrollableFrame import ScrollableFrame

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
    def OnLostFocus(self,_=None):
        self.RootWindow.destroy()