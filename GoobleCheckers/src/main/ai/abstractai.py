'''
Created on 2011-12-11

@author: Gooble
'''
from main.game import origin
from main.ai.originmoves import OriginMoves

class AbstractAI(object):

    def __init__(self, origin=origin.BOTTOM):
        self.origin = origin
        
    def make_move(self, game):
        move = self.choose_move(OriginMoves(game.board, self.origin).get_moves())
        game.make_move(move)
            
    def choose_move(self, all_moves):
        pass