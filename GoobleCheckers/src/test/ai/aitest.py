'''
Created on 2011-12-05

@author: Gooble
'''
import unittest
from test.util.testboard import TestBoard
import main.game.origin as origin
import main.view
import main.game
from test.view.slottingtest import MockEvent
import main.ai.easyai as easyai

class AITest(unittest.TestCase):

    def test_if_it_is_bottoms_turn_then_ai_auto_moves_piece_on_board(self):
        self.game = main.view.gameplay.GamePlay(ai=easyai.EasyAI())
        self.tboard = TestBoard(self.game.board)
        # # # # # # # # # #
        #  0 1 2 3 4 5 6 7#
        #0 _ _ _ _ _ _ _ _#
        #1 _ _ _ _ _ _ _ _#
        #2 _ _ _ _ _ _ _ _#
        #3 _ _ T _ _ _ _ _#
        #4 B _ _ B _ _ _ _#
        #5 _ _ _ _ x _ _ _#
        #6 _ _ _ _ _ B _ _#
        #7 _ _ _ _ _ _ x _#
        # # # # # # # # # #
        self.tboard.place_piece(3, 2, origin.TOP)
        self.tboard.place_piece(4, 0, origin.BOTTOM)
        self.tboard.place_piece(4, 3, origin.BOTTOM)
        self.tboard.place_piece(6, 5, origin.BOTTOM)
        
        self.move_piece(3, 2, 5, 4)
        self.move_piece(5, 4, 7, 6)
        
        self.assertTrue(self.tboard.board.get_piece(7, 6).is_king())
        self.assertTrue(self.tboard.board.get_piece(7, 6).is_king())
        self.assertIsNone(self.tboard.board.get_piece(4, 3))
        self.assertIsNone(self.tboard.board.get_piece(6, 5))
        
        self.game.check_and_use_ai()
        # AI moved piece
        self.assertIsNone(self.tboard.board.get_piece(4, 0))
        self.assertIsNotNone(self.tboard.board.get_piece(3, 1))

    def move_piece(self, from_row, from_col, to_row, to_col):
        self.game.slotting.select_piece(MockEvent(from_col * (main.view.gameplay.GamePlay.DEFAULT_WIDTH / main.game.board.Board.DEFAULT_WIDTH),
                                                  from_row * (main.view.gameplay.GamePlay.DEFAULT_HEIGHT / main.game.board.Board.DEFAULT_HEIGHT)))
        self.game.slotting.release_piece(MockEvent(to_col * (main.view.gameplay.GamePlay.DEFAULT_WIDTH / main.game.board.Board.DEFAULT_WIDTH),
                                                   to_row * (main.view.gameplay.GamePlay.DEFAULT_HEIGHT / main.game.board.Board.DEFAULT_HEIGHT)))

if __name__ == "__main__":
    unittest.main()