from Particule import *
from ClassSystem.EditorWindow import EditorWindow

class Scene(EditorWindow):
    def __init__(self,RootWindow):
        EditorWindow.__init__(self,RootWindow,Resize=True,ScrollbarShow=False)

        self.scenes = []#repertoire des scenes

        self.x = 0
        self.y = 0
        self.MouseClicAct = False
        self.MouseClicActMtn = False
        self.MaintenueElem = None
        self.mouseX = 0
        self.mouseY = 0
        self.zoom = 1

        self.surface = Canvas(self, background='white')
        self.surface.pack(fill=tkinter.BOTH, expand=True)#.grid(row=1, column=0)

        class MClic:
            def __init__(self, root):
                self.root = root
                self.X = 0
                self.Y = 0
                self.LastMclicX = None
                self.LastMclicY = None

            def ClicDuMilleu(self, event):
                X = event.x
                Y = event.y
                self.LastMclicX = X
                self.LastMclicY = Y

            def ClicDuMilleuDrag(self, event):
                X = event.x
                Y = event.y
                self.root.x -= int((X - self.LastMclicX) * 0.5)
                self.root.y += int((Y - self.LastMclicY) * 0.5)
                self.LastMclicX = X
                self.LastMclicY = Y

        classMClic = MClic(self)
        self.surface.bind('<Button-1>', self.Clic)  # evevement clic gauche (press)
        self.surface.bind('<B1-Motion>', self.Drag)
        self.surface.bind('<ButtonRelease-1>', self.Drop)

        self.surface.bind('<MouseWheel>', self.wheel)  # with Windows and MacOS, but not Linux
        #self.surface.bind('<Button-5>', self.wheel)  # only with Linux, wheel scroll down
        #self.surface.bind('<Button-4>', self.wheel)  # only with Linux, wheel scroll up

        self.surface.bind('<Button-2>', classMClic.ClicDuMilleu)
        self.surface.bind('<B2-Motion>', classMClic.ClicDuMilleuDrag)

        self.surface.bind("<Key-Right>", self.keyRIGHT)
        self.surface.bind("<Key-Left>", self.keyLEFT)
        self.surface.bind("<Key-Up>", self.keyUP)
        self.surface.bind("<Key-Down>", self.keyDOWN)
        self.surface.focus_set()

    def ChangeDimCanvas(self, nb):
        self.Particule.Wintaille = nb
        # CanevasAsset.FrameAssetStore.configure(width = 127*nb, height =63*nb)
        # CanevasAsset.FrameAssetImport.configure(width = 127*nb, height =63*nb)
        self.Particule.CanevasAsset.UpdateScreen()
        self.Particule.Scene.surface.configure(width=127 * nb, height=63 * nb)
        self.Particule.ScratchEditor.CanvasScriptEditor.configure(width=127 * nb, height=63 * nb)

    def keyRIGHT(self, event):
        self.x += 3

    def keyLEFT(self, event):
        self.x -= 3

    def keyUP(self, event):
        self.y += 3

    def keyDOWN(self, event):
        self.y -= 3

    def Drag(self, event):
        """ Gestion de l'evenement bouton gauche enfonce """
        self.mouseX, self.mouseY = event.x, event.y
        self.MouseClicAct = True
        self.MouseClicActMtn = True

    def Drop(self, event):
        self.mouseX, self.mouseY = event.x, event.y
        self.MouseClicAct = False
        self.MouseClicActMtn = False

    def Clic(self, event):
        self.mouseX, self.mouseY = event.x, event.y
        self.MouseClicAct = True
        self.MouseClicActMtn = False
        self.surface.focus_set()

    def bouton_blit(self, mouseX, mouseY, x, y, W, H, key, texte, texture, select, color=blanc, tl=None,
                    pl="BradBunR.ttf",
                    maintenir=False, sound=""):
        enter = False
        if tl == None:
            tl = H - 5
        if mouseX > x and mouseX < (x + W) and mouseY > y and mouseY < (y + H):
            if self.MouseClicAct:
                enter = True
        return enter

    def draw(self, grab, excepted=False):
        for ind, i in enumerate(Pj.Elements):
            if self.Particule.Mode == 0:
                if grab:
                    if type(excepted) == int:
                        if excepted != ind:
                            i.draw()
                    else:
                        i.draw()
                else:
                    i.Grab(ind)
            elif self.Particule.Mode == 1:
                i.draw()

    def wheel(self, event):
        ''' Zoom with mouse wheel '''
        #x = self.canvas.canvasx(event.x)
        #y = self.canvas.canvasy(event.y)
        if event.num == 5 or event.delta == -120:  # scroll down
            self.zoom-=0.5
        if event.num == 4 or event.delta == 120:  # scroll up
            self.zoom += 0.5

    def Update(self):
        if self.zoom<1:
            self.zoom=1
        GameObjects = self.Particule.Hierarchy.allGameObjectOnScene
        for ID, gameObject in GameObjects.items():
            gameObject.UpdateOnGUI()
