# -*- coding: utf-8 -*-
import pygame
import water as wt
import decoration as dec
import soldier as sol
import healthbar as hb
import itembox as ib
import __exit__ as ex

class World():
    def __init__(self, game):
        self.obstacle_list = []
        self.game = game

    def process_data(self, data):
        self.level_length = len(data[0])
        #iterate through each value in level data file
        for y, row in enumerate(data):
            for x, tile in enumerate(row):
                if tile >= 0:
                    img = self.game.img_list[tile]
                    img_rect = img.get_rect()
                    img_rect.x = x * self.game.TILE_SIZE
                    img_rect.y = y * self.game.TILE_SIZE
                    tile_data = (img, img_rect)
                    if tile >= 0 and tile <= 1:
                        self.obstacle_list.append(tile_data)
                    elif tile >= 2 and tile <= 3:
                        water = wt.Water(self.game, img, x * self.game.TILE_SIZE, y * self.game.TILE_SIZE)
                        self.game.water_group.add(water)
                    elif tile == 4:#create player
                        player = sol.Soldier(self.game, 'player', x * self.game.TILE_SIZE, y * self.game.TILE_SIZE, 1.65, 5, 20, 5)
                        health_bar = hb.HealthBar(self.game, 10, 10, player.health, player.health)
                    elif tile == 5:#create enemies
                        enemy = sol.Soldier(self.game, 'enemy', x * self.game.TILE_SIZE, y * self.game.TILE_SIZE, 1.65, 2, 20, 0)
                        self.game.enemy_group.add(enemy)
                    elif tile == 6:#create coin
                        item_box = ib.ItemBox(self.game, 'Coin', x * self.game.TILE_SIZE, y * self.game.TILE_SIZE)
                        self.game.item_box_group.add(item_box)
                    elif tile == 7:#create exit
                        __exit = ex.Exit(self.game, img, x * self.game.TILE_SIZE, y * self.game.TILE_SIZE)
                        self.game.exit_group.add(__exit)

        return player, health_bar


    def draw(self):
        for tile in self.obstacle_list:
            tile[1][0] += self.game.screen_scroll
            self.game.screen.blit(tile[0], tile[1])
