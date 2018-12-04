from abc import ABC, abstractmethod
from Sprite import Sprite
from Model import Model

class CoinBlock(Sprite):
    def __init__(self, x, y, w, h, model):
        Sprite.__init__(self, x, y, w, h, model)
        self.coinLimit = 0

    def update(self):
        pass
    
    def isMario(self):
        return False
    
    def isBrick(self):
        return False
    
    def isCoinBlock(self):
        return True
    def isCoin(self):
        return False