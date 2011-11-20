'''
Created on 2011-11-19

@author: Gooble
'''
from main.movements.move import Move

class Moves(list):
    
    def add(self, from_loc, to_loc):
        move = Move(from_loc, to_loc)
        if self._is_backwards_move(move):
            return # pretend like it never happened...
        
        self.append(move)
        
    def _is_backwards_move(self, move):
        for taken_move in self:
            if taken_move.to_loc == move.from_loc and taken_move.from_loc == move.to_loc:
                return True
        return False
    
    def contains_jump(self):
        for move in self:
            if move.is_jump():
                return True
        return False
    
    def contains_jump_ending_in(self, to_loc):
        for move in self:
            if move.is_jump() and move.to_loc == to_loc:
                return True
        return False
    
    def contains_move_ending_in(self, to_loc):
        for move in self:
            if move.to_loc == to_loc:
                return True
        return False
    
    def __add__(self, other):
        concatenated = Moves()
        for move in self:
            concatenated.append(move)
        for move in other:
            concatenated.append(move)
        return concatenated