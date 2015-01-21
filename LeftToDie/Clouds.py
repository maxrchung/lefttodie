import random
from Animation import AllSprites

class Clouds:
    def __init__(self):
        self.cloudnum = random.randint(5,15)

        self.clouds = []
        self.cloudimages = []
        self.cloudsinverted = []
        
        for sprite, image in AllSprites.items():
            if "cloud" in sprite:
                if "Normal" in sprite:
                    self.cloudimages.append(sprite)
                elif "Inverse" in sprite:
                    self.cloudsinverted.append(sprite)

        for i in range(0, self.cloudnum):
            # Random width [0]
            # Random height [1]
            # Random speed [2]
            # Random normal cloud [3]
            self.clouds.append([random.randrange(100, 900),random.randrange(117, 500), random.randint(1,2), self.cloudimages[random.randint(0,len(self.cloudimages) - 1)]])

        self.cloudimages.sort()
        self.cloudsinverted.sort()
            
    def cloudupdate(self, inverted):       
        if inverted:
            for i in range(len(self.clouds)):
                self.clouds[i][0] += self.clouds[i][2]
                if self.clouds[i][0] - 100 > 1020:
                    self.clouds[i][0] = -100
                    self.clouds[i][1] = random.randrange(117, 500)
                    self.clouds[i][3] = self.cloudimages[random.randint(0, len(self.cloudsinverted) - 1)]

            for i in range(0, len(self.clouds)):
                if "Inverse" not in self.clouds[i][3]:
                    self.clouds[i][3] = self.cloudsinverted[int(self.clouds[i][3][5]) - 1]
        else:
            for i in range(len(self.clouds)):
                self.clouds[i][0] -= self.clouds[i][2]
                if self.clouds[i][0] + 100 < 0:
                    self.clouds[i][0] = 1020
                    self.clouds[i][1] = random.randrange(117, 500)
                    self.clouds[i][3] = self.cloudimages[random.randint(0, len(self.cloudimages) - 1)]

            for i in range(0, len(self.clouds)):
                if "Normal" not in self.clouds[i][3]:
                    self.clouds[i][3] = self.cloudimages[int(self.clouds[i][3][5]) - 1]

