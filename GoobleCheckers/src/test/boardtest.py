'''
Created on 2011-10-02

@author: Gooble
'''
from main.game import origin
from main.game.board import Board
import unittest

class BoardTest(unittest.TestCase):
    
    def setUp(self):
        self.board = Board()

    def test_board_initial_configuration_correct(self):
        for col in range (0, Board.DEFAULT_WIDTH):
            [self.check_piece(row, col) for row in range(0, Board.DEFAULT_HEIGHT)]
                
    def check_piece(self, row, col):
        piece = self.board.get_piece(row, col)
        if row < 3 and (row + col) % 2 == 0:
            self.assertIsNotNone(piece)
            self.assertEqual(piece.get_origin(), origin.get_top())
        elif row > 4 and (row + col) % 2 == 0:
            self.assertIsNotNone(piece)
            self.assertEqual(piece.get_origin(), origin.get_bottom())
        else:
            self.assertIsNone(piece)
            
    def test_move_piece_to_invalid_location_does_nothing(self):
        original_board = Board()
        self.board.move_piece((2, 2), (5, 6))
        for row in range (0, Board.DEFAULT_HEIGHT):
            [self.check_pieces_equal(self.board.get_piece(row, col), original_board.get_piece(row, col)) for col in range(0, Board.DEFAULT_WIDTH)]
            
    def check_pieces_equal(self, piece1, piece2):
        if piece1 is None or piece2 is None:
            self.assertIsNone(piece1)
            self.assertIsNone(piece2)
            return
        
        self.assertEqual(piece1.get_origin(), piece2.get_origin())
        
    def test_move_piece_to_valid_location_only_works_if_location_is_in_move_list(self):
        self.assertIsNone(self.board.get_piece(3, 1))
        self.board.move_piece((2, 0), (3, 1))
        self.assertIsNone(self.board.get_piece(2, 0))
        self.assertIsNotNone(self.board.get_piece(3, 1))
        self.assertEqual(origin.get_top(), self.board.get_piece(3, 1).get_origin())
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()