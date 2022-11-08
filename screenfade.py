# -*- coding: utf-8 -*-
import pygame

class ScreenFade():
    def __init__(self, game, direction, colour, speed):
        self.direction = direction
        self.colour = colour
        self.speed = speed
        self.fade_counter = 0
        self.game = game


    def fade(self):
        self.fade_complete = False
        self.fade_counter += self.speed
        if self.direction == 1:#whole screen fade
            pygame.draw.rect(self.game.screen, self.colour, (0 - self.fade_counter, 0, self.game.SCREEN_WIDTH // 2, self.game.SCREEN_HEIGHT))
            pygame.draw.rect(self.game.screen, self.colour, (self.game.SCREEN_WIDTH // 2 + self.fade_counter, 0, self.game.SCREEN_WIDTH, self.game.SCREEN_HEIGHT))
            pygame.draw.rect(self.game.screen, self.colour, (0, 0 - self.fade_counter, self.game.SCREEN_WIDTH, self.game.SCREEN_HEIGHT // 2))
            pygame.draw.rect(self.game.screen, self.colour, (0,self.game. SCREEN_HEIGHT // 2 +self.fade_counter, self.game.SCREEN_WIDTH, self.game.SCREEN_HEIGHT))
        if self.direction == 2:#vertical screen fade down
            pygame.draw.rect(self.game.screen, self.colour, (0, 0, self.game.SCREEN_WIDTH, 0 + self.fade_counter))
        if self.fade_counter >= self.game.SCREEN_WIDTH:
            self.fade_complete = True

        return self.fade_complete

