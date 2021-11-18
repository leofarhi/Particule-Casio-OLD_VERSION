import pygame
pygame.init()
W, H=500, 500
screen = pygame.display.set_mode([500, 500])
running = True

bcg=(200, 200, 200)
red=(255, 0 ,0)
purp=(255, 0, 255)
wall=(100, 100, 100)

def collideLineLine(l1_p1, l1_p2, l2_p1, l2_p2):

    # normalized direction of the lines and start of the lines
    P  = pygame.math.Vector2(*l1_p1)
    line1_vec = pygame.math.Vector2(*l1_p2) - P
    R = line1_vec.normalize()
    Q  = pygame.math.Vector2(*l2_p1)
    line2_vec = pygame.math.Vector2(*l2_p2) - Q
    S = line2_vec.normalize()

    # normal vectors to the lines
    RNV = pygame.math.Vector2(R[1], -R[0])
    SNV = pygame.math.Vector2(S[1], -S[0])
    RdotSVN = R.dot(SNV)
    if RdotSVN == 0:
        return False

    # distance to the intersection point
    QP  = Q - P
    t = QP.dot(SNV) / RdotSVN
    u = QP.dot(RNV) / RdotSVN

    return t > 0 and u > 0 and t*t < line1_vec.magnitude_squared() and u*u < line2_vec.magnitude_squared()

def colideRectLine(rect, p1, p2):
    return (collideLineLine(p1, p2, rect.topleft, rect.bottomleft) or
            collideLineLine(p1, p2, rect.bottomleft, rect.bottomright) or
            collideLineLine(p1, p2, rect.bottomright, rect.topright) or
            collideLineLine(p1, p2, rect.topright, rect.topleft))

def collideRectPolygon(rect, polygon):
    for i in range(len(polygon)-1):
        if colideRectLine(rect, polygon[i], polygon[i+1]):
            return True
    return False

class player:
    def bg(self):        
        screen.fill(bcg)
        self.outer = self.createPolygon(self.x, self.y)
        pygame.draw.polygon(screen, wall, self.outer)
  
    def createPolygon(self, x, y):
        return [
            (x,y), (x+800, y), (x+1200, y+200), (x+1200, y+600), 
            (x+800, y+800), (x, y+800), (x-400, y+600), (x-400, y+200),           
            (x,y), (x, y+50), (x-350, y+225), (x-350, y+575), 
            (x, y+750), (x+800, y+750), (x+1150, y+575), (x+1150, y+225),
            (x+800, y+50),(x, y+50)]
    
    def __init__(self, color, size=20, speed=0.25):
        self.x=0
        self.y=0
        self.col=color
        self.size=size
        self.speed=speed

    def draw(self):
        s=self.size
        self.rect=pygame.Rect(W/2-s/2, H/2-s/2, self.size, self.size)
        pygame.draw.rect(screen, self.col, self.rect)

    def move(self, x, y):
        
        x *= self.speed
        y *= self.speed
        polygon = self.createPolygon(self.x + x, self.y + y)
        if not collideRectPolygon(self.rect, polygon):
            self.x += x
            self.y += y
            
p=player(red)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    p.bg()

    keys=pygame.key.get_pressed()
    
    if keys[pygame.K_a]: p.move(1, 0)
    if keys[pygame.K_d]: p.move(-1, 0)
    if keys[pygame.K_w]: p.move(0, 1)
    if keys[pygame.K_s]: p.move(0, -1)

    p.draw()
    pygame.display.update()

pygame.quit()
