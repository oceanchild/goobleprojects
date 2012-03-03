'''
Created on 2012-02-29

@author: Gooble
'''
import main.view.gamestate 
import main.view.difficultystate 
import main.view.splashstate

class Button(object):
    def __init__(self, sprite=None):
        self.sprite = sprite

    def draw(self, graphics, screen):
        graphics.sprite.RenderPlain(self.sprite).draw(screen)
        
    def was_clicked(self, pos):
        return self.sprite.rect.collidepoint(pos)

class NewGameButton(Button):
    def get_state(self, info):
        return main.view.gamestate.GameState(info)

class DifficultyButton(Button):
    def get_state(self, info):
        return main.view.difficultystate.DifficultyState(info)
    
class QuitButton(Button):
    def get_state(self, info):
        return None

class EasyButton(Button):
    def get_state(self, info):
        info["mode"] = "Easy"
        return main.view.difficultystate.DifficultyState(info)
    
class MediumButton(Button):
    def get_state(self, info):
        info["mode"] = "Medium"
        return main.view.difficultystate.DifficultyState(info)
    
class HardButton(Button):
    def get_state(self, info):
        info["mode"] = "Hard"
        return main.view.difficultystate.DifficultyState(info)
    
class BackButton(Button):
    def get_state(self, info):
        return main.view.splashstate.SplashState(info)
