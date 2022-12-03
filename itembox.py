# -*- coding: utf-8 -*-
import pygame

class ItemBox(pygame.sprite.Sprite):
    def __init__(self, game, item_type, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.item_type = item_type
        self.image = self.game.item_boxes[self.item_type]
        self.rect = self.image.get_rect()
        self.rect.midtop = (x + self.game.TILE_SIZE // 2, y + (self.game.TILE_SIZE - self.image.get_height()))


    def update(self):
        #scroll
        self.rect.x += self.game.screen_scroll
        #check if the player has picked up the box
        if pygame.sprite.collide_rect(self, self.game.player):
            self.game.player_score += 5
            self.game.score.prep_score()
            #check what kind of box it was
            if self.item_type == 'Coin':
                self.game.player.grenades += 3
            #delete the item box
            self.kill()

