'''
Created on 2012-02-26

@author: Gooble
'''
from main.ai import minimaxai, aithread
from main.view.eventhandler import EventHandler
import main.view.checkers
import main.view.canvas
import main.view.drawables

class GameState(object):
    
    def __init__(self):
        self.game = main.view.checkers.Checkers(ai=minimaxai.MinimaxAI(3))
        self.aithread = None 

    def display(self, screen, event=None):
        try:
            pos = event.pos
        except AttributeError:
            pos = None
        main.view.canvas.Canvas(screen).draw(self.create_drawables(pos))
    
    def process(self, event):
        EventHandler(self.game).handle(event)
        
    def post_process(self):
        self.check_and_use_ai()
        
    def check_and_use_ai(self):
        if self.time_to_use_ai():
            if self.aithread is not None:
                self.aithread.join(10)
            self.aithread = aithread.AIThread(self.game)
            self.aithread.start()
                
    def time_to_use_ai(self):
        return self.game.is_computers_turn() and (self.aithread is None or self.aithread.finished)
    
    def create_drawables(self, position):
        return main.view.drawables.Drawables(self.game).create(position)