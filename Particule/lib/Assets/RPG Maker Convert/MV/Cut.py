import pygame
import sys
import os
os.makedirs("Tilesets", exist_ok=True)
Lst = ['Dungeon_A1.png', 'Dungeon_A2.png', 'Dungeon_A4.png', 'Dungeon_A5.png', 'Dungeon_B.png', 'Dungeon_C.png', 'Inside_A1.png', 'Inside_A2.png', 'Inside_A4.png', 'Inside_A5.png', 'Inside_B.png', 'Inside_C.png', 'Outside_A1.png', 'Outside_A2.png', 'Outside_A3.png', 'Outside_A4.png', 'Outside_A5.png', 'Outside_B.png', 'Outside_C.png', 'SF_Inside_A4.png', 'SF_Inside_B.png', 'SF_Inside_C.png', 'SF_Outside_A3.png', 'SF_Outside_A4.png', 'SF_Outside_A5.png', 'SF_Outside_B.png', 'SF_Outside_C.png', 'World_A1.png', 'World_A2.png', 'World_B.png', 'World_C.png']
for i in Lst:
    name = os.path.splitext(i)[0]
    os.makedirs("Tilesets/"+name, exist_ok=True)
    IMG = pygame.image.load("Tilesets/"+i)
    w,h =IMG.get_size()
    for x in range(0,w,16):
        for y in range(0,h,16):
            img = IMG.subsurface(x,y,16,16)
            pygame.image.save(img,"Tilesets/"+name+"/"+name+"-"+str(x)+"-"+str(y)+".png")
