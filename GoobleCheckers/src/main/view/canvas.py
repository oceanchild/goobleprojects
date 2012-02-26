'''
Created on 2012-02-26

@author: Gooble
'''

import pygame

class Canvas(object):
    
    def __init__(self, screen, graphics=pygame):
        self.screen = screen
        self.graphics = graphics
    
    def draw(self, drawables):
        for drawable in drawables:
            drawable.draw(self.graphics, self.screen)
#            x = drawable.get_x()
#            y = drawable.get_y()
#            width = drawable.get_width()
#            height = drawable.get_height()
#            bgcolor = drawable.get_background_colour()
#            colour = drawable.get_colour()
#            self.graphics.draw.rect(self.screen, bgcolor, [x, y, width, height])
#            self.graphics.draw.ellipse(self.screen, colour, [x, y, width, height])
            