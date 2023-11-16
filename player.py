class Player:
    #The following constructer method takes a game instance as an arg so that I can access the instance of screen
    #that is present in the main game class. 
    def __init__(self, game):
        #Define the array that contains all of the frames of the samurai character.
        self.screen = game.screen
        self.RUNTIME_SCREEN_WIDTH = game.RUNTIME_SCREEN_WIDTH
        self.RUNTIME_SCREEN_HEIGH = game.RUNTIME_SCREEN_HEIGHT
        self.attack_frames = ["char/attack_0.png", "char/attack_1.png", "char/attack_2.png", "char/attack_3.png",
                              "char/attack_4.png", "char/attack_5.png", "char/attack_6.png", "char/attack_7.png"]
        self.idle_frames = ["char/idle_0.png", "char/idle_1.png", "char/idle_2.png", "char/idle_3.png"]
        self.jump_frames = ["char/run_0.png", "char/run_1.png", "char/run_2.png", "char/run_3.png", "char/run_4.png",
                            "char/run_5.png"]
        self.move_frame_index = 0
        self.attacking = False
        self.moving = False
        self.jumping = False

    
    def blit(self):
        pass
        #Consider whether character is in attacking, moving or jumping state
        #If character is in one of these states get current index of animation and display it.
        #Things to consider, jumping animation must synchroinse with when player hits the ground.
        #How am I going to get each index when I need each index.

    def centre_player(self):
        self.rect.middle = (self.RUNTIME_SCREEN_WIDTH//2, self.RUNTIME_SCREEN_HEIGHT//2)
