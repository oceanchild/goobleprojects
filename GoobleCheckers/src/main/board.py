'''
Created on 2011-10-02

@author: Gooble
'''
from main import origin
from main.piece import Piece
from main.movement import Movement
from main.turn import Turn

class Board(object):
    
    DEFAULT_WIDTH = 8
    DEFAULT_HEIGHT = 8

    def __init__(self):
        self.init_board()
        self.current_turn = Turn()
        
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
        
    
    def illegal_move(self, from_loc, to_loc, moves):
        piece = self.get_piece(from_loc[0], from_loc[1])
        if piece is not None and piece.get_origin() != self.current_turn.origin:
            return True
        
        if self.current_turn.piece is not None and self.current_turn.piece is not piece:
            return True
        
        for move_list in moves:
            if to_loc in move_list:
                self.current_turn.piece = piece
                return False
        return True
    
    def move_piece(self, from_loc, to_loc):
        moves = Movement(self, from_loc[0], from_loc[1]).get_available_moves()
        if self.illegal_move(from_loc, to_loc, moves):
            return
        
        self.set_piece(to_loc[0], to_loc[1], self.get_piece(from_loc[0], from_loc[1]))
        self.set_piece(from_loc[0], from_loc[1], None)
        
        self.current_turn.add_jumped_pieces(from_loc, to_loc)
        self.handle_jumped_pieces(from_loc, to_loc, moves)
    
    def handle_jumped_pieces(self, from_loc, to_loc, moves):
        for move_list in moves:
            if to_loc == move_list[-1]:
                jumped_pieces = self.current_turn.jumped_pieces
                while len(jumped_pieces) > 0:
                    jumped = jumped_pieces.pop()
                    self.set_piece(jumped[0], jumped[1], None);
                self.current_turn = Turn(self.current_turn.origin)