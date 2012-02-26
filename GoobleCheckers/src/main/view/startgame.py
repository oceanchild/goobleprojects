'''
Created on 2012-02-26

@author: Gooble
'''

import pygame
from main.view.gamepanel import GamePanel
from main.ai import minimaxai

class GameStart(object):
    
    def __init__(self):
        pass
    
    def draw(self, game):
        pass
    
    def start(self, game):
        pygame.init()
        screen = pygame.display.set_mode([self.DEFAULT_WIDTH, self.DEFAULT_HEIGHT])
        pygame.display.set_caption("Gooble Checkers")
        
        clock = pygame.time.Clock()
        font = pygame.font.Font(None, 25)
        
        done = False
        while not done:
            clock.tick(30)
            screen.fill([0,0,0])
            
            self.draw(game)
            
            
            pygame.display.flip()
        
        
if __name__=="__main__":
    GameStart(GamePanel(ai=minimaxai.MinimaxAI(3))).start()