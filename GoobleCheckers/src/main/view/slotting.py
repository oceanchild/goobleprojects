'''
Created on 2011-11-27

@author: Gooble
'''
from main.view.boardcoordinate import BoardCoordinate

class Slotting(object):
    
    def __init__(self, board):
        self.board = board
        
    def select_piece(self, event):
        self.start_row, self.start_col = BoardCoordinate().get_from(event.x, event.y)

    def release_piece(self, event):
        to_row, to_col = BoardCoordinate().get_from(event.x, event.y)
        self.board.move_piece((self.start_row, self.start_col), (to_row, to_col))