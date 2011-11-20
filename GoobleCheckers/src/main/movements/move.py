'''
Created on 2011-11-19

@author: Gooble
'''

class Move(object):
    
    def __init__(self, from_loc, to_loc):
        self.from_loc = from_loc
        self.to_loc = to_loc

    def is_jump(self):
        return abs(self.from_loc[0] - self.to_loc[0]) > 1 \
            and abs(self.from_loc[1] - self.to_loc[1]) > 1
            
    def get_jumped_piece(self):
        row_between = int((self.from_loc[0] + self.to_loc[0]) / 2)
        col_between = int((self.from_loc[1] + self.to_loc[1]) / 2)
        return row_between, col_between
    
    def __str__(self):
        return "Move from " + self.from_loc[0] + ", " + self.from_loc[1] + " to " \
            + str(self.to_loc[0]) + ", " + str(self.to_loc[1])
            
    def __eq__(self, other):
        if other is None or type(other) is not Move: return False
        
        return self.from_loc == other.from_loc and self.to_loc == other.to_loc
    
    def __neq__(self, other):
        return not self==other