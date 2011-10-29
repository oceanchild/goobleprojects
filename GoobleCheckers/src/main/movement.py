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
        total_moves = king_moves + self._add_moves_for_col(self.origin.value, -1) + self._add_moves_for_col(self.origin.value, +1)
        final_moves = total_moves
        ### we have to account for whether the piece is mid-jump or not..
        turn = self.board.current_turn
        if self.piece is turn.piece and len(turn.jumped_pieces) > 0:
            [final_moves.remove(move) for move in total_moves if not self.is_jump(move)]
        
        return final_moves
    
    def is_jump(self, move):
        first_move = move[0]
        
        return len(move) > 1 or (abs(first_move[0] - self.row) > 1 and abs(first_move[1] - self.col) > 1)
        
    def _add_moves_for_col(self, row_dir, col_dir):
        new_row = self.row + row_dir
        new_col = self.col + col_dir
        if self.board.valid_position(new_row, new_col) and self.board.get_piece(new_row, new_col) is None:
            return [[(new_row, new_col)]]
        elif self.board.get_piece(new_row, new_col) is not None and self.board.get_piece(new_row, new_col).get_origin() != self.origin:
            return self._calculate_jumped_moves(new_row, new_col, row_dir, col_dir)
            
        return []
        
    def _calculate_jumped_moves(self, row, col, row_dir, col_dir):
        #We have the row & column on which there is a piece. we have to keep going
        #along the diagonal -> if the next piece is occupied, return empty list - this isn't a valid move
        #if it's not occupied... that's the tricky part
        new_row = row + row_dir
        new_col = col + col_dir
        
        if self.board.get_piece(new_row, new_col) is not None or self.board.invalid_position(new_row, new_col):
            return []
        
        move = [(new_row, new_col)]
        moves = [move]
        
        #Keep going along the same direction
        new_new_row = new_row + row_dir
        self._add_jumped_moves(new_new_row, new_col, row_dir, -1, move, moves)
        self._add_jumped_moves(new_new_row, new_col, row_dir, +1, move, moves)
        
        #but if it's a king, it can change direction along the vertical...
        #making sure not to go back the way it came, it only continues in the given col_dir...
        if self.piece.is_king():
            new_new_row = new_row - row_dir
            self._add_jumped_moves(new_new_row, new_col, -row_dir, col_dir, move, moves)
        
        return moves
    
    def _add_jumped_moves(self, row, col, row_dir, col_dir, move, moves):
        if self.board.get_piece(row, col + col_dir) is not None and self.board.get_piece(row, col + col_dir).get_origin() != self.origin:
            new_moves = self._calculate_jumped_moves(row, col + col_dir, row_dir, col_dir)
            if len(new_moves) > 0 and move in moves:
                moves.remove(move)
            [moves.append(move + m) for m in new_moves]
        