from abc import ABCMeta, abstractmethod
from Sprite import Sprite

class Brick(Sprite):
    def __init__(self,x, y, w, h, model):
        Sprite.__init__(self,x,y,w,h, model)
    def isMario(self):
        return False
    def isBrick(self):
        return True
    def update(self):
        pass
    def isCoinBlock(self):
        return False
    def isCoin(self):
        return False