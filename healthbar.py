# -*- coding: utf-8 -*-
import pygame

class HealthBar():
    def __init__(self, game, x, y, health, max_health):
        self.x = x
        self.y = y
        self.health = health
        self.max_health = max_health
        self.game = game

    def draw(self, health):
        #update with new health
        self.health = health
        #calculate health ratio
        ratio = self.health / self.max_health
        pygame.draw.rect(self.game.screen, self.game.WHITE, (self.x, self.y + 6, 154, 24))
        pygame.draw.rect(self.game.screen, self.game.RED, (self.x + 2, self.y + 8, 150, 20))
        pygame.draw.rect(self.game.screen, self.game.GREEN, (self.x + 2, self.y + 8, 150 * ratio, 20))

