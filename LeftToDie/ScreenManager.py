import pygame


class Screen:

    pygame.init()
    screen = pygame.display
    background_colour = (255, 255, 255)

    def __init__(self):
        self.screen = pygame.display.set_mode((1024, 768))
        pygame.display.set_caption('Left To Die')

    def update(self):
        self.draw()

    def draw(self):
        print("Hello")