import pygame
from random import randint

class ScreenShaker:
    def __init__(self):
        self.active = False
        self.intensity = 0
        self.length = 0
        self.value = (0,0)
        self.shakeClock = pygame.time.Clock()
        self.timePassed = 0

    def getValue(self):
        return self.value

    def update(self):
        if self.active:
            self.timePassed += self.shakeClock.tick()
            if self.timePassed >= self.length:
                self.active = False
                self.value = (0, 0)
            else:
                self.value = randint(-self.intensity, self.intensity), randint(-self.intensity, self.intensity)

    def shake(self, intensity, length):
        self.active = True
        self.intensity = intensity
        self.length = length
        self.shakeClock = pygame.time.Clock()
        self.timePassed = 0
