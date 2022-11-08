# -*- coding: utf-8 -*-
import pygame 
import explosion as exp

class Grenade(pygame.sprite.Sprite):
    def __init__(self, game, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.timer = 100
        self.vel_y = -11
        self.speed = 7
        self.image = self.game.grenade_img
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.direction = direction

    def update(self):
        self.vel_y += self.game.GRAVITY
        dx = self.direction * self.speed
        dy = self.vel_y

        #check for collision with level
        for tile in self.game.world.obstacle_list:
            #check collision with walls
            if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                self.direction *= -1
                dx = self.direction * self.speed
            #check for collision in the y direction
            if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                self.speed = 0
                #check if below the ground, i.e. thrown up
                if self.vel_y < 0:
                    self.vel_y = 0
                    dy = tile[1].bottom - self.rect.top
                #check if above the ground, i.e. falling
                elif self.vel_y >= 0:
                    self.vel_y = 0
                    dy = tile[1].top - self.rect.bottom    


        #update grenade position
        self.rect.x += dx + self.game.screen_scroll
        self.rect.y += dy

        #countdown timer
        self.timer -= 1
        if self.timer <= 0:
            self.kill()
            self.game.grenade_fx.play()
            explosion = exp.Explosion(self.game, self.rect.x, self.rect.y, 0.5)
            self.game.explosion_group.add(explosion)
            #do damage to anyone that is nearby
            if abs(self.rect.centerx - self.game.player.rect.centerx) < self.game.TILE_SIZE * 2 and \
                abs(self.rect.centery - self.game.player.rect.centery) < self.game.TILE_SIZE * 2:
                self.game.player.health -= 50
            for enemy in self.game.enemy_group:
                if abs(self.rect.centerx - enemy.rect.centerx) < self.game.TILE_SIZE * 2 and \
                    abs(self.rect.centery - enemy.rect.centery) < self.game.TILE_SIZE * 2:
                    enemy.health -= 50


