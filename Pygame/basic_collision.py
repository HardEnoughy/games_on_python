import pygame, sys
from pygame.locals import *
from random import randint

pygame.init()
main_clock = pygame.time.Clock()

#constants
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
NEWFOOD = 40
FOODSIZE = 20
MOVESPEED = 6

#bools
is_left = False
is_right = False
is_up = False
is_down = False

#main window
window_surface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption("Basic collision")

#food
foods = [pygame.Rect(randint(0, WINDOWWIDTH - FOODSIZE), randint(0, WINDOWHEIGHT - FOODSIZE), FOODSIZE, FOODSIZE) for i in range(20)]
food_counter = 0

#player
player = pygame.Rect(300, 100, 50, 50)

#main loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                is_left = True
            if event.key == K_RIGHT:
                is_right = True
            if event.key == K_DOWN:
                is_down = True
            if event.key == K_UP:
                is_up = True
        if event.type == KEYUP:
            if event.key == K_LEFT:
                is_left = False 
            if event.key == K_RIGHT:
                is_right = False 
            if event.key == K_DOWN:
                is_down = False
            if event.key == K_UP:
                is_up = False
        
        if event.type == MOUSEBUTTONDOWN:
            foods.append(pygame.Rect(event.pos[0], event.pos[1], FOODSIZE, FOODSIZE))
        
    food_counter += 1
    if food_counter > NEWFOOD:
        food_counter = 0
        foods.append(pygame.Rect(randint(0, WINDOWWIDTH - FOODSIZE), randint(0, WINDOWHEIGHT - FOODSIZE), FOODSIZE, FOODSIZE)) 
    
    window_surface.fill(WHITE)
    
    if is_up and player.top > 0:
        player.top -= MOVESPEED
    if is_right and player.right < WINDOWWIDTH:
        player.right += MOVESPEED
    if is_down and player.bottom < WINDOWHEIGHT:
        player.top += MOVESPEED
    if is_left and player.left > 0:
        player.left -= MOVESPEED
    
    pygame.draw.rect(window_surface, BLACK, player)
    
    for food in foods[:]:
        if player.colliderect(food):
            foods.remove(food)
    
    for i in range(len(foods)):
        pygame.draw.rect(window_surface, GREEN, foods[i])
    
    pygame.display.update()
    main_clock.tick(40)
