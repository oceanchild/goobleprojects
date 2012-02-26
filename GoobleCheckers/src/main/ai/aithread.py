'''
Created on 2012-02-26

@author: Gooble
'''
import threading

class AIThread(threading.Thread):
    def __init__(self, ai, game):
        threading.Thread.__init__(self)
        self.ai=ai
        self.game=game
        self.finished=False
    
    def run(self):
        self.ai.make_move(self.game)
        self.finished=True