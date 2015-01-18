from GameManager import GameManager

import sys,pygame

game = GameManager("STARTSCREEN")

while game.go:
    game.run()
