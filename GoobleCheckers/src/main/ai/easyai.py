'''
Created on 2011-12-08

@author: Gooble
'''
from main.ai.abstractai import AbstractAI

class EasyAI(AbstractAI):

    def choose_move(self, all_moves):
        max_pieces_eaten = 0
        best_move = None
        for move_list in all_moves:
            for move in move_list:
                if move.get_pieces_eaten() >= max_pieces_eaten:
                    best_move = move
                    max_pieces_eaten = len(move)
                    
        return best_move