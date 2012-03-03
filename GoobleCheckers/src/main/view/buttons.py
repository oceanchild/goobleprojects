'''
Created on 2012-02-29

@author: Gooble
'''
from main.view.gamestate import GameState
class Button(object):
    def __init__(self, sprite=None):
        self.sprite = sprite

    def draw(self, graphics, screen):
        graphics.sprite.RenderPlain(self.sprite).draw(screen)
        
    def was_clicked(self, pos):
        return self.sprite.rect.collidepoint(pos)

class NewGameButton(Button):
    def get_state(self):
        return GameState()

class DifficultyButton(Button):
    def get_state(self):
        return None
    
class QuitButton(Button):
    def get_state(self):
        return None