'''
Created on 2012-02-26

@author: Gooble
'''
from main.view.drawable import DrawableKing, DrawablePiece, DrawableBackground
from main.view.colours import Colours

class Drawables(object):
    
    def __init__(self, game, slotting):
        self.game = game
        self.slotting = slotting
        self.tile_width = game.get_tile_width()
        self.tile_height = game.get_tile_height()

    def create(self, position):
        drawables = []
        held_drawable = None
        
        for row in range(0, self.game.get_num_rows()):
            for col in range(0, self.game.get_num_cols()):
                piece = self.game.get_piece(row, col)
                colour = Colours().piece(piece)
                x = col * self.tile_width
                y = row * self.tile_height
                drawables.append(self.get_background(x, y, row, col))
                
                if self.currently_holding_this_piece(position, row, col):
                    held_drawable = self.get_held_drawable(position, piece, colour)
                elif self.there_is_a_piece_here(row, col, piece):
                    drawables.append(self.get_current_drawable_piece(x, y, colour, piece))
                        
        if held_drawable is not None:
            drawables.append(held_drawable)
            
        return drawables
        
    def get_held_drawable(self, position, piece, colour):
        x = int(position[0] - self.tile_width / 2)
        y = int(position[1] - self.tile_height / 2)
        return self.get_current_drawable_piece(x, y, colour, piece)

    def get_current_drawable_piece(self, x, y, colour, piece):
        if piece is not None and piece.is_king():
            return DrawableKing(x, y, self.tile_width, self.tile_height, colour)
        else:
            return DrawablePiece(x, y, self.tile_width, self.tile_height, colour)

    def there_is_a_piece_here(self, row, col, piece):
        return not self.slotting.is_holding_piece(row, col) and piece is not None

    def currently_holding_this_piece(self, position, row, col):
        return self.slotting.is_holding_piece(row, col) and position is not None

    def get_background(self, x, y, row, col):
        bgcolour = Colours().background(row, col)
        return DrawableBackground(x, y, self.tile_width, self.tile_height, bgcolour)