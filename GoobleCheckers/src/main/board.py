'''
Created on 2011-10-02

@author: Gooble
'''
from main import origin
from main.piece import Piece

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
        

    def print_board(self):
        for row_of_pieces in self.pieces:
            for piece in row_of_pieces:
                if piece is not None:
                    print(piece.get_origin()[:1], end=' ')
                else:
                    print(' ', end=' ')
            print()
            
    def invalid_position(self, row, col):
        return col >= self.DEFAULT_WIDTH or row >= self.DEFAULT_HEIGHT or row < 0 or col < 0
    
    def valid_position(self, row, col):
        return not self.invalid_position(row, col)

    def get_piece(self, row, col):
        if self.invalid_position(row, col):
            return None
        
        return self.pieces[row][col]
    
    def move_piece(self, from_loc, to_loc):
        pass
                
                
if __name__ == '__main__':
    Board().print_board()
#    print ([i for c in range(1, 5, 2)])