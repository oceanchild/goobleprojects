'''
Created on 2011-11-20

@author: Gooble
'''

import main.game.gameplay as gameplay
import main.view.slotting
import main.view.canvas
import main.view.drawables
import pygame
import main.ai.aithread as aithread 
from main.ai import minimaxai

class GamePanel(object):

    DEFAULT_HEIGHT = 480
    DEFAULT_WIDTH = 480

    def __init__(self, ai=None):
        self.game = gameplay.GamePlay()
        
        self.screen = pygame.display.set_mode([self.DEFAULT_WIDTH, self.DEFAULT_HEIGHT])
        pygame.display.set_caption("Gooble Checkers")
        
        self.slotting = main.view.slotting.Slotting(self.game)
        self.ai = ai
        self.aithread = None
        
    def handle_events(self, game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit_game()
                return
            try:
                pos = event.pos
            except AttributeError:
                pos = None
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.draw_slotting(event.pos)
            if event.type == pygame.MOUSEBUTTONUP:
                self.draw_release(event.pos)
            self.draw(pos)
            
    def draw_slotting(self, position):
        if not self.game.current_turn.is_computers_turn(self.ai):
            self.slotting.select_piece(position)
                    
    def draw_release(self, position):
        if not self.game.current_turn.is_computers_turn(self.ai):
            self.slotting.release_piece(position)
    def check_and_use_ai(self):
        if self.ai is not None and self.game.current_turn.is_computers_turn(self.ai) and (self.aithread is None or self.aithread.finished):
            if self.aithread is not None:
                self.aithread.join(10)
            self.aithread = aithread.AIThread(self.ai, self.game)
            self.aithread.start()
        
    def create_drawables(self, game, position):
        return main.view.drawables.Drawables(self, self.slotting).create(position)
        
    def draw(self, position=None):
        main.view.canvas.Canvas(self.screen).draw(self.create_drawables(self.game, position))
    
    def start(self):
        pygame.init()
        
        self.clock = pygame.time.Clock()
        font = pygame.font.Font(None, 25)
        self.done = False
        while not self.done:
            self.clock.tick(30)
            self.screen.fill([0,0,0])
            
            self.draw()
            self.handle_events(self.game)
            self.check_and_use_ai()
            
            if self.game.current_turn.is_computers_turn(self.ai):
                text = font.render("The computer is thinking...", False, [150,150,150], [255,255,255])
                self.screen.blit(text, [self.DEFAULT_WIDTH/4, self.DEFAULT_HEIGHT/2 - 25])
            pygame.display.flip()


    def quit_game(self):
        self.done = True
        
    def new_game(self):
        self.game = gameplay.GamePlay()
        self.slotting = main.view.slotting.Slotting(self.game)
        
    def get_num_rows(self):
        return self.game.board.DEFAULT_HEIGHT
    
    def get_num_cols(self):
        return self.game.board.DEFAULT_WIDTH
    
    def get_tile_width(self):
        return self.DEFAULT_WIDTH / self.game.board.DEFAULT_WIDTH
    
    def get_tile_height(self):
        return self.DEFAULT_HEIGHT / self.game.board.DEFAULT_HEIGHT
    
    def get_piece(self, row, col):
        return self.game.get_piece(row, col)
        
if __name__ == '__main__':
    GamePanel(ai=minimaxai.MinimaxAI(3)).start()