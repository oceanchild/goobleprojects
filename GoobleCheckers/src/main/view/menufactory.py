'''
Created on 2011-12-09

@author: Gooble
'''
from tkinter import Menu

class MenuFactory(object):
    
    def make_menu(self, game):
        menubar = Menu(game.root)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="New Game", command=game.new_game)
        filemenu.add_command(label="Quit", command=game.root.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        game.root.config(menu=menubar)
