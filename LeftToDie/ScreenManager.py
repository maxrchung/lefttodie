import pygame
from Animation import Animate, AllSprites

class Screen:
    def __init__(self):
        self.state = "LIFESCREEN"
        self.screen = pygame.display.set_mode((1024, 768))
        self.startplayer= Animate(AllSprites['playerMoveNormal.png'], 2, 2, 5, 32, 32)
        self.current_level = 1
        self.lives = 3
        self.l_screen_clock = pygame.time.Clock()
        self.l_screen_time = 0

        
                                              
        
        self.cloud1x, self.cloud1y = 100, 200

                                              
        #pygame.display.set_caption('Left To Die')
        #animator = Animate(Animation.AllSprites['playerIdleNormal.png'], 2, 2, 5, 32, 32)

    def update(self):
        
        self.draw()
        
        

    def draw(self):
        if self.state == "LIFESCREEN":
            background_colour = (0, 0, 0)
            self.screen.fill(background_colour)
            self.startplayer.Aupdate(),
            self.startplayer.draw(self.screen, 460, 352)
            pygame.font.init()
            fontpath = pygame.font.match_font('lucidasans')
            font = pygame.font.Font(fontpath, 28)
            text = font.render("x " + str(self.lives), True, pygame.Color(255,255,255))
            self.screen.blit(text, (492, 347))
            self.l_screen_time += self.l_screen_clock.tick()
            if self.l_screen_time >= 3000:
                self.state = "GAMESCREEN"
                self.l_screen_time = 0
                                              
        elif self.state == "GAMESCREEN":
            self.background = AllSprites["backgroundNormal.png"]
            self.screen.blit(self.background,(0,0))
            self.screen.blit(AllSprites["cloud1Normal.png"], (self.cloud1x, self.cloud1y))
            
            
        elif self.state == "ENDSCREEN":
            pass            
 
        
        pygame.display.update()
