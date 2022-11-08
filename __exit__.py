# -*- coding: utf-8 -*-
import pygame 

class Exit(pygame.sprite.Sprite):
    def __init__(self, game, img, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.midtop = (x + self.game.TILE_SIZE // 2, y + (self.game.TILE_SIZE - self.image.get_height()))

    def update(self):
        self.rect.x += self.game.screen_scroll

