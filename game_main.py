# -*- coding: utf-8 -*-
"""
A quick main to mess with, change, and figure out what works

"""
# Import community libraries
import sys
import pygame
from time import sleep

# Import dev created modules



"""Overall class to manage game assets and behavior."""
class GameMain:
    
    
    """Initialize the game and create resources."""
    def __init__(self):
        
        # Init pygame
        pygame.init()
        
        # Create display and set to 1024x768
        self.screen = pygame.display.set_mode((1024, 768))
        ''' TODO name the game!'''
        pygame.display.set_caption("TBD Game Name")
        
        
    """ Defines the main loop for the game. """
    def run_game(self):
        
        while True:
            # Check events and respond.  should get replaced with _check_events
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    sys.exit()
            
            # Draws most recent screen.  should get replaced with _update_screen
            pygame.display.flip()
            
                    
        
if __name__ == '__main__':
    # Make an instance, and run the game.
    gm = GameMain()
    gm.run_game()
    
    