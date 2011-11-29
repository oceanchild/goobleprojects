'''
Created on 2011-11-28

@author: Gooble
'''
from tkinter import Canvas
import main.view.tile as tile

class BoardCanvas(Canvas):
    
    BACKGROUND_COLOURS = ['white', 'blue']
    
    def set_board(self, board):
        self.board = board
        
    def set_slotting(self, slotting):
        self.slotting = slotting
        
    def calculate_dimensions(self):
        self.tile_width = int(self.cget("width"))/self.board.DEFAULT_WIDTH
        self.tile_height = int(self.cget("height"))/self.board.DEFAULT_HEIGHT
    
    def draw(self, event=None):
        for row in range(0, self.board.DEFAULT_HEIGHT):
            for col in range(0, self.board.DEFAULT_WIDTH):
                piece = self.board.get_piece(row, col)
                colour = BoardCanvas.BACKGROUND_COLOURS[(row + col) % 2]
                t = tile.Tile(piece, self.board, self)
                t.draw_background(col * self.tile_width, row * self.tile_height, self.tile_width, self.tile_height, colour)
                if not self.slotting.is_holding_piece()\
                or row != self.slotting.start_row or col != self.slotting.start_col:
                    t.draw_piece(self.tile_width, self.tile_height, col * self.tile_width, row * self.tile_height)
                    
        self.draw_held_piece(event)
                    
    def draw_held_piece(self, event):
        if event is not None and self.slotting.is_holding_piece():
            piece = self.board.get_piece(self.slotting.start_row, self.slotting.start_col)
            tile.Tile(piece, self.board, self).\
                draw_piece(self.tile_width, self.tile_height, event.x - self.tile_width/2, event.y - self.tile_height/2)
