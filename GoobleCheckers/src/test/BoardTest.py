'''
Created on 2011-10-02

@author: Gooble
'''
import unittest
from main.board import Board
from main.colour import Colour

class BoardMovementTest(unittest.TestCase):


    def test_board_initial_configuration_correct(self):
        board = Board()
        # red on top black on bottom
        for i in range (0, Board.DEFAULT_WIDTH):
            [self.check_piece(board, i, j) for j in range(0, Board.DEFAULT_HEIGHT)]
                
                
    def check_piece(self, board, i, j):
        if i < 3 and (i + j) % 2 == 0:
            assert board.get_piece(i, j) is not None and board.get_piece(i, j).get_colour() == Colour.RED
        elif i > 4 and (i + j) % 2 == 0:
            assert board.get_piece(i, j) is not None and board.get_piece(i, j).get_colour() == Colour.BLACK
        else:
            assert board.get_piece(i, j) is None
            
    def test_can_move_piece_diagonally(self):
        board = Board()
        
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()