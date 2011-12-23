'''
Created on 2011-12-20

@author: Gooble
'''
import unittest
from main.game import origin
from test.util.testboard import TestBoard
from test.util.testcase import as_move_list
import copy
from main.ai.originmoves import OriginMoves


class BestMovementWithDepth(object):
    
    def __init__(self, depth, origin):
        self.depth = depth
        self.origin = origin
        
    def calculate_for(self, game):
        best_score = 0
        best_move = None
        all_moves = OriginMoves(game.board, self.origin).get_moves()
        
        


class SmartAITest(unittest.TestCase):

    def setUp(self):
        self.tboard = TestBoard()

    def test_calculate_moves_up_to_depth_one_does_not_touch_original_board_and_selects_best_move_considering_others_result_in_more_lost_pieces(self):
        # # # # # # # # # #
        #  0 1 2 3 4 5 6 7#
        #0 _ _ _ _ _ _ _ _#
        #1 _ _ _ _ _ _ _ _#
        #2 _ _ T _ _ _ _ _#
        #3 _ x _ x _ _ _ _#
        #4 B _ _ _ _ _ _ _#
        #5 _ _ _ _ _ _ _ _#
        #6 _ _ _ _ _ _ _ _#
        #7 _ _ _ _ _ _ _ _#
        # # # # # # # # # #
        self.tboard.place_piece(2, 2, origin.TOP)
        self.tboard.place_piece(4, 0, origin.BOTTOM)
        best_move = BestMovementWithDepth(1, origin.TOP).calculate_for(self.tboard.game)
        self.assertEquals(as_move_list([(2, 2), (3, 1)]), best_move)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()