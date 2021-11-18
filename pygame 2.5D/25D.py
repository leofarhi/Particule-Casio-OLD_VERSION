import pygame
pygame.init()
pygame.mixer.init()
surfaceW = 1270
surfaceH = 630
surface = pygame.display.set_mode((surfaceW,surfaceH),)
def creaTexteObj(texte, Police, couleur):
    texteSurface = Police.render(texte, True, couleur)
    return texteSurface, texteSurface.get_rect()

def message(texte, taille, col, x, y, police, trans=255):
    font_Texte = pygame.font.Font(police, taille)
    font_TexteSurf, font_TexteRect = creaTexteObj(texte, font_Texte, (col[0], col[1], col[2], 255))
    font_TexteRect.center = x, y
    surface.blit(font_TexteSurf, font_TexteRect)
def message_left(texte, taille, col, x, y, police, trans=255):
    font_Texte = pygame.font.Font(police, taille)
    font_TexteSurf, font_TexteRect = creaTexteObj(texte, font_Texte, (col[0], col[1], col[2], 255))
    font_TexteRect.topleft = x, y
    surface.blit(font_TexteSurf, font_TexteRect)
    return font_TexteSurf, font_TexteRect

def taille_texte_left(texte, taille, couleur, x, y, police):
    font_Texte = pygame.font.Font(police, taille)
    font_TexteSurf, font_TexteRect = creaTexteObj(texte, font_Texte, couleur)
    font_TexteRect.topleft = x, y
    return font_TexteSurf, font_TexteRect
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
        self.z=-100
        self.depth=50
        self.img = img
        self.w, self.h = img.get_size()

    def Print(self,):
        self.PrintObj(self.depth,1,self.z)
        #surface.blit(img,(self.x-camera.x,self.y+camera.y))

    def Clone(self):
        rx = self.Z_Pos+(camera.z/10)
        if rx<=0:
            return
        y=((self.y+camera.y)*(rx/20))+(surfaceH/2)
        x=((self.x-camera.x)*(rx/20))+(surfaceW/2)
        if y<-self.h or y>surfaceH or rx<16 or rx>145:
            return
        img= pygame.transform.scale(self.img, (int(self.w*(rx/100)), int(self.h*(rx/100))))
        surface.blit(img,(x,y))
    def PrintObj(self,TerrainLength,Resolution,StartPoint):
        #longueur = (((((20/30)*8)*TerrainLength)-160)/5)*(-Resolution)
        self.Z_Pos=-StartPoint
        self.Z_Pos-=TerrainLength
        for i in range(TerrainLength*abs(Resolution)):
            self.Clone()
            self.Z_Pos+=1/Resolution
    
obj = Obj25D()

obj2 = Obj25D()

obj2.x+=100

obj2.y+=5

obj2.z=-50

elems = [obj,obj2]
while True:
    clear_screen()
    for i in elems:
        i.Print()
    if GetKey(273):
        camera.z+=5
    if GetKey(274):
        camera.z-=5
        
    if GetKey(275):
        camera.x-=5
    if GetKey(276):
        camera.x+=5

    if GetKey(119):
        camera.y+=5
    if GetKey(115):
        camera.y-=5
    message(str(camera.z), 25, (0,0,0), 30, 10, "Calibri.ttf")
    show_screen()

