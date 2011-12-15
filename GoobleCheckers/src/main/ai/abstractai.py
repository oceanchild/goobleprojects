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
        for position_change in move:
            game.move_piece(position_change.from_loc, position_change.to_loc)
            
    def choose_move(self, all_moves):
        pass