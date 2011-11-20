'''
Created on 2011-10-23

@author: Gooble
'''
from main import origin
from main.movements.moves import Moves
from main.movements.movement import Movement


'''
a turn will become the list of currently taken moves.

if a player takes a move, one of the following will happen:
- if a negating move exists, that move will be deleted from the move list
- otherwise, the move will be added to the current set of moves

a negating move is the move with the same to and fro locations, but switched.
for example, a move from 1,2 to 2,3 would have a negating move of 2,3 to 1,2.

each move can quickly calculate whether it is a jump or not, 
'''
def other_origin(prev_origin):
    if prev_origin == origin.get_top():
        return origin.get_bottom()
    else:
        return origin.get_top()


class Turn(object):

    def __init__(self, board, prev_origin=origin.get_bottom()):
        self.board = board
        self.piece = None
        self.origin = other_origin(prev_origin)
        self.moves = Moves()
        self.over = False
    
    def handle_movement(self, from_loc, to_loc):
        if self._illegal_move(from_loc, to_loc):
            return
        
        self.board.set_piece(to_loc[0], to_loc[1], self.board.get_piece(from_loc[0], from_loc[1]))
        self.board.set_piece(from_loc[0], from_loc[1], None)
        
        self.moves.add(from_loc, to_loc)
        
        self._check_if_turn_complete(to_loc)
        
    def _check_if_turn_complete(self, to_loc):
        new_moves = Movement(self.board, to_loc[0], to_loc[1]).get_available_moves()
        for move_list in new_moves:
            if move_list.contains_jump():
                return
        self.over = True
        
        
    def _illegal_move(self, from_loc, to_loc):
        moves = Movement(self.board, from_loc[0], from_loc[1]).get_available_moves()
        piece = self.board.get_piece(from_loc[0], from_loc[1])
        if piece is not None and piece.get_origin() != self.origin:
            return True
        
        if self.piece is not None and self.piece is not piece:
            return True
        
        for move_list in moves:
            if (len(self.moves) > 0 and move_list.contains_jump_ending_in(to_loc)) \
            or (len(self.moves) == 0 and move_list.contains_move_ending_in(to_loc)):
                self.piece = piece
                return False
        return True    
        
    
    def handle_jumps(self):
        for move in self.moves:
            if move.is_jump():
                row, col = move.get_jumped_piece()
                self.board.set_piece(row, col, None)
    
    def is_over(self):
        return self.over