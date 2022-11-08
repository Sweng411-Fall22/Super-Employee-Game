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
            #check what kind of box it was
            if self.item_type == 'Health':
                self.game.player.health += 25
                if self.game.player.health > self.game.player.max_health:
                    self.game.player.health = self.game.player.max_health
            elif self.item_type == 'Ammo':
                self.game.player.ammo += 15
            elif self.item_type == 'Grenade':
                self.game.player.grenades += 3
            #delete the item box
            self.kill()

