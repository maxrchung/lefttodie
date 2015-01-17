import pygame


class Screen:

    screen = pygame.display

    def __init__(self):
        self.screen = pygame.display.set_mode((1024, 768))

    def update(self):
        self.draw()

    def draw(self):
        print("I'm drawing")