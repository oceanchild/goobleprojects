'''
Created on 2011-11-20

@author: Gooble
'''
from tkinter import Tk
import main.game.board as board
import main.view.slotting
import main.view.menufactory as menufactory
import main.view.boardcanvasfactory as boardcanvasfactory
import main.ai.easyai as easyai

class GamePlay(object):

    DEFAULT_HEIGHT = 480
    DEFAULT_WIDTH = 480

    def __init__(self, canvas_factory=boardcanvasfactory.BoardCanvasFactory(), menu_factory=menufactory.MenuFactory(), ai=None):
        self.board = board.Board()
        
        self.root = Tk()
        menu_factory.make_menu(self)
        
        self.slotting = main.view.slotting.Slotting(self.board)
        self.canvas = canvas_factory.make_canvas(self.root, self.board, self.slotting)
        self._add_bindings_for_canvas()
        self.ai = ai

    def _add_bindings_for_canvas(self):
        self.canvas.bind(sequence='<ButtonPress-1>', func=self.draw_slotting)
        self.canvas.bind(sequence='<Button1-Motion>', func=self.canvas.draw)
        self.canvas.bind(sequence='<ButtonRelease-1>', func=self.draw_release)
        
    def draw_slotting(self, event):
        self.slotting.select_piece(event)
        self.canvas.draw(event)
        
    def draw_release(self, event):
        self.slotting.release_piece(event)
        self.canvas.draw(event)
        self.check_and_use_ai()
            
    def check_and_use_ai(self):
        if self.ai is not None and self.board.current_turn.is_computers_turn(self.ai):
            self.ai.make_move(self.board)
            self.canvas.draw()
        
    def start(self):
        self.root.mainloop()
        self.check_and_use_ai()
        
    def new_game(self):
        self.board = board.Board()
        
if __name__ == '__main__':
    GamePlay(ai=easyai.EasyAI()).start()