import os, sys
import pygame
from pygame.locals import *


#Class to load spritesheet or parts of the spritesheet
class SpriteSheet(object):
    def __init__(self, file):
        try:
            self.sheet = pygame.image.load(os.path.join('Sprites', file)).convert()

        except pygame.error, message:
            print ('Unable to load spritesheet', file)
            raise SystemExit, message

    def crop(self, x, y, width, height):
        crop = pygame.Rect(x, y, width, height)
        sprite = pygame.Surface(crop.size).convert()
        sprite.blit(self.sheet, (0,0), crop)
        return sprite

    def sequence(self, rect, num_images):
        sprites = [(rect[0] + rect[2] * x, rect[1], rect[2], rect[3]) 
        
