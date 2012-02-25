'''
Created on 2011-11-27

@author: Gooble
'''
import main.view.boardcoordinate

class Slotting(object):
    
    def __init__(self, game):
        self.game = game
        self.start_row = None
        self.start_col = None
        
    def select_piece(self, event):
        self.start_row, self.start_col =  main.view.boardcoordinate.BoardCoordinate().get_from(event[0], event[1])

    def release_piece(self, event):
        to_row, to_col =  main.view.boardcoordinate.BoardCoordinate().get_from(event[0], event[1])
        self.game.move_piece((self.start_row, self.start_col), (to_row, to_col))
        self.start_row = None
        self.start_col = None
        
    def is_holding_piece(self):
        return self.start_row is not None and self.start_col is not None
