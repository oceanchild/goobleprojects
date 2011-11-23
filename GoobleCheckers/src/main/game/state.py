'''
Created on 2011-11-22

@author: Gooble
'''

class State(object):
    
    def __init__(self, board):
        self.board = board
        self.num_top_pieces = int(((board.DEFAULT_HEIGHT / 2) - 1) * (board.DEFAULT_WIDTH / 2))
        self.num_bottom_pieces = self.num_top_pieces
        
    def update_state_for_insertion(self, row, col, piece):
        self._decrement_for_original_piece_removal(self.board.get_piece(row, col))
        self._increment_for_new_piece_insertion(piece)
        
    def is_game_over(self):
        return self.num_bottom_pieces == 0 or self.num_top_pieces == 0
        
    def _decrement_for_original_piece_removal(self, piece):
        self._modify_piece_count(piece, -1)
            
    def _increment_for_new_piece_insertion(self, piece):
        self._modify_piece_count(piece, 1)
            
    def _modify_piece_count(self, piece, modifier):
        if piece is None:
            pass
        elif (piece.is_from_top()):
            self.num_top_pieces += modifier
        elif (piece.is_from_bottom()):
            self.num_bottom_pieces += modifier
            
