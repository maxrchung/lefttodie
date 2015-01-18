import pygame
from Animation import Animate
import Animation

w = 1280
h = 720
window = pygame.display.set_mode((w, h))

background_colour = (255, 255, 255)
#animator = Animate(Animation.AllSprites['playerIdleNormal.png'], 2, 2, 5, 32, 32)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit();
            sys.exit();

    window.fill(background_colour)
    pygame.display.update()


##player = Animate(AllSprites["playerMoveNormal.png"], 2, 2, 10, 32, 32)
##playerI = Animate(AllSprites["playerMoveInverse.png"], 2, 2, 10, 32, 32)
##
##
##
##
##
##x = 0
##y = 0
##
##w = 1280
##z = 720
##while True:
##    for event in pygame.event.get():
##        if event.type == pygame.QUIT:
##            pygame.quit();
##            sys.exit();
##                            
##    window.fill((255, 255, 255))
##    player.Aupdate()
##    player.draw(window, x,y)
##    playerI.Aupdate()
##    playerI.draw(window, w, z)
##    pygame.display.update()
##    x+= 3
##    y+= 3
##    w-= 3
##    z-= 3


class Screen:

    def __init__(self):
        pass

    def update(self):
        self.draw()

    def draw(self):
        animator.draw(screen, 100, 100)
