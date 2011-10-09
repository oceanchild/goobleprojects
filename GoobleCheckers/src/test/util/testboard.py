'''
Created on 2011-10-05

@author: Gooble
'''
from main.board import Board, Piece
from main import origin

class TestBoard(object):

    def __init__(self):
        self.board = Board()
        self.clear_board()
        
    def clear_board(self):
        self.board.pieces = [[None] * Board.DEFAULT_WIDTH for row in self.board.pieces]
        
    def place_piece(self, row, col, origin):
        self.board.pieces[row][col] = Piece(origin)
        
    def place_king(self, row, col, origin):
        self.place_piece(row, col, origin);
        self.board.get_piece(row, col).set_king(True)
        
        
if __name__ == '__main__':
    board = TestBoard()
    board.place_piece(3, 5, origin.get_top())
