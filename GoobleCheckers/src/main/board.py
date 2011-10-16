'''
Created on 2011-10-02

@author: Gooble
'''
from main import origin
from main.piece import Piece
from main.movement import Movement

class Board(object):
    
    DEFAULT_WIDTH = 8
    DEFAULT_HEIGHT = 8

    def __init__(self):
        self.init_board()
        
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
        
    
    def illegal_move(self, from_loc, to_loc):
        moves = Movement(self, from_loc[0], from_loc[1]).get_available_moves()
        for move_list in moves:
            if to_loc in move_list:
                return False
        return True
    
    def move_piece(self, from_loc, to_loc):
        if self.illegal_move(from_loc, to_loc):
            return
        
        self.set_piece(to_loc[0], to_loc[1], self.get_piece(from_loc[0], from_loc[1]))
        self.set_piece(from_loc[0], from_loc[1], None)
        
                
