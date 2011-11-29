'''
Created on 2011-11-20

@author: Gooble
'''
from tkinter import Menu, Tk
import main.game.board as board
import main.view.boardcanvas
import main.view.slotting

class GamePlay(object):

    DEFAULT_HEIGHT = 480
    DEFAULT_WIDTH = 480

    def __init__(self):
        self.board = board.Board()
        self.slotting = main.view.slotting.Slotting(self.board)

    def _init_menu(self, root):
        menubar = Menu(root)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="New Game", command=self.new_game)
        filemenu.add_command(label="Quit", command=root.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        root.config(menu=menubar)
        
    def _init_canvas(self, root):
        canvas = main.view.boardcanvas.BoardCanvas(root, width=self.DEFAULT_WIDTH, height=self.DEFAULT_HEIGHT)
        canvas.bind(sequence='<ButtonPress-1>', func=self.slotting.select_piece)
        canvas.bind(sequence='<ButtonRelease-1>', func=self.slotting.release_piece)
        canvas.pack()
        
        canvas.draw(self.board)
        
    def print_stuff(self, event):
        print(event.x, event.y)

    def start(self):
        root = Tk()
        self._init_menu(root)
        self._init_canvas(root)
        root.mainloop()
        
    def new_game(self):
        self.board = board.Board()
        
if __name__ == '__main__':
    GamePlay().start()