from tkinter import *
import tkinter
from tkinter.messagebox import *
import tkinter.simpledialog
from tkinter.filedialog import *
from tkinter import ttk
from ClassSystem.PFrame import PFrame

class WinFrameBas(PFrame):
    def __init__(self,RootWindow,Resize=False,ScrollbarShow=True,**kwargs):
        PFrame.__init__(self,RootWindow,borderwidth = 0, highlightthickness = 0,**kwargs)
        self.Resize = Resize
        self.ScrollbarShow= ScrollbarShow
        self.FolderOnglet = self
        self.WObject()
        self.frame = self.AllFolderObjframe


    def FolderObjframeconfig(self, event):
        self.FolderObjCanvasScroll.configure(
            scrollregion=self.FolderObjCanvasScroll.bbox("all"))  # ,width=200,height=200)

    def WObject(self):
        self.FolderObjFrameScroll = Frame(self.FolderOnglet, bg="white",borderwidth = 0, highlightthickness = 0)  # ,width=50,height=100,bd=1)
        self.FolderObjFrameScroll.pack(fill=BOTH, expand=True)  # .grid(row=3,column=0, sticky='EWNS')

        self.FolderObjCanvasScroll = Canvas(self.FolderObjFrameScroll,
                                            bg="white",
                                            borderwidth = 0, highlightthickness = 0)  # ,height=self.ScalePrefab*0.6)

        self.AllFolderObjframe = Frame(self.FolderObjCanvasScroll, bg="white",borderwidth = 0, highlightthickness = 0)
        self.AllFolderObjframe.pack(fill=BOTH, expand=True)

        self.FolderObjScroll = Scrollbar(self.FolderObjFrameScroll, orient="vertical",
                                         command=self.FolderObjCanvasScroll.yview)
        self.FolderObjCanvasScroll.configure(yscrollcommand=self.FolderObjScroll.set)

        self.FolderObjScroll2 = Scrollbar(self.FolderObjFrameScroll, orient="horizontal",
                                          command=self.FolderObjCanvasScroll.xview)
        self.FolderObjCanvasScroll.configure(xscrollcommand=self.FolderObjScroll2.set)
        if self.Resize and self.ScrollbarShow:
            self.FolderObjScroll.pack(side="right", fill="y")
            self.FolderObjScroll2.pack(side=BOTTOM, fill="x")

        self.FolderObjCanvasScroll.pack(side="left", fill=BOTH, expand=True)
        self.FolderObjCanvasCWin = self.FolderObjCanvasScroll.create_window((0, 0),
                                                                            window=self.AllFolderObjframe,
                                                                            anchor='nw')  # ,width = 124*LastScaleScreen)
        self.AllFolderObjframe.bind("<Configure>", self.FolderObjframeconfig)
        if self.Resize:
            self.FolderObjCanvasScroll.bind('<Configure>', self.FrameWidth)

    def FrameWidth(self, event):
        ecart=0
        if self.ScrollbarShow:
            ecart=10
        canvas_width = event.width
        canvas_height = event.height
        self.FolderObjCanvasScroll.itemconfig(self.FolderObjCanvasCWin,
                                              width=canvas_width-ecart,
                                              height=canvas_height-ecart)