'''
Created on 2011-11-28

@author: Gooble
'''
from tkinter import Canvas
import main.view.tile as tile

class BoardCanvas(Canvas):
    
    def draw(self, board):
        [[tile.Tile(row, col, board, self).draw() 
          for col in range(0, board.DEFAULT_WIDTH)] 
         for row in range(0, board.DEFAULT_HEIGHT)]