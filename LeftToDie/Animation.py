import os, sys
import pygame
#import window
#from pygame.locals import *


#Class to load spritesheet or parts of the spritesheet
class SpriteSheets():
    def __init__(self, folder):
        try:
            self.folder = folder
            os.path.isdir(self.folder)

        except pygame.error:
            print ('Unable to load art folder', folder)
            raise SystemExit

    def load(self, image):
        self.sheet = pygame.image.load(os.path.join(self.folder, image))

    def loadAll(self):
        self.all = {}
        for root, dirs, files in os.walk(self.folder):
           for image in files:
               if image[-3:] == "png":
                   self.all[image] = pygame.image.load(os.path.join(self.folder, image))
        return self.all

#animate sprites
class Animate():
    def __init__(self, image, frames, columns, timer):
        try:
            self.image = image
            self.frame = -1
            self.timer = timer
            self.frames = frames
            self.columns = columns
            self.clock = pygame.time.Clock()
            
        except pygame.error:
            print ('Unable to load images')
            raise SystemExit

    def Aupdate(self):
            self.frame += 1
            if self.frame > self.frames - 1:
                self.frame = 0

    def draw(self):
        window.blit(self.image, (0, 0), ((self.frame % self.columns) * w, 0, w, h))
        pygame.display.update()
        self.clock.tick(self.timer)

player = Animate(a["playerIdleNormal.png"], 2, 2, 5)

w = 32
h = 32
window = pygame.display.set_mode((w, h))


SpriteSheet = SpriteSheets("Art")
AllSprites = SpriteSheet.loadAll()

window.fill((255, 255, 255))



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit();
            sys.exit();
                            
    
    player.Aupdate()
    player.draw()
