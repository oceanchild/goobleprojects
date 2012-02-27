'''
Created on 2012-02-26

@author: Gooble
'''
import pygame
from main.view.quitnow import QuitNow
class EventHandler(object):
    
    def handle(self, event):
        if event.type == pygame.QUIT:
            raise QuitNow()
        
        return self.get_position(event)
    
    def get_position(self, event):
        try:
            pos = event.pos
        except AttributeError:
            pos = None
        return pos