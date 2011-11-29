'''
Created on 2011-11-25

@author: Gooble
'''
import main.game.origin as origin

class Tile(object):
    
    PIECE_COLOURS = {origin.TOP.desc:'red', origin.BOTTOM.desc:'black'}
    
    def __init__(self, piece, board, canvas):
        self.piece = piece
        self.board = board
        self.canvas = canvas
        
    def draw_background(self, startx, starty, width, height, colour):
        self.canvas.create_rectangle(startx, starty, startx + width, starty + height, fill=colour)
            
    def draw_piece(self, width, height, x, y):
        if self.piece is not None:
            colour = Tile.PIECE_COLOURS[self.piece.get_origin().desc]
            self.canvas.create_oval(x, y, x + width, y + height, fill=colour)
            if self.piece.is_king():
                self.canvas.create_line(x, y, x + width, y + height, fill='white')