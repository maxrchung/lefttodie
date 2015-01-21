class BackObjects:
    def __init__(self):
        self.width = 1022
        self.speedf = 5
        self.speedb = 2.5
        self.min = -self.width
        self.max = self.width

        self.fskyx = 0
        self.bskyx = 0
        self.fhillx = 0
        self.bhillx = 0

        self.fskyx2 = self.width
        self.bskyx2 = self.width
        self.fhillx2 = self.width
        self.bhillx2 = self.width

    def backupdate(self, inverse):
        if inverse:
            self.fskyx += self.speedf
            self.bskyx += self.speedb
            self.fhillx += self.speedf
            self.bhillx += self.speedb

            if self.fskyx > self.width:
                self.fskyx = self.min + 5

            if self.bskyx > self.width:
                self.bskyx = self.min

            if self.bhillx > self.width:
                self.bhillx = self.min

            if self.fhillx > self.width:
                self.fhillx = self.min + 5
            
            self.fskyx2 += self.speedf
            self.bskyx2 += self.speedb
            self.fhillx2 += self.speedf
            self.bhillx2 += self.speedb

            if self.fskyx2 > self.width:
                self.fskyx2 = self.min + 5

            if self.bskyx2 > self.width:
                self.bskyx2 = self.min

            if self.bhillx2 > self.width:
                self.bhillx2 = self.min

            if self.fhillx2 > self.width:
                self.fhillx2 = self.min + 5

        else:
            self.bskyx -= self.speedb
            self.fskyx -= self.speedf
            self.fhillx -= self.speedf
            self.bhillx -= self.speedb

            if self.fskyx < -self.width:
                self.fskyx = self.max - 5

            if self.bskyx < -self.width:
                self.bskyx = self.max

            if self.bhillx < -self.width:
                self.bhillx = self.max

            if self.fhillx < -self.width:
                self.fhillx = self.max - 5
                
            self.fskyx2 -= self.speedf
            self.bskyx2 -= self.speedb
            self.fhillx2 -= self.speedf
            self.bhillx2 -= self.speedb

            if self.fskyx2 < -self.width:
                self.fskyx2 = self.max - 5

            if self.bskyx2 < -self.width:
                self.bskyx2 = self.max

            if self.bhillx2 < -self.width:
                self.bhillx2 = self.max

            if self.fhillx2 < -self.width:
                self.fhillx2 = self.max - 5
