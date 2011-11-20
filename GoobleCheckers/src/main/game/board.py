'''
Created on 2011-10-02

@author: Gooble
'''
from main.game import origin
from main.game.piece import Piece
from main.game.turn import Turn

class Board(object):
    
    DEFAULT_WIDTH = 8
    DEFAULT_HEIGHT = 8

    def __init__(self):
        self.init_board()
        self.current_turn = Turn(self)
        
    def init_board(self):
        self.pieces = []
        for row in range (0, self.DEFAULT_HEIGHT):
            self.pieces.append([self.create_piece(row, col) for col in range(0, self.DEFAULT_WIDTH)])
            
            
    def create_piece(self, row, col):
        if row < (self.DEFAULT_HEIGHT / 2 - 1) and (row+col) % 2 == 0:
            return Piece(origin.get_top())
        elif row > (self.DEFAULT_HEIGHT / 2) and (row+col) % 2 == 0:
            return Piece(origin.get_bottom())
        else:
            return None
            
    def invalid_position(self, row, col):
        return col >= self.DEFAULT_WIDTH or row >= self.DEFAULT_HEIGHT or row < 0 or col < 0
    
    def valid_position(self, row, col):
        return not self.invalid_position(row, col)

    def get_piece(self, row, col):
        if self.invalid_position(row, col):
            return None
        
        return self.pieces[row][col]
    
    def set_piece(self, row, col, piece):
        if self.invalid_position(row, col):
            return
        
        self.pieces[row][col] = piece
    
    def move_piece(self, from_loc, to_loc):
        self.current_turn.handle_movement(from_loc, to_loc)
        
        if self.current_turn.is_over():
            self.current_turn.handle_jumps()
            self.king_piece_if_necessary(to_loc)
            self.current_turn = Turn(self, self.current_turn.origin)
            
    def king_piece_if_necessary(self, king_loc):
        piece = self.get_piece(king_loc[0], king_loc[1])
        piece.set_king(self._should_piece_be_king(piece, king_loc[0]))
            
    def _should_piece_be_king(self, piece, row):
        if piece.is_king():
            return True
        if piece.get_origin().value > 0 and row == self.DEFAULT_HEIGHT - 1:
            return True
        if piece.get_origin().value < 0 and row == 0:
            return True
        return False
