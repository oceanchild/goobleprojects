'''
Created on 2011-11-20

@author: Gooble
'''
from main.game.board import Board
from tkinter import Menu, Canvas, Tk
from main.game import origin


class Tile(object):
    
    BLANK_TILE_COLOURS = ['white', 'blue']
    PIECE_COLOURS = {origin.TOP.desc:'red', origin.BOTTOM.desc:'black'}
    
    def __init__(self, row, col, board, canvas):
        self.row = row
        self.col = col
        self.board = board
        self.canvas = canvas
        
    def draw(self):
        piece = self.board.get_piece(self.row, self.col)
        width = GamePlay.DEFAULT_WIDTH/Board.DEFAULT_WIDTH
        height = GamePlay.DEFAULT_HEIGHT/Board.DEFAULT_HEIGHT
        if piece is None:
            colour = Tile.BLANK_TILE_COLOURS[(self.row + self.col) % 2]
            self.canvas.create_rectangle(self.col * width, self.row * height, self.col * width + width, self.row * height + height, fill=colour)
        else:
            colour = Tile.PIECE_COLOURS[piece.get_origin().desc]
            self.canvas.create_oval(self.col * width, self.row * height, self.col * width + width, self.row * height + height, fill=colour)


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
        canvas = Canvas(root, width=self.DEFAULT_WIDTH, height=self.DEFAULT_HEIGHT)
        canvas.pack()
        
        for row in range(0, self.board.DEFAULT_HEIGHT):
            for col in range(0, self.board.DEFAULT_WIDTH):
                Tile(row, col, self.board, canvas).draw()
        

    def start(self):
        root = Tk()
        self._init_menu(root)
        self._init_canvas(root)
        root.mainloop()
        
    def new_game(self):
        self.board = Board()
        
if __name__ == '__main__':
    GamePlay().start()