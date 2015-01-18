import pygame
from Animation import Animate
import Animation

screen = pygame.display.set_mode((1024, 768))
background_colour = (255, 255, 255)
screen.fill(background_colour)
pygame.display.set_caption('Left To Die')
animator = Animate(Animation.AllSprites['playerIdleNormal.png'], 2, 2, 5, 32, 32)


class Screen:

    def __init__(self):
        pass

    def update(self):
        self.draw()

    def draw(self):
        animator.draw(screen, 100, 100)
        pygame.display.update()