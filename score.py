# -*- coding: utf-8 -*-
import pygame

class Score:
    """ A class to draw the current score to the screen and update scoreboard """
    
    def __init__(self, game):
        """Initialize score keeping attributes."""
        self.game = game
        self.screen = self.game.screen
        self.screen_rect = self.screen.get_rect()
        self.score = self.game.player_score
        
        # Get high scores list
        with open('scores.txt.', 'r') as file:
            self.high_scores = file.readlines()
            
        # convert to ints
        for i in range(len(self.high_scores)):
            self.high_scores[i] = int(self.high_scores[i])
            
        # get names list
        with open('names.txt.', 'r') as file:
            self.high_score_names = file.readlines()
        

        # Font settings
        self.text_color = (0, 0, 0)
        self.font_size = 35
        self.font = pygame.font.SysFont(None, self.font_size)

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
        self.score_rect.top = 20
        
    def show_score(self):
         self.screen.blit(self.score_image, self.score_rect)
         
    def check_scores(self):
        """Check to see if a high score was beaten, update if neccessary"""
        for i in range(len(self.high_scores)):
            if self.score > self.high_scores[i]:
                self.high_scores.insert(i, self.score)
                self.high_scores.pop(5)
                #TODO: update names
                # get name
                #self.high_score_names.insert(index, name)
                #self.high_score_names.pop(5)
                self.update_high_scores()
                break
        
    def update_high_scores(self):
        """Update high_score.csv to reflect high scores."""
        str_hs = ['', '', '', '', '']
        #TODO: update names file
        #with open('names.txt.', 'w') as file:
        #    file.writelines(self.high_score_names)
        for i in range(len(self.high_scores)):
            str_hs[i] = str(self.high_scores[i]) + "\n"
        with open('scores.txt.', 'w') as file:
            file.writelines(str_hs)
        