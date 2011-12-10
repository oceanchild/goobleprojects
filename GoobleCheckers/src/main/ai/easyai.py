'''
Created on 2011-12-08

@author: Gooble
'''
from main.game import origin
from main.ai.originmoves import OriginMoves

class EasyAI(object):
    
    def __init__(self):
        self.origin = origin.BOTTOM
    
    def make_move(self, board):
        all_moves = OriginMoves(board, self.origin).get_moves()
        
        if len(all_moves) > 0:
            move_list = all_moves[0][0]
            for move in move_list:
                board.move_piece(move.from_loc, move.to_loc)
