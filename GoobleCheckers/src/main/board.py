'''
Created on 2011-10-02

@author: Gooble
'''
from main.colour import Colour

class Piece(object):
    
    def __init__(self, colour):
        self.colour = colour
        
    def get_colour(self):
        return self.colour


class Board(object):
    
    DEFAULT_WIDTH = 8
    DEFAULT_HEIGHT = 8

    def __init__(self):
        self.init_board()
        
    def init_board(self):
        self.pieces = []
        for i in range (0, self.DEFAULT_WIDTH):
            self.pieces.append([self.create_piece(i, j) for j in range(0, self.DEFAULT_HEIGHT)])
            
            
    def create_piece(self, i, j):
        if i < (self.DEFAULT_HEIGHT / 2 - 1) and (i+j) % 2 == 0:
            return Piece(Colour.RED)
        elif i > (self.DEFAULT_HEIGHT / 2) and (i+j) % 2 == 0:
            return Piece(Colour.BLACK)
        else:
            return None
        
        
    def get_piece(self, i, j):
        if i >= self.DEFAULT_WIDTH or j >= self.DEFAULT_HEIGHT or j < 0 or i < 0:
            return None
        
        return self.pieces[i][j]
    
    
    def print_board(self):
        for row_of_pieces in self.pieces:
            for piece in row_of_pieces:
                if piece is not None:
                    print(piece.get_colour()[:1], end=' ')
                else:
                    print(' ', end=' ')
            print()
                
                
if __name__ == '__main__':
    Board().print_board()