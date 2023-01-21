import pygame, sys
import time
from pygame.locals import *

pygame.init()

#constants
DOWNLEFT = 'downleft'
DOWNRIGHT = 'downright'
UPLEFT = 'upleft'
UPRIGHT = 'upright'
MOVESPEED = 4
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WINDOW_V = 400
WINDOW_H = 400

#main window
window_surface = pygame.display.set_mode((WINDOW_H, WINDOW_V), 0, 32)
pygame.display.set_caption("Basic animation")

#boxes
b1 = {'rect': pygame.Rect(300, 80, 50, 100), 'color': RED, 'dir': UPRIGHT}
b2 = {'rect':pygame.Rect(200, 200, 20, 20), 'color':GREEN, 'dir':UPLEFT}
b3 = {'rect':pygame.Rect(100, 150, 60, 60), 'color':BLUE, 'dir':DOWNLEFT}
boxes = [b1, b2, b3]

#main loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    window_surface.fill(WHITE)
    
    for box in boxes:
        if box['dir'] == DOWNRIGHT:
            box['rect'].left += MOVESPEED
            box['rect'].top += MOVESPEED
        if box['dir'] == DOWNLEFT:
            box['rect'].left -= MOVESPEED
            box['rect'].top += MOVESPEED
        if box['dir'] == UPLEFT:
            box['rect'].left -= MOVESPEED
            box['rect'].top -= MOVESPEED
        if box['dir'] == UPRIGHT:
            box['rect'].left += MOVESPEED
            box['rect'].top -= MOVESPEED
        
        if box['rect'].top < 0:
            if box['dir'] == UPRIGHT:
                box['dir'] = DOWNRIGHT
            if box['dir'] == UPLEFT:
                box['dir'] = DOWNLEFT
        
        if box['rect'].right > WINDOW_H:
            if box['dir'] == UPRIGHT:
                box['dir'] = UPLEFT
            if box['dir'] == DOWNRIGHT:
                box['dir'] = DOWNLEFT
        
        if box['rect'].bottom > WINDOW_V:
            if box['dir'] == DOWNLEFT:
                box['dir'] = UPLEFT
            if box['dir'] == DOWNRIGHT:
                box['dir'] = UPRIGHT 
        
        if box['rect'].left < 0:
            if box['dir'] == UPLEFT:
                box['dir'] = UPRIGHT 
            if box['dir'] == DOWNLEFT:
                box['dir'] = DOWNRIGHT
    
        pygame.draw.rect(window_surface, box['color'], box['rect'])
    
    pygame.display.update()
    time.sleep(0.02)
