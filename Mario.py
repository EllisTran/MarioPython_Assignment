from abc import ABCMeta, abstractmethod
from Sprite import Sprite
class Mario(Sprite):
    marioImagesRight = []
    marioImagesLeft= []
    def __init__(self, x, y, w, h, model):
        Sprite.__init__(self, x, y, w, h, model)        
        self.jumpFrame = 0
        self.prevX = 0
        self.prevY = 0
        self.coinPop = 0
        marioImages = None
    def isMario(self):
        return True
    def isBrick(self):
        return False
    def isCoinBlock(self):
        return False

    def prevDestination(self):
        self.prevX = self.x
        self.prevY = self.y
    def isCoin(self):
        return False
    def update(self):
        self.model.camPos = self.x - 200
        if self.y < 300:
            self.vert_vel +=2.1
            self.y += self.vert_vel

        if self.y >= 300:
            self.jumpFrame = 0
            self.y = 300
            self.vert_vel = 0.0
            self.coinPop = 0
        self.jumpFrame += 1
    