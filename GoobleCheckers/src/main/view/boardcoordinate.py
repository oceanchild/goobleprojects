'''
Created on 2011-11-26

@author: Gooble
'''
import main.game.board as board
import main.view.gameplay

class BoardCoordinate(object):
    
    def __init__(self, 
                 canvas_size=(main.view.gameplay.GamePlay.DEFAULT_WIDTH, main.view.gameplay.GamePlay.DEFAULT_HEIGHT),
                 board_size=(board.Board.DEFAULT_WIDTH, board.Board.DEFAULT_HEIGHT)):
        self.canvas_width = canvas_size[0]
        self.canvas_height = canvas_size[1]
        self.board_width = board_size[0]
        self.board_height = board_size[1]
    
    def get_from(self, x, y):
        tile_width = self.canvas_width / self.board_width
        tile_height = self.canvas_height / self.board_height
        
        return int(y / tile_height), int(x / tile_width)
    
