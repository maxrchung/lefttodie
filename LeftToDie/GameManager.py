from ScreenManager import Screen


class GameManager:

    go = False
    state = ""
    screen = Screen()

    def __init__(self, state):
        self.go = True
        self.state = state

    def run(self):
        self.update()
        self.draw()

    def update(self):
        self.screen.draw()

    def draw(self):
        if self.state == "STARTSCREEN":
            print("I like pie")
        elif self.state == "LIFESCREEN":
            print("I Do not")
        elif self.state == "GAMESCREEN":
            print("Well you suck")
        elif self.state == "ENDSCREEN":
            print("At least I'm not Dead")

    def endGame(self):
        self.go = False

    def changeState(self, newState):
        self.state = newState