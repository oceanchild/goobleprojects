'''
Created on 2012-02-26

@author: Gooble
'''

from main.view.drawing import colours
from main.view.dimensions import DEFAULT_HEIGHT, DEFAULT_WIDTH
from main.view.gamestate import GameState
from main.view.quitnow import QuitNow
import pygame

class GameStart(object):
    
    def __init__(self):
        self.state = GameState()
        self.done = False
    
    def start(self):
        pygame.init()
        screen = pygame.display.set_mode([DEFAULT_WIDTH, DEFAULT_HEIGHT])
        pygame.display.set_caption("Gooble Checkers")
        
        clock = pygame.time.Clock()
        while not self.done:
            clock.tick(30)
            screen.fill(colours.BLACK)
            self.screen_tick(screen)
            pygame.display.flip()
        
    def screen_tick(self, screen):
        self.state.display(screen)
        self.handle_events(screen)
    
    def handle_events(self, screen):
        try:
            for event in pygame.event.get():
                self.state = self.state.process(event)
                self.state.display(screen, self.get_position(event))
            self.state.post_process()
        except QuitNow:
            self.quit_game()
            
    def get_position(self, event):
        try:
            return event.pos
        except AttributeError:
            return None
            
    def quit_game(self):
        self.done = True

if __name__=="__main__":
    GameStart().start()