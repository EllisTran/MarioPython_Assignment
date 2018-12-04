import pygame
from abc import ABC, abstractmethod
#from Model import Model
class Sprite(ABC):
    def __init__(self,x, y,w, h, model):
        self.model = model
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.vert_vel = 0.0
    @abstractmethod
    def update(self):
        pass
    @abstractmethod
    def isMario(self):
        return False
    @abstractmethod
    def isBrick(self):
        return False

    @abstractmethod
    def isCoin(self):
        return False
    
    def checkCollision(self, model, mario, sprite):
        if (mario.x + mario.w < sprite.x):
            return False
        if (mario.x > sprite.x + sprite.w):      #Checks to see if Mario is colliding with the right side of the sprite
            return False
        if (mario.y + mario.h < sprite.y):     #Checks to see if Mario is colliding with the top of the sprite
            return False
        if (mario.y > sprite.y + sprite.h):     #Checks to see if Mario is colliding with the bottom of the sprite
            return False
        self.collisionHandler(model, mario, sprite)    #Calls Collision method if collision occurs
        return True

    def collisionHandler(self, model, mario, sprite):
        if (mario.x + mario.w >= sprite.x and mario.prevX + mario.w <= sprite.x):
            mario.x = sprite.x - mario.w -3
        elif (mario.x <= sprite.x + sprite.w and mario.prevX >= sprite.x + sprite.w):
            mario.x = sprite.x + sprite.w + 3
        elif (mario.y + mario.h > sprite.y and mario.prevY + mario.h <= sprite.y + sprite.h):
            mario.y = sprite.y - mario.h
            mario.jumpFrame = 0
            mario.vert_vel = 2.1
            mario.coinPop = 0
        elif (mario.y < sprite.y + sprite.h and mario.prevY >= sprite.h):
            mario.y = sprite.y + sprite.h 
            mario.vert_vel = 0.0
            if (sprite.isCoinBlock() and mario.coinPop == 0):
                mario.coinPop +=1
                sprite.coinLimit+=1
                if (sprite.coinLimit <=5):
                    model.addCoin(sprite.x, sprite.y, 75, 75)
                    
    
