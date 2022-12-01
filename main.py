import pygame
from pygame import mixer
import os
import random
import csv
import button
import screenfade as sf
import world as wr
import grenade as gr
import score as Score

class GameMain:
    
    def __init__(self):
        mixer.init()
        pygame.init()
        
        ' SCREEN SETTINGS '
        self.SCREEN_WIDTH = 800
        self.SCREEN_HEIGHT = int(self.SCREEN_WIDTH * 0.8)
        
        self.clock = pygame.time.Clock()
        self.FPS = 60
        
        ' GAME VARIABLES '
        self.GRAVITY = 0.75
        self.SCROLL_THRESH = 200
        self.ROWS = 16
        self.COLS = 150
        self.TILE_SIZE = self.SCREEN_HEIGHT // self.ROWS
        self.TILE_TYPES = 21
        self.MAX_LEVELS = 3
        self.screen_scroll = 0
        self.bg_scroll = 0
        self.level = 1
        self.start_game = False
        self.start_intro = False
        self.menu_state = "main"
        
        
        ' PLAYER VARIABLES '
        self.moving_left = False
        self.moving_right = False
        self.shoot = False
        self.grenade = False
        self.grenade_thrown = False
        self.player_score = 0
        
        
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption('Super Employee Game')
        self.score = Score.Score(self)
        
        
        
        #load music and sounds
        #pygame.mixer.music.load('audio/music2.mp3')
        #pygame.mixer.music.set_volume(0.3)
        #pygame.mixer.music.play(-1, 0.0, 5000)
        self.jump_fx = pygame.mixer.Sound('audio/jump.wav')
        self.jump_fx.set_volume(0.05)
        self.shot_fx = pygame.mixer.Sound('audio/shot.wav')
        self.shot_fx.set_volume(0.05)
        self.grenade_fx = pygame.mixer.Sound('audio/grenade.wav')
        self.grenade_fx.set_volume(0.05)

        #game title image
        self.gametitle_img = pygame.image.load('img/gametitle.png')
        #use to manually re-size image:
        #self.gametitle_img = pygame.transform.scale(self.gametitle_img, (self.gametitle_img.get_width(), self.gametitle_img.get_height()))
        
        #load images
        #button images
        self.start_img = pygame.image.load('img/start_btn.png').convert_alpha()
        self.exit_img = pygame.image.load('img/exit_btn.png').convert_alpha()
        self.restart_img = pygame.image.load('img/restart_btn.png').convert_alpha()
        self.back_img = pygame.image.load('img/back_btn.png').convert_alpha()
        self.settings_img = pygame.image.load('img/settings_btn.png').convert_alpha()
        self.scoreboard_img = pygame.image.load('img/scoreboard_btn.png').convert_alpha()
        self.high_img = pygame.image.load('img/high_btn.png').convert_alpha()
        self.low_img = pygame.image.load('img/low_btn.png').convert_alpha()
        self.off_img = pygame.image.load('img/off_btn.png').convert_alpha()
        
        #background
        self.pine1_img = pygame.image.load('img/Background/pine1.png').convert_alpha()
        self.pine2_img = pygame.image.load('img/Background/pine2.png').convert_alpha()
        self.mountain_img = pygame.image.load('img/Background/mountain.png').convert_alpha()
        self.sky_img = pygame.image.load('img/Background/sky_cloud.png').convert_alpha()
        
        #store tiles in a list
        self.img_list = []
        for x in range(self.TILE_TYPES):
            self.img = pygame.image.load(f'img/Tile/{x}.png')
            self.img = pygame.transform.scale(self.img, (self.TILE_SIZE, self.TILE_SIZE))
            self.img_list.append(self.img)
        #bullet
        self.bullet_img = pygame.image.load('img/icons/bullet.png').convert_alpha()
        #grenade
        self.grenade_img = pygame.image.load('img/icons/grenade.png').convert_alpha()
        #pick up boxes
        self.health_box_img = pygame.image.load('img/icons/health_box.png').convert_alpha()
        self.ammo_box_img = pygame.image.load('img/icons/ammo_box.png').convert_alpha()
        self.grenade_box_img = pygame.image.load('img/icons/grenade_box.png').convert_alpha()
        self.item_boxes = {
            'Health'    : self.health_box_img,
            'Ammo'        : self.ammo_box_img,
            'Grenade'    : self.grenade_box_img
        }
        
        
        #define colours
        self.BG = (144, 201, 120)
        self.RED = (255, 0, 0)
        self.WHITE = (255, 255, 255)
        self.GREEN = (0, 255, 0)
        self.BLACK = (0, 0, 0)
        self.PINK = (235, 65, 54)
        
        #define font
        self.font = pygame.font.Font('font/ARCADECLASSIC.TTF', 30)
        
        #create screen fades
        self.intro_fade = sf.ScreenFade(self, 1, self.BLACK, 4)
        self.death_fade = sf.ScreenFade(self, 2, self.PINK, 4)

        #create buttons
        self.start_button = button.Button(self.SCREEN_WIDTH // 2 - 92, self.SCREEN_HEIGHT // 2 - 60, self.start_img, 0.7)
        self.scoreboard_button = button.Button(self.SCREEN_WIDTH // 2 - 170, self.SCREEN_HEIGHT // 2 + 20, self.scoreboard_img, 1)
        self.settings_button = button.Button(self.SCREEN_WIDTH // 2 - 118, self.SCREEN_HEIGHT // 2 + 100, self.settings_img, 0.7)
        self.exit_button = button.Button(self.SCREEN_WIDTH // 2 - 78, self.SCREEN_HEIGHT // 2 + 180, self.exit_img, 0.7)
        self.restart_button = button.Button(self.SCREEN_WIDTH // 2 - 100, self.SCREEN_HEIGHT // 2 - 50, self.restart_img, 2)
        self.back_button = button.Button(self.SCREEN_WIDTH - 120, self.SCREEN_HEIGHT // 100, self.back_img, 0.5)
        self.sfx_high_button = button.Button(self.SCREEN_WIDTH - 275, self.SCREEN_HEIGHT // 2 - 180, self.high_img, 1)
        self.sfx_low_button = button.Button(self.SCREEN_WIDTH - 475, self.SCREEN_HEIGHT // 2 - 180, self.low_img, 1)
        self.sfx_off_button = button.Button(self.SCREEN_WIDTH - 675, self.SCREEN_HEIGHT // 2 - 180, self.off_img, 1)

        #create sprite groups
        self.enemy_group = pygame.sprite.Group()
        self.bullet_group = pygame.sprite.Group()
        self.grenade_group = pygame.sprite.Group()
        self.explosion_group = pygame.sprite.Group()
        self.item_box_group = pygame.sprite.Group()
        self.decoration_group = pygame.sprite.Group()
        self.water_group = pygame.sprite.Group()
        self.exit_group = pygame.sprite.Group()
        
            
        #create empty tile list
        self.world_data = []
        for row in range(self.ROWS):
            r = [-1] * self.COLS
            self.world_data.append(r)
        #load in level data and create world
        with open(f'level{self.level}_data.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for x, row in enumerate(reader):
                for y, tile in enumerate(row):
                    self.world_data[x][y] = int(tile)
        self.world = wr.World(self)
        self.player, self.health_bar = self.world.process_data(self.world_data)
    
    
        
    
    def draw_text(self, text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        self.screen.blit(img, (x, y))
    
    
    def draw_bg(self):
        self.screen.fill(self.BG)
        width = self.sky_img.get_width()
        for x in range(5):
            self.screen.blit(self.sky_img, ((x * width) - self.bg_scroll * 0.5, 0))
            self.screen.blit(self.mountain_img, ((x * width) - self.bg_scroll * 0.6, self.SCREEN_HEIGHT - self.mountain_img.get_height() - 300))
            self.screen.blit(self.pine1_img, ((x * width) - self.bg_scroll * 0.7, self.SCREEN_HEIGHT - self.pine1_img.get_height() - 150))
            self.screen.blit(self.pine2_img, ((x * width) - self.bg_scroll * 0.8, self.SCREEN_HEIGHT - self.pine2_img.get_height()))
    
    
    #function to reset level
    def reset_level(self):
        self.enemy_group.empty()
        self.bullet_group.empty()
        self.grenade_group.empty()
        self.explosion_group.empty()
        self.item_box_group.empty()
        self.decoration_group.empty()
        self.water_group.empty()
        self.exit_group.empty()
        
    
        #create empty tile list
        data = []
        for row in range(self.ROWS):
            r = [-1] *self. COLS
            data.append(r)
    
        return data
    
    
    def runGame(self):
        self.run = True
        while self.run:
        
            self.clock.tick(self.FPS)
        
            if self.start_game == False:
                #draw menu
                self.screen.fill(self.BG)
                
                # check menu state
                # main menu
                if self.menu_state == "main":
                    #show game title image
                    self.screen.blit(self.gametitle_img, (self.SCREEN_WIDTH // 2 - 210, self.SCREEN_HEIGHT // 2 - 275))
                    #draw main menu screen buttons
                    if self.start_button.draw(self.screen):
                        self.start_game = True
                        self.start_intro = True
                    if self.settings_button.draw(self.screen):
                        self.menu_state = "settings"
                    if self.scoreboard_button.draw(self.screen):
                        self.menu_state = "scoreboard"
                    if self.exit_button.draw(self.screen):
                        self.run = False
                
                # settings menu
                if self.menu_state == "settings":
                    self.draw_text('SFX VOLUME ', self.font, self.WHITE, 50, 75)
                    if self.sfx_low_button.draw(self.screen):
                        self.jump_fx.set_volume(0.025)
                        self.shot_fx.set_volume(0.025)
                        self.grenade_fx.set_volume(0.025)
                    if self.sfx_high_button.draw(self.screen):
                        self.jump_fx.set_volume(0.075)
                        self.shot_fx.set_volume(0.075)
                        self.grenade_fx.set_volume(0.075)
                    if self.sfx_off_button.draw(self.screen):
                        self.jump_fx.set_volume(0)
                        self.shot_fx.set_volume(0)
                        self.grenade_fx.set_volume(0)
                    if self.back_button.draw(self.screen):
                        self.menu_state = "main"
                        
                # scoreboard menu
                if self.menu_state == "scoreboard":
                    self.score.show_scoreboard()
                    
                        
            else:
                #update background
                self.draw_bg()
                #draw world map
                self.world.draw()
                #return button
                if self.back_button.draw(self.screen):
                    self.start_game = False
                #show player health
                self.health_bar.draw(self.player.health)
                #show score
                self.score.show_score()
                       
        
                self.player.update()
                self.player.draw()
        
                for enemy in self.enemy_group:
                    enemy.ai()
                    enemy.update()
                    enemy.draw()
        
                #update and draw groups
                self.bullet_group.update()
                self.grenade_group.update()
                self.explosion_group.update()
                self.item_box_group.update()
                self.decoration_group.update()
                self.water_group.update()
                self.exit_group.update()
                self.bullet_group.draw(self.screen)
                self.grenade_group.draw(self.screen)
                self.explosion_group.draw(self.screen)
                self.item_box_group.draw(self.screen)
                self.decoration_group.draw(self.screen)
                self.water_group.draw(self.screen)
                self.exit_group.draw(self.screen)
        
                #show intro
                if self.start_intro == True:
                    if self.intro_fade.fade():
                        self.start_intro = False
                        self.intro_fade.fade_counter = 0
        
        
                #update player actions
                if self.player.alive:
                    if self.player.in_air:
                        self.player.update_action(2)#2: jump
                    elif self.moving_left or self.moving_right:
                        self.player.update_action(1)#1: run
                    else:
                        self.player.update_action(0)#0: idle
                    self.screen_scroll, self.level_complete = self.player.move(self.moving_left, self.moving_right)
                    self.bg_scroll -= self.screen_scroll
                    
                    #check if player has completed the level
                    if self.level_complete:
                        self.start_intro = True
                        self.level += 1
                        if self.level > 2:
                            self.level = 1
                        self.bg_scroll = 0
                        self.world_data = self.reset_level()
                        if self.level <= self.MAX_LEVELS:
                            #load in level data and create world
                            with open(f'level{self.level}_data.csv', newline='') as csvfile:
                                reader = csv.reader(csvfile, delimiter=',')
                                for x, row in enumerate(reader):
                                    for y, tile in enumerate(row):
                                        self.world_data[x][y] = int(tile)
                            self.world = wr.World(self)
                            self.player, self.health_bar = self.world.process_data(self.world_data)    
                else:
                    self.score.check_scores()
                    #self.score.show_scoreboard()
                    self.screen_scroll = 0
                    self.player_score = 0
                    self.score.prep_score()
                    if self.death_fade.fade():
                        if self.restart_button.draw(self.screen):
                            self.death_fade.fade_counter = 0
                            self.start_intro = True
                            self.bg_scroll = 0
                            self.world_data = self.reset_level()
                            #load in level data and create world
                            with open(f'level{self.level}_data.csv', newline='') as csvfile:
                                reader = csv.reader(csvfile, delimiter=',')
                                for x, row in enumerate(reader):
                                    for y, tile in enumerate(row):
                                        self.world_data[x][y] = int(tile)
                            self.world = wr.World(self)
                            self.player, self.health_bar = self.world.process_data(self.world_data)
        
        
            for event in pygame.event.get():
                #quit game
                if event.type == pygame.QUIT:
                    self.score.check_scores()
                    self.run = False
                #keyboard presses
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.moving_left = True
                    if event.key == pygame.K_d:
                        self.moving_right = True
                    if event.key == pygame.K_SPACE:
                        self.shoot = True
                    if event.key == pygame.K_q:
                        self.grenade = True
                    if event.key == pygame.K_w and self.player.alive:
                        self.player.jump = True
                        self.jump_fx.play()
                    if event.key == pygame.K_ESCAPE:
                        self.run = False
        
        
                #keyboard button released
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        self.moving_left = False
                    if event.key == pygame.K_d:
                        self.moving_right = False
                    if event.key == pygame.K_SPACE:
                        self.shoot = False
                    if event.key == pygame.K_q:
                        self.grenade = False
                        self.grenade_thrown = False
        
        
            pygame.display.update()
        
        pygame.quit()
    
if __name__ == '__main__':
    # Make an instance, and run the game.
    game = GameMain()
    game.runGame()
