'''
Created on 2011-11-20

@author: Gooble
'''
from main.game.board import Board
from tkinter import Menu, Canvas, Tk
import tile

class BoardCanvas(Canvas):
    
    def draw(self, board):
        [[tile.Tile(row, col, board, self).draw() for col in range(0, Board.DEFAULT_WIDTH)] for row in range(0, Board.DEFAULT_HEIGHT)]

class GamePlay(object):

    DEFAULT_HEIGHT = 480
    DEFAULT_WIDTH = 480

    def __init__(self):
        self.board = Board()

    def _init_menu(self, root):
        menubar = Menu(root)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="New Game", command=self.new_game)
        filemenu.add_command(label="Quit", command=root.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        root.config(menu=menubar)
        
    def _init_canvas(self, root):
        canvas = BoardCanvas(root, width=self.DEFAULT_WIDTH, height=self.DEFAULT_HEIGHT)
        canvas.bind(sequence='<Button-1>', func=self.print_stuff)
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
        self.board = Board()
        
if __name__ == '__main__':
    GamePlay().start()