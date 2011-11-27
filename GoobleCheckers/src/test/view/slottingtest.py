'''
Created on 2011-11-27

@author: Gooble
'''
import unittest
from main.game.board import Board
from main.view.slotting import Slotting

class MockEvent(object):
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

class SlottingTest(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        self.slotting = Slotting(self.board)

    def test_piece_gets_selected_and_slotted_when_slot_is_valid_move(self):
        self.assertIsNone(self.board.current_turn.piece)
        self.slotting.select_piece(MockEvent(140, 140))
        self.assertIsNotNone(self.board.current_turn.piece)
        self.assertEqual(2, self.slotting.start_row)
        self.assertEqual(2, self.slotting.start_col)
        self.slotting.release_piece(MockEvent(100, 200))
        self.assertIsNone(self.board.get_piece(2, 2))
        self.assertIsNotNone(self.board.get_piece(3, 1))
        
    def test_piece_does_not_get_placed_in_new_slot_when_invalid_move(self):
        self.slotting.select_piece(MockEvent(100, 100))
        self.assertIsNotNone(self.board.current_turn.piece)
        self.assertEqual(1, self.slotting.start_row)
        self.assertEqual(1, self.slotting.start_col)
        self.slotting.release_piece(MockEvent(300, 300))
        self.assertIsNotNone(self.board.get_piece(1, 1))
        self.assertIsNotNone(self.board.get_piece(2, 2))
        self.assertIsNone(self.board.get_piece(3, 1))
        self.assertIsNone(self.board.get_piece(4, 4))


if __name__ == "__main__":
    unittest.main()