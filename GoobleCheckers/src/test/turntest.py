'''
Created on 2011-10-16

@author: Gooble
'''
import unittest
from test.util.testboard import TestBoard
from main import origin
from main.movement import Movement
from main.turn import Turn


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
        
        self.tboard.board.move_piece((3, 2), (2, 1))
        self.assertIsNotNone(self.tboard.board.get_piece(3, 2))
        self.assertIsNone(self.tboard.board.get_piece(2, 1))
        
    def test_cannot_move_a_new_piece_while_move_in_progress_even_if_on_same_side(self):
        # # # # # # # # # #
        #  0 1 2 3 4 5 6 7#
        #0 _ _ _ _ _ _ x _#
        #1 _ _ _ _ _ T _ _#
        #2 _ _ _ _ x _ _ _#
        #3 _ x _ T _ _ _ _#
        #4 _ _ B _ _ _ _ _#
        #5 _ _ _ _ _ _ _ _#
        #6 _ _ _ _ B _ _ _#
        #7 _ _ _ _ _ _ _ _#
        # # # # # # # # # #
        self.tboard.place_piece(1, 5, origin.get_top())
        self.tboard.place_piece(3, 3, origin.get_top())
        self.tboard.place_piece(4, 2, origin.get_bottom())
        self.tboard.place_piece(6, 4, origin.get_bottom())
        calc = Movement(self.tboard.board, 4, 2)
        moves = calc.get_available_moves()
        self.assertEqual(2, len(moves))
        self.assertEqual([(3, 1)], moves[0])
        self.assertEqual([(2, 4), (0, 6)], moves[1])
        self.tboard.board.current_turn = Turn(origin.get_top())
        # start move
        self.tboard.board.move_piece((4, 2), (2, 4))
        self.assertIsNone(self.tboard.board.get_piece(4, 2))
        self.assertIsNotNone(self.tboard.board.get_piece(2, 4))
        
        # make sure can't move another piece of same type
        calc = Movement(self.tboard.board, 6, 4)
        moves = calc.get_available_moves()
        self.assertEqual(2, len(moves)) 
        self.assertEqual([(5, 3)], moves[0])
        self.assertEqual([(5, 5)], moves[1])
        self.tboard.board.move_piece((6, 4), (5, 5))
        self.assertIsNone(self.tboard.board.get_piece(5, 5))
        self.assertIsNotNone(self.tboard.board.get_piece(6, 4))
        
    def test_once_move_completed_jumped_pieces_eaten(self):
        # # # # # # # # # #
        #  0 1 2 3 4 5 6 7#
        #0 _ _ _ _ _ _ x _#
        #1 _ _ _ _ _ T _ _#
        #2 x _ _ _ x _ _ _#
        #3 _ T _ T _ _ _ _#
        #4 _ _ B _ _ _ _ _#
        #5 _ _ _ x _ _ _ _#
        #6 _ _ _ _ B _ _ _#
        #7 _ _ _ _ _ x _ _#
        # # # # # # # # # #
        self.tboard.place_piece(1, 5, origin.get_top())
        self.tboard.place_piece(3, 1, origin.get_top())
        self.tboard.place_piece(3, 3, origin.get_top())
        self.tboard.place_piece(4, 2, origin.get_bottom())
        self.tboard.place_piece(6, 4, origin.get_bottom())
        calc = Movement(self.tboard.board, 4, 2)
        moves = calc.get_available_moves()
        self.assertEqual(2, len(moves))
        self.assertEqual([(2, 0)], moves[0])
        self.assertEqual([(2, 4), (0, 6)], moves[1])
        self.tboard.board.current_turn = Turn(origin.get_top())
        self.tboard.board.move_piece((4, 2), (2, 4))
        self.tboard.board.move_piece((2, 4), (0, 6))
        
        self.assertIsNone(self.tboard.board.get_piece(4, 2))
        self.assertIsNone(self.tboard.board.get_piece(3, 3))
        self.assertIsNone(self.tboard.board.get_piece(2, 4))
        self.assertIsNone(self.tboard.board.get_piece(1, 5))
        self.assertIsNotNone(self.tboard.board.get_piece(0, 6))
        
    def test_can_move_opponent_piece_only_once_move_complete(self):
        # # # # # # # # # #
        #  0 1 2 3 4 5 6 7#
        #0 _ _ _ _ _ _ x _#
        #1 _ _ _ _ _ T _ _#
        #2 _ _ x _ x _ _ _#
        #3 _ T _ T _ x _ _#
        #4 _ _ B _ B _ _ _#
        #5 _ _ _ _ _ _ _ _#
        #6 _ _ _ _ _ _ _ _#
        #7 _ _ _ _ _ _ _ _#
        # # # # # # # # # #
        self.tboard.place_piece(1, 5, origin.get_top())
        self.tboard.place_piece(3, 1, origin.get_top())
        self.tboard.place_piece(3, 3, origin.get_top())
        self.tboard.place_piece(4, 2, origin.get_bottom())
        self.tboard.place_piece(4, 4, origin.get_bottom())
        self.tboard.board.current_turn = Turn(origin.get_top())
        self.tboard.board.move_piece((4, 2), (2, 4))
        self.assertIsNone(self.tboard.board.get_piece(4, 2))
        self.tboard.board.move_piece((2, 4), (0, 6))
        
        self.tboard.board.move_piece((4, 4), (3, 5))
        self.assertIsNotNone(self.tboard.board.get_piece(4, 4))
        self.assertIsNone(self.tboard.board.get_piece(3, 5))
        
        self.tboard.board.move_piece((3, 1), (4, 2))
        self.assertIsNone(self.tboard.board.get_piece(3, 1))
        self.assertIsNotNone(self.tboard.board.get_piece(4, 2))
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()