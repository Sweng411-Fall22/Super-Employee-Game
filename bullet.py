# -*- coding: utf-8 -*-
import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, game, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.speed = 10
        self.image = self.game.bullet_img
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.direction = direction

    def update(self):
        #move bullet
        self.rect.x += (self.direction * self.speed) + self.game.screen_scroll
        #check if bullet has gone off screen
        if self.rect.right < 0 or self.rect.left > self.game.SCREEN_WIDTH:
            self.kill()
        #check for collision with level
        for tile in self.game.world.obstacle_list:
            if tile[1].colliderect(self.rect):
                self.kill()

        #check collision with characters
        if pygame.sprite.spritecollide(self.game.player, self.game.bullet_group, False):
            if self.game.player.alive:
                self.game.player.health -= 5
                self.kill()
        for enemy in self.game.enemy_group:
            if pygame.sprite.spritecollide(enemy, self.game.bullet_group, False):
                if enemy.alive:
                    enemy.health -= 25
                    self.kill()


