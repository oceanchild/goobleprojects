'''
Created on 2011-10-03

@author: Gooble
'''

class Movement(object):

    def __init__(self, board, row, col):
        self.board = board
        self.row = row
        self.col = col
        self.piece = board.get_piece(row, col)
        if self.piece is not None:
            self.origin = self.piece.get_origin()
        
    def get_available_moves(self):
        if self.piece is None:
            return []
        
        king_moves = []
        if self.piece.is_king():
            king_moves = self._add_moves_for_col(-self.origin.value, -1)\
                       + self._add_moves_for_col(-self.origin.value, +1)
        
        return king_moves\
             + self._add_moves_for_col(self.origin.value, -1)\
             + self._add_moves_for_col(self.origin.value, +1)
        
    def _add_moves_for_col(self, row_dir, col_dir):
        new_row = self.row + row_dir
        new_col = self.col + col_dir
        if self.board.valid_position(new_row, new_col) and self.board.get_piece(new_row, new_col) is None:
            return [[(new_row, new_col)]]
        elif self.board.get_piece(new_row, new_col) is not None and self.board.get_piece(new_row, new_col).get_origin() != self.origin:
            return self._start_recursion(new_row, new_col, row_dir, col_dir)
            
        return []
        
    def _start_recursion(self, row, col, row_dir, col_dir):
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
        
        
        '''Keep going along the same direction'''
        new_new_row = new_row + row_dir
        self._recurse(new_new_row, new_col, row_dir, -1, move, moves)
        self._recurse(new_new_row, new_col, row_dir, +1, move, moves)
        
        
        '''but if it's a king, it can change direction along the vertical...'''
        if self.piece.is_king():
            new_new_row = new_row - row_dir
            self._recurse(new_new_row, new_col, -row_dir, col_dir, move, moves)
        
        return moves
    
    def _recurse(self, row, col, row_dir, col_dir, move, moves):
        if self.board.get_piece(row, col + col_dir) is not None and self.board.get_piece(row, col + col_dir).get_origin() != self.origin:
            new_moves = self._start_recursion(row, col + col_dir, row_dir, col_dir)
            if len(new_moves) > 0 and move in moves:
                moves.remove(move)
            [moves.append(move + m) for m in new_moves]
        