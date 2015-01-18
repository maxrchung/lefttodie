import pygame

class soundmanager():
    def __init__(self):
        # Preload sounds so we don't run into processing issues
        self.syobon = pygame.mixer.music.load("Sounds/syobon.mp3")
        # Loop music
        pygame.mixer.music.play(-1)

        self.jumpSound = pygame.mixer.Sound("Sounds/jump.wav")
        self.jumpSound.set_volume(0.5)
        self.deathSound = pygame.mixer.Sound("Sounds/death.wav")
        self.deathSound.set_volume(0.5)
        self.victorySound = pygame.mixer.Sound("Sounds/victory.wav")
        self.victorySound.set_volume(0.5)
        self.levelDieSound = pygame.mixer.Sound("Sounds/levelDie.wav")
        self.levelDieSound.set_volume(0.5)
        self.levelUpSound = pygame.mixer.Sound("Sounds/levelUp.wav")
        self.levelUpSound.set_volume(0.5)
        self.inverseSound = pygame.mixer.Sound("Sounds/inverse.wav")
        self.inverseSound.set_volume(0.5)

    def playsound(self, soundname):
        if soundname == "jump":
            self.jumpSound.play()
        elif soundname == "death":
            self.deathSound.play()
        elif soundname == "victory":
            self.victorySound.play()
        elif soundname == "levelDie":
            self.levelDieSound.play()
        elif soundname == "levelUp":
            self.levelUpSound.play()
        elif soundname == "inverse":
            self.inverseSound.play(-1)
            pygame.mixer.music.pause()
        elif soundname == "syobon":
            self.inverseSound.stop()
            pygame.mixer.music.unpause()
        else:
            print("Can't locate sound file.")
