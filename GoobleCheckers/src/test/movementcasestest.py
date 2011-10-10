'''
Created on 2011-10-08

@author: Gooble
'''
from main import origin
from main.movement import Movement
from test.util.testboard import TestBoard
import unittest


class MovementCasesTest(unittest.TestCase):

    def setUp(self):
        self.tboard = TestBoard()

    def test_get_avail_moves_with_opponent_piece_returns_jumped_position(self):
        self.tboard.place_piece(1, 5, origin.get_top())
        self.tboard.place_piece(2, 4, origin.get_bottom())
        self.calc = Movement(self.tboard.board)
        moves = self.calc.get_available_moves(1, 5)
        self.assertEqual(2, len(moves))
        self.assertEqual([(3, 3)], moves[0])
        self.assertEqual([(2, 6)], moves[1])
        
    def test_moves_case_1(self):
        # # # # # # # # # #
        #  0 1 2 3 4 5 6 7#
        #0 _ _ _ _ _ _ _ _#
        #1 _ _ _ _ _ _ _ _#
        #2 _ _ _ T _ _ _ _#
        #3 _ _ B _ B _ _ _#
        #4 _ x _ _ _ x _ _#
        #5 _ _ B _ _ _ _ _#
        #6 _ _ _ x _ _ _ _#
        #7 _ _ _ _ _ _ _ _#
        # # # # # # # # # #
        
        self.tboard.place_piece(2, 3, origin.get_top())
        self.tboard.place_piece(3, 2, origin.get_bottom())
        self.tboard.place_piece(3, 4, origin.get_bottom())
        self.tboard.place_piece(5, 2, origin.get_bottom())
        self.calc = Movement(self.tboard.board)
        moves = self.calc.get_available_moves(2, 3)
        self.assertEqual(2, len(moves))
        self.assertEqual([(4, 1), (6, 3)], moves[0])
        self.assertEqual([(4, 5)], moves[1])
        
    def test_moves_case_2(self):
        # # # # # # # # # #
        #  0 1 2 3 4 5 6 7#
        #0 _ _ _ _ _ _ _ _#
        #1 _ _ _ _ _ _ _ _#
        #2 _ _ _ T _ _ _ _#
        #3 _ _ B _ B _ _ _#
        #4 _ x _ _ _ B _ _#
        #5 _ _ B _ _ _ _ _#
        #6 _ _ _ x _ _ _ _#
        #7 _ _ _ _ B _ _ _#
        # # # # # # # # # #
        self.tboard.place_piece(2, 3, origin.get_top())
        self.tboard.place_piece(3, 2, origin.get_bottom())
        self.tboard.place_piece(3, 4, origin.get_bottom())
        self.tboard.place_piece(4, 5, origin.get_bottom())
        self.tboard.place_piece(5, 2, origin.get_bottom())
        self.tboard.place_piece(7, 4, origin.get_bottom())
        self.calc = Movement(self.tboard.board)
        moves = self.calc.get_available_moves(2, 3)
        self.assertEqual(1, len(moves))
        self.assertEqual([(4, 1), (6, 3)], moves[0])
        
    def test_moves_case_3(self):
        # # # # # # # # # #
        #  0 1 2 3 4 5 6 7#
        #0 _ _ _ _ _ _ _ _#
        #1 _ _ _ _ _ _ _ _#
        #2 _ _ _ T _ _ _ _#
        #3 _ _ B _ B _ _ _#
        #4 _ x _ _ _ _ _ _#
        #5 _ _ B _ _ _ B _#
        #6 _ _ _ B _ _ _ T#
        #7 _ _ _ _ _ _ _ _#
        # # # # # # # # # #
        self.tboard.place_piece(2, 3, origin.get_top())
        self.tboard.place_piece(3, 2, origin.get_bottom())
        self.tboard.place_piece(3, 4, origin.get_bottom())
        self.tboard.place_piece(5, 2, origin.get_bottom())
        self.tboard.place_piece(5, 6, origin.get_bottom())
        self.tboard.place_piece(6, 3, origin.get_bottom())
        self.tboard.place_piece(6, 7, origin.get_top())
        self.calc = Movement(self.tboard.board)
        moves = self.calc.get_available_moves(2, 3)
        self.assertEqual(2, len(moves))
        self.assertEqual([(4, 1)], moves[0])
        self.assertEqual([(4, 5)], moves[1])
        
    def test_moves_case_4(self):
        # # # # # # # # # #
        #  0 1 2 3 4 5 6 7#
        #0 _ _ _ T _ _ _ _#
        #1 _ _ B _ x _ _ _#
        #2 _ x _ _ _ _ _ _#
        #3 _ _ B _ _ _ _ _#
        #4 _ _ _ x _ _ _ _#
        #5 _ _ B _ _ _ _ _#
        #6 _ x _ _ _ _ _ T#
        #7 _ _ _ _ _ _ _ _#
        # # # # # # # # # #
        self.tboard.place_piece(0, 3, origin.get_top())
        self.tboard.place_piece(1, 2, origin.get_bottom())
        self.tboard.place_piece(3, 2, origin.get_bottom())
        self.tboard.place_piece(5, 2, origin.get_bottom())
        self.calc = Movement(self.tboard.board)
        moves = self.calc.get_available_moves(0, 3)
        self.assertEqual(2, len(moves))
        self.assertEqual([(2, 1), (4, 3), (6, 1)], moves[0])
        self.assertEqual([(1, 4)], moves[1])
        
    def test_moves_case_5(self):
        # # # # # # # # # #
        #  0 1 2 3 4 5 6 7#
        #0 _ _ _ T _ _ _ _#
        #1 _ _ B _ x _ _ _#
        #2 _ x _ _ _ _ _ _#
        #3 _ _ B _ _ _ _ _#
        #4 _ _ _ x _ _ _ _#
        #5 _ _ B _ B _ _ _#
        #6 _ x _ _ _ x _ _#
        #7 _ _ _ _ _ _ _ _#
        # # # # # # # # # #
        self.tboard.place_piece(0, 3, origin.get_top())
        self.tboard.place_piece(1, 2, origin.get_bottom())
        self.tboard.place_piece(3, 2, origin.get_bottom())
        self.tboard.place_piece(5, 2, origin.get_bottom())
        self.tboard.place_piece(5, 4, origin.get_bottom())
        self.calc = Movement(self.tboard.board)
        moves = self.calc.get_available_moves(0, 3)
        self.assertEqual(3, len(moves))
        self.assertEqual([(2, 1), (4, 3), (6, 1)], moves[0])
        self.assertEqual([(2, 1), (4, 3), (6, 5)], moves[1])
        self.assertEqual([(1, 4)], moves[2])
        
    def test_cannot_jump_over_own_kind(self):
        # # # # # # # # # #
        #  0 1 2 3 4 5 6 7#
        #0 _ _ _ _ _ _ _ _#
        #1 _ _ _ _ _ _ _ _#
        #2 _ _ _ _ _ _ _ _#
        #3 _ _ T _ _ _ _ _#
        #4 _ T _ T _ _ _ _#
        #5 _ _ _ _ _ _ _ _#
        #6 _ _ _ _ _ _ _ _#
        #7 _ _ _ _ _ _ _ _#
        # # # # # # # # # #
        self.tboard.place_piece(3, 2, origin.get_top())
        self.tboard.place_piece(4, 1, origin.get_top())
        self.tboard.place_piece(4, 3, origin.get_top())
        self.calc = Movement(self.tboard.board)
        moves = self.calc.get_available_moves(3, 2)
        self.assertEqual(0, len(moves))
        
    def test_cannot_jump_over_own_kind_case_2(self):
        # # # # # # # # # #
        #  0 1 2 3 4 5 6 7#
        #0 _ _ _ _ _ _ _ _#
        #1 _ _ _ _ _ _ _ _#
        #2 _ _ _ _ _ _ _ _#
        #3 _ _ T _ _ _ _ _#
        #4 _ T _ B _ _ _ _#
        #5 _ _ _ _ x _ _ _#
        #6 _ _ _ _ _ T _ _#
        #7 _ _ _ _ _ _ _ _#
        # # # # # # # # # #
        self.tboard.place_piece(3, 2, origin.get_top())
        self.tboard.place_piece(4, 1, origin.get_top())
        self.tboard.place_piece(4, 3, origin.get_bottom())
        self.tboard.place_piece(6, 5, origin.get_top())
        self.calc = Movement(self.tboard.board)
        moves = self.calc.get_available_moves(3, 2)
        self.assertEqual(1, len(moves))
        self.assertEqual([(5, 4)], moves[0])
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'MovementCasesTest.testName']
    unittest.main()