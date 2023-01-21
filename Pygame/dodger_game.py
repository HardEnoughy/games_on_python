import pygame, sys, random
from pygame.locals import *

pygame.init()

#constants
PLAYERSPEED = 6
WHITE = (255, 255, 255)
NEWENEMY = 20
WINDOWWIDTH = 800
WINDOWHEIGHT = 800
PLAYERSIZE = 50
BLUE = (0, 0, 255)

class DodgerGame():
    def __init__(self):

        #main window
        self.main_clock = pygame.time.Clock()
        self.main_surface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
        pygame.display.set_caption("Dodger game")

        #player setting
        self.player = pygame.Rect(WINDOWWIDTH // 2, WINDOWHEIGHT - PLAYERSIZE, PLAYERSIZE, PLAYERSIZE)
        self.player_image = pygame.image.load("images/player.png")

        #baddies settings
        self.baddie_image = pygame.image.load("images/baddie.png")
        self.baddies_stretch = []
        self.baddies = []
        for i in range(10):
            self.add_baddie()
        
        #bools for buttons
        self.is_left = False
        self.is_right = False
        self.is_up = False
        self.is_down = False

        #text for end game
        self.main_font = pygame.font.SysFont(None, 48)
        self.game_over_text = self.main_font.render("GAME OVER", False, WHITE, BLUE)
        self.font = pygame.font.SysFont(None, 30)
        self.after_game_text = self.font.render("Do you want to try again? Press space for again and esc for exit", False, WHITE, BLUE)

        #scoring
        self.score = 0
    
    def show_game_over(self):
        spacing = 50
        
        #score text
        score_text = self.font.render(f"Your score is {int(self.score)}", False, WHITE, BLUE)
        score_text_rect = score_text.get_rect()
        
        #game over text
        game_over_rect = self.game_over_text.get_rect()
        game_over_rect.centerx = self.main_surface.get_rect().centerx
        game_over_rect.centery = self.main_surface.get_rect().centery

        #score text placement
        score_text_rect.centerx = self.main_surface.get_rect().centerx
        score_text_rect.centery = game_over_rect.centery + spacing

        #hint text
        after_game_rect = self.after_game_text.get_rect()
        after_game_rect.centerx = self.main_surface.get_rect().centerx
        after_game_rect.centery = score_text_rect.centery + spacing

        self.main_surface.fill(BLUE)

        self.main_surface.blit(self.game_over_text, game_over_rect)
        self.main_surface.blit(score_text, score_text_rect)
        self.main_surface.blit(self.after_game_text, after_game_rect)

        pygame.display.update()

        is_again = False
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    if event.key == K_SPACE:
                        is_again = True 
                    
            if is_again:
                break
        
        self.run_game()

    
    def add_baddie(self):
        size = random.randint(5, 40)
        self.baddies.append(pygame.Rect(random.randint(0, WINDOWWIDTH - 20), random.randint(0, 50), size, size))
        self.baddies_stretch.append(pygame.transform.scale(self.baddie_image, (size, size)))
    
    def move_baddie(self, baddie):
        speed = random.randint(1, 10)
        baddie.bottom += speed
    
    def draw_baddie(self, baddie):
        self.main_surface.blit(self.baddies_stretch[self.baddies.index(baddie)], baddie)
    
    def run_game(self):
        self.main_surface.fill(WHITE)
        self.baddies = []
        self.baddies_stretch = []
        self.is_left = False
        self.is_right = False
        self.is_up = False
        self.is_down = False
        self.score = 0
        pygame.mixer.music.load("sounds/background.mid")
        pygame.mixer.music.play(-1, 0.0)
        die_sound = pygame.mixer.Sound("sounds/gameover.wav")
        music_playing = True

        pygame.display.update()
        is_game_over = False
        while True:
            #event checks
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                
                #keydown events 
                if event.type == KEYDOWN:
                    if event.key == K_LEFT:
                        self.is_left = True
                    if event.key == K_RIGHT:
                        self.is_right = True
                    if event.key == K_DOWN:
                        self.is_down = True
                    if event.key == K_UP:
                        self.is_up = True
                    if event.key == K_m:
                        if music_playing:
                            pygame.mixer.music.stop()
                        else:
                            pygame.mixer.music.play(-1, 0.0) 
                        music_playing = not music_playing
                
                #keyup events
                if event.type == KEYUP:
                    if event.key == K_LEFT:
                        self.is_left = False 
                    if event.key == K_RIGHT:
                        self.is_right = False 
                    if event.key == K_DOWN:
                        self.is_down = False
                    if event.key == K_UP:
                        self.is_up = False
            
            #adding baddies if there is not enough
            while len(self.baddies) < NEWENEMY:
                self.add_baddie()
            
            #filling display
            self.main_surface.fill(WHITE)

            #moving player if needed
            if self.is_up and self.player.top > 0:
                self.player.top -= PLAYERSPEED
            if self.is_right and self.player.right < WINDOWWIDTH:
                self.player.right += PLAYERSPEED
            if self.is_down and self.player.bottom < WINDOWHEIGHT:
                self.player.top += PLAYERSPEED
            if self.is_left and self.player.left > 0:
                self.player.left -= PLAYERSPEED
            
            #removing or moving baddies
            for baddie in self.baddies[:]:
                if baddie.bottom >= WINDOWHEIGHT:
                    self.baddies.remove(baddie) 
                    # del self.baddies_stretch[self.baddies.index(baddie)]
                else:
                    self.move_baddie(baddie)
                    self.draw_baddie(baddie)
                
                #checking collision
                if self.player.colliderect(baddie):
                   is_game_over = True
            
            if is_game_over:
                pygame.mixer.music.stop()
                if music_playing:
                    die_sound.play()
                break
                    
            #drawing player
            self.main_surface.blit(self.player_image, self.player)

            #scoring
            self.score += 0.07

            #updating display
            pygame.display.update()
            self.main_clock.tick(60)
        
        self.show_game_over()

game = DodgerGame()
game.run_game()
