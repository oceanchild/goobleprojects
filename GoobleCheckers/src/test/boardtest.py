'''
Created on 2011-10-02

@author: Gooble
'''
from main.game import origin
from main.game.board import Board
from test.util.testboard import TestBoard
import unittest

class BoardTest(unittest.TestCase):
    
    def setUp(self):
        self.board = Board()
        self.tboard = TestBoard()

    def test_board_initial_configuration_correct(self):
        for col in range (0, Board.DEFAULT_WIDTH):
            [self.check_piece(row, col) for row in range(0, Board.DEFAULT_HEIGHT)]
                
    def check_piece(self, row, col):
        piece = self.board.get_piece(row, col)
        if row < 3 and (row + col) % 2 == 0:
            self.assertIsNotNone(piece)
            self.assertTrue(piece.is_from_top())
        elif row > 4 and (row + col) % 2 == 0:
            self.assertIsNotNone(piece)
            self.assertTrue(piece.is_from_bottom())
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
        self.assertTrue(self.board.get_piece(3, 1).is_from_top())
        
    def test_game_over_when_one_type_of_piece_runs_out_simple_board(self):
        # # # # # # # # # #
        #  0 1 2 3 4 5 6 7#
        #0 _ _ _ _ _ _ _ _#
        #1 x _ x _ _ _ _ _#
        #2 _ t _ _ _ _ _ _#
        #3 x _ B _ _ _ _ _#
        #4 _ _ _ x _ _ _ _#
        #5 _ _ _ _ _ _ _ _#
        #6 _ _ _ _ _ _ _ _#
        #7 _ _ _ _ _ _ _ _#
        # # # # # # # # # #
        self.tboard.place_king(2, 1, origin.TOP)
        self.tboard.place_piece(3, 2, origin.BOTTOM)
        
        self.assertFalse(self.tboard.board.is_game_over())
        self.tboard.board.move_piece((2, 1), (4, 3))
        self.assertTrue(self.tboard.board.is_game_over())
        
        self._check_board_empty_except([(4, 3)])
        self.assertTrue(self.tboard.board.is_game_over())
        
    def _check_board_empty_except(self, list_of_exceptions):
        for row in range(0, Board.DEFAULT_HEIGHT):
            for col in range (0, Board.DEFAULT_WIDTH):
                if (row, col) in list_of_exceptions: continue
                self.assertIsNone(self.tboard.board.get_piece(row, col))
                
        for loc in list_of_exceptions:
            self.assertIsNotNone(self.tboard.board.get_piece(loc[0], loc[1]))
        
    def test_game_over_when_one_type_of_piece_runs_out_less_simple_board(self):
        # # # # # # # # # #
        #  0 1 2 3 4 5 6 7#
        #0 _ _ _ _ _ _ _ _#
        #1 x _ x _ _ _ _ _#
        #2 _ t _ _ _ _ _ _#
        #3 x _ B _ _ _ _ _#
        #4 _ _ _ x _ B _ _#
        #5 _ _ _ _ _ _ _ _#
        #6 _ _ _ _ _ _ _ _#
        #7 _ _ _ _ _ _ _ _#
        # # # # # # # # # #
        self.tboard.place_king(2, 1, origin.TOP)
        self.tboard.place_piece(3, 2, origin.BOTTOM)
        self.tboard.place_piece(4, 5, origin.BOTTOM)
        
        self.assertFalse(self.tboard.board.is_game_over())
        self.tboard.board.move_piece((2, 1), (4, 3))
        self._check_board_empty_except([(4, 3), (4, 5)])
        
        self.assertFalse(self.tboard.board.is_game_over())
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()