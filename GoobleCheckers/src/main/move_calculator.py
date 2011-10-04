'''
Created on 2011-10-03

@author: Gooble
'''
from main.origin import Origin

class MoveCalculator(object):

    def __init__(self, board):
        self.board = board
        
    def get_available_moves(self, row, col):
        if self.board.invalid_position(row, col):
            return []
        
        moves = []
        piece = self.board.get_piece(row, col)
        if piece is None:
            return []
        
        if piece.get_origin() == Origin.TOP:
            left_col = col - 1
            lower_row = row + 1
            if self.board.get_piece(lower_row, left_col) is None and self.board.valid_position(lower_row, left_col):
                moves.append((lower_row, left_col))
                
            right_col = col + 1
            if self.board.get_piece(lower_row, right_col) is None and self.board.valid_position(lower_row, right_col):
                moves.append((lower_row, right_col))
                
        elif piece.get_origin() == Origin.BOTTOM:
            pass
        
        return moves