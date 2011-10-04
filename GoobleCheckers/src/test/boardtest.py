'''
Created on 2011-10-02

@author: Gooble
'''
import unittest
from main.board import Board
from main.origin import Origin

class BoardTest(unittest.TestCase):

    def test_board_initial_configuration_correct(self):
        board = Board()
        for col in range (0, Board.DEFAULT_WIDTH):
            [self.check_piece(board, row, col) for row in range(0, Board.DEFAULT_HEIGHT)]
                
    def check_piece(self, board, row, col):
        piece = board.get_piece(row, col)
        if row < 3 and (row + col) % 2 == 0:
            self.assertIsNotNone(piece)
            self.assertEqual(piece.get_origin(), Origin.TOP)
        elif row > 4 and (row + col) % 2 == 0:
            self.assertIsNotNone(piece)
            self.assertEqual(piece.get_origin(), Origin.BOTTOM)
        else:
            self.assertIsNone(piece)
            
    def test_move_piece_to_invalid_location_does_nothing(self):
        original_board = Board()
        board = Board()
        board.move_piece((2, 2), (5, 6))
        for row in range (0, Board.DEFAULT_HEIGHT):
            [self.check_pieces_equal(board.get_piece(row, col), original_board.get_piece(row, col)) for col in range(0, Board.DEFAULT_WIDTH)]
            
    def check_pieces_equal(self, piece1, piece2):
        if piece1 is None or piece2 is None:
            self.assertIsNone(piece1)
            self.assertIsNone(piece2)
            return
        
        self.assertEqual(piece1.get_origin(), piece2.get_origin())
            

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()