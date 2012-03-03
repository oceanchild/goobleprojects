'''
Created on 2012-02-27

@author: Gooble
'''
import os
from main.view.dimensions import DEFAULT_WIDTH, DEFAULT_HEIGHT
from main.view.buttons import DifficultyButton, NewGameButton, QuitButton

PADDING = 50

class SplashStateButtons(object):
    
    def create(self, graphics):
        imagefiles = ['newgamebtn.bmp', 'difficultybtn.bmp', 'quitbtn.bmp']
        buttons = [NewGameButton(), DifficultyButton(), QuitButton()]
        y = int(DEFAULT_HEIGHT / 3)
        
        for i in range (0, len(buttons)):
            image = graphics.image.load_basic(os.path.join('..', '..', 'resources', imagefiles[i]))
            image = image.convert()
            sprite = graphics.sprite.Sprite()
            sprite.image = image
            sprite.rect = image.get_rect()
            x = int(DEFAULT_WIDTH/2 - sprite.rect.width/2) 
            sprite.rect.topleft = x, y
            y += sprite.rect.height + PADDING
            buttons[i].sprite = sprite
            
        return buttons
