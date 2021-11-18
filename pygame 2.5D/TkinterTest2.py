import pygame
import tkinter as tk
from tkinter import *
import os
import platform

root = tk.Tk()
embed = Canvas(root, width = 500, height = 500) #creates embed frame for pygame window
#embed.grid(columnspan = (600), rowspan = 500) # Adds grid
embed.pack(side = LEFT) #packs window to the left
os.environ['SDL_WINDOWID'] = str(embed.winfo_id())
#if platform.system == "Windows":
    #os.environ['SDL_VIDEODRIVER'] = 'windib'

screen = pygame.display.set_mode((500,500))
screen.fill(pygame.Color(255,255,255))
pygame.display.init()
pygame.display.update()
def draw():
    pygame.draw.circle(screen, (0,0,0), (250,250), 125)
    pygame.display.update()
    

img = pygame.image.load("download.png")
draw()

"""
while True:
    pygame.display.update()
    #screen.blit(img,(0,0))
    root.update()   
"""
root.mainloop()
