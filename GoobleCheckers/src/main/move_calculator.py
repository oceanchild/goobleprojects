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
            self._add_moves_about_col(row + 1, col, moves)
                
        elif piece.get_origin() == Origin.BOTTOM:
            self._add_moves_about_col(row - 1, col, moves)
        
        return moves
    
    def _add_if_valid_move(self, row, col, moves):
        if self.board.get_piece(row, col) is None and self.board.valid_position(row, col):
            moves.append((row, col))
            
    def _add_moves_about_col(self, row, col, moves):
        left_col = col - 1
        right_col = col + 1
        self._add_if_valid_move(row, left_col, moves)
        self._add_if_valid_move(row, right_col, moves)