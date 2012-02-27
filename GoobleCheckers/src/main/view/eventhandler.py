'''
Created on 2012-02-26

@author: Gooble
'''
import pygame
from main.view.quitnow import QuitNow

class EventHandler(object):
    
    def __init__(self, game):
        self.game = game
    
    def handle(self, event):
        if event.type == pygame.QUIT:
            raise QuitNow()
        if self.game.is_computers_turn():
            return
        
        pos = self.get_position(event)
        self.handle_input(event, pos)
        return pos

    def get_position(self, event):
        try:
            pos = event.pos
        except AttributeError:
            pos = None
        return pos

    def handle_input(self, event, pos):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.game.select_piece(pos)
        if event.type == pygame.MOUSEBUTTONUP:
            self.game.release_piece(pos)