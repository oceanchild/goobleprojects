'''
Created on 2011-12-11

@author: Gooble
'''
from main.ai.abstractai import AbstractAI
import random

class RandomAI(AbstractAI):
    
    def choose_move(self, all_moves):
        move_list_index = random.Random().randint(0, len(all_moves) - 1)
        move_index = random.Random().randint(0, len(all_moves[move_list_index]) - 1)
        return all_moves[move_list_index][move_index]
        