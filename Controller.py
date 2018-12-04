import pygame
import time
from View import View
from Sprite import Sprite
from Mario import Mario
from pygame.locals import*
from time import sleep

class Controller():
	def __init__(self, model):
		self.model = model
		self.keep_going = True
		self.Mario = self.model.sprites[0]
	def update(self):
		self.Mario.prevDestination()
		for event in pygame.event.get():
			if event.type == QUIT:
				self.keep_going = False
			elif event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					self.keep_going = False
				if event.key == K_LEFT:
					self.model.marioLeft = True
				if event.key == K_RIGHT:
					self.model.marioRight = True
			elif event.type == pygame.MOUSEBUTTONUP:
				self.model.set_dest(pygame.mouse.get_pos())
			elif event.type == KEYUP:
				if event.key == K_RIGHT:
					self.model.marioRight = False
				if event.key == K_LEFT:
					self.model.marioLeft = False
		keys = pygame.key.get_pressed()
		if keys[K_LEFT]:
			self.Mario.x -= 10
		if keys[K_RIGHT]:
			self.Mario.x += 10
		if keys[K_SPACE]:
			if self.Mario.jumpFrame < 5:
				self.Mario.vert_vel -= 8.0
				self.Mario.y += self.Mario.vert_vel
		if keys[K_DOWN]:
			self.Mario.y += 10