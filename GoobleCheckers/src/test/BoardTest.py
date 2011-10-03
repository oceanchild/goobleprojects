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
        piece = board.get_piece(i, j)
        if i < 3 and (i + j) % 2 == 0:
            self.assertIsNotNone(piece)
            self.assertEqual(piece.get_colour(), Colour.RED)
        elif i > 4 and (i + j) % 2 == 0:
            self.assertIsNotNone(piece)
            self.assertEqual(piece.get_colour(), Colour.BLACK)
        else:
            self.assertIsNone(piece)
            
    def test_get_available_moves_from_location_with_no_piece(self):
        board = Board()
        moves = board.get_available_moves(0, 1)
        self.assertEqual(len(moves), 0)
        
    def test_get_avail_moves_from_location_with_piece_that_can_move(self):
        board = Board()
        moves = board.get_available_moves(2, 2);
        self.assertEqual(len(moves), 2)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()