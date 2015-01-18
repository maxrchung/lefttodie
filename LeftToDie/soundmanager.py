import pygame

class soundmanager():
    def __init__(self):
        pygame.mixer.init(frequency = 441100, size = -16, channels = 2, buffer = 4096)

        # Preload sounds so we don't run into processing issues
        self.syobon = pygame.mixer.music.load("Sounds/syobon.mp3")
        self.jumpSound = pygame.mixer.Sound("Sounds/jump.wav")
        self.deathSound = pygame.mixer.Sound("Sounds/death.wav")
        self.levelDieSound = pygame.mixer.Sound("Sounds/levelDie.wav")
        self.levelDieSound = pygame.mixer.Sound("Sounds/levelUp.wav")
        self.inverseSound = pygame.mixer.Sound("Sounds/inverse.wav")

        # Loop music
        pygame.mixer.music.play(-1)

    def playsound(self, soundname):
        if soundname == "jump":
            self.jumpSound.play()
        elif soundname == "death":
            self.deathSound.play()
        elif soundname == "levelDie":
            self.levelDieSound.play()
        elif soundname == "levelUp":
            self.levelUpSound.play()
        elif soundname == "inverse":
            self.inverseSound.play(-1)
            pygame.mixer.music.pause()
        elif soundname == "syobon":
            self.inverseSound.stop()
            pygame.mixer.music.play(-1)
        else:
            print("Can't locate sound file.")
