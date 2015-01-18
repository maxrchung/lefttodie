import pygame
from Animation import Animate, AllSprites
import random

class Screen:
    def __init__(self):
        self.state = "LIFESCREEN"
        self.left = False
        self.screenw = 1024
        self.screenh = 768
        self.screen = pygame.display.set_mode((self.screenw, self.screenh))    
        self.clouds = Clouds()
        self.cloudlist = self.clouds.clouds
        self.cloudsnormal = sorted(self.clouds.cloudimages)
        self.cloudsinverted = sorted(self.clouds.cloudsinverted)
        self.startplayer= Animate(AllSprites['playerMoveNormal.png'], 2, 2, 5, 32, 32)
        self.current_level = 1
        self.lives = 3
        self.l_screen_clock = pygame.time.Clock()
        self.l_screen_time = 0
        self.fhill = AllSprites["groundFrontNormal.png"]
        self.bhill = AllSprites["groundBackNormal.png"]


                                              
    def update(self):
##        print("UPDATE LOOP")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    print('INPUT LEFT')
                    self.left = True
                elif event.key == pygame.K_RIGHT:
                    self.left = False     

        if self.state == "LIFESCREEN":
            self.startplayer.Aupdate()
        elif self.state == "GAMESCREEN":
##                print(event)  
            self.clouds.cloudupdate()
            
        elif self.state == "ENDSCREEN":
            pass

##        self.draw()


    def draw(self):
        if self.state == "LIFESCREEN":
            background_colour = (0, 0, 0)
            self.screen.fill(background_colour)
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
##            print('DRAW LOOP')
            if self.left:
                self.background = AllSprites["backgroundInverse.png"]
                for i in range(0, len(self.cloudlist)):
                    if "Inverse" not in self.cloudlist[i][3]:
                        self.cloudlist[i][3] = self.cloudsinverted[int(self.cloudlist[i][3][5]) - 1]
                self.fhill = AllSprites["groundBackInverse.png"]
                self.bhill = AllSprites["groundFrontInverse.png"]
                
                                 
            else:
                for i in range(0, len(self.cloudlist)):
                    if "Normal" not in self.cloudlist[i][3]:
                        self.cloudlist[i][3] = self.cloudsnormal[int(self.cloudlist[i][3][5]) - 1]

                self.fhill = AllSprites["groundBackNormal.png"]
                self.bhill = AllSprites["groundFrontNormal.png"]

                
                self.background = AllSprites["backgroundNormal.png"]

            self.screen.blit(self.background, (0, 0))
            self.screen.blit(self.fhill, (0, 534))
            self.screen.blit(self.bhill, (0, 593))


            for i in range(0, len(self.cloudlist)):
                self.screen.blit(AllSprites[self.cloudlist[i][3]], (self.cloudlist[i][0], self.cloudlist[i][1]))

        elif self.state == "ENDSCREEN":
            pass            
 
        
        pygame.display.update()


class Clouds:
    def __init__(self):
        self.cloudnum = random.randint(5,15)

        self.clouds = []
        self.cloudimages = []
        self.cloudsinverted = []
        
        for sprite, image in AllSprites.items():
            if "cloud" in sprite:
                if "Normal" in sprite:
                    self.cloudimages.append(sprite)
                elif "Inverse" in sprite:
                    self.cloudsinverted.append(sprite)

        for i in range(0, self.cloudnum):
            self.clouds.append([random.randrange(100, 900),random.randrange(117, 500), random.randint(1,2), self.cloudimages[random.randint(0,len(self.cloudimages) - 1)]])

    def cloudupdate(self):
        for i in range(len(self.clouds)):
            self.clouds[i][0] -= self.clouds[i][2]
            if self.clouds[i][0] + 100 < 0:
                self.clouds[i][0] = 1020
                self.clouds[i][1] = random.randrange(117, 500)
                self.clouds[i][3] = self.cloudimages[random.randint(0, len(self.cloudimages) - 1)]

