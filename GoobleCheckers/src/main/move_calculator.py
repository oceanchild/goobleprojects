'''
Created on 2011-10-03

@author: Gooble
'''
from main import origin

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
        
        if piece.get_origin() == origin.get_top():
            self._add_moves_about_col(row + 1, col, moves, origin.get_top())
                
        elif piece.get_origin() == origin.get_bottom():
            self._add_moves_about_col(row - 1, col, moves, origin.get_bottom())
        
        return moves
    
    def _add_moves_about_col(self, row, col, moves, origin):
        move1 = self._add_if_valid_move(row, col, -1, [], origin)
        if len(move1) > 0: moves.append(move1)
        move2 = self._add_if_valid_move(row, col, 1, [], origin)
        if len(move2) > 0: moves.append(move2)
        
    def _add_if_valid_move(self, row, col, direction, move, origin):
        new_col = col + direction
        if not self.board.valid_position(row, new_col):
            return move
        
        piece = self.board.get_piece(row, new_col)
        if piece is None:
            move.append((row, new_col))
            return move
        elif piece.get_origin() == origin:
            return move
        elif piece.get_origin() != origin:
            new_row = row + origin.value
            new_new_col = new_col + direction
            if self.board.get_piece(new_row, new_new_col) is not None:
                return move
            
            return self._add_if_valid_move(new_row, new_col, direction, move, origin)
        
        
        
        
        
        