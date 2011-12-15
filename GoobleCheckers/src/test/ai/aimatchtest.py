'''
Created on 2011-12-10

@author: Gooble
'''
import unittest
from main.ai.easyai import EasyAI
from main.game import origin
from main.view.display import BoardDisplay
from main.ai.randomai import RandomAI
from main.ai.match import Match
import main.game.gameplay

class AIMatchTest(unittest.TestCase):

    @unittest.skip
    def test_two_ais_face_off_eventually_it_is_gameover(self):
        self.game = main.game.gameplay.GamePlay()
        Match(game=self.game, ai_top=RandomAI(origin.TOP), ai_bottom=EasyAI(origin.BOTTOM)).go()
        self.assertTrue(self.game.is_game_over())
        BoardDisplay(self.game.board).print_board()


if __name__ == "__main__":
    unittest.main()