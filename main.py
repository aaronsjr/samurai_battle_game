import pygame
import sys
from settings import Settings
from player import Player
import pygame.mixer

class Game:
    #Here is an example of a constructor method.
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption("Samurai battle game")
        self.background = pygame.image.load("./background.jpg")
        self.settings = Settings(self)
        theme_1 = pygame.mixer.Sound("theme_1.mp3")
        theme_2 = pygame.mixer.Sound("theme_2.mp3")

        #Check if user has specified fullscreen as an option in settings and enable if true
        if self.settings.FULLSCREEN == True:
            self.screen = pygame.display.set_mode((self.settings.SCREEN_WIDTH, self.settings.SCREEN_HEIGHT), pygame.FULLSCREEN)
        else:
            self.screen = pygame.display.set_mode((self.settings.SCREEN_WIDTH, self.settings.SCREEN_HEIGHT))
        
        self.RUNTIME_SCREEN_WIDTH = self.screen.get_width()
        self.RUNTIME_SCREEN_HEIGHT = self.screen.get_height()
        self.yellow_player = Player(self)
        self.clock = pygame.time.Clock()
 
    def run(self):
        while True:
            self.__check_events()
            self.__update()
    
    #Below is an example of a private method, of course it is not really private because python does
    #not have support for private methods, but I have indicated that it is private by putting a double
    #underscore.
    def __update(self):
        pygame.display.flip()
        self.screen.blit(self.background, (0, 0))
        self.yellow_player.blit()
        self.clock.tick(self.settings.FPS)
    
    #Another example of a private method.
    def __check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            #Check keydown events
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    if self.settings.DEBUG_MODE == True:
                        print("w:keydown")
                    self.yellow_player.jumping = True
                    self.yellow_player.vertical_velocity = self.yellow_player.VERTICAL_MOVE_SPEED
                elif event.key == pygame.K_a:
                    if self.settings.DEBUG_MODE == True:
                        print("a: keydown")
                    self.yellow_player.horizontal_velocity = 0-self.yellow_player.HORIZONTAL_MOVE_SPEED
                    self.yellow_player.moving = True
                elif event.key == pygame.K_s:
                    if self.settings.DEBUG_MODE == True:
                        print("s: keydown")
                elif event.key == pygame.K_d:
                    if self.settings.DEBUG_MODE == True:
                        print("d: keydown") 
                    self.yellow_player.horizontal_velocity = self.yellow_player.HORIZONTAL_MOVE_SPEED  
                    self.yellow_player.moving = True
                elif event.key == pygame.K_SPACE:
                    if self.settings.DEBUG_MODE == True:
                        print("spacebar: keydown ")
                elif event.key == pygame.K_LSHIFT:
                    if self.settings.DEBUG_MODE == True:
                        print("lshift: keydown")
                    self.yellow_player.attacking = True
                    self.yellow_player.attack_sound.play()
                    
            
            #Check keyup events
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    if self.settings.DEBUG_MODE == True:
                        print("w: keyup")
                    self.yellow_player.vertical_velocity = 0
                    #self.yellow_player.jumping = False
                elif event.key == pygame.K_a:
                    if self.settings.DEBUG_MODE == True:
                        print("a: keyup")
                    self.yellow_player.horizontal_velocity = 0
                    self.yellow_player.moving = False
                elif event.key == pygame.K_d:
                    if self.settings.DEBUG_MODE == True:
                        print("d: keyup")
                    self.yellow_player.horizontal_velocity = 0
                    self.yellow_player.moving = False
                elif event.key == pygame.K_s:
                    if self.settings.DEBUG_MODE == True:
                        print("s: keyup")
                    self.yellow_player.vertical_velocity = 0
                elif event.key == pygame.K_LSHIFT:
                    if self.settings.DEBUG_MODE == True:
                        print("lshift: keyup")
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.settings.DEBUG_MODE == True:
                    print(f"click: {pygame.mouse.get_pos()}")

#This ensures that if I have imported main.py into another file then it does not run the game as part of the import.
#Although this would cause a circular import so im not gonna do that!
if __name__ == "__main__":
    game = Game()
    game.run()
