'''
Created on 2011-10-08

@author: Gooble
'''

class TestCase(object):

    def __init__(self):
        pass
    

    def print_piece_code(self, indent, i, pieces, j):
        move_row=0
        move_col=0
        piece = pieces[j]
        if piece.strip('*') == 'T':
            print(indent + 'self.tboard.place_piece(' + str(i) + ', ' + str(j) + ', origin.get_top())')
        elif piece.strip('*') == 'B':
            print(indent + 'self.tboard.place_piece(' + str(i) + ', ' + str(j) + ', origin.get_bottom())')
        elif piece.strip('*') == 't':
            print(indent + 'self.tboard.place_king(' + str(i) + ', ' + str(j) + ', origin.get_top())')
        elif piece.strip('*') == 'b':
            print(indent + 'self.tboard.place_king(' + str(i) + ', ' + str(j) + ', origin.get_bottom())')
        if len(piece) == 3:
            return i, j
        return move_row, move_col

    def print_test_case(self, display):
        indent = ' ' * 8
        print(display)
        lines = display.split('\n')
        lines = lines[2:-1]
        move_row = 0
        move_col = 0
        for i in range(len(lines)):
            line = lines[i].strip().strip('#')
            line = line[2:]
            pieces = line.split(' ')
            for j in range(len(pieces)):
                move_row, move_col = self.print_piece_code(indent, i, pieces, j)
        
        print (indent + 'calc = Movement(self.tboard.board, '+str(move_row)+', '+str(move_col)+')')
        print (indent + 'moves = calc.get_available_moves()')
        
        
if __name__ == '__main__':
    writer = TestCase()
    writer.print_test_case('\
        # # # # # # # # # #\n\
        #  0 1 2 3 4 5 6 7#\n\
        #0 _ _ _ _ _ _ _ _#\n\
        #1 _ _ _ _ _ _ _ _#\n\
        #2 _ _ _ _ _ _ _ _#\n\
        #3 _ T _ T _ _ _ _#\n\
        #4 _ _ B _ _ _ _ _#\n\
        #5 _ x _ _ _ _ _ _#\n\
        #6 _ _ B _ _ _ _ _#\n\
        #7 _ _ _ x _ _ _ _#\n\
        # # # # # # # # # #')
    
