import pygame
from Animation import Animate, AllSprites
import sys
from soundmanager import soundmanager
import math
from ScreenShaker import *
import Tiles
from Clouds import Clouds
from BackObjects import BackObjects

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
        self.previouspos = [0,0]
        self.playerpos = [64, 600]

        self.clouds = Clouds()

        self.lock = False
        self.dead = False
        self.win = False
        
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

        self.TALevel2 = Tiles.TilesArray(self.screen, 'level2.txt')
        self.TALevel2.make_tiles()
        self.TALevel2.make_inverse()

        self.levels.append(self.TALevel2)
        self.tiles.append(self.TALevel2.tiles)
        self.tilesInverse.append(self.TALevel2.inverted_tiles)

        #load level 3

        self.TALevel3 = Tiles.TilesArray(self.screen, 'level3.txt')
        self.TALevel3.make_tiles()
        self.TALevel3.make_inverse()

        self.levels.append(self.TALevel3)
        self.tiles.append(self.TALevel3.tiles)
        self.tilesInverse.append(self.TALevel3.inverted_tiles)

        #load level 4
        
        self.TALevel4 = Tiles.TilesArray(self.screen, 'level4.txt')
        self.TALevel4.make_tiles()
        self.TALevel4.make_inverse()

        self.levels.append(self.TALevel4)
        self.tiles.append(self.TALevel4.tiles)
        self.tilesInverse.append(self.TALevel4.inverted_tiles)

        #load level 5
        self.TALevel5 = Tiles.TilesArray(self.screen, 'level5.txt')
        self.TALevel5.make_tiles()
        self.TALevel5.make_inverse()

        self.levels.append(self.TALevel5)
        self.tiles.append(self.TALevel5.tiles)
        self.tilesInverse.append(self.TALevel5.inverted_tiles)

        #load level 6
        self.TALevel6 = Tiles.TilesArray(self.screen, 'level6.txt')
        self.TALevel6.make_tiles()
        self.TALevel6.make_inverse()

        self.levels.append(self.TALevel6)
        self.tiles.append(self.TALevel6.tiles)
        self.tilesInverse.append(self.TALevel6.inverted_tiles)

        #load level 7
        self.TALevel7 = Tiles.TilesArray(self.screen, 'level7.txt')
        self.TALevel7.make_tiles()
        self.TALevel7.make_inverse()

        self.levels.append(self.TALevel7)
        self.tiles.append(self.TALevel7.tiles)
        self.tilesInverse.append(self.TALevel7.inverted_tiles)

        #load level 8
        self.TALevel8 = Tiles.TilesArray(self.screen, 'level8.txt')
        self.TALevel8.make_tiles()
        self.TALevel8.make_inverse()

        self.levels.append(self.TALevel8)
        self.tiles.append(self.TALevel8.tiles)
        self.tilesInverse.append(self.TALevel8.inverted_tiles)


        

    def update(self):
        self.leftPressed = False
        self.rightPressed = False
        self.upPressed = False

        if not self.lock:
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
        self.currentTiles = self.tiles[self.currentLevel]
        self.currentTilesInverse = self.tilesInverse[self.currentLevel]
        self.clouds.cloudupdate(self.left)
        
        if self.state == "LIFESCREEN":
            self.screenShaker.stop()
            self.velocity = [0.3, 0]
            self.sound.playsound("syobon")
            self.left = False
            self.lock = False
            self.dead = False
            self.win = False

            self.startplayer.Aupdate()
            if self.left:
                self.mainplayer= Animate(AllSprites['playerIdleInverse.png'], 2, 2, 500, 32, 32)
            else:
                self.mainplayer= Animate(AllSprites['playerIdleNormal.png'], 2, 2, 500, 32, 32)
                
            self.l_screen_time += self.l_screen_clock.tick()
            if self.l_screen_time >= 3000:
                self.playerpos = self.levels[self.currentLevel].startpos
                self.state = "GAMESCREEN"
                self.l_screen_time = 0


        elif self.state == "GAMESCREEN":
            if not self.dead:
                if self.playerpos[1] > 1024:
                    self.lives -= 1
                    self.dead = True
            
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
                self.sound.playsound("syobon")
                self.velocity[0] += 3.0
                self.left = False
            
            # Left movement
            if keys[pygame.K_LEFT]:
                self.sound.playsound("inverse")
                self.velocity[0] += -3.0
                self.left = True

            if abs(self.velocity[0]) > 10.0:
                if self.velocity[0] > 0:
                    self.velocity[0] = 10.0
                elif self.velocity[0] < 0:
                    self.velocity[0] = -10.0

            self.previouspos = [self.playerpos[0], self.playerpos[1]]

            self.playerpos[0] += self.velocity[0]
            self.playerpos[1] += self.velocity[1]

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
            if not self.dead:
                if not self.win:
                    if self.left:
                        self.checkCollision(self.previouspos, self.playerpos, self.currentTilesInverse)
                    else:
                        self.checkCollision(self.previouspos, self.playerpos, self.currentTiles)

            self.mainplayer.Aupdate()
            self.backobjects.backupdate(self.left)

        if self.win:
            self.lock = True
            if self.playerpos[1] < -64:
                if self.currentLevel +1 >= len(self.levels):
                    self.currentLevel = 0
                else:
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

            self.previouspos = [self.playerpos[0], self.playerpos[1]]

            self.playerpos[0] += self.velocity[0]
            self.playerpos[1] += self.velocity[1]

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
            self.backobjects.backupdate(self.left)

        if self.dead:
            self.lock = True
            if self.playerpos[1] > 1076:
                self.velocity[1] = 0
                self.state = "LIFESCREEN"
                self.l_screen_clock.tick()

            if abs(self.velocity[0]) > 10.0:
                if self.velocity[0] > 0:
                    self.velocity[0] = 10.0
                elif self.velocity[0] < 0:
                    self.velocity[0] = -10.0

            self.previouspos = [self.playerpos[0], self.playerpos[1]]

            self.playerpos[0] += self.velocity[0]
            self.playerpos[1] += self.velocity[1]

            if abs(self.velocity[0]) > 0.1:
                self.velocity[0] *= 0.6
            else:
                self.velocity[0] = 0

            self.velocity[1] += 5
            if self.playerpos[0]+8 < 0:
                self.playerpos[0] = -8
            elif self.playerpos[0] + 24 > 1024:
                self.playerpos[0] = 1024 - 24

            self.mainplayer.Aupdate()
            self.backobjects.backupdate(self.left)

        elif self.state == "ENDSCREEN":
            pass

    def checkCollision(self, previouspos, playerpos, tiles):
        # Make our playerRect based on the given position
        playerRect = pygame.Rect(playerpos[0] + 8, playerpos[1] + 8, 16, 24)
        collisions = []

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
                    self.screenShaker.shake(10, 800)
                    if not self.left:
                        self.mainplayer = Animate(AllSprites['playerJumpNormal.png'], 1, 1, 1000, 32, 32)
                    else:
                        self.mainplayer = Animate(AllSprites['playerJumpInverse.png'], 1, 1, 1000, 32, 32)
                    self.lives -= 1
                    self.lock = True
                    self.dead = True
                    self.velocity[1] = -25
                    return
                elif tile.name == "end":
                    self.mainplayer = Animate(AllSprites['playerJumpNormal.png'], 1, 1, 1000, 32, 32)
                    self.lock = True
                    self.win = True
                    self.sound.playsound("victory")
                    self.sound.playsound("levelUp")
                    if not self.left:
                        self.mainplayer = Animate(AllSprites['playerJumpNormal.png'], 1, 1, 1000, 32, 32)
                    else:
                        self.mainplayer = Animate(AllSprites['playerJumpInverse.png'], 1, 1, 1000, 32, 32)
                    return
                elif tile.name == "block":
                    playerPos = previouspos
                    tilePos = [tile.x*32, tile.y*32]
                    tileRect = pygame.Rect(tile.x*32, tile.y*32, 32, 32)
                    diff = (playerPos[0]-tilePos[0], playerPos[1]-tilePos[1])

                    # If x is larger than the y, then we know that it is a horizontal collision
                    if abs(diff[0]) > abs(diff[1]):
                        # If x is positive, then we reset player on the right of the tile
                        if  diff[0] > 0:
                            playerRect.left = tileRect.right
                        # Else if negative, we set the player left of the tile
                        elif diff[0] < 0:
                            playerRect.right = tileRect.left
                    # If y is larger than x, then there is a vertical collision
                    elif abs(diff[1]) > abs(diff[0]):
                        # If y is negative, then reset player on the top of the tile
                        # Note that this is opposite of x calclations because we have to keep
                        # in mind that y is reversed according to top left coordinates
                        if diff[1] < 0:
                            self.velocity[1] = 0
                            playerRect.bottom = tileRect.top
                            self.jumped = False
                        elif diff[1] > 0:
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

            for i in range(0, len(self.clouds.clouds)):
                self.screen.blit(AllSprites[self.clouds.clouds[i][3]], (self.clouds.clouds[i][0], self.clouds.clouds[i][1]))
        
            if self.left:
                for tile in self.currentTilesInverse:
                    tile.draw()

            else:
                for tile in self.currentTiles:
                    tile.draw()

            self.mainplayer.draw(self.screen, self.playerpos[0], self.playerpos[1])
        
        self.screenShaker.update()
        self.shakeScreen.blit(self.screen, self.screenShaker.getValue())
        pygame.display.update()
