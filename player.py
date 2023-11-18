import pygame

class Player:
    #The following constructer method takes a game instance as an arg so that I can access the instance of screen
    #that is present in the main game class. 
    def __init__(self, game):
        #Define the array that contains all of the frames of the samurai character.
        self.screen = game.screen
        self.RUNTIME_SCREEN_WIDTH = game.RUNTIME_SCREEN_WIDTH
        self.RUNTIME_SCREEN_HEIGHT = game.RUNTIME_SCREEN_HEIGHT
        self.HORIZONTAL_MOVE_SPEED = game.RUNTIME_SCREEN_WIDTH//160
        self.VERTICAL_MOVE_SPEED = game.RUNTIME_SCREEN_HEIGHT//90
        self.JUMP_CUTOFF = 0.8*self.RUNTIME_SCREEN_WIDTH
        self.image = pygame.image.load("yellow_player/run_0.png")
        self.rect = self.image.get_rect()
        self.attack_frames = ["yellow_player/attack_0.png", "yellow_player/attack_1.png", "yellow_player/attack_2.png", "yellow_player/attack_3.png",
                              "yellow_player/attack_4.png", "yellow_player/attack_5.png", "yellow_player/attack_6.png", "yellow_player/attack_7.png"]
        self.idle_frames = ["yellow_player/idle_0.png", "yellow_player/idle_1.png", "yellow_player/idle_2.png", "yellow_player/idle_3.png"]
        self.jump_frames = ["yellow_player/jump_0.png", "yellow_player/jump_1.png", "yellow_player/jump_2.png", "yellow_player/jump_3.png"]
        self.move_frames = ["yellow_player/run_0.png","yellow_player/run_1.png","yellow_player/run_2.png","yellow_player/run_3.png",
                            "yellow_player/run_4.png","yellow_player/run_5.png"]
        self.move_frame_index = 0
        self.attack_frame_index = 0
        self.jump_frame_index = 0
        self.idle_frame_index = 0
        self.attacking = False
        self.moving = False
        self.jumping = False
        self.horizontal_velocity = 0
        self.vertical_velocity = 0
        self.centre_player()

    
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
        if self.moving == True:
            self.image = pygame.image.load(self.move_frames[self.move_frame_index])
            self.move_frame_index += 1
        elif self.attacking == True:
            self.image = pygame.image.load(self.attack_frames[self.attack_frame_index])
            self.attack_frame_index += 1
        elif self.jumping == True:
            if self.is_airborne() == 1:
                self.image = pygame.image.load(self.jump_frames[1])
            elif self.is_airborne() == -1:
                self.image = pygame.image.load(self.jump_frames[2])
            else:
                self.image = pygame.image.load(self.jump_frames[self.jump_frame_index])
                self.jump_frame_index += 1
        else:
            self.image = pygame.image.load(self.idle_frames[self.idle_frame_index])
            self.idle_frame_index += 1
        
        self.screen.blit(self.image, self.rect)

    def centre_player(self):
        self.rect.midbottom = (self.RUNTIME_SCREEN_WIDTH//2, self.RUNTIME_SCREEN_HEIGHT-20)

    def is_airborne():
        if self.rect.y < self.JUMP_CUTOFF and self.vertical_velocity < 0:
            return -1
        elif self.rect.y < self.JUMP_CUTOFF and self.vertical_velocity > 0:
            return 1
