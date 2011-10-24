'''
Created on 2011-10-23

@author: Gooble
'''
from main import origin

def other_origin(prev_origin):
    if prev_origin == origin.get_top():
        return origin.get_bottom()
    else:
        return origin.get_top()

class Turn(object):

    def __init__(self, prev_origin=origin.get_bottom()):
        self.piece = None
        self.jumped_pieces = []
        self.origin = other_origin(prev_origin)
    
    def add_jumped_pieces(self, from_loc, to_loc):
        if abs(from_loc[0] - to_loc[0]) == 1:
            return
        
        row_between = int((from_loc[0] + to_loc[0]) / 2)
        col_between = int((from_loc[1] + to_loc[1]) / 2)
        self.jumped_pieces.append((row_between, col_between))