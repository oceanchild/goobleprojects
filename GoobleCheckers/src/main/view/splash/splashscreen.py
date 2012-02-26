'''
Created on 2012-02-26

@author: Gooble
'''
from main.view.splash.choosedifficulty import ChooseDifficultyCommand
from main.view.splash.howtoplay import HowToPlayCommand
from main.view.splash.newgame import NewGameCommand
from main.view.splash.quitting import QuitCommand

class SplashScreen(object):
    
    def __init__(self):
        self.text = ["New Game", "Choose Difficulty", "How to Play", "Quit"];
        self.options = {"New Game"          : NewGameCommand(), 
                        "Choose Difficulty" : ChooseDifficultyCommand(), 
                        "How to Play"       : HowToPlayCommand(), 
                        "Quit"              : QuitCommand()}
    
    def get_text(self):
        return self.text
    
    def choose_option(self, opt):
        return self.options[opt].process()