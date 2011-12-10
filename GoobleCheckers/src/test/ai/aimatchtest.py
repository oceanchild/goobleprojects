'''
Created on 2011-12-10

@author: Gooble
'''
import unittest
import main.game.board
from main.ai.easyai import EasyAI
from main.game import origin
from main.view.display import BoardDisplay


class Match(object):
    
    def __init__(self, board, ai_top, ai_bottom):
        self.board = board
        self.ai_top = ai_top
        self.ai_bottom = ai_bottom
        
    def go(self):
        while not self.board.is_game_over():
            if self.board.current_turn.origin == origin.BOTTOM:
                self.ai_bottom.make_move(self.board)
            else:
                self.ai_top.make_move(self.board)


class AIMatchTest(unittest.TestCase):

    @unittest.skip
    def test_two_ais_face_off_eventually_it_is_gameover(self):
        self.board = main.game.board.Board()
        Match(board=self.board, ai_top=EasyAI(origin.TOP), ai_bottom=EasyAI(origin.BOTTOM)).go()
        self.assertTrue(self.board.is_game_over())
        BoardDisplay(self.board).print_board()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_two_ais_face_off_eventually_it_is_gameover']
    unittest.main()