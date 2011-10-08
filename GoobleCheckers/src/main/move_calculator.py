'''
Created on 2011-10-03

@author: Gooble
'''

class MoveCalculator(object):

    def __init__(self, board):
        self.board = board
        
    def get_available_moves(self, row, col):
        if self.board.invalid_position(row, col):
            return []
        
        piece = self.board.get_piece(row, col)
        if piece is None:
            return []
        
        return self._add_moves_about_col(row + piece.get_origin().value, col, piece.get_origin())
        
    def _add_moves_about_col(self, row, col, origin):
        '''
        (1) The first time this is called -> if the adjacent piece is Empty then return it immediately; rather, append it to moves, and stop the recursion there
        (2) Otherwise the piece isn't empty: recursion must start -> check the "next" piece along the diagonal
            -> (a) if the next piece is empty, continue the search from there, adding it to the move 
            -> (b) if the piece isn't empty, it's an invalid move; return nothing
            
        note: We already have the new row; just check each side
        '''
        return self._add_moves_for_col(row, col, -1, origin) + self._add_moves_for_col(row, col, +1, origin)
            
    def _add_moves_for_col(self, row, col, direction, origin):
        new_col = col + direction
        if self.board.valid_position(row, new_col) and self.board.get_piece(row, new_col) is None:
            return [[(row, new_col)]]
        elif self.board.get_piece(row, new_col) is not None:
            return self._start_recursion(row, new_col, direction, origin)
            
        return []
        
    def _start_recursion(self, row, col, direction, origin):
        '''
        We have the row & column on which there is a piece. we have to keep going
        along the diagonal -> if the next piece is occupied, return empty list - this isn't a valid move
        
        if it's not occupied... that's the tricky part
        '''
        new_row = row + origin.value
        new_col = col + direction
        
        if self.board.get_piece(new_row, new_col) is not None or not self.board.valid_position(new_row, new_col):
            return []
        
        move = [(new_row, new_col)]
        moves = [move]
        
        new_new_row = new_row + origin.value
        self._recurse(new_new_row, new_col, -1, move, moves, origin)
        self._recurse(new_new_row, new_col, +1, move, moves, origin)
        
        return moves
    
    def _recurse(self, row, col, direction, move, moves, origin):
        if self.board.get_piece(row, col + direction) is not None:
            new_moves = self._start_recursion(row, col + direction, direction, origin)
            if len(new_moves) > 0 and move in moves:
                moves.remove(move)
            [moves.append(move + m) for m in new_moves]      
        
        