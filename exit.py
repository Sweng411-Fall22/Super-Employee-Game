# -*- coding: utf-8 -*-
import pygame 
import main

class Exit(pygame.sprite.Sprite):
	def __init__(self, img, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = img
		self.rect = self.image.get_rect()
		self.rect.midtop = (x + main.TILE_SIZE // 2, y + (main.TILE_SIZE - self.image.get_height()))

	def update(self):
		self.rect.x += main.screen_scroll

