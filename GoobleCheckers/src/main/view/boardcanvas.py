'''
Created on 2011-11-28

@author: Gooble
'''
from tkinter import Canvas
import main.view.tile as tile

class BoardCanvas(Canvas):
    
    def set_board(self, board):
        self.board = board
        
    def set_slotting(self, slotting):
        self.slotting = slotting
        
    def calculate_dimensions(self):
        self.tile_width = int(self.cget("width"))/self.board.DEFAULT_WIDTH
        self.tile_height = int(self.cget("height"))/self.board.DEFAULT_HEIGHT
    
    def draw(self):
        for row in range(0, self.board.DEFAULT_HEIGHT):
            for col in range(0, self.board.DEFAULT_WIDTH):              
                t = tile.Tile(row, col, self.board, self)
                t.draw_background(self.tile_width, self.tile_height)
                if not self.slotting.is_holding_piece()\
                or row != self.slotting.start_row or col != self.slotting.start_col:
                    t.draw_piece(self.tile_width, self.tile_height)
                    
    def draw_held_piece(self, event):
        radius = self.tile_width / 2
        start_x = event.x - radius
        start_y = event.y - radius
        self.create_oval(start_x, start_y, start_x + radius * 2, start_y + radius * 2, fill='orange')
