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

class DrawableKing(Drawable):
    def draw(self, graphics, screen):
        graphics.draw.ellipse(screen, self.colour, [self.x, self.y, self.width, self.height])
        graphics.draw.line(screen, WHITE, [self.x, self.y], [self.x+self.width,self.y+self.height])
        
class DrawablePiece(Drawable):
    def draw(self, graphics, screen):
        graphics.draw.ellipse(screen, self.colour, [self.x, self.y, self.width, self.height])

class DrawableBackground(Drawable):
    def draw(self, graphics, screen):
        graphics.draw.rect(screen, self.colour, [self.x, self.y, self.width, self.height])

class Drawables(object):
    
    def create(self, game, current_position, slotting):
        position = current_position
        drawables = []
        held_drawable = None
        
        for row in range(0, game.board.DEFAULT_HEIGHT):
            for col in range(0, game.board.DEFAULT_WIDTH):
                piece = game.get_piece(row, col)
                if piece is not None and piece.get_origin() == origin.BOTTOM:
                    colour = RED
                elif piece is not None:
                    colour = BLACK
                
                if (row + col) % 2 == 0:
                    bgcolour = WHITE
                else:
                    bgcolour = BLUE
                
                x = col * 60
                y = row * 60
                drawables.append(DrawableBackground(x, y, 60, 60, bgcolour))
                
                if slotting.is_holding_piece(row, col) and position is not None:
                    x = position[0] - 30
                    y = position[1] - 30
                    if piece is not None and piece.is_king():
                        held_drawable = DrawableKing(x, y, 60, 60, colour)
                    elif piece is not None:
                        held_drawable = DrawablePiece(x, y, 60, 60, colour)
                elif not slotting.is_holding_piece(row, col):
                    if piece is not None and piece.is_king():
                        drawables.append(DrawableKing(x, y, 60, 60, colour))
                    elif piece is not None:
                        drawables.append(DrawablePiece(x, y, 60, 60, colour))
                        
        if held_drawable is not None:
            drawables.append(held_drawable)
        return drawables