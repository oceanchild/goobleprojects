'''
Created on 2011-12-20

@author: Gooble
'''

class MaxMove(object):


    def _compare_and_get_higher_move(self, max_pieces_eaten, move):
        if move.get_pieces_eaten() >= max_pieces_eaten:
            best_move = move
            max_pieces_eaten = len(move)
        return best_move

    def get_max_move(self, all_moves):
        max_pieces_eaten = 0
        best_move = None
        for move_list in all_moves:
            for move in move_list:
                best_move = self._compare_and_get_higher_move(max_pieces_eaten, move)
        
        return best_move