import pygame, sys, random
from pygame.locals import *

#constants
PLAYERSPEED = 6
WHITE = (255, 255, 255)
NEWENEMY = 7
WINDOWWIDTH = 400
WINDOWHEIGHT = 400

class DodgerGame():
    def __init__(self):

        #main window
        self.main_clock = pygame.time.Clock()
        self.main_surface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
        pygame.display.set_caption("Dodger game")

        #player setting
        self.player = pygame.Rect(200, 380, 40, 40)
        self.player_image = pygame.image.load("images/player.png")

        #baddies settings
        self.baddie_image = pygame.image.load("images/baddie.png")
        self.baddies_stretch = []
        self.baddies = []
        self.baddies_counter = 0
        for i in range(10):
            self.add_baddie()
        
        #bools for buttons
        self.is_left = False
        self.is_right = False
        self.is_up = False
        self.is_down = False
    
    def add_baddie(self):
        size = random.randint(5, 40)
        self.baddies.append(pygame.Rect(random.randint(0, WINDOWWIDTH - 20), random.randint(0, 50), size, size))
        self.baddies_stretch.append(pygame.transform.scale(self.baddie_image, (size, size)))
    
    def move_baddie(self, baddie):
        speed = random.randint(1, 8)
        baddie.bottom += speed
    
    def draw_baddie(self, baddie):
        self.main_surface.blit(self.baddies_stretch[self.baddies.index(baddie)], baddie)
    
    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == KEYDOWN:
                    if event.key == K_LEFT:
                        self.is_left = True
                    if event.key == K_RIGHT:
                        self.is_right = True
                    if event.key == K_DOWN:
                        self.is_down = True
                    if event.key == K_UP:
                        self.is_up = True

                if event.type == KEYUP:
                    if event.key == K_LEFT:
                        self.is_left = False 
                    if event.key == K_RIGHT:
                        self.is_right = False 
                    if event.key == K_DOWN:
                        self.is_down = False
                    if event.key == K_UP:
                        self.is_up = False
            
            while len(self.baddies) < NEWENEMY:
                self.add_baddie()
            
            self.main_surface.fill(WHITE)

            if self.is_up and self.player.top > 0:
                self.player.top -= PLAYERSPEED
            if self.is_right and self.player.right < WINDOWWIDTH:
                self.player.right += PLAYERSPEED
            if self.is_down and self.player.bottom < WINDOWHEIGHT:
                self.player.top += PLAYERSPEED
            if self.is_left and self.player.left > 0:
                self.player.left -= PLAYERSPEED
            
            for baddie in self.baddies[:]:
                if baddie.bottom >= WINDOWHEIGHT:
                    self.baddies.remove(baddie) 
                    # del self.baddies_stretch[self.baddies.index(baddie)]
                else:
                    self.move_baddie(baddie)
                    self.draw_baddie(baddie)
                
                if self.player.colliderect(baddie):
                    pygame.quit()
                    sys.exit()
                    
            self.main_surface.blit(self.player_image, self.player)

            pygame.display.update()
            self.main_clock.tick(40)

game = DodgerGame()
game.run_game()
