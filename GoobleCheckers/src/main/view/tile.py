'''
Created on 2011-11-25

@author: Gooble
'''
import main.game.origin as origin

class Tile(object):
    
    BLANK_TILE_COLOURS = ['white', 'blue']
    PIECE_COLOURS = {origin.TOP.desc:'red', origin.BOTTOM.desc:'black'}
    
    def __init__(self, row, col, board, canvas):
        self.row = row
        self.col = col
        self.board = board
        self.canvas = canvas
        
    def draw_background(self, width, height):
        colour = Tile.BLANK_TILE_COLOURS[(self.row + self.col) % 2]
        self.canvas.create_rectangle(self.col * width, self.row * height, self.col * width + width, self.row * height + height, fill=colour)
            
    def draw_piece(self, width, height):
        piece = self.board.get_piece(self.row, self.col)
        if piece is not None:
            colour = Tile.PIECE_COLOURS[piece.get_origin().desc]
            self.canvas.create_oval(self.col * width, self.row * height, self.col * width + width, self.row * height + height, fill=colour)