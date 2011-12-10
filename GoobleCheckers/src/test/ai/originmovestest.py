'''
Created on 2011-12-10

@author: Gooble
'''
import unittest
from main.game import origin
from test.util.testboard import TestBoard
from test.util.testcase import as_move_list
import main.game.movements.movement as movement

class OriginMoves(object):
    
    def __init__(self, board):
        self.board = board
        
    def get_moves_for(self, origin):
        all_moves = []
        for row in range(0, self.board.DEFAULT_HEIGHT):
            for col in range(0, self.board.DEFAULT_WIDTH):
                if self.board.get_piece(row, col) is not None and self.board.get_piece(row, col).get_origin() == origin:
                    all_moves.append(movement.Movement(self.board, row, col).get_available_moves())
            
        return all_moves

class OriginMovesTest(unittest.TestCase):
    
    def setUp(self):
        self.tboard = TestBoard()
        
    def test_get_all_moves_for_given_origin(self):
        # # # # # # # # # #
        #  0 1 2 3 4 5 6 7#
        #0 _ _ _ _ _ _ _ _#
        #1 _ _ _ _ _ _ _ _#
        #2 _ _ _ _ _ _ _ _#
        #3 _ x x _ x _ _ _#
        #4 B _ _ B _ _ _ _#
        #5 _ _ _ _ x _ x _#
        #6 _ _ _ _ _ B _ _#
        #7 _ _ _ _ _ _ _ _#
        # # # # # # # # # #
        self.tboard.place_piece(4, 0, origin.BOTTOM)
        self.tboard.place_piece(4, 3, origin.BOTTOM)
        self.tboard.place_piece(6, 5, origin.BOTTOM)
        allmoves = OriginMoves(self.tboard.board).get_moves_for(origin.BOTTOM)
        
        self.assertEqual(1, len(allmoves[0]))
        self.assertEqual(as_move_list([(4, 0), (3, 1)]), allmoves[0][0])
        
        self.assertEqual(2, len(allmoves[1]))
        self.assertEqual(as_move_list([(4, 3), (3, 2)]), allmoves[1][0])
        self.assertEqual(as_move_list([(4, 3), (3, 4)]), allmoves[1][1])
        
        self.assertEqual(2, len(allmoves[1]))
        self.assertEqual(as_move_list([(6, 5), (5, 4)]), allmoves[2][0])
        self.assertEqual(as_move_list([(6, 5), (5, 6)]), allmoves[2][1])

if __name__ == "__main__":
    unittest.main()