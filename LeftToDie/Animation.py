import os, sys
import pygame



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

    pos = [100, 600]

    def __init__(self, image, frames, columns, timer, imagew, imageh):

        #image = Spritesheet you wantto use from "AllSprites" dictionary. ex: AllSprites['playerIdleNormal.png]
        #frames = how many frames are in the sprite sheet. i put 2 for the regular walk, idle, etc
        #columns = how many sequences are in the actual sprite sheet. the playeridle and walk both have 2 different sprites on one row in their png file
        #timer = integer used to control how fast it loops through the animation
        #imagew = image width, the sprites for now are all 32 width
        #imageh = image height, the sprites for now are all 32 height
        
        try:
            self.image = image 
            self.frame = -1
            self.timer = timer
            self.frames = frames
            self.columns = columns
            self.clock = pygame.time.Clock()
            self.imagew = imagew
            self.imageh = imageh
            
        except pygame.error:
            print ('Unable to load images')
            raise SystemExit

    def Aupdate(self):
            self.frame += 1
            if self.frame > self.frames - 1:
                self.frame = 0

    def draw(self, win,  x, y):
        #x, y are where on the screen you want the sprite to draw
        win.blit(self.image, (x, y), ((self.frame % self.columns) * self.imagew, 0, self.imagew, self.imageh))
        self.clock.tick(self.timer)

SpriteSheet = SpriteSheets("Art")
AllSprites = SpriteSheet.loadAll()
