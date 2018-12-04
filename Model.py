import pygame
from Sprite import Sprite
from Coin import Coin
class Model():
	def __init__(self):
		self.sprites = []
		self.camPos = 0
		self.marioRight = False
		self.marioLeft = False
		self.floorImage = pygame.image.load("dirtGround.png")
		self.bricks = pygame.transform.scale(self.floorImage, (100, 100))

	def set_dest(self, pos):
		pass

	def update(self):
		self.mario = self.sprites[0]
		for i in self.sprites:
			i.update()
			if(i.isBrick()):
				if(i.checkCollision(self, self.mario, i)):
					pass
			if(i.isCoinBlock()):
				if(i.checkCollision(self, self.mario, i)):
					pass

	def addCoin(self, x, y, w, h):
		self.sprites.append( Coin(x, y, w, h, self) )
	def removeCoin(self, coin):
		self.sprites.remove(coin)
