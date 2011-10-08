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
        
        moves = []
        piece = self.board.get_piece(row, col)
        if piece is None:
            return []
        
        self._add_moves_about_col(row + piece.get_origin().value, col, moves, piece.get_origin())
        
        print(moves)
        return moves
    
    def _add_moves_about_col(self, row, col, moves, origin):
        '''
        (1) The first time this is called -> if the adjacent piece is Empty then return it immediately; rather, append it to moves, and stop the recursion there
        (2) Otherwise the piece isn't empty: recursion must start -> check the "next" piece along the diagonal
            -> (a) if the next piece is empty, continue the search from there, adding it to the move 
            -> (b) if the piece isn't empty, it's an invalid move; return nothing
            
        note: We already have the new row; just check each side
        '''
        
        # LEFT SIDE
        if self.board.valid_position(row, col - 1) and self.board.get_piece(row, col - 1) is None:
            moves.append([(row, col - 1)])
        elif self.board.get_piece(row, col - 1) is not None:
            moves.extend(self._start_recursion(row, col-1, -1, origin))
        
        # RIGHT SIDE
        if self.board.valid_position(row, col + 1) and self.board.get_piece(row, col + 1) is None:
            moves.append([(row, col + 1)])
        elif self.board.get_piece(row, col + 1) is not None:
            moves.extend(self._start_recursion(row, col+1, 1, origin)) 
        
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
        new_left_col = new_col - 1
        new_right_col = new_col + 1
        
        
        # LEFT
        if self.board.get_piece(new_new_row, new_left_col) is not None:
            new_left_moves = self._start_recursion(new_new_row, new_left_col, -1, origin)
            if len(new_left_moves) > 0 and move in moves:
                moves.remove(move)
            for m in new_left_moves:
                moves.append(move + m)
            
        # RIGHT
        if self.board.get_piece(new_new_row, new_right_col) is not None:
            new_right_moves = self._start_recursion(new_new_row, new_right_col, 1, origin)
            if len(new_right_moves) > 0 and move in moves:
                moves.remove(move)
            for m in new_right_moves:
                moves.append(move + m)
        
        return moves
        
        
        
        