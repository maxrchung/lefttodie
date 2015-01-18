import pygame
from Animation import Animate, AllSprites
import random
import sys
from soundmanager import soundmanager
import math
from ScreenShaker import *
import Tiles

class Screen:
    def __init__(self):
        pygame.init()
        self.go = True
        self.state = "LIFESCREEN"
        self.left = False
        self.screenw = 1024
        self.screenh = 768
        self.sound = soundmanager()
        self.shakeScreen = pygame.display.set_mode((self.screenw, self.screenh))
        self.screen = self.shakeScreen.copy()
        self.screenShaker = ScreenShaker()

        pygame.display.set_caption("Left to Die")
        pygame.font.init()
        self.fontpath = pygame.font.match_font('comicsansms')
        self.font = pygame.font.Font(self.fontpath, 28)
        self.velocity = [.03, 0]
        self.playerpos = [64, 600]

        self.clouds = Clouds()
        self.cloudlist = self.clouds.clouds
        self.cloudsnormal = sorted(self.clouds.cloudimages)
        self.cloudsinverted = sorted(self.clouds.cloudsinverted)
        self.lock = True
        self.backobjects = BackObjects()
        self.startplayer= Animate(AllSprites['playerMoveNormal.png'], 2, 2, 128, 32, 32)
        self.mainplayer= Animate(AllSprites['playerIdleNormal.png'], 2, 2, 500, 32, 32)

        self.current_level = 1
        self.lives = 3
        self.l_screen_clock = pygame.time.Clock()
        self.l_screen_time = 0

        self.jumped = False
        self.TALevel1 = Tiles.TilesArray(self.screen,'level1.txt')
        self.TALevel1.make_tiles()
        self.TALevel1.make_inverse()
        
        self.levels = [self.TALevel1]
        self.tiles = [self.TALevel1.tiles]
        self.tilesInverse = [self.TALevel1.inverted_tiles]
        self.currentLevel = 0
        self.currentTiles = self.tiles[self.currentLevel]
        self.currentTilesInverse = self.tilesInverse[self.currentLevel]

    def update(self):
        self.leftPressed = False
        self.rightPressed = False
        self.upPressed = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.leftPressed = True
                    self.left = True

                elif event.key == pygame.K_RIGHT:
                    self.rightPressed = True
                    self.left = False

                elif event.key == pygame.K_UP:
                    self.upPressed = True

                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        keys = pygame.key.get_pressed()
            
        if self.state == "LIFESCREEN":
            self.startplayer.Aupdate()
            self.l_screen_time += self.l_screen_clock.tick()
            if self.l_screen_time >= 3000:
                self.state = "GAMESCREEN"
                self.l_screen_time = 0
                self.playerpos = self.levels[self.currentLevel].startpos
                self.playerpos = [250, 250]

        elif self.state == "GAMESCREEN":
            if self.left:
                self.screenShaker.shake(1, 9999)

                if self.leftPressed:
                    self.sound.playsound("inverse")
                if self.jumped:
                    if not self.mainplayer.image == AllSprites['playerJumpInverse.png']:
                        self.mainplayer = Animate(AllSprites['playerJumpInverse.png'], 1, 1, 1000, 32, 32)
                elif keys[pygame.K_LEFT]:
                    if not self.mainplayer.image == AllSprites['playerMoveInverse.png']:
                        self.mainplayer = Animate(AllSprites['playerMoveInverse.png'], 2, 2, 128, 32, 32)
                else:
                    if not self.mainplayer.image == AllSprites['playerIdleInverse.png']:
                        self.mainplayer = Animate(AllSprites['playerIdleInverse.png'], 2, 2, 500, 32, 32)

            else:
                self.screenShaker.stop()

                if self.rightPressed:
                    self.sound.playsound("syobon")
                if self.jumped:
                    if not self.mainplayer.image == AllSprites['playerJumpNormal.png']:
                        self.mainplayer = Animate(AllSprites['playerJumpNormal.png'], 1, 1, 1000, 32, 32)
                elif keys[pygame.K_RIGHT]:
                    if not self.mainplayer.image == AllSprites['playerMoveNormal.png']:
                        self.mainplayer = Animate(AllSprites['playerMoveNormal.png'], 2, 2, 128, 32, 32)
                else:
                    if not self.mainplayer.image == AllSprites['playerIdleNormal.png']:
                        self.mainplayer = Animate(AllSprites['playerIdleNormal.png'], 2, 2, 500, 32, 32)

            if self.upPressed and not self.jumped:
                self.sound.playsound("jump")
                self.jumped = True
                self.velocity[1] = -25.0

            # Right movement
            if keys[pygame.K_RIGHT]:
                self.velocity[0] += 3.0
            
            # Left movement
            elif keys[pygame.K_LEFT]:
                self.velocity[0] += -3.0
            elif keys[pygame.K_DOWN]:
                self.mainplayer = Animate(AllSprites['playerJumpNormal.png'], 1, 1, 1000, 32, 32)
                self.state = "VICTORYLEAP"

            if abs(self.velocity[0]) > 10.0:
                if self.velocity[0] > 0:
                    self.velocity[0] = 10.0
                elif self.velocity[0] < 0:
                    self.velocity[0] = -10.0

            self.previouspos = self.playerpos

            self.playerpos[0] += self.velocity[0]
            self.playerpos[1] += self.velocity[1]

            if self.left:
                self.checkCollision(self.previouspos, self.playerpos, self.currentTilesInverse)
            else:
                self.checkCollision(self.previouspos, self.playerpos, self.currentTiles)

            if self.velocity[1] > 0:
                self.jumped = True

            if abs(self.velocity[0]) > 0.1:
                self.velocity[0] *= 0.6
            else:
                self.velocity[0] = 0

            # Gravity application
            self.velocity[1] += 3.2
            if self.velocity[1] > 15.0:
                self.velocity[1] = 15.0
            if self.playerpos[0]+8 < 0:
                self.playerpos[0] = -8
            elif self.playerpos[0] + 24 > 1024:
                self.playerpos[0] = 1024 - 24

            self.mainplayer.Aupdate()
            self.clouds.cloudupdate(self.left)
            self.backobjects.backupdate(self.left)

        elif self.state == "VICTORYLEAP":
            if self.playerpos[1] < -64:
                self.currentLevel += 1
                self.state = "LIFESCREEN"
                self.velocity[1] = 0
                self.l_screen_clock.tick()
            else:
                self.velocity[1] = -25.0

            if abs(self.velocity[0]) > 10.0:
                if self.velocity[0] > 0:
                    self.velocity[0] = 10.0
                elif self.velocity[0] < 0:
                    self.velocity[0] = -10.0

            self.previouspos = self.playerpos

            self.playerpos[0] += self.velocity[0]
            self.playerpos[1] += self.velocity[1]

            self.checkCollision(self.previouspos, self.playerpos, self.currentTiles)

            if abs(self.velocity[0]) > 0.1:
                self.velocity[0] *= 0.6
            else:
                self.velocity[0] = 0

            self.velocity[1] += 3.2
            if self.velocity[1] > 15.0:
                self.velocity[1] = 15.0
            if self.playerpos[0]+8 < 0:
                self.playerpos[0] = -8
            elif self.playerpos[0] + 24 > 1024:
                self.playerpos[0] = 1024 - 24

            self.mainplayer.Aupdate()
            self.clouds.cloudupdate(self.left)
            self.backobjects.backupdate(self.left)

        elif self.state == "DEATHDROP":
            pass

        elif self.state == "ENDSCREEN":
            pass
    def checkCollision(self, previouspos, playerpos, tiles):
        # Make our playerRect based on the given position
        playerRect = pygame.Rect(playerpos[0] + 8, playerpos[1] + 8, 16, 24)
        for tile in tiles:
            # Don't care if it's empty
            if tile.name == "empty":
                continue
            tileRect = pygame.Rect(tile.x*32, tile.y*32, 32, 32)
                
            if playerRect.colliderect(tileRect):
                if tile.name == "spikes":
                    # DEATH DROP STATE EXECUTE
                    self.sound.playsound("death")
                    self.sound.playsound("levelDie")
                elif tile.name == "end":
                    # VICTORY LEAP STATE EXECUTE
                    self.sound.playsound("victory")
                    self.sound.playsound("levelUp")
                elif tile.name == "block":
                    # Reposition the player
                    # Finds center points of the boundingRects
                    playerPos = [previouspos[0] + 16, previouspos[1] + 16]
                    tilePos = [tile.x*32 + 16, tile.y*32 + 16]

                    # Finds diff vector between player and tile
                    diff = (playerPos[0]-tilePos[0], playerPos[1]-tilePos[1])
                
                    # If x is larger than the y, then we know that it is a horizontal collision
                    if abs(diff[0]) >= abs(diff[1]):
                        # If x is positive, then we reset player on the right of the tile
                        if  diff[0] > 0:
                            playerRect.left = tileRect.right
                        # Else if negative, we set the player left of the tile
                        else:
                            playerRect.right = tileRect.left


                    # If y is larger than x, then there is a vertical collision
                    elif abs(diff[1]) >= abs(diff[0]):
                        # If y is negative, then reset player on the top of the tile
                        # Note that this is opposite of x calclations because we have to keep
                        # in mind that y is reversed according to top left coordinates
                        if diff[1] < 0:
                            self.velocity[1] = 0
                            playerRect.bottom = tileRect.top
                            self.jumped = False
                        else:
                            playerRect.top = tileRect.bottom

                    self.playerpos = [playerRect.x - 8, playerRect.y - 8]



    def draw(self):
        if self.state == "LIFESCREEN":
            background_colour = (0, 0, 0)
            self.screen.fill(background_colour)
            self.startplayer.draw(self.screen, 460, 352)
            text = self.font.render("x " + str(self.lives), True, pygame.Color(255,255,255))
            self.screen.blit(text, (492, 347))
                                              
        elif self.state == "GAMESCREEN":             
            if self.left:
                self.sun = AllSprites["sunInverse.png"]
                self.background = AllSprites["backgroundInverse.png"]
                for i in range(0, len(self.cloudlist)):
                    if "Inverse" not in self.cloudlist[i][3]:
                        self.cloudlist[i][3] = self.cloudsinverted[int(self.cloudlist[i][3][5]) - 1]
                self.bhill = AllSprites["groundBackInverse.png"]
                self.fhill = AllSprites["groundFrontInverse.png"]
                self.fsky = AllSprites["skyFrontInverse.png"]
                self.bsky = AllSprites["skyBackInverse.png"]

                self.bhill2 = AllSprites["groundBackInverse.png"]
                self.fhill2 = AllSprites["groundFrontInverse.png"]
                self.fsky2 = AllSprites["skyFrontInverse.png"]
                self.bsky2 = AllSprites["skyBackInverse.png"]

            else:
                self.sun = AllSprites["sunNormal.png"]
                self.background = AllSprites["backgroundNormal.png"]
                for i in range(0, len(self.cloudlist)):
                    if "Normal" not in self.cloudlist[i][3]:
                        self.cloudlist[i][3] = self.cloudsnormal[int(self.cloudlist[i][3][5]) - 1]

                self.bhill = AllSprites["groundBackNormal.png"]
                self.fhill = AllSprites["groundFrontNormal.png"]
                self.fsky = AllSprites["skyFrontNormal.png"]
                self.bsky = AllSprites["skyBackNormal.png"]

                self.bhill2 = AllSprites["groundBackNormal.png"]
                self.fhill2 = AllSprites["groundFrontNormal.png"]
                self.fsky2 = AllSprites["skyFrontNormal.png"]
                self.bsky2 = AllSprites["skyBackNormal.png"]
                
                self.background = AllSprites["backgroundNormal.png"]

            self.screen.blit(self.background, (0, 0))
            self.screen.blit(self.sun, (0, 0))
            
            self.screen.blit(self.bsky, (self.backobjects.bskyx,0))
            self.screen.blit(self.bsky2, (self.backobjects.bskyx2,0))
            self.screen.blit(self.bhill, (self.backobjects.bhillx, 534))
            self.screen.blit(self.bhill2, (self.backobjects.bhillx2, 534))

            self.screen.blit(self.fhill, (self.backobjects.fhillx, 593))
            self.screen.blit(self.fhill2, (self.backobjects.fhillx2, 593))
            self.screen.blit(self.fsky, (self.backobjects.fskyx,0))
            self.screen.blit(self.fsky2, (self.backobjects.fskyx2,0))

            for i in range(0, len(self.cloudlist)):
                self.screen.blit(AllSprites[self.cloudlist[i][3]], (self.cloudlist[i][0], self.cloudlist[i][1]))
        
            if self.left:
                for tile in self.currentTilesInverse:
                    tile.draw()

            else:
                for tile in self.currentTiles:
                    tile.draw()

            self.mainplayer.draw(self.screen, self.playerpos[0], self.playerpos[1])

        elif self.state == "VICTORYLEAP":

            if self.left:
                self.sun = AllSprites["sunInverse.png"]
                self.background = AllSprites["backgroundInverse.png"]
                for i in range(0, len(self.cloudlist)):
                    if "Inverse" not in self.cloudlist[i][3]:
                        self.cloudlist[i][3] = self.cloudsinverted[int(self.cloudlist[i][3][5]) - 1]
                self.bhill = AllSprites["groundBackInverse.png"]
                self.fhill = AllSprites["groundFrontInverse.png"]
                self.fsky = AllSprites["skyFrontInverse.png"]
                self.bsky = AllSprites["skyBackInverse.png"]

                self.bhill2 = AllSprites["groundBackInverse.png"]
                self.fhill2 = AllSprites["groundFrontInverse.png"]
                self.fsky2 = AllSprites["skyFrontInverse.png"]
                self.bsky2 = AllSprites["skyBackInverse.png"]

            else:
                self.sun = AllSprites["sunNormal.png"]
                self.background = AllSprites["backgroundNormal.png"]
                for i in range(0, len(self.cloudlist)):
                    if "Normal" not in self.cloudlist[i][3]:
                        self.cloudlist[i][3] = self.cloudsnormal[int(self.cloudlist[i][3][5]) - 1]

                self.bhill = AllSprites["groundBackNormal.png"]
                self.fhill = AllSprites["groundFrontNormal.png"]
                self.fsky = AllSprites["skyFrontNormal.png"]
                self.bsky = AllSprites["skyBackNormal.png"]

                self.bhill2 = AllSprites["groundBackNormal.png"]
                self.fhill2 = AllSprites["groundFrontNormal.png"]
                self.fsky2 = AllSprites["skyFrontNormal.png"]
                self.bsky2 = AllSprites["skyBackNormal.png"]

                self.background = AllSprites["backgroundNormal.png"]

            self.screen.blit(self.background, (0, 0))
            self.screen.blit(self.sun, (0, 0))

            self.screen.blit(self.bsky, (self.backobjects.bskyx,0))
            self.screen.blit(self.bsky2, (self.backobjects.bskyx2,0))
            self.screen.blit(self.bhill, (self.backobjects.bhillx, 534))
            self.screen.blit(self.bhill2, (self.backobjects.bhillx2, 534))

            self.screen.blit(self.fhill, (self.backobjects.fhillx, 593))
            self.screen.blit(self.fhill2, (self.backobjects.fhillx2, 593))
            self.screen.blit(self.fsky, (self.backobjects.fskyx,0))
            self.screen.blit(self.fsky2, (self.backobjects.fskyx2,0))

            for i in range(0, len(self.cloudlist)):
                self.screen.blit(AllSprites[self.cloudlist[i][3]], (self.cloudlist[i][0], self.cloudlist[i][1]))

            for tile in self.currentTiles:
                tile.draw()

            self.mainplayer.draw(self.screen, self.playerpos[0], self.playerpos[1])


        elif self.state == "DEATHDROP":
            pass

        elif self.state == "ENDSCREEN":
            pass
        
        self.screenShaker.update()
        self.shakeScreen.blit(self.screen, self.screenShaker.getValue())
        pygame.display.update()

