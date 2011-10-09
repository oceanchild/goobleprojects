'''
Created on 2011-10-08

@author: Gooble
'''
import unittest
from test.util.testboard import TestBoard
from main import origin
from main.movement import Movement


class KingMovementTest(unittest.TestCase):

    def setUp(self):
        self.tboard = TestBoard()

    def test_king_can_move_in_either_direction(self):
        # # # # # # # # # #
        #  0 1 2 3 4 5 6 7#
        #0 _ _ _ _ _ _ _ _#
        #1 _ _ _ _ _ _ _ _#
        #2 _ x _ x _ _ _ _#
        #3 _ _ b _ _ _ _ _#
        #4 _ x _ T _ _ _ _#
        #5 _ _ _ _ x _ _ _#
        #6 _ _ _ _ _ _ _ _#
        #7 _ _ _ _ _ _ _ _#
        # # # # # # # # # #
        self.tboard.place_king(3, 2, origin.get_bottom())
        self.tboard.place_piece(4, 3, origin.get_top())
        self.calc = Movement(self.tboard.board)
        moves = self.calc.get_available_moves(3, 2)
        self.assertEqual(4, len(moves))
        self.assertEqual([(4, 1)], moves[0])
        self.assertEqual([(5, 4)], moves[1])
        self.assertEqual([(2, 1)], moves[2])
        self.assertEqual([(2, 3)], moves[3])


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'KingMovementTest.testName']
    unittest.main()