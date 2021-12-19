from Particule import *
from ClassSystem.ScrollableFrame import ScrollableFrame

class AddComponentFrame(EditorWindow):
    def __init__(self,RootWindow):
        bt = RootWindow.Particule.Inspector.Bouton_AddComponent
        geo=str(bt.winfo_width())+"x250"
        geo+="+"+str(bt.winfo_rootx())+"+"+str(bt.winfo_rooty()+bt.winfo_height() )
        EditorWindow.__init__(self, RootWindow,
                              ExternalWindow={"name": "Add Component","geometry":geo},
                              Resize=False, ScrollbarShow=False)
        self.RootWindow.overrideredirect(True)
        self.pack(fill=tkinter.BOTH, expand=True)
        self.mainFrame = LabelFrame(self)
        self.mainFrame.pack(fill=tkinter.BOTH, expand=True)

        if (self.Particule.Hierarchy.ItemSelected==None):
            self.RootWindow.destroy()
            return

        self.var_barreRecherche = StringVar()
        self.entry_barreRecherche = Entry(self.mainFrame, textvariable=self.var_barreRecherche)
        self.entry_barreRecherche.pack(fill=tkinter.X, expand=True)
        self.entry_barreRecherche.bind('<KeyRelease>', self.rechercheBind)

        self.label_Component = Label(self.mainFrame, text="Component")
        self.label_Component.pack()

        self.frame_Compo = Frame(self.mainFrame)
        self.frame_Compo.pack(fill=BOTH, expand=True)

        self.frame_AllCompo = ScrollableFrame(self.frame_Compo,bt.winfo_width())
        self.frame_AllCompo.pack(fill=X, expand=True)

        #self.Particule.AllComponent=range(100)
        self.lstButton=[]
        ItemSelected = self.Particule.Hierarchy.ItemSelected
        for compo in self.Particule.AllComponent:
            name=(compo.__name__).split(".")[-1]
            if self.RemoveTypeComponent(name):
                continue
            temp = Button(self.frame_AllCompo.scrollable_frame,text=name,
                          width=self.frame_AllCompo.canvas.winfo_width(),command = partial(ItemSelected.AddComponent,compo))
            temp.pack(fill=tkinter.X, expand=True)
            self.lstButton.append(temp)

        self.focus_set()
        self.frame_AllCompo.UpdateScroll()
    def OnLostFocus(self,_=None):
        self.frame_AllCompo.OnDestroy()
        self.frame_AllCompo.destroy()
        self.RootWindow.destroy()

    def rechercheBind(self,_):
        ItemSelected = self.Particule.Hierarchy.ItemSelected
        if ItemSelected==None:
            return
        for i in  self.lstButton:
            i.destroy()
        self.lstButton = []
        for compo in self.Particule.AllComponent:
            name=(compo.__name__).split(".")[-1]
            if not self.var_barreRecherche.get().lower() in name.lower():
                continue
            if self.RemoveTypeComponent(name):
                continue
            temp = Button(self.frame_AllCompo.scrollable_frame, text=name,
                          width=self.frame_AllCompo.canvas.winfo_width(),command = partial(ItemSelected.AddComponent,compo))
            temp.pack(fill=tkinter.X, expand=True)
            self.lstButton.append(temp)
        self.frame_AllCompo.UpdateScroll()
    def RemoveTypeComponent(self,name):
        Lst=["MissingScript","Transform"]
        return name in Lst
