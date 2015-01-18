from GameManager import GameManager
from soundmanager import soundmanager

import sys,pygame

game = GameManager("STARTSCREEN")
sm = soundmanager()

while game.go:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_1:
                sm.playsound("jump")
            elif event.key == pygame.K_2:
                sm.playsound("death")
            elif event.key == pygame.K_3:
                sm.playsound("levelDie")
            elif event.key == pygame.K_4:
                sm.playsound("levelUp")
            elif event.key == pygame.K_5:
                sm.playsound("inverse")
            elif event.key == pygame.K_6:
                sm.playsound("syobon")
