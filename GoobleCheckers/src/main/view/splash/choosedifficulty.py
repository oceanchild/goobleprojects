'''
Created on 2012-02-26

@author: Gooble
'''

class ChooseDifficultyScreen(object):
    def get_text(self):
        return ["Easy", "Medium", "Difficult", "Go Back"]
    
    
    
class ChooseDifficultyCommand(object):
    def process(self):
        return ChooseDifficultyScreen()