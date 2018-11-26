import pygame
import time
from Model import Model
from View import View
from Controller import Controller
from Sprite import Sprite
from pygame.locals import*
from time import sleep


pygame.init()
m = Model()
v = View(m)
c = Controller(m)
while c.keep_going:
	c.update()
	m.update()
	v.update()
	sleep(0.04)
print("Goodbye")

print("LALALA")