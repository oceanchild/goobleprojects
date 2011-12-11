'''
Created on 2011-12-10

@author: Gooble
'''
import unittest
import main.game.board
from main.ai.easyai import EasyAI
from main.game import origin
from main.view.display import BoardDisplay
from main.ai.randomai import RandomAI
from main.ai.match import Match

class AIMatchTest(unittest.TestCase):

    def test_two_ais_face_off_eventually_it_is_gameover(self):
        self.board = main.game.board.Board()
        Match(board=self.board, ai_top=RandomAI(origin.TOP), ai_bottom=EasyAI(origin.BOTTOM)).go()
        self.assertTrue(self.board.is_game_over())
        BoardDisplay(self.board).print_board()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_two_ais_face_off_eventually_it_is_gameover']
    unittest.main()