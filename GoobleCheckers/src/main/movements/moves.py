'''
Created on 2011-11-19

@author: Gooble
'''
from main.movements.move import Move

class Moves(list):
    
    def add(self, from_loc, to_loc):
        move = Move(from_loc, to_loc)
        if self._get_backwards_move(move):
            self.remove(self._get_backwards_move(move))
            return
        self.append(move)
        
    def _get_backwards_move(self, move):
        for taken_move in self:
            if taken_move.get_backwards_move() == move:
                return taken_move
        return None
    
    def contains_jump(self):
        for move in self:
            if move.is_jump():
                return True
        return False
    
    def jumps_are_not_backward_from(self, other_moves):
        for move in self:
            if move.is_jump() and other_moves._get_backwards_move(move) is not None:
                return False
        return True
    
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