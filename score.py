# -*- coding: utf-8 -*-
import pygame
import time

class Score:
    """ A class to draw the current score to the screen and update scoreboard """
    
    
    
    def __init__(self, game):
        """Initialize score keeping attributes."""
        self.game = game
        self.screen = self.game.screen
        self.screen_rect = self.screen.get_rect()
        self.score = self.game.player_score
        
        # Get high scores list
        with open('scores.txt', 'r') as file:
            self.high_scores = file.readlines()
            
        # convert to ints
        for i in range(len(self.high_scores)):
            self.high_scores[i] = int(self.high_scores[i])
            
        # get names list
        with open('names.txt', 'r') as file:
            self.high_score_names = file.readlines()

        # Font settings
        self.text_color = (255, 255, 255)
        self.font = pygame.font.Font('font/ARCADECLASSIC.TTF', 35)

        # Prep initial score images.
        self.prep_score()
        
        
        
    def prep_score(self):
        """Turn score into rendered image."""
        self.score = self.game.player_score
        score_str = "{:,}".format(self.score)
        self.score_image = self.font.render(score_str, True,
                            self.text_color, None)

        # Display score at top of screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = (self.screen_rect.right / 2) + (self.score_rect.width / 2)
        self.score_rect.top = 15
        
        
        
    def show_score(self):
        '''shows current score on screen'''
        self.screen.blit(self.score_image, self.score_rect)
         
        
        
    def check_scores(self):
        """Check to see if a high score was beaten, update if neccessary"""
        
        # scroll high scores
        for i in range(len(self.high_scores)):
            
            if self.score > self.high_scores[i]:
                # update highscore, shifting the others and removing the 6th
                self.high_scores.insert(i, self.score)
                self.high_scores.pop(5)
                
                # get name from user, update name list as above
                name = self.get_text()
                self.high_score_names.insert(i, name)
                self.high_score_names.pop(5)   
                
                # update the names.txt and scores.txt files
                self.update_high_scores()
                
                # show scoreboard
                self.show_scoreboard()
                break
            
            
        
    def update_high_scores(self):
        """Update high_score.csv to reflect high scores."""
        str_hs = ['', '', '', '', '']
        
        # update names file
        with open('names.txt', 'w') as file:
            file.writelines(self.high_score_names)
            
        # update scores file
        for i in range(len(self.high_scores)):
            str_hs[i] = str(self.high_scores[i]) + "\n"
        with open('scores.txt', 'w') as file:
            file.writelines(str_hs)
            
            
                        
    def get_text(self):
        '''gets text input from user, returns text in string plus a newline at the end'''
        font = self.font
        
        # enter name msg
        text1 = font.render('Enter Name', True, (255, 255, 255))
        rect1 = text1.get_rect()
        rect1.center = ((self.game.SCREEN_WIDTH / 2), (self.game.SCREEN_HEIGHT / 2))
        
        # name text
        name = 'player'
 
        # render the text
        img = font.render(name, True, (255, 255, 255))
        rect = img.get_rect()
        rect.center = (((self.game.SCREEN_WIDTH / 2) - 20), ((self.game.SCREEN_HEIGHT / 2) + 40))
        cursor = pygame.Rect(rect.topright, (3, rect.height))
 
        running = True
 
        while running:
     
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game.run = False
                    
                # detect if key is physically
                # pressed down
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        if len(name) > 0:
                     
                            # stores the text except last
                            # character
                            name = name[:-1]
 
                    elif event.key == pygame.K_RETURN:
                        running = False
                    else:
                        name += event.unicode
                 
                    img = font.render(name, True, (255, 255, 255))
                    rect.size = img.get_size()
                    cursor.topleft = rect.topright
 
            # Add background color and show text to the window screen
            self.game.draw_bg()
            self.screen.blit(img, rect)
            self.screen.blit(text1, rect1)
     
            # cursor is made to blink after every 0.5 sec
            if time.time() % 1 > 0.5:
                pygame.draw.rect(self.screen, (255, 255, 255), cursor)
         
            # update display
            pygame.display.update()
            
            
        return name + "\n"
    
    
    
    def show_scoreboard(self):
        ''' prints top 5 high scores to screen '''

        font = pygame.font.Font('font/ARCADECLASSIC.TTF', 40)
        color = self.game.WHITE
        
        # title coordinates
        ntx = 180
        nty = 20
        stx = ((self.game.SCREEN_WIDTH / 2) + 20) + 72
        sty = 20
        
        # name title
        _name = font.render('Player Name', True, color)
        _name_rect = _name.get_rect()
        _name_rect.topleft = (ntx, nty + 180)
        
        # score title
        _score = font.render('Score', True, color)
        _score_rect = _score.get_rect()
        _score_rect.topleft = (stx, sty + 180)
        
        
        ##############################################################
        #          IMAGES: high score names 1 - 5                    #
        ##############################################################
        hsn1 = font.render(self.high_score_names[0].rstrip("\n"), True, color)
        hsn1_rect = hsn1.get_rect()
        hsn1_rect.topleft = (ntx, nty + 230)
        
        hsn2 = font.render(self.high_score_names[1].rstrip("\n"), True, color)
        hsn2_rect = hsn2.get_rect()
        hsn2_rect.topleft = (ntx, nty + 270)
        
        hsn3 = font.render(self.high_score_names[2].rstrip("\n"), True, color)
        hsn3_rect = hsn3.get_rect()
        hsn3_rect.topleft = (ntx, nty + 310)
        
        hsn4 = font.render(self.high_score_names[3].rstrip("\n"), True, color)
        hsn4_rect = hsn4.get_rect()
        hsn4_rect.topleft = (ntx, nty + 350)
        
        hsn5 = font.render(self.high_score_names[4].rstrip("\n"), True, color)
        hsn5_rect = hsn5.get_rect()
        hsn5_rect.topleft = (ntx, nty + 390)
        
        
        ##############################################################
        #               IMAGES: high scores 1 - 5                    #
        ##############################################################
        hs1 = font.render(str(self.high_scores[0]).rstrip("\n"), True, color)
        hs1_rect = hs1.get_rect()
        hs1_rect.topleft = (stx, sty + 230)
        
        hs2 = font.render(str(self.high_scores[1]).rstrip("\n"), True, color)
        hs2_rect = hs2.get_rect()
        hs2_rect.topleft = (stx, sty + 270)
        
        hs3 = font.render(str(self.high_scores[2]).rstrip("\n"), True, color)
        hs3_rect = hs3.get_rect()
        hs3_rect.topleft = (stx, sty + 310)
        
        hs4 = font.render(str(self.high_scores[3]).rstrip("\n"), True, color)
        hs4_rect = hs4.get_rect()
        hs4_rect.topleft = (stx, sty + 350)
        
        hs5 = font.render(str(self.high_scores[4]).rstrip("\n"), True, color)
        hs5_rect = hs5.get_rect()
        hs5_rect.topleft = (stx, sty + 390)
        
        
        ##############################################################
        #                         DISPLAY                            #
        ##############################################################
        
        # set background color
        self.game.draw_bg()

        # display titles
        self.screen.blit(_name, _name_rect)
        self.screen.blit(_score, _score_rect)
        
        # display high score names
        self.screen.blit(hsn1, hsn1_rect)
        self.screen.blit(hsn2, hsn2_rect)
        self.screen.blit(hsn3, hsn3_rect)
        self.screen.blit(hsn4, hsn4_rect)
        self.screen.blit(hsn5, hsn5_rect)
        
        # display high scores
        self.screen.blit(hs1, hs1_rect)
        self.screen.blit(hs2, hs2_rect)
        self.screen.blit(hs3, hs3_rect)
        self.screen.blit(hs4, hs4_rect)
        self.screen.blit(hs5, hs5_rect)
        
            
        
        # while loop flag
        running = True
        
        while running:
            
           
            # exit scoreboard when enter is pressed
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        running = False
                if event.type == pygame.QUIT:
                    running = False
                    self.game.run = False
                if self.game.menu_state == "scoreboard":
                    if self.game.back_button.draw(self.screen):
                        self.game.menu_state = "main"
                        running = False
            
           
            
            # update display
            pygame.display.update()
        