class BackObjects:
    def __init__(self):
        self.width = 1022
        self.speedf = 5
        self.speedb = 2.5
        self.min = -self.width
        self.max = self.width
        
        self.fskyx = 0
        self.bskyx = 0
        self.fhillx = 0
        self.bhillx = 0
        
        self.fskyx2 = self.width
        self.bskyx2 = self.width
        self.fhillx2 = self.width
        self.bhillx2 = self.width

    def backupdate(self, inverse):
        if inverse:
            self.fskyx += self.speedf
            self.bskyx += self.speedb
            self.fhillx += self.speedf
            self.bhillx += self.speedb

            if self.fskyx > self.width:
                self.fskyx = self.min + 5

            if self.bskyx > self.width:
                self.bskyx = self.min

            if self.bhillx > self.width:
                self.bhillx = self.min

            if self.fhillx > self.width:
                self.fhillx = self.min + 5
            
            self.fskyx2 += self.speedf
            self.bskyx2 += self.speedb
            self.fhillx2 += self.speedf
            self.bhillx2 += self.speedb

            if self.fskyx2 > self.width:
                self.fskyx2 = self.min + 5

            if self.bskyx2 > self.width:
                self.bskyx2 = self.min

            if self.bhillx2 > self.width:
                self.bhillx2 = self.min

            if self.fhillx2 > self.width:
                self.fhillx2 = self.min + 5

        else:
            self.bskyx -= self.speedb
            self.fskyx -= self.speedf
            self.fhillx -= self.speedf
            self.bhillx -= self.speedb

            if self.fskyx < -self.width:
                self.fskyx = self.max - 5

            if self.bskyx < -self.width:
                self.bskyx = self.max

            if self.bhillx < -self.width:
                self.bhillx = self.max

            if self.fhillx < -self.width:
                self.fhillx = self.max - 5
                
            self.fskyx2 -= self.speedf
            self.bskyx2 -= self.speedb
            self.fhillx2 -= self.speedf
            self.bhillx2 -= self.speedb

            if self.fskyx2 < -self.width:
                self.fskyx2 = self.max - 5

            if self.bskyx2 < -self.width:
                self.bskyx2 = self.max

            if self.bhillx2 < -self.width:
                self.bhillx2 = self.max

            if self.fhillx2 < -self.width:
                self.fhillx2 = self.max - 5

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
            # Random width [0]
            # Random height [1]
            # Random speed [2]
            # Random normal cloud [3]
            self.clouds.append([random.randrange(100, 900),random.randrange(117, 500), random.randint(1,2), self.cloudimages[random.randint(0,len(self.cloudimages) - 1)]])

    def cloudupdate(self, inverted):       
        if inverted:
            for i in range(len(self.clouds)):
                self.clouds[i][0] += self.clouds[i][2]
                if self.clouds[i][0] - 100 > 1020:
                    self.clouds[i][0] = 0
                    self.clouds[i][1] = random.randrange(117, 500)
                    self.clouds[i][3] = self.cloudimages[random.randint(0, len(self.cloudsinverted) - 1)]
        else:
            for i in range(len(self.clouds)):
                self.clouds[i][0] -= self.clouds[i][2]
                if self.clouds[i][0] + 100 < 0:
                    self.clouds[i][0] = 1020
                    self.clouds[i][1] = random.randrange(117, 500)
                    self.clouds[i][3] = self.cloudimages[random.randint(0, len(self.cloudimages) - 1)]

