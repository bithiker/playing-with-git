import pygame,sys
from pygame.locals import *
pygame.init()
DISPLAY_MAIN=pygame.display.set_mode((1400,300))
pygame.display.set_caption('Main window')
while True: #main game loop
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
pygame.display.update()


