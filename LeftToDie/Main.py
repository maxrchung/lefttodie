from GameManager import GameManager
import sys,pygame

game = GameManager("STARTSCREEN")

while game.go:
    game.run()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()