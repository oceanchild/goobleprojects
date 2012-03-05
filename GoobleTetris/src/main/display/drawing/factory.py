'''
Created on 2012-03-04

@author: Gooble
'''

import pygame
import os

class DrawableSprite(object):
    def __init__(self, sprite):
        self.sprite = sprite
    
    def draw(self, screen):
        pygame.sprite.RenderPlain(self.sprite).draw(screen)
        
class DrawableText(object):
    def __init__(self, text, x, y):
        self.text = text
        self.x = self.y
        
    def draw(self, screen):
        screen.blit(self.text, [self.x, self.y])

class DrawableFactory(object):
    def createImage(self, imagefile, x, y):
        image = pygame.image.load_basic(os.path.join('resources', imagefile))
        image = image.convert()
        sprite = pygame.sprite.Sprite()
        sprite.image = image
        sprite.rect = image.get_rect()
        sprite.rect.topleft = x, y
        return DrawableSprite(sprite)
    
    def createText(self, text, x, y, fontsize=25):
        font = pygame.font.Font(None, fontsize)
        rendered_text = font.render(text, True, pygame.color.THECOLORS['white'])
        return DrawableText(rendered_text, x, y)
    
