import pygame

class soundmanager():
    def __init__(self):
        pygame.mixer.init(frequency = 441100, size = -16, channels = 2, buffer = 4096)

        backmusic = pygame.mixer.music.load("")

        pygame.mixer.music.play(-1)

    def playsound(self, soundname):
        if soundname == "jump":
            sound = pygame.mixer.Sound("")
            sound.play()
        elif soundname == "death":
            sound = pygame.mixer.Sound("")
            sound.play()
        elif soundname == "win":
            sound = pygame.mixer.Sound("")
            sound.play()
        elif soundname == "inverse":
            sound = pygame.mixer.Sound("")
            sound.play()
        else:
            print("Can't locate sound file.")
