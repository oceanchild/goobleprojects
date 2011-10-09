'''
Created on 2011-10-03

@author: Gooble
'''

class Movement(object):

    def __init__(self, board):
        self.board = board
        
    def get_available_moves(self, row, col):
        if self.board.invalid_position(row, col):
            return []
        
        piece = self.board.get_piece(row, col)
        if piece is None:
            return []
        
        origin = piece.get_origin()
        king_moves = []
        if piece.is_king():
            king_moves = self._get_moves_for_king(row, col, origin) 
        
        return king_moves + self._add_moves_for_col(row + origin.value, col, -1, origin.value, origin)\
             + self._add_moves_for_col(row + origin.value, col, +1, origin.value, origin)
        
    def _add_moves_for_col(self, row, col, col_dir, row_dir, origin):
        new_col = col + col_dir
        if self.board.valid_position(row, new_col) and self.board.get_piece(row, new_col) is None:
            return [[(row, new_col)]]
        elif self.board.get_piece(row, new_col) is not None:
            return self._start_recursion(row, new_col, col_dir, row_dir, origin)
            
        return []
        
    def _start_recursion(self, row, col, col_dir, row_dir, origin):
        '''
        We have the row & column on which there is a piece. we have to keep going
        along the diagonal -> if the next piece is occupied, return empty list - this isn't a valid move
        
        if it's not occupied... that's the tricky part
        '''
        new_row = row + row_dir
        new_col = col + col_dir
        
        if self.board.get_piece(new_row, new_col) is not None or not self.board.valid_position(new_row, new_col):
            return []
        
        move = [(new_row, new_col)]
        moves = [move]
        
        new_new_row = new_row + row_dir
        self._recurse(new_new_row, new_col, -1, row_dir, move, moves, origin)
        self._recurse(new_new_row, new_col, +1, row_dir, move, moves, origin)
        
        return moves
    
    def _recurse(self, row, col, col_dir, row_dir, move, moves, origin):
        if self.board.get_piece(row, col + col_dir) is not None:
            new_moves = self._start_recursion(row, col + col_dir, col_dir, row_dir, origin)
            if len(new_moves) > 0 and move in moves:
                moves.remove(move)
            [moves.append(move + m) for m in new_moves]
            
    def _get_moves_for_king(self, row, col, origin):
        return self._add_moves_for_col(row - origin.value, col, -1, -origin.value, origin)\
             + self._add_moves_for_col(row - origin.value, col, +1, -origin.value, origin)
        
        