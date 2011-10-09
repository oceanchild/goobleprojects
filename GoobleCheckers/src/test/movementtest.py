'''
Created on 2011-10-03

@author: Gooble
'''
import unittest
from main.board import Board
from main.movement import Movement


class MovementCalculatorTest(unittest.TestCase):

    def setUp(self):
        self.calc = Movement(Board())

    def test_get_available_moves_from_location_with_no_piece(self):
        moves = self.calc.get_available_moves(0, 1)
        self.assertEqual(len(moves), 0)
        
    def test_get_avail_moves_from_location_with_piece_that_can_move_from_top(self):
        moves = self.calc.get_available_moves(2, 2);
        self.assertEqual(len(moves), 2)
        self.assertEqual([(3, 1)], moves[0])
        self.assertEqual([(3, 3)], moves[1])
        
    def test_get_avail_moves_from_location_with_piece_that_can_move_from_bottom(self):
        moves = self.calc.get_available_moves(5, 1)
        self.assertEqual(len(moves), 2)
        self.assertEqual([(4, 0)], moves[0])
        self.assertEqual([(4, 2)], moves[1])
        
    def test_get_avail_moves_from_corner_location_from_bottom_gives_only_one_valid_move(self):
        moves = self.calc.get_available_moves(5, 7)
        self.assertEqual(len(moves), 1)
        self.assertEqual([(4, 6)], moves[0])
        
    def test_get_avail_moves_from_corner_location_from_top_gives_only_one_valid_move(self):
        moves = self.calc.get_available_moves(2, 0)
        self.assertEqual(len(moves), 1)
        self.assertEqual([(3, 1)], moves[0])
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()