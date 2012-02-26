'''
Created on 2012-02-26

@author: Gooble
'''
import unittest
from main.view.drawables import Drawables, DrawableBackground, DrawablePiece,\
    BLUE, WHITE, BLACK, DrawableKing, RED
from main.game import origin
from main.game.piece import Piece

class MockGame(object):
    def __init__(self):
        top_king = Piece(origin.TOP)
        top_king.set_king(True)
        bottom_king = Piece(origin.BOTTOM)
        bottom_king.set_king(True)
        self.pieces = [[Piece(origin.TOP), None, top_king], 
                       [Piece(origin.BOTTOM), None, bottom_king]]
        
    def get_tile_width(self):
        return 10
    def get_tile_height(self):
        return 15
    
    def get_num_rows(self):
        return len(self.pieces)
    
    def get_num_cols(self):
        return len(self.pieces[0])
    
    def get_piece(self, row, col):
        return self.pieces[row][col]

class MockSlotting(object):
    def __init__(self, row=None, col=None):
        self.row = row
        self.col = col
    
    def is_holding_piece(self, row, col):
        return row == self.row and col == self.col

class Test(unittest.TestCase):

    def test_create_when_not_holding_piece(self):
        game = MockGame()
        slotting = MockSlotting()
        drawables = Drawables(game, slotting).create(None)
        
        # two drawables per occupied slot, and one drawable per unoccupied --> 4 * 2 + 2 = 10
        self.assertEqual(10, len(drawables))
        
        self.assertEqual(DrawableBackground(0, 0, 10, 15, WHITE), drawables[0])
        self.assertEqual(DrawablePiece(0, 0, 10, 15, BLACK), drawables[1])
        
        self.assertEqual(DrawableBackground(10, 0, 10, 15, BLUE), drawables[2])
        
        self.assertEqual(DrawableBackground(20, 0, 10, 15, WHITE), drawables[3])
        self.assertEqual(DrawableKing(20, 0, 10, 15, BLACK), drawables[4])
        
        self.assertEqual(DrawableBackground(0, 15, 10, 15, BLUE), drawables[5])
        self.assertEqual(DrawablePiece(0, 15, 10, 15, RED), drawables[6])
        
        self.assertEqual(DrawableBackground(10, 15, 10, 15, WHITE), drawables[7])
        
        self.assertEqual(DrawableBackground(20, 15, 10, 15, BLUE), drawables[8])
        self.assertEqual(DrawableKing(20, 15, 10, 15, RED), drawables[9])
        
    def test_create_when_holding_piece(self):
        game = MockGame()
        slotting = MockSlotting(0, 0)
        drawables = Drawables(game, slotting).create((15, 15))
        
        self.assertEqual(10, len(drawables))
        
        self.assertEqual(DrawableBackground(0, 0, 10, 15, WHITE), drawables[0])
        
        self.assertEqual(DrawableBackground(10, 0, 10, 15, BLUE), drawables[1])
        
        self.assertEqual(DrawableBackground(20, 0, 10, 15, WHITE), drawables[2])
        self.assertEqual(DrawableKing(20, 0, 10, 15, BLACK), drawables[3])
        
        self.assertEqual(DrawableBackground(0, 15, 10, 15, BLUE), drawables[4])
        self.assertEqual(DrawablePiece(0, 15, 10, 15, RED), drawables[5])
        
        self.assertEqual(DrawableBackground(10, 15, 10, 15, WHITE), drawables[6])
        
        self.assertEqual(DrawableBackground(20, 15, 10, 15, BLUE), drawables[7])
        self.assertEqual(DrawableKing(20, 15, 10, 15, RED), drawables[8])
        
        self.assertEqual(DrawablePiece(10, 7, 10, 15, BLACK), drawables[9])


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_create']
    unittest.main()