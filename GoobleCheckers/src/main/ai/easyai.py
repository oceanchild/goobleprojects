'''
Created on 2011-12-08

@author: Gooble
'''
from main.game import origin
from main.ai.originmoves import OriginMoves

class EasyAI(object):
    
    def __init__(self, origin=origin.BOTTOM):
        self.origin = origin
    
    def make_move(self, board):
        all_moves = OriginMoves(board, self.origin).get_moves()
        
        max_pieces_eaten = 0
        best_move = None
        for move_list in all_moves:
            for move in move_list:
                if move.get_pieces_eaten() >= max_pieces_eaten:
                    best_move = move
                    max_pieces_eaten = len(move)
                    
        for move in best_move:
            board.move_piece(move.from_loc, move.to_loc)
