import pygame
class View():
	def __init__(self, model):
		screen_size = (800, 600)		#Sets screen size
		self.screen = pygame.display.set_mode(screen_size, 32)

		#Initializes the lists for Mario moving left and right
		self.marioImagesRight = []
		self.marioImagesLeft = []
		self.marioImagesLeftArray =  ["mariobackwards1.png","mariobackwards2.png","mariobackwards3.png","mariobackwards4.png","mariobackwards5.png",]
		self.marioImagesRightArray = ["mariofrontwards1.png", "mariofrontwards2.png", "mariofrontwards3.png", "mariofrontwards4.png", "mariofrontwards5.png"]
		#Loads the images from the above arrays to each appropriate array slot
		for i in range(4):
			self.marioImagesRight.append(pygame.image.load(self.marioImagesRightArray[i]))
			self.marioImagesLeft.append(pygame.image.load(self.marioImagesLeftArray[i]))

		#Loads the initial Mario, ground, background, coin blocks, coins, and brick images
		self.marioImage = pygame.image.load("mariofrontwards1.png")
		self.floorImage = pygame.image.load("dirtGround.png")
		self.floorImage = pygame.transform.scale(self.floorImage, (2000, 1000))
		self.coinBlock = pygame.image.load("coinblock1.png")
		self.coinBlockEmpty = pygame.image.load("emptycoinblock.png")
		self.coins = pygame.image.load("coin.png")
		self.bricks = pygame.transform.scale(self.floorImage, (100, 100))
		self.backgroundImage = pygame.image.load("Background.png")

		self.cycle = 0			#Cycles through the pictures
		self.model = model
		self.switching = -1		#Allows for Mario to switch
		
	#Update Method
	def update(self):
		self.screen.fill([0, 200, 100])
		self.mario = self.model.sprites[0]
		for i in range(5):
			self.screen.blit(self.backgroundImage,[ 20 - (i * 1800) - (self.model.camPos /10), 0])
			self.screen.blit(self.floorImage, [(i * 1800) - (self.model.camPos/5), 400])

		#	brick= Brick(500*i, 300, 100, 100)
		for i in range(self.model.sprites.__len__()):
			s = self.model.sprites[i]
			if(s.isBrick()):
				self.screen.blit(self.bricks, [s.x - self.model.camPos, s.y])
			if(s.isCoinBlock()):
				if(s.coinLimit < 5):
					self.screen.blit(self.coinBlock, [s.x - self.model.camPos, s.y])
				else:
					self.screen.blit(self.coinBlockEmpty, [s.x - self.model.camPos, s.y])
			if (s.isMario()):
				if (self.switching == -1):
					self.screen.blit(self.marioImagesRight[self.cycle], (self.mario.x - self.model.camPos, self.mario.y))
				if (self.model.marioRight):
					self.screen.blit(self.marioImagesRight[self.cycle], (self.mario.x - self.model.camPos, self.mario.y))
					self.cycle +=1
					if (self.cycle == 4):
						self.cycle = 0
					self.switching = 0
				elif (self.model.marioLeft):
					self.screen.blit(self.marioImagesLeft[self.cycle], (self.mario.x - self.model.camPos, self.mario.y))
					self.cycle +=1
					if (self.cycle == 4):
						self.cycle = 0
					self.switching = 1
				elif (self.switching ==0):
					self.screen.blit(self.marioImagesRight[self.cycle], (self.mario.x - self.model.camPos, self.mario.y))
				elif (self.switching == 1):
					self.screen.blit(self.marioImagesLeft[self.cycle], (self.mario.x - self.model.camPos, self.mario.y))
			if (s.isCoin()):
				self.screen.blit(self.coins,[ s.x - self.model.camPos, s.y])
		pygame.display.flip()


