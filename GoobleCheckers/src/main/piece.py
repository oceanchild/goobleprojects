'''
Created on 2011-10-09

@author: Gooble
'''

class Piece(object):
    
    def __init__(self, origin):
        self.origin = origin
        self.king = False
        
    def get_origin(self):
        return self.origin
    
    def is_king(self):
        return self.king
    
    def set_king(self, king):
        self.king = king