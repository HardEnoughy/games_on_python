import pygame, sys
from pygame.locals import *

pygame.init()

#colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#main window
window_surface = pygame.display.set_mode((400, 500), 0, 32)
pygame.display.set_caption("Hello world!")
window_surface.fill(WHITE)

#hello world text
main_font = pygame.font.SysFont(None, 48)
text = main_font.render("Hello, world!", False, WHITE, BLUE)
text_rect = text.get_rect()
text_rect.centerx = window_surface.get_rect().centerx
text_rect.centery = window_surface.get_rect().centery

#put text on screen
window_surface.blit(text, text_rect)

#updating screen
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
