'''
Created on 2011-10-03

@author: Gooble
'''
import unittest
from main.board import Board
from main.move_calculator import MoveCalculator


class MovementCalculatorTest(unittest.TestCase):

    def test_get_available_moves_from_location_with_no_piece(self):
        calc = MoveCalculator(Board())
        moves = calc.get_available_moves(0, 1)
        self.assertEqual(len(moves), 0)
        
    def test_get_avail_moves_from_location_with_piece_that_can_move(self):
        calc = MoveCalculator(Board())
        moves = calc.get_available_moves(2, 2);
        self.assertEqual(len(moves), 2)
        self.assertEqual((3, 1), moves[0])
        self.assertEqual((3, 3), moves[1])
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()