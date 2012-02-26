'''
Created on 2012-02-26

@author: Gooble
'''
from main.game import origin

RED = [255,0,0]
BLACK = [0,0,0]
WHITE = [255,255,255]
BLUE = [0,0,255]

class Drawable(object):
    def __init__(self, x, y, width, height, colour):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour

class DrawablePiece(Drawable):
    def draw(self, graphics, screen):
        graphics.draw.ellipse(screen, self.colour, [self.x, self.y, self.width, self.height])

class DrawableKing(DrawablePiece):
    def draw(self, graphics, screen):
        DrawablePiece.draw(self, graphics, screen)
        graphics.draw.line(screen, WHITE, [self.x, self.y], [self.x+self.width, self.y+self.height])
        
class DrawableBackground(Drawable):
    def draw(self, graphics, screen):
        graphics.draw.rect(screen, self.colour, [self.x, self.y, self.width, self.height])

class Drawables(object):
    
    def __init__(self, game, slotting):
        self.game = game
        self.slotting = slotting
    
    def create(self, current_position):
        position = current_position
        drawables = []
        held_drawable = None
        
        tile_width = self.game.get_tile_width()
        tile_height = self.game.get_tile_height()
        
        for row in range(0, self.game.get_num_rows()):
            for col in range(0, self.game.get_num_cols()):
                piece = self.game.get_piece(row, col)
                if piece is not None and piece.get_origin() == origin.BOTTOM:
                    colour = RED
                elif piece is not None:
                    colour = BLACK
                
                if (row + col) % 2 == 0:
                    bgcolour = WHITE
                else:
                    bgcolour = BLUE
                
                x = col * tile_width
                y = row * tile_height
                drawables.append(DrawableBackground(x, y, tile_width, tile_height, bgcolour))
                
                if self.slotting.is_holding_piece(row, col) and position is not None:
                    x = position[0] - tile_width/2
                    y = position[1] - tile_height/2
                    if piece is not None and piece.is_king():
                        held_drawable = DrawableKing(x, y, tile_width, tile_height, colour)
                    elif piece is not None:
                        held_drawable = DrawablePiece(x, y, tile_width, tile_height, colour)
                elif not self.slotting.is_holding_piece(row, col):
                    if piece is not None and piece.is_king():
                        drawables.append(DrawableKing(x, y, tile_width, tile_height, colour))
                    elif piece is not None:
                        drawables.append(DrawablePiece(x, y, tile_width, tile_height, colour))
                        
        if held_drawable is not None:
            drawables.append(held_drawable)
        return drawables