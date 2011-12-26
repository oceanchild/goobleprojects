'''
Created on 2011-11-20

@author: Gooble
'''
from tkinter import Tk
import main.game.gameplay as gameplay
import main.view.slotting
import main.view.menufactory as menufactory
import main.view.boardcanvasfactory as boardcanvasfactory
from main.ai import contemplativeai, minimaxai

class GamePanel(object):

    DEFAULT_HEIGHT = 480
    DEFAULT_WIDTH = 480

    def __init__(self, canvas_factory=boardcanvasfactory.BoardCanvasFactory(), menu_factory=menufactory.MenuFactory(), ai=None):
        self.game = gameplay.GamePlay()
        
        self.root = Tk()
        menu_factory.make_menu(self)
        
        self.slotting = main.view.slotting.Slotting(self.game)
        self.canvas = canvas_factory.make_canvas(self.root, self.game.board, self.slotting)
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
        if (self.game.is_game_over()):
            self.new_game()
            
    def check_and_use_ai(self):
        if self.ai is not None and self.game.current_turn.is_computers_turn(self.ai):
            self.ai.make_move(self.game)
            self.canvas.draw()
        
    def start(self):
        self.root.mainloop()
        self.check_and_use_ai()
        
    def new_game(self):
        self.game = gameplay.GamePlay()
        self.slotting = main.view.slotting.Slotting(self.game)
        self.canvas.board = self.game.board
        self.canvas.slotting = self.slotting
        self.canvas.draw()
        
if __name__ == '__main__':
    GamePanel(ai=minimaxai.MinimaxAI(4)).start()