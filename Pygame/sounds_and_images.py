import pygame, sys, time, random
from pygame.locals import *

#constants
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
WHITE = (255, 255, 255)
MOVESPEED = 6

pygame.init()
main_clock = pygame.time.Clock()

#main window
main_surface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption("Sounds and images")

#player
player = pygame.Rect(300, 100, 40, 40)
player_image = pygame.image.load("images/player.png")
player_stretched_image = pygame.transform.scale(player_image, (40, 40))

#food
food_image = pygame.image.load("images/cherry.png")
foods = []
for i in range(20):
    foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - 20), random.randint(0, WINDOWHEIGHT - 20), 20, 20))
food_counter = 0
NEWFOOD = 40

#keyboard bools
is_left = False
is_right = False
is_up = False
is_down = False

#music
pick_up_music = pygame.mixer.Sound("sounds/pickup.wav")
pygame.mixer.music.load("sounds/background.mid")
pygame.mixer.music.play(-1, 0.0)
music_playing = True

#main cycle
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

            if event.key == K_m:
                if music_playing:
                    pygame.mixer.music.stop()
                else:
                    pygame.mixer.music.play(-1, 0.0) 
                music_playing = not music_playing

        if event.type == KEYUP:
            if event.key == K_LEFT:
                is_left = False 
            if event.key == K_RIGHT:
                is_right = False 
            if event.key == K_DOWN:
                is_down = False
            if event.key == K_UP:
                is_up = False
    
    food_counter += 1
    if food_counter > NEWFOOD:
        food_counter = 0
        foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - 20), random.randint(0, WINDOWHEIGHT - 20), 20, 20))
    
    main_surface.fill(WHITE)

    if is_up and player.top > 0:
        player.top -= MOVESPEED
    if is_right and player.right < WINDOWWIDTH:
        player.right += MOVESPEED
    if is_down and player.bottom < WINDOWHEIGHT:
        player.top += MOVESPEED
    if is_left and player.left > 0:
        player.left -= MOVESPEED

    main_surface.blit(player_stretched_image, player)

    for food in foods[:]:
        if player.colliderect(food):
            player = pygame.Rect(player.left, player.top, player.width + 2, player.height + 2)
            player_stretched_image = pygame.transform.scale(player_image, (player.width, player.height))
            foods.remove(food)
            if music_playing:
                pick_up_music.play()
    
    for food in foods:
        main_surface.blit(food_image, food)
    
    pygame.display.update()
    main_clock.tick(40)
