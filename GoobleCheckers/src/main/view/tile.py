'''
Created on 2011-11-25

@author: Gooble
'''
from main.game import origin
import gameplay
from main.game.board import Board

class Tile(object):
    
    BLANK_TILE_COLOURS = ['white', 'blue']
    PIECE_COLOURS = {origin.TOP.desc:'red', origin.BOTTOM.desc:'black'}
    
    def __init__(self, row, col, board, canvas):
        self.row = row
        self.col = col
        self.board = board
        self.canvas = canvas
        
    def draw(self):
        piece = self.board.get_piece(self.row, self.col)
        width = gameplay.GamePlay.DEFAULT_WIDTH/Board.DEFAULT_WIDTH
        height = gameplay.GamePlay.DEFAULT_HEIGHT/Board.DEFAULT_HEIGHT
        
        colour = Tile.BLANK_TILE_COLOURS[(self.row + self.col) % 2]
        self.canvas.create_rectangle(self.col * width, self.row * height, self.col * width + width, self.row * height + height, fill=colour)
        
        if piece is not None:
            colour = Tile.PIECE_COLOURS[piece.get_origin().desc]
            self.canvas.create_oval(self.col * width, self.row * height, self.col * width + width, self.row * height + height, fill=colour)