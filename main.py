import pygame,sys
from pygame.locals import *
pygame.init()
SurfXObj=pygame.display.set_mode((400,300))
pygame.display.set_caption('Main window')
while True: #main game loop
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
pygame.display.update()


