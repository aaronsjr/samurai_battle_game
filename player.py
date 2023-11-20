import pygame
import pygame.mixer
import math

#Define the private class player (it is only inhereted never directly used)
class __Player:
    #The following constructer method takes a game instance as an arg so that I can access the instance of screen
    #that is present in the main game class. 
    def __init__(self, game):
        #Define the array that contains all of the frames of the samurai character.
        self.screen = game.screen
        self.settings = game.settings
        self.RUNTIME_SCREEN_WIDTH = game.RUNTIME_SCREEN_WIDTH
        self.RUNTIME_SCREEN_HEIGHT = game.RUNTIME_SCREEN_HEIGHT
        self.HORIZONTAL_MOVE_SPEED = game.RUNTIME_SCREEN_WIDTH//160
        self.VERTICAL_MOVE_SPEED = game.RUNTIME_SCREEN_HEIGHT//90
        self.JUMP_CUTOFF = math.floor(0.68*self.RUNTIME_SCREEN_HEIGHT)
        self.rect = self.image.get_rect()
        self.move_frame_index = 0
        self.attack_frame_index = 0
        self.jump_frame_index = 0
        self.idle_frame_index = 0
        self.attacking = False
        self.moving = False
        self.jumping = False
        self.falling = False
        self.horizontal_velocity = 0
        self.vertical_velocity = 0
        self.attack_sound = pygame.mixer.Sound("./attack_sound.mp3")
        self.theme_1 = pygame.mixer.Sound("./theme_1.mp3")
        self.FLOOR_HEIGHT = game.FLOOR_HEIGHT
        self.reset_player()

    
    def blit(self):
        #Check to see if the each frame index is greater than that of the length of the list containing the 
        #frames and if so reset the value of the frame index to zero to restart the animation.
        if self.move_frame_index == len(self.move_frames):
            self.move_frame_index = 0
        elif self.attack_frame_index == len(self.attack_frames):
            self.attack_frame_index = 0
            self.attacking = False
        elif self.idle_frame_index == len(self.idle_frames):
            self.idle_frame_index = 0
        elif self.jump_frame_index == len(self.jump_frames):
            self.jump_frame_index = 0
        elif self.idle_frame_index == len(self.idle_frames):
            self.idle_frame_index = 0

        #If player is moving right then update the animation every time player_obj.blit() is called.
        if self.attacking == True:
            self.image = pygame.image.load(self.attack_frames[self.attack_frame_index])
            self.attack_frame_index += 1
        
        elif self.moving == True and self.jumping == False:
            if self.rect.x + self.horizontal_velocity >= self.RUNTIME_SCREEN_WIDTH - 200: #200 is sprite width.
                self.moving = False
            elif self.rect.x + self.horizontal_velocity <= 0:
                self.moving = False
            else:
                self.rect.x += self.horizontal_velocity
                self.image = pygame.image.load(self.move_frames[self.move_frame_index])
                self.move_frame_index += 1

        elif self.jumping == True:
            #If player is below (pixels will be greater) self.JUMP_CUTOFF then subtract self.vertical_velocity
            #If player is above (pixels will be smaller) self.JUMP_CUTOFF then add self.vertical_velocity
            #If change in velocity would cause player y rect to be > self.RUNTIME_SCREEN_HEIGHT, then ignore input
            #and set self.jumping = False.
            if self.rect.y - self.vertical_velocity < self.JUMP_CUTOFF and self.falling == False:
                if self.settings.DEBUG_MODE == True:
                    print(f"DEBUG: {self}.JUMP_CUTOFF reached")
                if self.moving == True and self.rect.x + self.horizontal_velocity > 0 and self.rect.x + self.horizontal_velocity < self.RUNTIME_SCREEN_WIDTH-200:
                    self.rect.x +=  self.horizontal_velocity
                self.falling = True
            elif self.rect.y > self.JUMP_CUTOFF and self.falling == False:
                self.rect.y -= self.vertical_velocity
                self.image = pygame.image.load(self.jump_frames[0])                
                if self.moving == True and self.rect.x + self.horizontal_velocity > 0 and self.rect.x + self.horizontal_velocity < self.RUNTIME_SCREEN_WIDTH-200:
                    self.rect.x += self.horizontal_velocity
                if self.settings.DEBUG_MODE == True:
                    print(f"DEBUG: {self} is rising")
            elif self.rect.y + self.vertical_velocity >= self.FLOOR_HEIGHT:
                self.rect.y = self.FLOOR_HEIGHT
                self.vertical_velocity = 0
                self.falling = False
                self.jumping = False
           
            elif self.falling == True:
                print(f"DEBUG {self} is falling")
                if self.moving == True and self.rect.x + self.horizontal_velocity > 0 and self.rect.x + self.horizontal_velocity < self.RUNTIME_SCREEN_WIDTH-200:
                    self.rect.x += self.horizontal_velocity
                self.rect.y += self.vertical_velocity

            

        else:
            self.image = pygame.image.load(self.idle_frames[self.idle_frame_index])
            self.idle_frame_index += 1

        self.screen.blit(self.image, self.rect)

    def reset_player(self):
        self.rect.x, self.rect.y = (self.RUNTIME_SCREEN_WIDTH//8, self.RUNTIME_SCREEN_HEIGHT-150)

class Yellow_Player(__Player):
    def __init__(self, game):
        self.image = pygame.image.load("yellow_player/run_0.png")
        self.attack_frames = ["yellow_player/attack_0.png", "yellow_player/attack_1.png", "yellow_player/attack_2.png", "yellow_player/attack_3.png",
                              "yellow_player/attack_4.png", "yellow_player/attack_5.png", "yellow_player/attack_6.png", "yellow_player/attack_7.png"]
        self.idle_frames = ["yellow_player/idle_0.png", "yellow_player/idle_0.png", "yellow_player/idle_1.png", "yellow_player/idle_1.png", 
                            "yellow_player/idle_2.png", "yellow_player/idle_2.png", "yellow_player/idle_3.png", "yellow_player/idle_3.png"]
        self.jump_frames = ["yellow_player/jump_0.png", "yellow_player/jump_1.png", "yellow_player/jump_2.png", "yellow_player/jump_3.png"]
        self.move_frames = ["yellow_player/run_0.png","yellow_player/run_1.png","yellow_player/run_2.png","yellow_player/run_3.png",
                            "yellow_player/run_4.png","yellow_player/run_5.png"]
        super().__init__(game)

class Red_Player(__Player):
    def __init__(self, game):
        self.image = None
        self.attack_frames = [None]
        self.idle_frames = [None]
        self.jump_frames = [None]
        self.move_frames = [None]
        super().__init__(game)
   
    def reset_player(self):
        #An example of polymorphism 
        self.rect.x, self.rect.y = (self.RUNTIME_SCREEN_WIDTH - self.RUNTIME_SCREEN_WIDTH//8, self.RUNTIME_SCREEN_HEIGHT-150)
