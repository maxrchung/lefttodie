import os, sys
import pygame
from pygame.locals import *


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
        


w = 32
h = 32
window = pygame.display.set_mode((w, h))
frame = -1
clock = pygame.time.Clock()
columns = 2

s = SpriteSheets("Art")
#s.load("playerIdleNormal.png")
a = s.loadAll()
print(a)
a["playerIdleNormal.png"]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit();
            sys.exit();
    window.fill((255, 255, 255))
    frame += 1;
    if frame > 1:
        frame = 0

    window.blit(a["playerIdleNormal.png"], (0, 0), ((frame % columns) * w, 0, w, h))
    pygame.display.update()
    clock.tick(5)

class Animate():
    def __init__(self, image):
        try:
            self.image = image
            self.frame = -1
            
        except pygame.error:
            print ('Unable to load images')
            raise SystemExit

    def Aupdate(self, frames, columns, int timer):
            self.frame += 1
            if self.frame > frames - 1:
                self.frame = 0

            window.blit(a["playerIdleNormal.png"], (0, 0), ((self.frame % columns) * w, 0, w, h))
            pygame.display.update()
            clock.tick(timer)

    def draw(self):
        pass
