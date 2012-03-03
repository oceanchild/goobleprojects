'''
Created on 2012-02-27

@author: Gooble
'''

from main.view.buttons import DifficultyButton, NewGameButton, QuitButton
from main.view.buttonpositions import ButtonPositions

class SplashStateButtons(object):
    
    def create(self, graphics):
        imagefiles = ['newgamebtn.bmp', 'difficultybtn.bmp', 'quitbtn.bmp']
        buttons = [NewGameButton(), DifficultyButton(), QuitButton()]

        ButtonPositions(graphics).center(buttons, imagefiles)
            
        return buttons
