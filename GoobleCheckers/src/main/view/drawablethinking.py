'''
Created on 2012-02-26

@author: Gooble
'''
from main.view.dimensions import DEFAULT_HEIGHT, DEFAULT_WIDTH
from main.view import colours

ANTIALIAS = True

class DrawableThinkingText(object):
    def draw(self, graphics, screen):
        font = graphics.font.Font(None, 25)
        text = font.render("The computer is thinking...", ANTIALIAS, colours.MEDIUMGRAY, colours.WHITE)
        screen.blit(text, [DEFAULT_WIDTH/4, DEFAULT_HEIGHT/2 - 25])