from ScreenManager import Screen
import Global
import sys,pygame

Global.Screen = Screen()
framerateClock = pygame.time.Clock()

while Global.Screen.go:
    framerateClock.tick(60)
    Global.Screen.update()
    Global.Screen.draw()
