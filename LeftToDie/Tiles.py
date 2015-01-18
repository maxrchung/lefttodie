import pygame
import Animation
class BlockTile:
    def __init__(self, x, y, screen, is_inverted): #x and y in grid both start at zero
        self.x = x
        self.y = y
        self.screen = screen
        self.is_inverted = is_inverted
        if self.is_inverted:
            self.image = AllSprites["tileBlockInverted.png"]
        else:
            self.image = AllSprites["tileBlockNormal.png"]

        self.screen.blit(self.image,(x*32,y*32))

    def invert(self):
        SpikeTile(self.x,self.y,self.screen, !self.is_inverted)

class SpikeTile:
    def __init__(self, x, y, screen, is_inverted):
        self.x = x
        self.y = y
        self.screen = screen
        self.is_inverted = is_inverted
        if self.is_inverted:
            self.image = AllSprites["tileSpikeInverted.png"]
        else:
            self.image = AllSprites["tileSpikeNormal.png"]

        self.screen.blit(self.image, x*32, y*32)
    def invert(self):
        BlockTile(self.x, self.y, self.screen, !self.is_inverted)

class EndTile:
    def __init__(self, x, y, screen, is_inverted):
        self.x = x
        self.y = y
        self.screen = screen
        self.is_inverted = is_inverted
        if self.is_inverted:
            self.image = AllSprites["tileEndInverse.png"]
        else:
            self.image = AllSprites["tileEndNormal.png"]
    def invert(self):
        BlockTile(self, self.x, self.y, self.screen, !self.is_inverted)

class EmptyTile:
    def __init__(self,x,y):
        self.x = x
        self.y = y


class TilesArray:
    def __init__(self, screen, mapfile):
        self.screen = screen
        self.mapfile = map.open(mapfile, 'w')
        self.matrix = []

    def make_tiles(self):
        x = 0
        y = 0
        for row in self.mapfile:
            self.matrix.append([])
            for char in row:
                if char == "B":
                    self.matriz[y].append(BlockTile())
                elif char == "S":
                    self.matrix[y].append(SpikeTile())
                elif char == "X":
                    self.matrix[y].append(EmptyTile())
                elif char == "V":
                    self.matrix[y].append(EndTile())





