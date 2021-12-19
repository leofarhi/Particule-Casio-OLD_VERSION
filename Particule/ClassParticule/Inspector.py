from Particule import *
from ClassSystem.EditorWindow import EditorWindow
from ClassParticule.AddComponentFrame import AddComponentFrame
from ClassParticule.Tag import Tag
from ClassParticule.Layer import Layer
import platform

class Inspector(EditorWindow):
    def __init__(self,RootWindow):
        EditorWindow.__init__(self,RootWindow,Resize=True,ScrollbarShow=False)

        self.GameObjectWindow = Frame(self)
        self.GameObjectWindow.pack(fill=tkinter.BOTH, expand=True)

        self.mainframe = LabelFrame(self.GameObjectWindow)
        self.mainframe.pack(fill=tkinter.X,side=TOP)#.pack(fill=tkinter.X, expand=True,side=tkinter.TOP, anchor=NW)

        self.ApercuWidth = 50
        self.ApercuHeight = self.ApercuWidth
        self.ApercuCanevas = Canvas(self.mainframe, width=self.ApercuWidth, height=self.ApercuHeight)
        self.ImgApercu = PhotoImage(file="lib/vide.png")
        self.ApercuCanevasImg = self.ApercuCanevas.create_image(0, 0, anchor=NW, image=self.ImgApercu)
        self.ApercuCanevas.grid(row=0, column=0)


        self.SetApercuImage("lib/Empty.png")

        self.frameStatic = Frame(self.mainframe)
        self.frameStatic.grid(row=0, column=1)

        self.frameTop = Frame(self.frameStatic)
        self.frameTop.pack(fill=tkinter.X, expand=True,side=tkinter.TOP, anchor=N)

        self.varActive = IntVar()
        self.varActive.set(1)
        #self.varActive.trace("w", self.updateDataGameObj)
        self.CheckActive = Checkbutton(self.frameTop, variable=self.varActive, offvalue=0, onvalue=1,command=self.ChangeActifSelf)
        self.CheckActive.grid(row=0, column=0)
        #self.CheckActive.bind("<ButtonRelease-1>", self.ChangeActifSelf)

        self.var_Entry_name = StringVar()
        #self.var_Entry_name.trace("w", self.updateDataGameObj)
        self.entry_name = Entry(self.frameTop, textvariable=self.var_Entry_name)
        self.entry_name.bind('<KeyRelease>', self.updateDataGameObj)
        self.entry_name.grid(row=0, column=1)


        self.varStatic = IntVar()
        #self.varStatic.trace("w", self.updateDataGameObj)
        self.CheckStatic = Checkbutton(self.frameTop, variable=self.varStatic, text="Static", offvalue=0, onvalue=1,command=self.updateDataGameObj)
        self.CheckStatic.grid(row=0, column=2)
        #self.CheckStatic.bind("<ButtonRelease-1>", self.updateDataGameObj)

        self.frameBottom = Frame(self.frameStatic)
        self.frameBottom.pack(fill=tkinter.X, expand=True)

        self.label_Tag = Label(self.frameBottom, text="Tag : ")
        self.label_Tag.grid(row=0, column=0)
        self.CurSelectTag = StringVar()
        self.LstAllSelectTag = ttk.Combobox(self.frameBottom, textvariable=self.CurSelectTag, width=10)
        self.LstAllSelectTag.grid(row=0, column=1)
        self.LstAllSelectTag.bind('<<ComboboxSelected>>', self.updateDataGameObj)

        self.label_Layer = Label(self.frameBottom, text="Layer : ")
        self.label_Layer.grid(row=0, column=2)
        self.CurSelectLayer = StringVar()
        self.LstAllSelectLayer = ttk.Combobox(self.frameBottom, textvariable=self.CurSelectLayer, width=10)
        self.LstAllSelectLayer.grid(row=0, column=3)
        self.LstAllSelectLayer.bind('<<ComboboxSelected>>', self.updateDataGameObj)

        self.label_Order = Label(self.frameBottom, text="Order : ")
        self.label_Order.grid(row=1, column=0)
        self.var_Entry_Order = IntVar()
        # self.var_Entry_name.trace("w", self.updateDataGameObj)
        self.entry_Order = Entry(self.frameBottom, textvariable=self.var_Entry_Order)
        self.entry_Order.bind('<KeyRelease>', self.updateDataGameObj)
        self.entry_Order.grid(row=1, column=1)

        FrameTemp = Frame(self.GameObjectWindow)
        FrameTemp.pack(fill=tkinter.BOTH,expand=True,side=TOP)
        self.ZoneComponentCanvas = Canvas(FrameTemp)
        self.ZoneComponentCanvas.pack(side=LEFT,fill=tkinter.BOTH,expand=True, anchor=N)

        yscrollbar = ttk.Scrollbar(FrameTemp,orient="vertical",command = self.ZoneComponentCanvas.yview)
        yscrollbar.pack(side=RIGHT,fill="y")

        self.ZoneComponentCanvas.bind('<Configure>',lambda e:self.ZoneComponentCanvas.configure(scrollregion = self.ZoneComponentCanvas.bbox('all')))
        self.ZoneComponentCanvas.bind('<Button-1>', lambda e: self.ZoneComponentCanvas.configure(
            scrollregion=self.ZoneComponentCanvas.bbox('all')))

        self.ZoneComponentCanvas.bind('<Enter>', self._bound_to_mousewheel)
        self.ZoneComponentCanvas.bind('<Leave>', self._unbound_to_mousewheel)


        self.ZoneComponentCanvas.configure(yscrollcommand = yscrollbar.set)

        FrameTemp2 = Frame(self.ZoneComponentCanvas)
        self.ZoneComponentCanvas.create_window((0,0),window=FrameTemp2,anchor='n')

        self.Bouton_AddComponent = Button(FrameTemp2, text=TradTxt("Ajouter un Component"),
                                          command=partial(AddComponentFrame, self.Particule.Mafenetre))
        self.Bouton_AddComponent.pack(fill=tkinter.X, expand=True, anchor=N, padx=10,
                                      pady=10)  # .pack(padx=10,pady=10,fill=tkinter.X, expand=True)#,side=tkinter.TOP, anchor=N)

        self.mainComponentsFrame = LabelFrame(FrameTemp2)
        self.mainComponentsFrame.pack(fill=tkinter.BOTH,expand=True, anchor=N)

    def _bound_to_mousewheel(self, event):
        if platform.system()=="Linux":
            self.ZoneComponentCanvas.bind_all("<Button-4>", self._on_mousewheel)
            self.ZoneComponentCanvas.bind_all("<Button-5>", self._on_mousewheel)
        else:
            self.ZoneComponentCanvas.bind_all("<MouseWheel>", self._on_mousewheel)

    def _unbound_to_mousewheel(self, event):
        if platform.system()=="Linux":
            self.ZoneComponentCanvas.unbind_all("<Button-4>")
            self.ZoneComponentCanvas.unbind_all("<Button-5>")
        else:
            self.ZoneComponentCanvas.unbind_all("<MouseWheel>")
    def _on_mousewheel(self, event):
        self.ZoneComponentCanvas.configure(scrollregion=self.ZoneComponentCanvas.bbox('all'))
        self.ZoneComponentCanvas.update()
        self.ZoneComponentCanvas.yview_scroll(int(-1 * (event.delta / 120)), "units")


    def updateDataGameObj(self,*args):
        ItemSelected = self.Particule.Hierarchy.ItemSelected
        if ItemSelected==None:
            return
        ItemSelected.name = self.var_Entry_name.get()
        ItemSelected.activeSelf = bool(self.varActive.get())
        #print(bool(self.varActive.get()))
        ItemSelected.isStatic = bool(self.varStatic.get())
        ItemSelected.tag = Tag(self.LstAllSelectTag.current())
        ItemSelected.layer = Layer(self.LstAllSelectLayer.current())
        lastOrder = ItemSelected.Order
        ItemSelected.Order = self.var_Entry_Order.get()
        if lastOrder!=ItemSelected.Order:
            self.Particule.Scene.RefreshOrder()
        #print(bool(self.varStatic.get()))
        if ItemSelected.activeSelf and ItemSelected.activeInHierarchy:
            tag = 'Active'
        else :
            tag = 'Desactive'
        self.Particule.Hierarchy.t.item(str(ItemSelected.ID), text=ItemSelected.name,tags=(tag))
    def OnFocus(self,event=None):
        self.ZoneComponentCanvas.configure(scrollregion=self.ZoneComponentCanvas.bbox('all'))
        self.LstAllSelectTag["values"] = [i.replace("Tag.","") for i in list(map(str, Tag))]
        self.LstAllSelectLayer["values"] = [i.replace("Layer.","") for i in list(map(str, Layer))]

    def SetApercuImage(self,path):
        ImgApercu = ImageTk.Image.open(path)
        ImgApercu = ImgApercu.resize((self.ApercuWidth, self.ApercuHeight), Image.ANTIALIAS)
        self.ImgApercu = ImageTk.PhotoImage(ImgApercu)
        self.ApercuCanevas.itemconfig(self.ApercuCanevasImg, image=self.ImgApercu)


    def UpdateItemSelected(self):
        ItemSelected=self.Particule.Hierarchy.ItemSelected
        #self.GameObjectWindow.pack(fill=tkinter.BOTH, expand=True)
        if ItemSelected==None:
            return
        #print(ItemSelected.name,ItemSelected.ID)
        self.OnFocus()
        self.var_Entry_name.set(ItemSelected.name)
        self.varActive.set(int(ItemSelected.activeSelf))
        self.varStatic.set(int(ItemSelected.isStatic))
        self.LstAllSelectTag.current(ItemSelected.tag.value)
        self.LstAllSelectLayer.current(ItemSelected.layer.value)
        self.var_Entry_Order.set(ItemSelected.Order)

        """self.mainComponentsFrame.destroy()
        self.mainComponentsFrame = LabelFrame(self)
        self.mainComponentsFrame.grid(row=1, column=0, sticky='EWNS')"""
        lst = self.all_children(self.mainComponentsFrame)
        for i in lst:
            i.pack_forget()
        for i in ItemSelected.ListOfComponent:
            i.PrintOnGui()
        for i in range(3):
            self.ZoneComponentCanvas.configure(scrollregion=self.ZoneComponentCanvas.bbox('all'))
            self.ZoneComponentCanvas.update()

    def all_children(self, wid):
        finList=[]
        _list = wid.winfo_children()
        for item in _list:
            finList.append(item)
        return finList

    def ChangeActifSelf(self,*args):
        self.updateDataGameObj()
        ItemSelected = self.Particule.Hierarchy.ItemSelected
        if ItemSelected == None:
            return
        ItemSelected.ChangeActifSelf()
