from abc import ABC, abstractmethod
from Sprite import Sprite
#from Model import Model
import random
class Coin(Sprite):
    def __init__(self, x, y, w, h, model):
        Sprite.__init__(self, x, y, w, h, model)
        self.moveCoinX = random.randint(1, 10)
        self.vert_vel = -20.0
    def isMario(self):
        return False
    def isBrick(self):
        return False
    def isCoinBlock(self):
        return False
    def isCoin(self):
        return True

    def update(self):
        self.vert_vel += 1.7
        self.y += self.vert_vel

        self.vert_vel += 3.1

        self.y += self.vert_vel

        if (self.moveCoinX <= 5):
            self.x += self.moveCoinX+5
        else:
            self.x -= self.moveCoinX
        if (self.y >= 300):
            self.model.removeCoin(self)