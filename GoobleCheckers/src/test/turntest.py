'''
Created on 2011-10-16

@author: Gooble
'''
import unittest
from test.util.testboard import TestBoard
from main import origin
from main.movement import Movement


class TurnTest(unittest.TestCase):
    
    def setUp(self):
        self.tboard = TestBoard()

    def test_cannot_move_opponent_piece_while_player_move_not_complete(self):
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
        calc = Movement(self.tboard.board, 2, 3)
        moves = calc.get_available_moves()
        self.assertEqual(2, len(moves))
        self.assertEqual([(4, 1), (6, 3)], moves[0])
        self.assertEqual([(4, 5),], moves[1])
        
        self.tboard.board.move_piece((2, 3), (4, 1))
        self.assertIsNone(self.tboard.board.get_piece(2, 3))
        self.assertIsNotNone(self.tboard.board.get_piece(4, 1))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()