'''
Created on 2012-02-26

@author: Gooble
'''

import pygame
from main.ai import minimaxai, aithread
import main.view.canvas
import main.view.gamepanel
import main.view.drawables
from main.view.quitnow import QuitNow
from main.view.eventhandler import EventHandler
from main.view import colours
from main.view.dimensions import DEFAULT_HEIGHT, DEFAULT_WIDTH

class GameStart(object):
    
    def __init__(self, game):
        self.game = game
        self.aithread = None
        self.done = False
    
    def create_drawables(self, position):
        return main.view.drawables.Drawables(self.game).create(position)
    
    def draw(self, screen, position=None):
        main.view.canvas.Canvas(screen).draw(self.create_drawables(position))
    
    def handle_events(self, screen):
        try:
            for event in pygame.event.get():
                pos = EventHandler(self.game).handle(event)
                self.draw(screen, pos)
        except QuitNow:
            self.quit_game()
            
    def quit_game(self):
        self.done = True
    
    def time_to_use_ai(self):
        return self.game.is_computers_turn() and (self.aithread is None or self.aithread.finished)
    
    def check_and_use_ai(self):
        if self.time_to_use_ai():
            if self.aithread is not None:
                self.aithread.join(10)
            self.aithread = aithread.AIThread(self.game)
            self.aithread.start()
    
    def print_text(self, screen):
        font = pygame.font.Font(None, 25)
        if self.game.is_computers_turn():
            text = font.render("The computer is thinking...", False, colours.MEDIUMGRAY, colours.WHITE)
            screen.blit(text, [DEFAULT_WIDTH/4, DEFAULT_HEIGHT/2 - 25])
    
    def start(self):
        pygame.init()
        screen = pygame.display.set_mode([DEFAULT_WIDTH, DEFAULT_HEIGHT])
        pygame.display.set_caption("Gooble Checkers")
        
        clock = pygame.time.Clock()
        while not self.done:
            clock.tick(30)
            screen.fill(colours.BLACK)
            
            self.draw(screen)
            self.handle_events(screen)
            self.check_and_use_ai()
            self.print_text(screen)
            
            pygame.display.flip()
        
        
if __name__=="__main__":
    GameStart(main.view.gamepanel.GamePanel(ai=minimaxai.MinimaxAI(3))).start()