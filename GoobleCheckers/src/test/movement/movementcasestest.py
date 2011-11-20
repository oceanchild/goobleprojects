'''
Created on 2011-10-08

@author: Gooble
'''
from main.game import origin
from main.game.movements.movement import Movement
from test.util.testboard import TestBoard
from test.util.testcase import as_move_list
import unittest

class MovementCasesTest(unittest.TestCase):

    def setUp(self):
        self.tboard = TestBoard()

    def test_get_avail_moves_with_opponent_piece_returns_jumped_position(self):
        self.tboard.place_piece(1, 5, origin.get_top())
        self.tboard.place_piece(2, 4, origin.get_bottom())
        calc = Movement(self.tboard.board, 1, 5)
        moves = calc.get_available_moves()
        self.assertEqual(2, len(moves))
        self.assertEqual(as_move_list([(1, 5), (3, 3)]), moves[0])
        self.assertEqual(as_move_list([(1, 5), (2, 6)]), moves[1])
        
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
        calc = Movement(self.tboard.board, 2, 3)
        moves = calc.get_available_moves()
        self.assertEqual(2, len(moves))
        self.assertEqual(as_move_list([(2, 3), (4, 1), (6, 3)]), moves[0])
        self.assertEqual(as_move_list([(2, 3), (4, 5)]), moves[1])
        
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
        calc = Movement(self.tboard.board, 2, 3)
        moves = calc.get_available_moves()
        self.assertEqual(1, len(moves))
        self.assertEqual(as_move_list([(2, 3), (4, 1), (6, 3)]), moves[0])
        
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
        calc = Movement(self.tboard.board, 2, 3)
        moves = calc.get_available_moves()
        self.assertEqual(2, len(moves))
        self.assertEqual(as_move_list([(2, 3), (4, 1)]), moves[0])
        self.assertEqual(as_move_list([(2, 3), (4, 5)]), moves[1])
        
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
        calc = Movement(self.tboard.board, 0, 3)
        moves = calc.get_available_moves()
        self.assertEqual(2, len(moves))
        self.assertEqual(as_move_list([(0, 3), (2, 1), (4, 3), (6, 1)]), moves[0])
        self.assertEqual(as_move_list([(0, 3), (1, 4)]), moves[1])
        
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
        calc = Movement(self.tboard.board, 0, 3)
        moves = calc.get_available_moves()
        self.assertEqual(3, len(moves))
        self.assertEqual(as_move_list([(0, 3), (2, 1), (4, 3), (6, 1)]), moves[0])
        self.assertEqual(as_move_list([(0, 3), (2, 1), (4, 3), (6, 5)]), moves[1])
        self.assertEqual(as_move_list([(0, 3), (1, 4)]), moves[2])
        
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
        calc = Movement(self.tboard.board, 3, 2)
        moves = calc.get_available_moves()
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
        calc = Movement(self.tboard.board, 3, 2)
        moves = calc.get_available_moves()
        self.assertEqual(1, len(moves))
        self.assertEqual(as_move_list([(3, 2), (5, 4)]), moves[0])

        
    def test_move_top_piece_along_and_do_some_backward_movement_to_trip_stuff_up(self):
        # # # # # # # # # #
        #  0 1 2 3 4 5 6 7#
        #0 _ _ _ _ _ _ _ _#
        #1 _ _ _ T _ _ _ _#
        #2 _ _ B _ x _ _ _#
        #3 _ x _ _ _ _ _ _#
        #4 _ _ B _ _ _ _ _#
        #5 _ _ _ x _ _ _ _#
        #6 _ _ _ _ B _ _ _#
        #7 _ _ _ _ _ x _ _#
        # # # # # # # # # #
        self.tboard.place_piece(1, 3, origin.get_top())
        self.tboard.place_piece(2, 2, origin.get_bottom())
        self.tboard.place_piece(4, 2, origin.get_bottom())
        self.tboard.place_piece(6, 4, origin.get_bottom())
        moves = Movement(self.tboard.board, 1, 3).get_available_moves()
        self.assertEqual(2, len(moves))
        self.assertEqual(as_move_list([(1, 3), (3, 1), (5, 3), (7, 5)]), moves[0])
        self.assertEqual(as_move_list([(1, 3), (2, 4)]), moves[1])
        
        self.tboard.board.move_piece((1, 3), (3, 1))
        self.assertIsNone(self.tboard.board.get_piece(1, 3))
        self.assertIsNotNone(self.tboard.board.get_piece(2, 2))
        self.assertIsNotNone(self.tboard.board.get_piece(3, 1))
        
        moves = Movement(self.tboard.board, 3, 1).get_available_moves()
        self.assertEqual(2, len(moves))
        self.assertEqual(as_move_list([(3, 1), (4, 0)]), moves[0])
        self.assertEqual(as_move_list([(3, 1), (5, 3), (7, 5)]), moves[1])
        
        # move backward just to trip things up
        self.tboard.board.move_piece((3, 1), (1, 3))
        self.assertIsNone(self.tboard.board.get_piece(3, 1))
        self.assertIsNotNone(self.tboard.board.get_piece(2, 2))
        self.assertIsNotNone(self.tboard.board.get_piece(1, 3))
        
        moves = Movement(self.tboard.board, 1, 3).get_available_moves()
        self.assertEqual(2, len(moves))
        self.assertEqual(as_move_list([(1, 3), (3, 1), (5, 3), (7, 5)]), moves[0])
        ### bug-- it's 1,3 instead of 2,4 because 2,4 is gone- it's gone because
        ### you've jumped a piece so valid jumps are no longer there. 1,3 shouldn't be there either
        ### the problem is : if you're going backwards, pieces shouldn't be jumped over. Moves are different
        ### they're not just locations. there has to be a Move Object -> and this object will say whether
        ### it's a backwards movement, or a jumped movement, or just a regular movement
        ### time for some massive refactoring because we've been using tuples as moves...
        
        ### well, we don't want to take out all instances of tuples. maybe the inner functioning will change.
        ### ie the implementation details. 
        ### each time you make a move, the list of moves will have a new MOVE object.
        
        ### post-refactoring: The move is now off the list because there are moves in the moves object for the turn.
        ### this a bug that has been fixed using this test.-->actually, was the bug even there?
        self.assertEqual(as_move_list([(1, 3), (2, 4)]), moves[1])
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'MovementCasesTest.testName']
    unittest.main()