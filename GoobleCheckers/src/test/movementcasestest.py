'''
Created on 2011-10-08

@author: Gooble
'''
from main import origin
from main.move_calculator import MoveCalculator
from test.util.testboard import TestBoard
import unittest


class Test(unittest.TestCase):


    def setUp(self):
        self.tboard = TestBoard()


    def test_get_avail_moves_with_opponent_piece_returns_jumped_position(self):
        self.tboard.place_piece(1, 5, origin.get_top())
        self.tboard.place_piece(2, 4, origin.get_bottom())
        self.calc = MoveCalculator(self.tboard.board)
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
        self.calc = MoveCalculator(self.tboard.board)
        moves = self.calc.get_available_moves(2, 3)
        self.assertEqual(2, len(moves))
        print(moves)
        self.assertEqual([(4, 1), (6, 3)], moves[0])
        self.assertEqual([(4, 5)], moves[1])


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()