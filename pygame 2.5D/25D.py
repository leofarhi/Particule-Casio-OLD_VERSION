import pygame
pygame.init()
pygame.mixer.init()
surfaceW = 1270
surfaceH = 630
surface = pygame.display.set_mode((surfaceW,surfaceH),)

KEYDOWN=[]
KEYPRESS=[]
KEYUP=[]
def GetKey(key):
    return key in KEYPRESS
def GetKeyDOWN(key):
    return key in KEYDOWN
def GetKeyUP(key):
    return key in KEYUP
def Keyboard():
    global KEYDOWN, _quit
    KEYDOWN.clear()
    KEYUP.clear()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            _quit = True
        if event.type == pygame.KEYDOWN:
            KEYDOWN.append(event.key)
            if not event.key in KEYPRESS:
                KEYPRESS.append(event.key)
        if event.type == pygame.MOUSEBUTTONDOWN:
            KEYDOWN.append(event.button)
        if event.type == pygame.MOUSEBUTTONUP:
            pass
        if event.type == pygame.KEYUP:
            KEYUP.append(event.key)
            if event.key in KEYPRESS:
                KEYPRESS.remove(event.key)
def Mouse():
    x, y = pygame.mouse.get_pos()
    if fullscreen:
        # zoom_surface=(surfaceW/fullscreenW)
        x, y = x * (surfaceW / fullscreenW), y * (surfaceH / fullscreenH)
    return x, y

def print_surface():
    global surface
    pygame.display.update()
###

def set_pixel(x,y,color):
    surface.set_at((x, y), color)


def show_screen():
    #pygame.display.update()
    Keyboard()
    print_surface()

def clear_screen():
    surface.fill((255,255,255))

class Camera:
    def __init__(self):
        self.x=0
        self.y=0
        self.z=0

camera = Camera()
camera.x=0
camera.y=0
img = pygame.image.load("download.png")
class Obj25D:
    def __init__(self):
        self.x=0
        self.y=0
        self.img = img
        self.w, self.h = img.get_size()

    def Print(self,):
        self.PrintObj(100,-2,250)
        #surface.blit(img,(self.x-camera.x,self.y+camera.y))

    def Clone(self):
        rx = self.Z_Pos+camera.z
        if int(self.w*(rx/100))<0 or int(self.h*(rx/100))<0:
            return
        y=abs(rx*-1.2)+camera.y+((self.y+camera.y)*(rx/1))+(surfaceH/2)+self.y
        x=camera.x+((self.x-camera.x)*(rx/1))+(surfaceW/2)
        if y<-self.w or y>surfaceH or rx<16 or rx>145:
            return
        img= pygame.transform.scale(self.img, (int(self.w*(rx/100)), int(self.h*(rx/100))))
        surface.blit(img,(x,y))
    def PrintObj(self,TerrainLength,Resolution,StartPoint):
        longueur = (((((20/30)*8)*TerrainLength)-160)/5)*(-Resolution)
        self.Y_Base=100
        self.Z_Pos=StartPoint
        self.Y_Base-=2
        self.Z_Pos+=Resolution
        self.Z_Pos+=TerrainLength*Resolution
        for i in range(TerrainLength):
            self.Clone()
            self.Z_Pos-=Resolution
    
obj = Obj25D()

obj2 = Obj25D()

obj2.x+=5

obj2.y+=5

elems = [obj,obj2]
while True:
    clear_screen()
    for i in elems:
        i.Print()
    if GetKey(273):
        camera.z+=0.1
    if GetKey(274):
        camera.z-=0.1
        
    if GetKey(275):
        camera.x-=0.1
    if GetKey(276):
        camera.x+=0.1

    if GetKey(119):
        camera.y+=0.1
    if GetKey(115):
        camera.y-=0.1
    show_screen()

