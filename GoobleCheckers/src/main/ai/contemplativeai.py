'''
Created on 2011-12-22

@author: Gooble
'''
from main.ai.abstractai import AbstractAI
from main.ai.bestmovedepth import BestMovementWithDepth

class ContemplativeAI(AbstractAI):
    
    def __init__(self, max_depth):
        AbstractAI.__init__(self)
        self.max_depth = max_depth

    def choose_move(self, game, all_moves):
        return BestMovementWithDepth(self.max_depth, self.origin).calculate_for(game)
