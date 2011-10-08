'''
Created on 2011-10-08

@author: Gooble
'''

class TestCaseWriter(object):

    def __init__(self):
        pass
    
    def print_test_case(self, display):
        lines = display.split('\n')
        lines = lines[2:-1]
        for i in range(len(lines)):
            line = lines[i].strip().strip('#')
            line = line[2:]
            pieces = line.split(' ')
            for j in range(len(pieces)):
                piece = pieces[j]
                if piece == 'T':
                    print ('self.tboard.place_piece('+str(i)+', '+str(j)+', origin.get_top())')
                elif piece == 'B':
                    print ('self.tboard.place_piece('+str(i)+', '+str(j)+', origin.get_bottom())')
        
        
        
if __name__ == '__main__':
    writer = TestCaseWriter()
    writer.print_test_case('\
         # # # # # # # # # #\n\
         #  0 1 2 3 4 5 6 7#\n\
         #0 _ _ _ _ _ _ _ _#\n\
         #1 _ _ _ _ _ _ _ _#\n\
         #2 _ _ _ T _ _ _ _#\n\
         #3 _ _ B _ B _ _ _#\n\
         #4 _ x _ _ _ x _ _#\n\
         #5 _ _ B _ _ _ _ _#\n\
         #6 _ _ _ x _ _ _ _#\n\
         #7 _ _ _ _ _ _ _ _#\n\
         # # # # # # # # # #')
    
