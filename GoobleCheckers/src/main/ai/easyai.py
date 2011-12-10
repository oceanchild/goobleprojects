'''
Created on 2011-12-08

@author: Gooble
'''
from main.game import origin

class EasyAI(object):
    
    def __init__(self):
        self.origin = origin.BOTTOM
    
    def make_move(self, board):
        board.move_piece((4, 0), (3, 1))