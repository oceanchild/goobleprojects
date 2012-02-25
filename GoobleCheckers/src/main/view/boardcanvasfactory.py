'''
Created on 2011-12-09

@author: Gooble
'''
import main.view.boardcanvas
import main.view.gamepanel

class BoardCanvasFactory(object):

    def make_canvas(self, screen, board, slotting):
        canvas = main.view.boardcanvas.BoardCanvas(screen)
        canvas.set_board(board)
        canvas.set_slotting(slotting)
        canvas.calculate_dimensions()
        canvas.draw()
        return canvas
    
        