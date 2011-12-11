'''
Created on 2011-12-11

@author: Gooble
'''
from main.game import origin

class Match(object):
    
    def __init__(self, board, ai_top, ai_bottom):
        self.board = board
        self.ai_top = ai_top
        self.ai_bottom = ai_bottom
        
    def go(self):
        while not self.board.is_game_over():
            if self.board.current_turn.origin == origin.BOTTOM:
                self.ai_bottom.make_move(self.board)
            else:
                self.ai_top.make_move(self.board)