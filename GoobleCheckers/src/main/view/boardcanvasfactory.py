'''
Created on 2011-12-09

@author: Gooble
'''
import main.view.boardcanvas
import main.view.gameplay

class BoardCanvasFactory(object):

    def make_canvas(self, root_pane, board, slotting):
        canvas = main.view.boardcanvas.BoardCanvas(root_pane, width=main.view.gameplay.GamePlay.DEFAULT_WIDTH, height=main.view.gameplay.GamePlay.DEFAULT_HEIGHT)
        canvas.set_board(board)
        canvas.set_slotting(slotting)
        canvas.calculate_dimensions()
        canvas.pack()
        canvas.draw()
        return canvas
    
        