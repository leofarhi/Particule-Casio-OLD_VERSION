import pygame
import sys
import os
os.makedirs("Tilesets", exist_ok=True)
rer
Outside_A5 = pygame.image.load('Outside_A5.png')
w,h =Outside_A5.get_size()
for x in range(0,w,16):
    for y in range(0,h,16):
        img = Outside_A5.subsurface(x,y,16,16)
        pygame.image.save(img,"Outside_A5/"+str(x)+"-"+str(y)+".png")
