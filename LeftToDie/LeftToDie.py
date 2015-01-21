from ScreenManager import Screen
import Global
import sys,pygame

Global.Screen = Screen()

while Global.Screen.go:
    Global.Screen.update()
    Global.Screen.draw()
