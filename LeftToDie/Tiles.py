import pygame
from Animation import Animate, AllSprites
import Tiles
class BlockTile:
    def __init__(self, x, y, screen, is_inverted): #x and y in grid both start at zero
        self.x = x
        self.y = y
        self.rectangle = pygame.Rect(x,y,32,32)
        self.screen = screen
        self.name = "block"
        self.is_inverted = is_inverted
        if self.is_inverted:
            self.image = AllSprites["tileBlockInverted.png"]
        else:
            self.image = AllSprites["tileBlockNormal.png"]

    def draw(self):
        self.screen.blit(self.image,(self.x*32,self.y*32))

class SpikeTile:
    def __init__(self, x, y, screen, is_inverted):
        self.x = x
        self.y = y
        self.rectangle = pygame.Rect(x,y,32,32)
        self.screen = screen
        self.is_inverted = is_inverted
        self.name = "spikes"
        if self.is_inverted:
            self.image = AllSprites["tileSpikeInverted.png"]
        else:
            self.image = AllSprites["tileSpikeNormal.png"]

    def draw(self):
         self.screen.blit(self.image,(self.x*32,self.y*32))


class EndTile:
    def __init__(self, x, y, screen, is_inverted):
        self.x = x
        self.y = y
        self.rectangle = pygame.Rect(x,y,32,32)
        self.screen = screen
        self.is_inverted = is_inverted
        self.name = "end"
        if self.is_inverted:
            self.image = AllSprites["tileEndInverse.png"]
        else:
            self.image = AllSprites["tileEndNormal.png"]
    def draw(self):
         self.screen.blit(self.image,(self.x*32,self.y*32))

class EmptyTile:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.name = "empty"

    def draw(self):
        pass

class TilesArray:
    def __init__(self, screen, mapfile):
        self.screen = screen
        self.mapfile = open(mapfile, 'r')
        self.tiles = []
        self.inverted_tiles = []
        self.startpos = [0,0]

    def make_tiles(self):
        x = 0
        y = 0
        lines = self.mapfile.readlines()
        for row in lines:
            for char in row:
                if char == "B":
                    self.tiles.append(BlockTile(x, y, self.screen, False)) #normal block tile
                elif char == "I":
                    self.startpos = [x*32, y*32]
                elif char == "S":
                    self.tiles.append(SpikeTile(x, y, self.screen, False)) #Spike tile
                elif char == "X":
                    self.tiles.append(EmptyTile(x, y)) #empty tile
                elif char == "V":
                    self.tiles.append(EndTile(x, y, self.screen, False)) #victory/end tile
                x+=1
            x = 0
            y+=1
            
    def make_inverse(self):
        x = 0
        y = 0
        for row in self.mapfile:
            for char in row:
                if char == "B":
                    self.inverted_tiles.append(SpikeTile(x, y, self.screen, True)) #normal block tile
                elif char == "S":
                    self.inverted_tiles.append(BlockTile(x, y, self.screen, True)) #Spike tile
                elif char == "X":
                    self.inverted_tiles.append(EmptyTile(x, y)) #empty tile
                elif char == "V":
                    self.inverted_tiles.append(EndTile(x, y, self.screen, True)) #victory/end tile
                x+=1
            x = 0
            y+=1

