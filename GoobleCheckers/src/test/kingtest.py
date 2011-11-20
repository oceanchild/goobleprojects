'''
Created on 2011-11-20

@author: Gooble
'''
import unittest
from test.util.testboard import TestBoard
from main import origin


class Test(unittest.TestCase):


    def setUp(self):
        self.tboard = TestBoard()


    def test_piece_becomes_king_when_reaching_other_side(self):
        # # # # # # # # # #
        #  0 1 2 3 4 5 6 7#
        #0 _ _ _ _ _ _ _ _#
        #1 _ _ _ _ _ _ _ _#
        #2 _ _ _ _ _ _ _ _#
        #3 _ _ _ _ _ _ _ _#
        #4 _ _ _ _ _ _ _ _#
        #5 _ _ _ T _ _ _ _#
        #6 _ _ B _ x _ _ _#
        #7 _ x _ _ _ _ _ _#
        # # # # # # # # # #
        self.tboard.place_piece(5, 3, origin.get_top())
        self.tboard.place_piece(6, 2, origin.get_bottom())

        self.tboard.board.move_piece((5, 3), (7, 1))
        self.assertIsNone(self.tboard.board.get_piece(5, 3))
        self.assertIsNone(self.tboard.board.get_piece(6, 2))
        self.assertIsNotNone(self.tboard.board.get_piece(7, 1))
        
        self.assertTrue(self.tboard.board.get_piece(7, 1).is_king())


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_piece_becomes_king_when_reaching_other_side']
    unittest.main()