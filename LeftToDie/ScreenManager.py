import pygame
from Animation import Animate, AllSprites

class Screen:
    def __init__(self):
        self.state = "LIFESCREEN"
        self.screen = pygame.display.set_mode((1024, 768))

        
                                              
        
        self.cloud1x, self.cloud1y = 100, 200

                                              
        #pygame.display.set_caption('Left To Die')
        #animator = Animate(Animation.AllSprites['playerIdleNormal.png'], 2, 2, 5, 32, 32)

    def update(self):
        self.draw()

    def draw(self):
        if self.state == "LIFESCREEN":
            background_colour = (255, 255, 255)
            self.screen.fill(background_colour)
                                              
        elif self.state == "GAMESCREEN":
            self.background = AllSprites["backgroundNormal.png"]
            self.screen.blit(self.background, (0, 0))
            self.screen.blit(AllSprites["cloud1Normal.png"], (self.cloud1x, self.cloud1y))
            
        elif self.state == "ENDSCREEN":
            pass            
 
        
        pygame.display.update()
