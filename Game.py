import pygame
import time
from Model import Model
from Mario import Mario
from Brick import Brick
from CoinBlock import CoinBlock
from View import View
from Sprite import Sprite
from Coin import Coin
from Controller import Controller
from Sprite import Sprite
from pygame.locals import*
from time import sleep


pygame.init()
m = Model()
v = View(m)
mario = Mario(400, 0, 60, 95, m)
m.sprites.append(mario)
c = Controller(m)
for i in range(10):
	brick = Brick(500*i, 300, 100, 100, m)
	coinBlockUp = CoinBlock(500*i, 0, 100, 100, m)
	coinBlockDown = CoinBlock( 250 + (500*i), 150, 89, 86, m)
	m.sprites.append(brick)
	m.sprites.append(coinBlockUp)
	m.sprites.append(coinBlockDown)
	
while c.keep_going:
	c.update()
	m.update()
	v.update()
	sleep(0.04)
print("Goodbye")